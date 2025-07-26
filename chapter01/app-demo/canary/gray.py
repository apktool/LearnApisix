import asyncio
from asyncio import CancelledError
from contextlib import asynccontextmanager

import grpc
import uvicorn
from fastapi import FastAPI, APIRouter
from grpc import Server

from canary import canary_pb2_grpc
from canary.consul_util import register_consul_service, unregister_consul_service
from canary.service import GrayService
from canary.util import get_service_ip_port

server_host = "0.0.0.0"
http_server_port = 8002
rpc_server_port = 9002
instance_name = "app-instance-gray"
service_name = "canary-gray"

router = APIRouter(prefix="/api/canary/v1", tags=["api"])


async def start_http():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        ip = get_service_ip_port()
        port = http_server_port
        service_id = "{}-http".format(instance_name)
        await register_consul_service(host=ip, port=port, service_name=service_name, instance_name=service_id,
                                      scheme="http")
        yield
        await unregister_consul_service(instance_name=service_name)

    app = FastAPI(lifespan=lifespan)
    app.include_router(router)

    config = uvicorn.Config(
        app=app,
        host=server_host,
        port=http_server_port,
        log_level="info",
    )

    server = uvicorn.Server(config)
    return server


async def start_rpc():
    @asynccontextmanager
    async def lifespan(server: Server):
        ip = get_service_ip_port()
        port = rpc_server_port
        service_id = "{}-rpc".format(instance_name)
        await register_consul_service(host=ip, port=port, service_name=service_name, instance_name=service_id,
                                      scheme="grpc")
        yield
        # FastAPI 为啥在 yield 的时候就可以卡住，而自己写的就不行呢
        # await unregister_consul_service(instance_name=service_id)

    server = grpc.aio.server()
    server.add_insecure_port(f"{server_host}:{rpc_server_port}")
    canary_pb2_grpc.add_CanaryServiceServicer_to_server(GrayService(), server)

    async with lifespan(server):
        await server.start()

    return server


@router.get("/")
async def read_root():
    # GET /api/canary/v1/
    return {"Hello": "Gray World"}


@router.get("/id/{ids}")
async def read_item(ids: int):
    # /api/canary/v1/id/1
    return {"Hello Gray": ids}


async def main():
    http_server = await start_http()
    grpc_server = await start_rpc()

    try:
        await asyncio.gather(http_server.serve(), grpc_server.wait_for_termination())
    except KeyboardInterrupt and CancelledError:
        await grpc_server.stop(0)
        await http_server.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

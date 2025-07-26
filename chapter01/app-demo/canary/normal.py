from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, APIRouter

from canary.consul_util import register_consul_service, unregister_consul_service
from canary.util import get_service_ip_port

server_host = "0.0.0.0"
server_port = 8001
instance_name = "app-instance"
service_name = "canary"

router = APIRouter(prefix="/api/canary/v1", tags=["api"])


@asynccontextmanager
async def lifespan(app: FastAPI):
    ip = get_service_ip_port()
    port = server_port
    await register_consul_service(host=ip, port=port, service_name=service_name, instance_name=instance_name)
    yield
    await unregister_consul_service(instance_name=instance_name)


@router.get("/")
async def read_root():
    # GET /api/canary/v1/
    return {"Hello": "Normal World"}


@router.get("/id/{ids}")
async def read_item(ids: int):
    # /api/canary/v1/id/1
    return {"Hello": ids}


if __name__ == "__main__":
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    uvicorn.run(app, host=server_host, port=server_port)

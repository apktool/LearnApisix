from consul.aio import Consul
from consul.check import Check

from canary.config import consul_host, consul_port
from canary.logger_setup import logger

service_name = "app-demo"


async def _get_available_consul_services():
    cs = Consul(host=consul_host, port=consul_port)
    return cs


async def register_consul_service(host: str, port: int, service_id: str):
    check = Check.tcp(
        host=host,
        port=port,
        interval="10s",
        timeout="10s",
        deregister="30s"
    )

    cs = await _get_available_consul_services()

    try:
        response = await cs.agent.service.register(
            name=service_name,
            service_id=service_id,
            check=check,
            tags=["grpc"]
        )
        logger.debug(f"registered successfully, service_id={service_id}, response={response}")
    except Exception as e:
        logger.exception(f"failed to register service_id={service_id}: {e}")


async def unregister_consul_service(service_id: str):
    cs = await _get_available_consul_services()
    try:
        response = await cs.agent.service.deregister(service_id=service_id)
        logger.debug(f"unregistered successfully, service_id={service_id}, response={response}")
    except Exception as e:
        logger.exception(f"failed to unregister service_id={service_id}: {e}")

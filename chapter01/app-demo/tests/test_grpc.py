import grpc
import pytest

from canary import canary_pb2_grpc
from canary.canary_pb2 import Request


@pytest.mark.asyncio
async def test_grpc_client():
    print(f"gRPC 版本: {grpc.__version__}")
    async with grpc.aio.insecure_channel('localhost:9001') as channel:
        stub = canary_pb2_grpc.CanaryServiceStub(channel)
        request = Request(name="Hello YourName")

        try:
            response = await stub.add(request)
            print(f"Status Code: {response.code}")
            print(f"Message: {response.message}")
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}, {e.details()}")

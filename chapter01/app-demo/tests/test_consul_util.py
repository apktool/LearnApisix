import asyncio
import pytest

from canary.consul_util import register_consul_service


@pytest.mark.asyncio
async def test_register_consul_service():
    await register_consul_service()

    cnt = 0
    while True:
        cnt += 1
        print(cnt)
        await asyncio.sleep(1)

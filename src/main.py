import asyncio

import aiohttp
from sqlalchemy.ext.asyncio import AsyncConnection

from config import GlobalConfig
from ISICVerifier import ISICVerifier


async def main():
    session = aiohttp.ClientSession()
    verif = await ISICVerifier.create(session)
    print(await verif.verify("S421000648595J"))
    print("Hello from independent-reviews!")


if __name__ == "__main__":
    asyncio.run(main())

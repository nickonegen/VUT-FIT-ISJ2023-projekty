#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession, ClientError


async def get_url(url: str, session: ClientSession) -> tuple[str, str]:
    try:
        async with session.get(url) as response:
            return str(response.status), url
    except Exception as e:  # skipcq: PYL-W0703
        if isinstance(e, ClientError):
            return "aiohttp.ClientError", url
        return type(e).__name__, url


async def get_urls(urls: list[str]) -> list[tuple[str, str]]:
    async with ClientSession() as session:
        tasks = [asyncio.create_task(get_url(url, session)) for url in urls]
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "https://www.fit.vutbr.cz",
        "https://www.szn.cz",
        "https://www.alza.cz",
        "https://office.com",
        "https://aukro.cz",
    ]

    # for MS Windows
    if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore

    res = asyncio.run(get_urls(urls))

    print(res)

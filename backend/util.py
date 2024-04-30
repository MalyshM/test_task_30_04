import aiohttp as aiohttp


async def get_request(url: str) -> dict:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url, ssl=False) as response:
            return await response.json()
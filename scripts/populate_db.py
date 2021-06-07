import asyncio
import aiohttp

async def add_entries(payload):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/boss/', data=payload) as resp:
            print(payload, resp.status)


async def main():
    tasks = []
    db_entries = [
        {'name': 'Grumpy Boss', 'health': 10},
        {'name': 'Mean Boss', 'health': 100},
        {'name': 'Terrifying Boss', 'health': 1000},
    ]
    for entry in db_entries:
        tasks.append(asyncio.create_task(add_entries(entry)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
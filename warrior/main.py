import asyncio
import os
import sys
from typing import List, Tuple
from models.awarrior import Warrior
from aiomultiprocess import Pool



async def async_query_rbaas(queries=[]) -> List[Tuple[str, int]]:
    w = Warrior(os.getenv('RBAAS_HOST', 'http://127.0.0.1:8000'))

    expected_values = {
        'Grumpy Boss': 10, 
        'Mean Boss': 100,
        'Terrifying Boss': 1000,
    }

    successful_queries = []
    failed_queries = []
    async with Pool() as pool:
        async for result in pool.map(w.get_boss, queries):
            result_name, result_health = result.get('name'), int(result.get('health', -1))
            if result_name not in expected_values.keys():
                failed_queries.append(f'Name not supported {result_name}')
            elif result_health != expected_values.get(result_name):
                failed_queries.append(f'Health mismatch {result_name}, {result_health}')
            else:
                successful_queries.append((result_name, result_health))

    return successful_queries, failed_queries


if __name__ == '__main__':
    print(asyncio.run(async_query_rbaas(sys.argv[1:])))
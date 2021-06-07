import attr
import validators
import logging
from aiohttp import request

@attr.s
class Warrior:
    host = attr.ib()

    @host.validator
    def check(self, _, value: str):
        if not validators.url(value):
            raise ValueError('Url not formatted correctly [url:{url}]')

    async def get_boss(self, resource):
        w = Warrior.format_url(self.host, resource)
        async with request('GET', w) as response:
            request_json = {}
            try:
                request_json = await response.json()
            except Exception:
                logging.exception('Big bad exception happened')

            status = response.status
            if not request_json or status != 200:
                logging.warn(f'Request did not return anything or not OK[status_code:{response.status}]')
                return {}
            
            return request_json

    def format_url(host: str, resource: str) -> str:
        return f'{host}/{resource}'

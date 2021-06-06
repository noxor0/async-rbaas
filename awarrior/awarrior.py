import attr
import validators
import requests

@attr.s
class Warrior:
    url = attr.ib()

    @url.validator
    def check(self, _, value: str):
        if not validators.url(value):
            raise ValueError('Url not formatted correctly [url:{url}]')

    def get_boss(self, resource='boss'):
        r = requests.get(f'{self.url}/{resource}')

import pytest
from warrior.models.awarrior import Warrior
from warrior.tests.conftest import TEST_HOST
from warrior.main import async_query_rbaas

@pytest.mark.asyncio
@pytest.mark.integration
@pytest.mark.usefixtures('set_test_envs')
class TestMain():
    
    async def test_successful_given_single_ok_request(self, mocker):
        resource = 'boss/1'
        expected_name = 'Grumpy Boss'

        actual_successful, actual_failed = await async_query_rbaas(queries=[resource])

        assert len(actual_successful) == 1
        assert len(actual_failed) == 0
        assert actual_successful[0][0] == expected_name
     

    async def test_successful_given_multiple_ok_requests(self):
        expected_names = ('Grumpy Boss', 'Mean Boss', 'Terrifying Boss')

        actual_successful, actual_failed = await async_query_rbaas(queries=['boss/1', 'boss/2', 'boss/3'])

        assert len(actual_successful) == 3
        assert len(actual_failed) == 0
        for idx in range(len(expected_names)):
            assert actual_successful[idx][0] == expected_names[idx]


    async def test_successful_given_not_found_requests(self):
        expected_names = ('Grumpy Boss', 'Mean Boss', 'Terrifying Boss')

        actual_successful, actual_failed = await async_query_rbaas(queries=['boss/4'])

        assert len(actual_successful) == 0
        assert len(actual_failed) == 1
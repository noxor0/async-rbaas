import os
import pytest

TEST_HOST = 'http://127.0.0.1:8000'


@pytest.fixture
def set_test_envs():
    os.environ['RBAAS_HOST'] = TEST_HOST
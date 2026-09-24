import pytest

from api.api_handler import APIHandler
from config.config import BASE_URL, API_TOKEN, REQUEST_TIMEOUT


@pytest.fixture
def api_handler():

    return APIHandler(
        base_url=BASE_URL,
        token=API_TOKEN,
        timeout=REQUEST_TIMEOUT
    )
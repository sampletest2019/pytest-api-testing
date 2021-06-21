import requests
import pytest
from resources.json_placeholder_enum import PlaceholderEnum


@pytest.mark.jsonplaceholdertestdelete
def test_post_request():
    response = requests.delete(PlaceholderEnum.JsonPut.value)
    assert response.status_code == 200
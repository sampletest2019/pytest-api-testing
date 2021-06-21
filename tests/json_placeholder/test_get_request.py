import requests
import pytest
from resources.json_placeholder_enum import PlaceholderEnum


@pytest.mark.jsonplaceholdertest
def test_validate_response_code():
    response = requests.get(PlaceholderEnum.JsonPost.value)
    assert response.status_code == 200
    assert 'application/json; charset=utf-8' in response.headers["Content-Type"]


@pytest.mark.jsonplaceholdertest
def test_validate_userid_and_id():
    response = requests.get(PlaceholderEnum.JsonPost.value)
    assert response.status_code == 200
    assert 'application/json; charset=utf-8' in response.headers["Content-Type"]
    data = response.json()
    assert data[0]['userId'] == 1
    assert data[0]['id'] == 1

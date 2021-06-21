import requests
import pytest
from resources.json_placeholder_enum import PlaceholderEnum


@pytest.mark.jsonplaceholdertestput
def test_post_request():
    my_obj = {
        "userId": 1,
        "id": 1,
        "title": 'foo',
        "body": 'bar'
    }

    response = requests.put(PlaceholderEnum.JsonPut.value, data=my_obj)
    assert response.status_code == 200

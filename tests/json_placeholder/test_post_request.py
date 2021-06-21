import requests
import pytest
from resources.json_placeholder_enum import PlaceholderEnum


@pytest.mark.jsonplaceholdertestpost
def test_post_request():
    my_obj ={
        "userId": 1,
        "id": 1,
        "title": "my title",
        "body": "body example"
    }
    response = requests.post(PlaceholderEnum.JsonPost.value, data=my_obj)
    assert response.status_code == 201





import requests
import pytest
from resources.json_placeholder_enum import PlaceholderEnum


@pytest.mark.jsonplaceholdertestpatch
def test_post_request():
    my_obj ={
        "title": "my updated title"
    }
    response = requests.patch(PlaceholderEnum.JsonPut.value, data=my_obj)
    assert response.status_code == 200





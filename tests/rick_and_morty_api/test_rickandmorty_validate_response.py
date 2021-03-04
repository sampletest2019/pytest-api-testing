import requests
import pytest


@pytest.mark.rickandmorty
def test_validate_get_response_code():
    res = requests.get("https://rickandmortyapi.com/api/character/?name=rick&status=alive")
    assert res.status_code == 200



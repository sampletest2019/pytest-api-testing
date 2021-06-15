import requests
import pytest


@pytest.mark.rickandmorty
def test_validate_get_response_code_and_headers():
    res = requests.get("https://rickandmortyapi.com/api/character/?name=rick&status=alive")
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json; charset=utf-8"



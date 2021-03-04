import requests
import pytest


@pytest.mark.rickandmorty
def test_validate_get_response_code():
    response = requests.get("https://rickandmortyapi.com/api/character")
    assert response.status_code == 200



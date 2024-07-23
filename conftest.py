import pytest
import requests
import configuration
from helpers import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.register_new_user()
    login_data = payload.copy()
    del login_data["name"]
    double_email = payload.copy()
    del double_email["name"]
    del double_email["password"]
    response = requests.post(configuration.CREATE_USER_PATH, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token, double_email
    requests.delete(configuration.DELETE_USER_PATH, headers={'Authorization': f'{token}'})

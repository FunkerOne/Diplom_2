import pytest
import requests
import allure
import configuration
from helpers import User


@allure.suite("Регистрация пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = User.register_new_user()
        response = requests.post(configuration.CREATE_USER_PATH, data=payload)
        token = response.json()["accessToken"]
        assert response.status_code == 200 and response.json()["success"] is True
        requests.delete(configuration.DELETE_USER_PATH, headers={"Authorization": f"{token}"})

    @allure.title("Попытка создания пользователя, который уже зарегистрирован")
    def test_create_double_user(self):
        payload = User.register_new_user()
        response_1 = requests.post(configuration.CREATE_USER_PATH, data=payload)
        token = response_1.json()["accessToken"]
        response_2 = requests.post(configuration.CREATE_USER_PATH, data=payload)
        assert response_2.status_code == 403 and response_2.json()["success"] is False
        requests.delete(configuration.DELETE_USER_PATH, headers={"Authorization": f"{token}"})

    @allure.title("Попытка создания пользователя с невалидными данными")
    @pytest.mark.parametrize("payload", [User.register_new_user_without_email(),
                                         User.register_new_user_without_password(),
                                         User.register_new_user_without_name()])
    def test_create_invalid_user(self, payload):
        response = requests.post(configuration.CREATE_USER_PATH, data=payload)
        assert response.status_code == 403 and response.json()["success"] is False

import requests
import allure
import configuration
from helpers import User


@allure.suite("Изменение данных пользователя")
class TestChangingUserData:

    @allure.title("Изменение email авторизованного пользователя")
    def test_update_user_email_auth(self, create_user):
        payload = {"email": User.register_new_user()["email"]}
        token = {"Authorization": create_user[3]}
        response = requests.patch(configuration.CHANGE_USER_DATA_PATH, headers=token, data=payload)
        assert response.status_code == 200 and response.json()["user"]["email"] == payload["email"]

    @allure.title("Изменение name авторизованного пользователя")
    def test_update_user_name_auth(self, create_user):
        payload = {"name": User.register_new_user()["name"]}
        token = {"Authorization": create_user[3]}
        response = requests.patch(configuration.CHANGE_USER_DATA_PATH, headers=token, data=payload)
        assert response.status_code == 200 and response.json()["user"]["name"] == payload["name"]

    @allure.title("Изменение password авторизованного пользователя")
    def test_update_user_password_auth(self, create_user):
        payload = {"password": User.register_new_user()["password"]}
        token = {"Authorization": create_user[3]}
        response = requests.patch(configuration.CHANGE_USER_DATA_PATH, headers=token, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Попытка изменения у авторизованного пользователя email, которая уже используется")
    def test_update_user_double_email_auth(self, create_user):
        payload = {"email": create_user[4]}
        token = {"Authorization": create_user[3]}
        response = requests.patch(configuration.CHANGE_USER_DATA_PATH, headers=token, data=payload)
        assert response.status_code == 403 and response.json()["success"] is False

    @allure.title("Попытка изменения данных неавторизованного пользователя")
    def test_update_user_data_unauth(self):
        response = requests.patch(configuration.CHANGE_USER_DATA_PATH, data=User.register_new_user())
        assert response.status_code == 401 and response.json()["success"] is False

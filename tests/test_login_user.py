import requests
import allure
import configuration
from helpers import User


@allure.suite("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_success_login(self, create_user):
        payload = create_user[2]
        response = requests.post(configuration.LOGIN_USER_PATH, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Логин с неверным логином и паролем")
    def test_unsuccess_login(self):
        payload = User.register_new_user_without_name()
        response = requests.post(configuration.LOGIN_USER_PATH, data=payload)
        assert response.status_code == 401 and response.json()["success"] is False

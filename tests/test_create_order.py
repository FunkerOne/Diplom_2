import requests
import allure
import configuration


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа под зарегистрированным пользователем")
    def test_create_order_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        response = requests.get(configuration.GET_INGREDIENTS_DATA_PATH)
        order_id = response.json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        response_create_order = requests.post(configuration.CREATE_ORDER_PATH, headers=token, data=payload)
        assert response_create_order.status_code == 200 and response_create_order.json()["success"] is True

    @allure.title("Попытка создания заказа под незарегистрированным пользователем")
    def test_create_order_unauth(self):
        response = requests.get(configuration.GET_INGREDIENTS_DATA_PATH)
        order_id = response.json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        response_create_order = requests.post(configuration.CREATE_ORDER_PATH, data=payload)
        assert response_create_order.status_code == 200 and response_create_order.json()["success"] is True

    @allure.title("Попытка создания заказа, если отправить невалидный хеш ингредиента")
    def test_create_order_invalid_hash_ingred(self):
        payload = {"ingredients": "ad1234df567hfd89"}
        response = requests.post(configuration.CREATE_ORDER_PATH, data=payload)
        assert response.status_code == 500 and "Internal Server Error" in response.text

    @allure.title("Попытка создания заказа, если отправить поле ингредиенты = пустой ввод")
    def test_create_order_empty_ingred(self):
        payload = {"ingredients": ""}
        response = requests.post(configuration.CREATE_ORDER_PATH, data=payload)
        assert response.status_code == 400 and response.json()["success"] is False

    @allure.title("Попытка создания заказа, если не отправлять тело")
    def test_create_order_empty_body(self):
        response = requests.post(configuration.CREATE_ORDER_PATH)
        assert response.status_code == 400 and response.json()["success"] is False

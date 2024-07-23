import requests
import allure
import configuration


@allure.suite("Получение заказов конкретного пользователя")
class TestGetUserOrder:

    @allure.title("Получение номера заказа зарегистрированного пользователя")
    def test_get_user_order_auth(self, create_user):
        token = {"Authorization": create_user[3]}
        response = requests.get(configuration.GET_INGREDIENTS_DATA_PATH)
        order_id = response.json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        response_order_create = requests.post(configuration.CREATE_ORDER_PATH, headers=token, data=payload)
        response_get_order = requests.get(configuration.GET_ORDERS_PATH, headers=token)
        assert (response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] ==
                response_order_create.json()['order']['number'])

    @allure.title("Попытка получения заказов незарегистрированного пользователя")
    def test_get_user_order_unauth(self):
        response = requests.get(configuration.GET_ORDERS_PATH)
        assert response.status_code == 401 and response.json()["success"] is False

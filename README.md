# Задание 2: "REST API" тестирование  на курсе "Автоматизатор тестирования на Python" | Diplom_2
Для тестирования был выбран сервис [Stella Burgers](https://stellarburgers.nomoreparties.site/) | [API Stella Burgers](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)

Тесты: 

[Создание пользователя](tests/test_create_user.py)
- Создание уникального пользователя
- Создание пользователя, который уже зарегистрирован
- Создание пользователя с незаполненными одним из обязательных полей

[Авторизация пользователя](tests/test_login_user.py)
- Логин под существующим пользователем
- Логин с неверным логином и паролем

[Изменение данных пользователя](tests/test_changing_user_data.py)
- C авторизацией / Без авторизации

[Создание заказа](tests/test_create_order.py)
- C авторизацией / Без авторизации
- С ингредиентами / Без ингредиентов 
- С неверным хешем ингредиентов

[Получение заказов конкретного пользователя](tests/test_get_user_order.py)
- Авторизованный пользователь / Неавторизованный пользователь

---
### Установить зависимости 
``` shell
pip install -r requirements.txt
```
### Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
### Посмотреть отчет в веб версии пройденного прогона
```shell
allure serve allure_results
```
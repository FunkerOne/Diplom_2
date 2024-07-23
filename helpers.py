from faker import Faker


class User:
    @staticmethod
    def register_new_user():
        fake = Faker()
        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    @staticmethod
    def register_new_user_without_email():
        fake = Faker()
        reg_data = {
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    @staticmethod
    def register_new_user_without_password():
        fake = Faker()
        reg_data = {
            "email": fake.email(),
            "name": fake.name()}
        return reg_data

    @staticmethod
    def register_new_user_without_name():
        fake = Faker()
        reg_data = {
            "email": fake.email(),
            "password": fake.password()}
        return reg_data

import requests
import allure
from utils.helpers import generate_random_string, BASE_URL

class TestCreateCourier:

    @allure.title("Создание курьера успешно")
    def test_create_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(f'{BASE_URL}/courier', json=payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True

    @allure.title("Создание дублирующего курьера")
    def test_create_duplicate_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(f'{BASE_URL}/courier', json=payload)
        assert response.status_code == 201
        duplicate_response = requests.post(f'{BASE_URL}/courier', json=payload)
        assert duplicate_response.status_code == 409

    @allure.title("Создание курьера с отсутствующими полями")
    def test_create_courier_missing_fields(self):
        # Отсутствует поле "login"
        payload_missing_login = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response_missing_login = requests.post(f'{BASE_URL}/courier', json=payload_missing_login)
        assert response_missing_login.status_code == 400

        # Отсутствует поле "password"
        payload_missing_password = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response_missing_password = requests.post(f'{BASE_URL}/courier', json=payload_missing_password)
        assert response_missing_password.status_code == 400

        # Отсутствуют оба поля
        payload_missing_both = {
            "firstName": generate_random_string(10)
        }
        response_missing_both = requests.post(f'{BASE_URL}/courier', json=payload_missing_both)
        assert response_missing_both.status_code == 400

    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_existing_login(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(f'{BASE_URL}/courier', json=payload)
        assert response.status_code == 201
        duplicate_response = requests.post(f'{BASE_URL}/courier', json=payload)
        assert duplicate_response.status_code == 409
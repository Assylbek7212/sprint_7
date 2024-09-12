import pytest
import requests
import allure
from utils.helpers import generate_random_string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'

class TestCreateOrder:

    @allure.title("Создание заказа успешно")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order(self, colors):
        payload = {
            "firstName": generate_random_string(10),
            "lastName": generate_random_string(10),
            "address": f"{generate_random_string(10)} street",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-01",
            "comment": generate_random_string(20),
            "color": colors
        }
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()

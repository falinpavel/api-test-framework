import allure
import pytest
import requests


@pytest.fixture(scope="function")
def generate_new_object():
    with allure.step("Sending POST/objects request for precondition"):
        headers = {
            "Content-Type": "application/json"
        }
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    with allure.step(f"Sending POST/objects request for creating new object and getting id"):
        response_generator = requests.post(
            "https://api.restful-api.dev/objects", headers=headers, json=body
        ).json()
    yield response_generator
    with allure.step(f"Sending DELETE/objects/{response_generator['id']} request"):
        requests.delete(f"https://api.restful-api.dev/objects/{response_generator['id']}")
        assert requests.get(f"https://api.restful-api.dev/objects/{response_generator['id']}").status_code == 404

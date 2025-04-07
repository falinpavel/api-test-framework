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
    with allure.step(f"Checking that REST-full API for learning not reached limit today"):
        try:
            if response_generator["error"]:
                raise Exception("REST-full API for learning not reached limit today, status code 405")
        except Exception as e:
            raise e
    with allure.step(f"Checking that param 'createdAt' is not null"):
        assert response_generator["createdAt"] is not None, "Object is not created"
    yield response_generator
    with allure.step(f"Sending DELETE/objects/{response_generator['id']} request"):
        requests.delete(f"https://api.restful-api.dev/objects/{response_generator['id']}")
        assert requests.get(f"https://api.restful-api.dev/objects/{response_generator['id']}").status_code == 404

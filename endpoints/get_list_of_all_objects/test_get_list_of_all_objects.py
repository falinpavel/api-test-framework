import requests
import pytest
import allure


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method GET/objects")
@allure.story("Getting a list of all objects")
def test_get_list_of_all_objects():
    with allure.step("Sending GET/objects request"):
        response = requests.get("https://api.restful-api.dev/objects")
    with allure.step("Checking status code"):
        assert response.status_code == 200
    with allure.step("Checking content type"):
        assert response.headers["Content-Type"] == "application/json"
    with allure.step("Checking response body is not empty"):
        assert response.json()
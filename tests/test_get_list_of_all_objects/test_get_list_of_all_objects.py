import requests
import pytest
import allure


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method GET/objects")
@allure.story("Getting a list of all objects")
@allure.title("Получение списка уже созданных обьектов")
@allure.description("""
1. Запрос полного списка обьектов
2. Проверка, что ответ не пустой
3. Проверка общего колличества обьектов в массиве из ответа
4. Проверка консистентности данных в ответе, а именно для первого обьекта со следующими параметрами:
{
	"id": "1",
	"name": "Google Pixel 6 Pro",
	"data": {
		"color": "Cloudy White",
		"capacity": "128 GB"
	}
}
5. 
""")
def test_get_list_of_all_objects():
    with allure.step("Sending GET/objects request"):
        response = requests.get("https://api.restful-api.dev/objects")
    with allure.step("Checking status code"):
        assert response.status_code == 200
    with allure.step("Checking content type"):
        assert response.headers["Content-Type"] == "application/json"
    with allure.step("Checking response body is not empty"):
        assert response.json()
    with allure.step("Checking total amount objects in response"):
        assert len(response.json()) == 13
    with allure.step("Checking params data in first object in response"):
        first_object = response.json()[0]
        assert first_object["id"] == "1"
        assert first_object["name"] == "Google Pixel 6 Pro"
        assert first_object["data"]["color"] == "Cloudy White"
        assert first_object["data"]["capacity"] == "128 GB"

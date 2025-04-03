import requests
import pytest
import allure


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method GET/objects/{id}")
@allure.story("Getting single object by id")
@allure.title("Получение созданного в предусловии обьекта по его идентификатору")
@allure.description("""
1. Создание нового обиекта со следующими параметрами:
{
	"name": "Apple MacBook Pro 16",
	"data": {
		"year": 2019,
		"price": 1849.99,
		"CPU model": "Intel Core i9",
		"Hard disk size": "1 TB"
	}
}
2. Проверка маппинга каждого поля по отвельности
""")
def test_get_single_object(generate_new_object):
    with allure.step("Sending GET/objects/{id} request"):
        response = requests.get(f"https://api.restful-api.dev/objects/{generate_new_object['id']}")
    with allure.step("Checking status code"):
        assert response.status_code == 200
    with allure.step("Checking content type"):
        assert response.headers["Content-Type"] == "application/json"
    with allure.step("Checking response body is not empty"):
        assert response.json()
    with allure.step("Checking response body contains all params"):
        get_object = response.json()
        # проверяем параметры созданного POST запросом в фикстуре обьекта с полученными в GET запросе (проверка удаления обьекта реализована в фикстуре)
        assert get_object["name"] == generate_new_object["name"]
        assert get_object["data"]["year"] == generate_new_object["data"]["year"]
        assert get_object["data"]["price"] == generate_new_object["data"]["price"]
        assert get_object["data"]["CPU model"] == generate_new_object["data"]["CPU model"]
        assert get_object["data"]["Hard disk size"] == generate_new_object["data"]["Hard disk size"]
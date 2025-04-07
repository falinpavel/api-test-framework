import pytest
import allure
from endpoints.get_single_object.get_single_object import GetSingleObject


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method GET/objects/{id}")
@allure.story("Getting single object by id")
@allure.title("Получение созданного в предусловии обьекта по его идентификатору")
@allure.description(
    """Тест кейс проверяет, что GET/objects/{id}
    возвращает статус код 200 ОК, обьект
    соответствует требованиям (см. параметры созданного обьекта в фикстуре)
    """)
def test_get_single_object(generate_new_object):
    request = GetSingleObject()
    request.check_get_single_object(generate_new_object["id"])
    request.check_response_status_code(
        request=request,
        expected_status_code=200)
    request.check_headers(
        request=request,
        expected_headers=request.headers)
    request.check_response_object_contains_all_params()
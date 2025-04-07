import pytest
import allure

from endpoints.get_list_of_all_objects.get_list_of_all_objects import GetListOfAllObjects


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method GET/objects")
@allure.story("Getting a list of all objects")
@allure.title("Получение списка уже созданных обьектов")
@allure.description(
    """Тест кейс проверяет, что GET/objects
    возвращает статус код 200 ОК, общее колличество обьектов
    в ответе равно 13, первый обьект в списке соответствует требованиям
    """)
def test_get_list_of_all_objects():
    request = GetListOfAllObjects()
    request.check_get_list_of_all_objects()
    request.check_response_status_code(
        request=request,
        expected_status_code=200)
    request.check_headers(
        request=request,
        expected_headers=request.headers)
    request.check_response_total_objects()
    request.check_response_first_object()

import pytest
import allure


@pytest.mark.api
@allure.epic("REST API")
@allure.feature("REST API. Method POST/objects")
@allure.story("Adding new object")
@allure.title("Добавление нового обьекта")
@allure.description(
    """Тест кейс проверяет, что POST/objects
    возвращает статус код 201 Created, обьект
    соответствует требованиям (см. параметры созданного обьекта в фикстуре)
    """)
def test_post_add_new_object(generate_new_object):
    pass
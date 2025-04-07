import allure
import requests


class GetSingleObject:
    def __init__(self):
        self.headers = None
        self.object = None
        self.total_objects = None
        self.status_code = None

    def check_get_single_object(self, object_id):
        with allure.step("Sending GET/objects/{object_id} request"):
            request = requests.get(f"https://api.restful-api.dev/objects/{object_id}")
        self.status_code = request.status_code
        self.total_objects = len(request.json())
        self.object = request.json()
        self.headers = request.headers
        return request

    def check_headers(self):
        with allure.step("Checking content type"):
            assert self.headers["Content-Type"] == "application/json"

    def check_response_status_code(self):
        with allure.step("Checking status code"):
            assert self.status_code == 200

    def check_response_object_contains_all_params(self):
        with allure.step("Checking response body contains all params"):
            get_object = self.object
            assert get_object["id"] == self.object["id"]
            assert get_object["name"] == self.object["name"]
            assert get_object["data"]["year"] == self.object["data"]["year"]
            assert get_object["data"]["price"] == self.object["data"]["price"]
            assert get_object["data"]["CPU model"] == self.object["data"]["CPU model"]
            assert get_object["data"]["Hard disk size"] == self.object["data"]["Hard disk size"]
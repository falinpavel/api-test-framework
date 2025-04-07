import allure
import requests

from endpoints.base_endpoint_handler import BaseEndpointHandler


class GetListOfAllObjects(BaseEndpointHandler):
    def __init__(self):
        super().__init__()
        self.first_object = None
        self.total_objects = None

    def check_get_list_of_all_objects(self):
        with allure.step("Sending GET/objects request"):
            request = requests.get("https://api.restful-api.dev/objects")
        self.status_code = request.status_code
        self.total_objects = len(request.json())
        self.first_object = request.json()[0]
        self.headers = request.headers
        return request

    def check_response_total_objects(self):
        with allure.step("Checking total amount objects in response"):
            assert self.total_objects == 13

    def check_response_first_object(self):
        with allure.step("Checking params data in first object in response"):
            assert self.first_object["id"] == "1"
            assert self.first_object["name"] == "Google Pixel 6 Pro"
            assert self.first_object["data"]["color"] == "Cloudy White"
            assert self.first_object["data"]["capacity"] == "128 GB"


import allure


class BaseEndpointHandler:
    def __init__(self):
        self.headers = None
        self.status_code = None

    def check_response_status_code(self, request, expected_status_code):
        with allure.step("Checking status code"):
            assert request.status_code == expected_status_code

    def check_headers(self, request, expected_headers):
        with allure.step("Checking headers"):
            assert request.headers == expected_headers

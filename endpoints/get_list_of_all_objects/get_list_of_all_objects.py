import requests


class GetListOfAllObjects:
    def url_for_get_list_of_all_objects(self):
        request = requests.get("https://api.restful-api.dev/objects")
        return request

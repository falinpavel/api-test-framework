from locust import HttpUser, task


class PerformanceTest(HttpUser):
    @task
    def get_list_of_all_objects(self):
        self.client.get("/objects")
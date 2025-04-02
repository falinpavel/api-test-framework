# api-test-framework
## requirements:
    - pip install pytest (test runner)
    - pip install allure-pytest (test reporter)
    - pip install requests (HTTP requests)
    - pip install pytest-xdist (parallel execution)
# Links:
REST API Documentation - https://restful-api.dev/

# Structure:
    - api-test-framework
        - tests:
            - test_api.py
        - endpoints:
            - delete_object:
            - get_list_of_all_objects:
            - get_list_of_objects_by_ids:
            - get_single_object:
            - patch_partially_update_object:
            - post_add_new_object:
            - put_update_object:
        - .gitignore
        - conftest.py
        - README.md
        - requirements.txt
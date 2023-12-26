import requests
import unittest
import logging
import allure
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_directory, 'app.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseAPITestCase(unittest.TestCase):
    base_url = "http://localhost:5555"

    @classmethod
    def setUpClass(cls):
        cls.headers = {'Content-Type': 'application/json'}

    def send_request(self, method, url, data=None):
        with allure.step(f"Sending {method} request to {url}"):
            if method == 'GET':
                response = requests.get(f"{self.base_url}/{url}", headers=self.headers)
            elif method == 'POST':
                response = requests.post(f"{self.base_url}/{url}", json=data, headers=self.headers)
            elif method == 'PUT':
                response = requests.put(f"{self.base_url}/{url}", json=data, headers=self.headers)
            elif method == 'DELETE':
                response = requests.delete(f"{self.base_url}/{url}", headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            logger.info(f"{method} Response: {response.text}")
            return response


class APITestCase(BaseAPITestCase):

    @allure.feature("CRUD Operations - Users")
    @allure.title("Create User")
    def test_01_create_user(self):
        response = self.send_request('POST', 'users', {"name": "Test User", "age": 25, "email": "test@example.com"})
        self.assertEqual(response.status_code, 201)

    @allure.feature("CRUD Operations - Users")
    @allure.title("Read User")
    def test_02_read_user(self):
        response = self.send_request('GET', 'users/3')
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Users")
    @allure.title("Update User")
    def test_03_update_user(self):
        response = self.send_request('PUT', 'users/3',
                                     {"name": "Updated User", "age": 30, "email": "updated@example.com"})
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Users")
    @allure.title("Delete User")
    def test_04_delete_user(self):
        response = self.send_request('DELETE', 'users/5')
        self.assertEqual(response.status_code, 200)



    @allure.feature("CRUD Operations - Posts")
    @allure.title("Create Post")
    def test_05_create_post(self):
        response = self.send_request('POST', 'posts',
                                     {"title": "Test Post", "body": "This is a test post.", "userId": 2})
        self.assertEqual(response.status_code, 201)

    @allure.feature("CRUD Operations - Posts")
    @allure.title("Read Post")
    def test_06_read_post(self):
        response = self.send_request('GET', 'posts/3')
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Posts")
    @allure.title("Update Post")
    def test_07_update_post(self):
        response = self.send_request('PUT', 'posts/3',
                                     {"title": "Updated Post", "body": "This is an updated post.", "userId": 2})
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Posts")
    @allure.title("Delete Post")
    def test_08_delete_post(self):
        response = self.send_request('DELETE', 'posts/5')
        self.assertEqual(response.status_code, 200)



    @allure.feature("CRUD Operations - Comments")
    @allure.title("Create Comment")
    def test_09_create_comment(self):
        response = self.send_request('POST', 'comments', {"body": "This is a test comment.", "postId": 2})
        self.assertEqual(response.status_code, 201)

    @allure.feature("CRUD Operations - Comments")
    @allure.title("Read Comment")
    def test_10_read_comment(self):
        response = self.send_request('GET', 'comments/3')
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Comments")
    @allure.title("Update Comment")
    def test_11_update_comment(self):
        response = self.send_request('PUT', 'comments/3', {"body": "This is an updated comment.", "postId": 2})
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Comments")
    @allure.title("Delete Comment")
    def test_12_delete_comment(self):
        response = self.send_request('DELETE', 'comments/5')
        self.assertEqual(response.status_code, 200)



    @allure.feature("CRUD Operations - Tasks")
    @allure.title("Create Task")
    def test_13_create_task(self):
        response = self.send_request('POST', 'tasks', {"title": "Test Task", "completed": False, "userId": 2})
        self.assertEqual(response.status_code, 201)

    @allure.feature("CRUD Operations - Tasks")
    @allure.title("Read Task")
    def test_14_read_task(self):
        response = self.send_request('GET', 'tasks/3')
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Tasks")
    @allure.title("Update Task")
    def test_15_update_task(self):
        response = self.send_request('PUT', 'tasks/3', {"title": "Updated Task", "completed": True, "userId": 2})
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Tasks")
    @allure.title("Delete Task")
    def test_16_delete_task(self):
        response = self.send_request('DELETE', 'tasks/5')
        self.assertEqual(response.status_code, 200)



    @allure.feature("CRUD Operations - Categories")
    @allure.title("Create Category")
    def test_17_create_category(self):
        response = self.send_request('POST', 'categories', {"name": "Test Category"})
        self.assertEqual(response.status_code, 201)

    @allure.feature("CRUD Operations - Categories")
    @allure.title("Read Category")
    def test_18_read_category(self):
        response = self.send_request('GET', 'categories/3')
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Categories")
    @allure.title("Update Category")
    def test_19_update_category(self):
        response = self.send_request('PUT', 'categories/3', {"name": "Updated Category"})
        self.assertEqual(response.status_code, 200)

    @allure.feature("CRUD Operations - Categories")
    @allure.title("Delete Category")
    def test_20_delete_category(self):
        response = self.send_request('DELETE', 'categories/5')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

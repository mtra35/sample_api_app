from api_app import create_app
import unittest

app = create_app()


class TestPost(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_normal_data(self):
        # using 2nd example
        payload = '[{"package": "freeciv", "version": "1.1.2", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, \
            {"package": "photoshop", "version": "2.1.1","host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, \
                {"package": "freeciv", "version": "1.0.9","host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, \
                    {"package": "flash", "version": "78.3.9","host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, \
                        {"package": "mint-linux", "version": "2015.2.0", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}]'

        response = self.app.post(
            '/vuln', headers={"Content-Type": "application/json"}, data=payload)

        expected_result = {"74d2d85b57664f819ccea15b57fed5c0.example.org": [
            "CVE-2020-0003", "CVE-2020-0004", "CVE-2020-0001", "CVE-2020-0005"]}

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response)
        self.assertDictEqual(response.json, expected_result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

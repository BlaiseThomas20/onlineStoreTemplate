import unittest
from app import app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_login(self):
        # send a POST request with valid login credentials
        response = self.client.post('/home', data={'username': 'myusername', 'password': 'mypassword'})
        
        # check if the response status code is 200
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    print('All tests passed!')
import unittest
import requests


class TestApp(unittest.TestCase):

    def test_a_base(self):
        responce = requests.get('http://localhost:5000')
        self.assertEqual(responce.status_code, 200)

   # def test_result(self):


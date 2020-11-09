import unittest
import requests
import json
from flask import jsonify 


class TestApp(unittest.TestCase):

    def test_a_base(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_result_neutral(self):

        params = {
            'Sentence': 'ok'
        }
        response = requests.post('http://localhost:5000/get_result', json=params)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.strip().replace('"', ''), "neutral")

    def test_result_positive(self):

        params = {
            'Sentence': 'nice'
        }
        response = requests.post('http://localhost:5000/get_result', json=params)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.strip().replace('"', ''), "positive")

    def test_result_negative(self):

        params = {
            'Sentence': 'worst'
        }
        response = requests.post('http://localhost:5000/get_result', json=params)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.strip().replace('"', ''), "negative")



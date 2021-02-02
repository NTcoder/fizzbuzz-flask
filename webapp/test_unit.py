from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")
import unittest
from unittest import mock
from flask_app import  app
import time
import json
import os

class test_Merge(unittest.TestCase):
    def setUp(self):
        self.test_client =  app.test_client(self)  

    def tearDown(self):
        pass

    def testfizz(self):

        payload = {
                "input": 12
            }
        response = self.test_client.post('/fizzbuzz', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("fizz",json.loads(response.data))
     
    def testbuzz(self):

        payload = {
                "input": 20
            }
        response = self.test_client.post('/fizzbuzz', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("buzz",json.loads(response.data))

    def testfizzbuzz(self):

        payload = {
                "input": 30
            }
        response = self.test_client.post('/fizzbuzz', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("fizzbuzz",json.loads(response.data))

    def testnone(self):

        payload = {
                "input": 11
            }
        response = self.test_client.post('/fizzbuzz', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("11",json.loads(response.data))

    def testIncorrect(self):

        payload = {
                "input": -1
            }
        response = self.test_client.post('/fizzbuzz', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(400, response.status_code)
        self.assertEqual("Invalid number",json.loads(response.data))
        
if __name__ == "__main__":
    unittest.main()
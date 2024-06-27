#!/usr/bin/env python3

import unittest
import sys
import os

# Directory of the 'api' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_404_error(self):
        response = self.app.get('/nonexistent_route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not found', response.data)

if __name__ == "__main__":
    unittest.main()

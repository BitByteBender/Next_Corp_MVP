#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("sys.path:", sys.path)

from api.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get('/corp_auth/register')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.app.get('/non_existent_page')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()

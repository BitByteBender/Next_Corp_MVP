#!/usr/bin/env python3

import unittest
import sys
import os

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

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_auth_register(self):
        response = self.app.get('/corp_auth/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_auth_login(self):
        response = self.app.get('/corp_auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_dashboard(self):
        response = self.app.get('/admin/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

if __name__ == "__main__":
    unittest.main()

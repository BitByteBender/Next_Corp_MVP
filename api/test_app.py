#!/usr/bin/env python3

import unittest
from flask import current_app
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
        self.assertIn(b'Welcome', response.data)  # Adjust according to the expected content

    def test_auth_register(self):
        response = self.app.get('/corp_auth/register')  # Adjust the route if necessary
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)  # Adjust according to the expected content

    def test_auth_login(self):
        response = self.app.get('/corp_auth/login')  # Adjust the route if necessary
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)  # Adjust according to the expected content

    def test_dashboard(self):
        response = self.app.get('/admin/dashboard')  # Adjust the route if necessary
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)  # Adjust according to the expected content

if __name__ == "__main__":
    unittest.main()

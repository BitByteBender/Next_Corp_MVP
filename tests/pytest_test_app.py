#!/usr/bin/env python3

import pytest
from api.app import app  # Adjust import path as per your structure

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_register_page(client):
    rv = client.get('/corp_auth/register')
    assert rv.status_code == 200

def test_404(client):
    rv = client.get('/non_existent_page')
    assert rv.status_code == 404

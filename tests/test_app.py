import os
import tempfile
import requests
import pytest
LOCALHOST = 'http://127.0.0.1:8080'
# TODO: Connect to testing database

# TODO: Test to make sure it is empty

def test_root_returns_200():
    response = requests.get(LOCALHOST)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
    response.
# def test_root_content_type():
#     response = requests.get


# def test_api_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200


# def test_root_returns_200():
#     response = requests.get(LOCALHOST)
#     assert response.status_code == 200

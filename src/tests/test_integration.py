
from unittest.mock import patch
import pytest

from .pytest_fixtures import client
from ..services import add_number, sample_10

def test_correct_response_sample(client):
    rv = client.get('/sample10')
    assert rv.status_code == 200

def test_correct_response_add(client):
    rv = client.post('/add', json={'number': "141"})
    assert rv.status_code == 200

def test_the_correct_number_is_added(client):
    rv = client.post('/add', json={'number': "777"})
    with open('numbers.txt', 'r') as f:
        last_line = int(f.readlines()[-1])
    assert last_line == 777

def test_200_response_even_when_file_is_empty(client):
    with open("numbers.txt", 'r+') as f:
        f.truncate()
    rv = client.get('/sample10')
    assert rv.status_code == 200

def test_200_response_even_when_input_is_string(client):
    rv = client.post('/add', json={'number': "hhi"})
    assert rv.status_code == 200

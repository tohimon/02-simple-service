
import pytest
import json
from simple_service import model

@pytest.fixture()
def test_data():
    return [1,3,2,5,4,6]

@pytest.fixture()
def invalid_input_data():
    return ['1','3','2','5','4','t']

def test_subtraction(test_data):
    assert model.subtraction(test_data) == [0,2,1,4,3,5]

def test_multiplication(test_data):
    json_data = '{"numbers": [1,3,2,5,4,6], "multiplication": 720}'
    json_obj = json.loads(json_data)
    assert (json_obj == model.multiplication(test_data))

def test_random(test_data):
    assert model.random_number(test_data) in test_data

def test_sort_ascending(test_data):
    assert model.sort_ascending(test_data) == [1,2,3,4,5,6]

def test_sort_descending(test_data):
    assert model.sort_descending(test_data) == [6,5,4,3,2,1]

def test_input_data_value_error(invalid_input_data):
    with pytest.raises(ValueError):
        model.parse(invalid_input_data)
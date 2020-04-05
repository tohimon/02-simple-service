
import pytest
from simple_service import service

@pytest.fixture()
def test_data_missing():
    return ['service.py']

@pytest.fixture()
def test_data_too_much_arguments():
    return ['service.py', '1', '2', '3', '4', '5', '6', '7']

def test_input_data_missing(test_data_missing):
        with pytest.raises(SystemExit) as exit_status:
            service.main(test_data_missing)
        assert exit_status.value.code == 1

def test_input_data_too_much_arguments(test_data_too_much_arguments):
        with pytest.raises(SystemExit) as exit_status:
            service.main(test_data_too_much_arguments)
        assert exit_status.value.code == 1
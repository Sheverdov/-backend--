from src.utils import loading_file, examination, sort_by_date, change_date, change_map
import os
from config import ROOT_DIR
import pytest

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 1, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]
@pytest.fixture
def operations_fixture():
    return operations

test_path = os.path.join(ROOT_DIR, 'test', 'test_operations.json')
def test_loading_file():
    assert loading_file(test_path) == []

def test_examination(operations_fixture):
    assert len(examination(operations_fixture)) == 3

def test_sort_by_date(operations_fixture):
    assert [i["id"] for i in sort_by_date(operations_fixture)] == [3, 2, 4, 1]

def test_change_date():
    assert change_date("2018-01-01T00:00:00.000000") == "01.01.2018"

def test_change_map():
    assert change_map("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert change_map("Счет 84163357546688983493") == "Счет **3493"

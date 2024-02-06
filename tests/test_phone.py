import pytest

from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("Nokia", 5000, 5, 1)


# Testcase number of sim
def test_number_of_sim(phone):
    assert phone.number_of_sim == 1


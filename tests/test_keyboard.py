import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard("ABC_5000", 3300, 10)


#Testcase change_lang
def test_change_lang(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"

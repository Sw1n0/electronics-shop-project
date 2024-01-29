import pytest
from src.item import Item

@pytest.fixture
# """Здесь надо написать тесты с использованием pytest для модуля item."""
def monitor():
    return Item("Монитор", 5000, 5)
def test_Item_calculate_total_price(monitor):

    assert monitor.calculate_total_price() == 25000

def test_Item_apply_discount(monitor):

    assert monitor.apply_discount() == None

import pytest
from src.item import Item
import os.path


@pytest.fixture
# """Здесь надо написать тесты с использованием pytest для модуля item."""
def monitor():
    return Item("Монитор", 5000, 5)


@pytest.fixture
def csv_file():
    return os.path.join("..", "src", "items.csv")


# TestCase Item calculate total price
def test_Item_calculate_total_price(monitor):

    assert monitor.calculate_total_price() == 25000


# TestCase apply discount
def test_Item_apply_discount(monitor):

    assert monitor.apply_discount() == None


# TestCase name
def test_Item_name(monitor):
    assert monitor.name == "Монитор"


# TestCase name.setter
def test_Item_name_setter(monitor):
    monitor.name = "СуперМоник"
    assert monitor.name == "СуперМоник"


# TestCase name.setter longer than 10
def test_Item_name_setter(monitor):
    monitor.name = "МоникСуперПупер"
    assert monitor.name == "МоникСупер"


# TestCase instantiate_from_csv
def test_instantiate_from_csv(csv_file):
    Item.all.clear()
    Item.instantiate_from_csv(csv_file)
    assert len(Item.all) == 5


# TestCase string_to_number
def test_string_to_number():
    assert Item.string_to_number("45.5") == 45


# TestCase __repr__
def test_repr(monitor):
    assert repr(monitor) == "Item('Монитор', 5000, 5)"


# TestCase __str__
def test_str(monitor):
    assert str(monitor) == "Монитор"

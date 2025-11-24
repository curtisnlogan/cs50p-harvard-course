import pytest

from fuel import convert, gauge


def test_fuel_y_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_fuel_numeric_only():
    with pytest.raises(ValueError):
        convert("A/4")


def test_fuel_negatives():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_fuel_int_only():
    with pytest.raises(ValueError):
        convert("4/1.5")


def test_fuel_x_greater_y():
    with pytest.raises(ValueError):
        convert("4/2")


def test_fuel_convert_rtn():
    assert convert("1/4") == 25


def test_fuel_percentage():
    assert gauge(12) == "12%"


def test_fuel_100():
    assert gauge(99) == "F"


def test_fuel_1():
    assert gauge(1) == "E"

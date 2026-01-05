import pytest

from working import convert


def test__not_raise_err():
    convert("9:00 PM to 1:00 AM")


def test_hour_greater_12():
    with pytest.raises(ValueError):
        convert("13:00 PM to 09:00 AM")


def test_min_greater_59():
    with pytest.raises(ValueError):
        convert("11:96 PM to 09:00 AM")


def test_hours_off_by_one():
    assert convert("10:24 AM to 12:35 AM") == ("10:24 to 00:35")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 1:00 PM")


def test_no_am_pm():
    with pytest.raises(ValueError):
        convert("9:00 AM to 1:00")


def test_missing_colon():
    with pytest.raises(ValueError):
        convert("900 AM to 1:00 PM")


def test_missing_min():
    with pytest.raises(ValueError):
        convert("9:0 AM to 1:00 PM")


def test_missing_hour():
    with pytest.raises(ValueError):
        convert(":00 AM to 1:00 PM")

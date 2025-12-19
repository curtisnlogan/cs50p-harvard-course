from numb3rs import validate


def test_leading_zeros():
    assert validate("0.25.150.01") is False


def test_missing_dots():
    assert validate("0.232.53") is False


def test_num_greater_255():
    assert validate("256.2.10.52") is False


def test_non_numeric_chars():
    assert validate("0.a2.50.150") is False


def test_five_octets():
    assert validate("0.12.25.12.150") is False

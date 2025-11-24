from plates import is_valid


def test_plates_first_2():
    assert is_valid("12") is False


def test_plates_less():
    assert is_valid("q") is False


def test_plates_numbers_middle():
    assert is_valid("AAA22A") is False


def test_plates_numbers_first_num():
    assert is_valid("uni0") is False


# with this test, i initially wasn't taking into account
# that it needs to be non-error causing in all other ways, asides from
# this one rule, which i am testing for
def test_plates_non_alnum():
    assert is_valid("aa dd1") is False

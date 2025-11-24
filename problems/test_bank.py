from bank import value


def test_bank_hello():
    assert value("hello") == 0


def test_bank_hllo():
    assert value("hllo") == 20


def test_bank_anything_else():
    assert value("universe") == 100


# overlooked testing for case insensitivity initially
# an example of an edge case
def test_bank_case_insensitive():
    assert value("HelLO") == 0

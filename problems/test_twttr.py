from twttr import shorten


def test_shorten_lower():
    assert shorten("universe") == "nvrs"


def test_shorten_upper():
    assert shorten("UNIVERSE") == "NVRS"


def test_shorten_n():
    assert shorten("1") == "1"


def test_shorten_punc():
    assert shorten(",") == ","

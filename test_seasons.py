import pytest

from seasons import convert_mins_to_words


def test_no_and():
    assert convert_mins_to_words(17098560) == (
        "Seventeen million, ninety-eight thousand, five hundred sixty minutes"
    )

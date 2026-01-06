import pytest

from um import count


def test_um_in_words():
    assert count("Um thumb") == 1


def test_only_spaces_um():
    assert count(" um um ,um,") == 3


def test_case_sensitive():
    assert count("UM um Um uM my thumb") == 4

from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity=12)
    assert jar.capacity == 12


def test_str():
    jar = Jar(capacity=12, size=12)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(capacity=12, size=9)
    jar.deposit(3)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(4)


def test_withdraw():
    jar = Jar(capacity=12, size=9)
    jar.withdraw(3)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(13)

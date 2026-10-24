import pytest

import boh
from boh.model import attributes


def test_valid_attribute():
    attributes(soul=1)


def test_invalid_attribute():
    with pytest.raises(ValueError):
        attributes(foo=1)

    with pytest.raises(ValueError):
        attributes(soul=0)


def test_has_attribute():
    assert attributes(soul=1).has("soul")
    assert not attributes(soul=1).has("thing")


def test_attribute_value():
    assert attributes(soul=1).value("soul") == 1
    assert attributes(soul=1).value("thing") == 0

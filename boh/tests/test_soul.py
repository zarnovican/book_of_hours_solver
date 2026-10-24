import boh
from boh.item import *
from boh.model import card, condition


def test_basic():
    s = card.for_(soul.chor)
    assert s.has_attribute("soul")
    assert s.contribute_power("grail") == 1
    assert s.contribute_power("sky") == 0


def test_fatigue():
    s = card.for_(soul.chor)
    assert not s.has_attribute("fatigued")
    assert s.contribute_power("heart") == 2
    s = s.fatigue()
    assert s.has_attribute("fatigued")
    assert s.contribute_power("heart") == 0
    s = s.recover()
    assert not s.has_attribute("fatigued")
    assert s.contribute_power("heart") == 2
    s = s.recover()
    assert not s.has_attribute("fatigued")
    assert s.contribute_power("heart") == 2


def test_malady():
    s = card.for_(soul.health)
    assert not s.has_attribute("malady")
    assert s.contribute_power("nectar") == 1
    s = s.malady()
    assert s.has_attribute("malady")
    assert s.contribute_power("nectar") == 0
    s = s.cure()
    assert not s.has_attribute("malady")
    assert s.contribute_power("nectar") == 1

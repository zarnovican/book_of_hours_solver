import boh
from boh.item import *
from boh.state import state


def test_soul():
    s = state()
    s.inventory_add(soul.chor, soul.health)

    chor = s.inventory_lookup(soul.chor)
    assert not (chor.has_attribute("fatigued") and chor.has_attribute("malady"))

    health = s.inventory_lookup(soul.health)
    assert not (health.has_attribute("fatigued") and health.has_attribute("malady"))

    s.fatigue(soul.chor)
    chor = s.inventory_lookup(soul.chor)
    assert chor.has_attribute("fatigued")

    s.malady(soul.health)
    health = s.inventory_lookup(soul.health)
    assert health.has_attribute("malady")

    s.recover(soul.chor)
    chor = s.inventory_lookup(soul.chor)
    assert not (chor.has_attribute("fatigued") and chor.has_attribute("malady"))

    s.cure(soul.health)
    health = s.inventory_lookup(soul.health)
    assert not (health.has_attribute("fatigued") and health.has_attribute("malady"))

import boh
from boh.item import *
from boh.model import card, condition, learning


def test_level1():
    s = card.for_(skill.anbary_and_lapidary)
    assert s.contribute_power("heart") == 0
    assert s.contribute_power("sky") == 2


def test_upgrade():
    s = card.for_(skill.anbary_and_lapidary)
    s = s.upgrade()
    s = s.upgrade()
    assert s.contribute_power("heart") == 0
    assert s.contribute_power("sky") == 4


def test_commit():
    s = card.for_(skill.purifications_and_exaltations)
    s = s.upgrade()

    lantern_before = s.contribute_power("lantern")
    sky_before = s.contribute_power("sky")
    assert s.has_attribute("illumination")
    assert s.has_attribute("ithastry")

    s = s.commit("illumination")
    soul_type = s.commit_output()

    assert s.contribute_power("lantern") == lantern_before
    assert s.contribute_power("sky")     == sky_before
    assert s.has_attribute("illumination")
    assert s.has_attribute("attuned_mettle")
    assert not s.has_attribute("ithastry")
    assert soul_type is soul.mettle


def test_fulfill():
    s = card.for_(skill.purifications_and_exaltations)
    s = s.upgrade()
    s = s.commit("illumination")

    lantern_before = s.contribute_power("lantern")
    sky_before = s.contribute_power("sky")
    assert s.has_attribute("attuned_mettle")
    assert not s.has_attribute("attunement_fulfilled")

    s = s.fulfill()

    assert s.contribute_power("lantern") == lantern_before
    assert s.contribute_power("sky")     == sky_before
    assert not s.has_attribute("attuned_mettle")
    assert s.has_attribute("attunement_fulfilled")


def test_condition_one_of():
    s = card.for_(skill.purifications_and_exaltations)
    c = condition(one_of=(skill.purifications_and_exaltations, ))
    assert c.match(s)
    s = s.upgrade()
    assert c.match(s)
    s = s.commit("illumination")
    assert c.match(s)


def test_condition_attribute():
    s = card.for_(skill.purifications_and_exaltations)
    c = condition(attuned_mettle=1)
    assert not c.match(s)
    s = s.upgrade()
    assert not c.match(s)
    s = s.commit("illumination")
    assert c.match(s)


def test_learning():
    assert learning.skill_for(lesson.inks_of_revelation)        is skill.inks_of_revelation
    assert learning.skill_for(lesson.lockworks_and_clockworks)  is skill.lockworks_and_clockworks

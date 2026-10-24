import boh
from boh.item import comfort, flower, leaf
from boh.model import and_condition, card, condition, match_any_card, match_no_card


def test_hash():
    a = condition(flower=1)
    b = condition(leaf=1)
    c = condition(flower=1)
    assert hash(a) == hash(c)
    assert hash(a) != hash(b)

    assert hash(condition(flower=1, leaf=1)) == hash(condition(leaf=1, flower=1))


def test_match_any():
    c = condition(flower=1, leaf=1)
    assert     c.match(card.for_(flower.catsclaw))
    assert     c.match(card.for_(leaf.potted_bamboo))
    assert not c.match(card.for_(comfort.atrium_chair))


def test_one_of():
    c = condition(one_of=(flower.blue_crown, flower.catsclaw))
    assert     c.match(card.for_(flower.catsclaw))
    assert     c.match(card.for_(flower.blue_crown))
    assert not c.match(card.for_(comfort.atrium_chair))


def test_or_():
    c = condition(one_of=(flower.blue_crown, ), comfort=1, leaf=1)
    assert     c.match(card.for_(flower.blue_crown))
    assert     c.match(card.for_(flower.catsclaw))
    assert     c.match(card.for_(comfort.atrium_chair))
    assert not c.match(card.for_(flower.agave_aeterna))


def test_trivial_match():
    assert     match_any_card.match(card.for_(flower.blue_crown))
    assert not match_no_card.match(card.for_(flower.blue_crown))


def test_and_condition():
    c = and_condition(leaf=1, flower=1)
    assert     c.match(card.for_(flower.catsclaw))
    assert not c.match(card.for_(flower.blue_crown))
    assert not c.match(card.for_(leaf.potted_bamboo))
    assert not c.match(card.for_(comfort.atrium_chair))

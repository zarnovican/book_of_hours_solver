import boh
from boh.item import flower, wall_art
from boh.model import card, opportunity


def test_opportunity():
    s = opportunity.slots_for("art_its_educational")[0]
    assert     s.match(card.for_(wall_art.a_sacrifice))
    assert not s.match(card.for_(flower.blue_crown))
    assert s.optional


def test_mood():
    s = opportunity.slots_for("awen")[0]
    awen_card = opportunity.mood_card_types_for("awen")[0]
    assert     s.match(card.for_(awen_card))
    assert not s.match(card.for_(flower.blue_crown))
    assert s.optional

import boh
from boh.item import flower, skill
from boh.model import condition, slot


def test_empty():
    assert slot().match(flower.catsclaw)


def test_cache_key():
    a = slot(essential=condition(flower=1))
    b = slot(essential=condition(leaf=1))
    c = slot(essential=condition(flower=1))
    assert a.cache_key == c.cache_key
    assert a.cache_key != b.cache_key


def test_essential():
    s = slot(essential=condition(flower=1))
    assert     s.match(flower.catsclaw)
    assert not s.match(skill.anbary_and_lapidary)


def test_essential_and_required():
    s = slot(essential=condition(flower=1), required=condition(edge=1))
    assert     s.match(flower.catsclaw)
    assert not s.match(flower.blue_crown)


def test_essential_and_forbidden():
    s = slot(essential=condition(flower=1), forbidden=condition(edge=1))
    assert     s.match(flower.blue_crown)
    assert not s.match(flower.catsclaw)

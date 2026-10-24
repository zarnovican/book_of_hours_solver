import boh
from boh.item import *
from boh.model import card, is_consumable, is_mystery_item


def test_hash():
    a = card.for_(device.dearday_lens)
    b = card.for_(device.dearday_lens)
    assert hash(a) != hash(b)


def test_is_consumable():
    for card_type in (
        assistance.barber,
        beverage.armagnac_dys_bottle,
        cache.abandoned_luggage,
        candle.aglaophotis_scented_candle,
        device.dearday_lens,
        employable.skulking_nearby_a_fugitive,
        flower.agave_aeterna,
        fruit.basket_of_apples,
        leaf.ch_second_flush_assam_packet,
        lesson.anbary_and_lapidary,
        liquid.amethyst_ampoule,
        mark.bisclavrets_knot,
        material.ambergris_chunk,
        memory.a_stolen_secret,
        memory.old_wound,
        remains.canned_ham,
        sustenance.basket_of_vegetables,
        weather.clouds,
    ):
        assert is_consumable(card_type)
        assert is_consumable(card.for_(card_type))

    for card_type in (
        codex.a_light_in_the_inkwell,
        comfort.ambroses_favourite_chair,
        tool.baron_silences_astrolabe,
    ):
        assert not is_consumable(card_type)
        assert not is_consumable(card.for_(card_type))


def test_is_mystery_item():
    for card_type in (
        codex.a_light_in_the_inkwell,
        #journal.a_drowned_book_fet_phost,
        scroll.the_fire_circle_tantra,
        phonograph_record.a_tower_falls,
        reel_of_film.colours_in_the_liver,
    ):
        assert is_mystery_item(card_type)

    for card_type in (
        memory.a_stolen_secret,
        lesson.anbary_and_lapidary,
    ):
        assert not is_mystery_item(card_type)

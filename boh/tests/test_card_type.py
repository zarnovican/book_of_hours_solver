import boh
from boh.item import *
from boh.model import card_type
from boh.state import perish_at_dawn


def test_perish_at_dawn():
    assert perish_at_dawn(assistance.barber)
    assert perish_at_dawn(employable.skulking_nearby_a_fugitive)
    assert perish_at_dawn(memory.a_stolen_secret)
    assert perish_at_dawn(weather.clouds)

    assert not perish_at_dawn(memory.old_wound)
    assert not perish_at_dawn(lesson.anbary_and_lapidary)
    assert not perish_at_dawn(beverage.armagnac_dys_bottle)


def test_str():
    assert str(an_introduction.blacksmith) == "an_introduction.blacksmith"
    assert str(assistance.blacksmith) == "assistance.blacksmith"
    assert str(beast.chimeric_larva) == "beast.chimeric_larva"
    assert str(beverage.armagnac_dys_bottle) == "beverage.armagnac_dys_bottle"
    assert str(cache.abandoned_luggage) == "cache.abandoned_luggage"
    assert str(candle.aglaophotis_scented_candle) == "candle.aglaophotis_scented_candle"
    assert str(codex.a_light_in_the_inkwell) == "codex.a_light_in_the_inkwell"
    assert str(comfort.ambroses_favourite_chair) == "comfort.ambroses_favourite_chair"
    assert str(device.dearday_lens) == "device.dearday_lens"
    assert str(employable.skulking_nearby_a_fugitive) == "employable.skulking_nearby_a_fugitive"
    assert str(fixed_in_place.stained_glass_window_the_madrugad) == "fixed_in_place.stained_glass_window_the_madrugad"
    assert str(flower.agave_aeterna) == "flower.agave_aeterna"
    assert str(fruit.basket_of_apples) == "fruit.basket_of_apples"
    assert str(incident.the_affair_of_the_oriflamme_heist) == "incident.the_affair_of_the_oriflamme_heist"
    assert str(journal.a_drowned_book) == "journal.a_drowned_book"
    assert str(leaf.ch_second_flush_assam_packet) == "leaf.ch_second_flush_assam_packet"
    assert str(lesson.anbary_and_lapidary) == "lesson.anbary_and_lapidary"
    assert str(liquid.amethyst_ampoule) == "liquid.amethyst_ampoule"
    assert str(mark.bisclavrets_knot) == "mark.bisclavrets_knot"
    assert str(material.ambergris_chunk) == "material.ambergris_chunk"
    assert str(memory.a_stolen_secret) == "memory.a_stolen_secret"
    assert str(notype.a_letter_to_the_librarian) == "notype.a_letter_to_the_librarian"
    assert str(pence.crown) == "pence.crown"
    assert str(phonograph_record.a_tower_falls) == "phonograph_record.a_tower_falls"
    assert str(reel_of_film.colours_in_the_liver) == "reel_of_film.colours_in_the_liver"
    assert str(remains.canned_ham) == "remains.canned_ham"
    assert str(scroll.the_fire_circle_tantra) == "scroll.the_fire_circle_tantra"
    assert str(skill.anbary_and_lapidary) == "skill.anbary_and_lapidary"
    assert str(soul.chor) == "soul.chor"
    assert str(soul_option.chor) == "soul_option.chor"
    assert str(sustenance.basket_of_vegetables) == "sustenance.basket_of_vegetables"
    assert str(tally.bronze_spintria) == "tally.bronze_spintria"
    assert str(thing.abbot_geffrey) == "thing.abbot_geffrey"
    assert str(tool.baron_silences_astrolabe) == "tool.baron_silences_astrolabe"
    assert str(uncatalogued.uncatalogued_book_baronial) == "uncatalogued.uncatalogued_book_baronial"
    assert str(visitor.dr_ibn_al_adim) == "visitor.dr_ibn_al_adim"
    assert str(wall_art.a_sacrifice) == "wall_art.a_sacrifice"
    assert str(weather.clouds) == "weather.clouds"

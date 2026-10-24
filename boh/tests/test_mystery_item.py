from boh.item import codex, lesson, reel_of_film, skill, uncatalogued
from boh.model import card, cataloguing, condition, language, mastering


def test_not_mastered():
    i = card.for_(codex.a_light_in_the_inkwell)
    assert not i.is_mastered()


def test_language():
    i = card.for_(codex.a_novel_method_for_invocation_and_contrition)
    assert i.language() == "ericapaean"


def test_unlockable():
    i = card.for_(codex.a_light_in_the_inkwell)
    assert i.unlockable()


def test_uncatalogued():
    assert cataloguing.uncatalogued_for(codex.a_light_in_the_inkwell)                         is uncatalogued.uncatalogued_book_baronial
    assert cataloguing.uncatalogued_for(codex.a_novel_method_for_invocation_and_contrition)   is uncatalogued.uncatalogued_book_curia
    assert cataloguing.uncatalogued_for(codex.on_matthias_and_the_amethyst_imago_pursuit)     is uncatalogued.uncatalogued_book_dawn
    assert cataloguing.uncatalogued_for(codex.an_exorcists_field_manual)                      is uncatalogued.uncatalogued_book_nocturnal
    assert cataloguing.uncatalogued_for(codex.a_second_glory)                                 is uncatalogued.uncatalogued_book_solar

    # exceptions
    assert cataloguing.uncatalogued_for(codex.key_of_night)                is uncatalogued.uncatalogued_book_curia
    assert cataloguing.uncatalogued_for(codex.the_radical_measure_glossed) is uncatalogued.uncatalogued_book_curia


def test_mastering():
    assert mastering.lessons_from(codex.a_light_in_the_inkwell)             == (lesson.inks_of_revelation, lesson.inks_of_revelation)
    assert mastering.lessons_from(codex.a_true_history_of_valentine_dewulf) == (lesson.furs_and_feathers, )
    assert mastering.lessons_from(reel_of_film.colours_in_the_liver)        == (lesson.resurgences_and_emergences, )


def test_language():
    assert language.name_from_item(codex.a_light_in_the_inkwell)                        == "english"
    assert language.name_from_item(codex.a_novel_method_for_invocation_and_contrition)  == "ericapaean"
    assert language.name_from_item(codex.bancroft_diaries)                              == "latin"

    assert language.skill_for("cracktrack") is skill.cracktrack

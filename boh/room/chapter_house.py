from ..item import beverage, candle, liquid, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Desk: Nonna
#
# Abbess Nonna, apothecary, scholar, dancer.
desk_nonna = station("desk_nonna",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, heart=1, lantern=1, nectar=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, heart=1, lantern=1, nectar=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, heart=1, lantern=1, nectar=1),
        ),
        slot(
            required=condition(readable=1, blank=1),
            forbidden=condition(phonograph_record=1, reel_of_film=1),
        ),
        slot(
            required=condition(tool=1, ink=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Echoing Chamber
#
# This has long been a holy place, but the voices of the monks have outlasted their prayers. A surly muttering circles the room, picking up speed as it goes. Each time it passes me, it almost manages to articulate my name.
# ---
# Chapter House
#
# Here the monastic superiors would meet to manage the affairs of St Brandan's and to resolve its disputes. Here in 1349, the last trial of the last nuns of St Brandan's took place. Two were executed for the murder of Abbess Nonna, supposedly with 'perversions of the healing arts'. Nonna was the last abbess of St Brandan's, and after the trial, the monastery never accepted female novices again. From the wide windows, the sea is always visible, beating on the rocks far below.
chapter_house = room("chapter_house",
    attributes(solar_gothic_period=1),
    inventory = (
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_pot,
        candle.tall_candlestick,
        candle.tall_candlestick,
        liquid.perhibiate,
        thing.quire_of_paper,
        thing.white_matilda,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
    ),
    neighbors = ("windlit_gallery", ),
    power_requirements = attributes(lantern=9, moon=9, winter=9),
    stations = (
        desk_nonna,
    ),
)

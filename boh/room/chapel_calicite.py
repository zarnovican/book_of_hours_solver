from ..item import beverage, candle, material, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Calicite Altar
#
# The Red Grail, birth and appetite, denied and condemned by the clergy of the Sun for her temptress-role in the Sun's division. Those of us who oppose Eternity might instead give her thanks and praise. But cautiously.
calicite_altar = station("calicite_altar",
    attributes(evolve_via_bosk=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, heart=1, moon=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, heart=1, moon=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, heart=1, moon=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, omen=1, mark=1, beverage=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(woven=1, memory=1, flower=1, remains=1, beverage=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# A Red Forbidding
#
# Crimson mists beckon and sway.
# ---
# Chapel Calicite
#
# The Red Grail says: Never speak of this Mystery. I was always the first, and I must always be greatest. When we spilt the blood of the Thunderskin, I feasted and I grew strong, stronger again than the Twins. There is always a feast, and nothing is truly wasted.
chapel_calicite = room("chapel_calicite",
    attributes(dawn_period=1),
    inventory = (
        beverage.lambig_broceliande_chalice,
        beverage.sacrament_calicite,
        candle.widows_candle,
        candle.widows_candle,
        candle.widows_candle,
        candle.widows_candle,
        material.ambergris_chunk,
        thing.bobos_of_spring,
        thing.goddess_who_changes_skin,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("hall_of_voices", ),
    power_requirements = attributes(grail=14, nectar=14),
    stations = (
        calicite_altar,
    ),
)

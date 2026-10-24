from ..item import material, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Altar: Ascite
#
# The Horned-Axe, who opens the way and keeps the threshold, is accounted the last of the Gods-from-Stone.
altar_ascite = station("altar_ascite",
    attributes(evolve_via_nyctodromy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, knock=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, knock=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, knock=1, scale=1, winter=1),
        ),
        slot(
            required=condition(soul=1, tool=1, omen=1, mark=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(tool=1, memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# A Wintry Forbidding
#
# Icy mists coil and drift.
# ---
# Chapel Ascite
#
# The Horned-Axe says: Never speak of this Mystery. When the Thunderskin was mortal, he served the Hours who slew my kind. I required the Thunderskin's death, and so the Grail gave him up. There is always a reckoning, and nothing is truly forgiven.
chapel_ascite = room("chapel_ascite",
    attributes(dawn_period=1),
    inventory = (
        material.granite_slab,
        material.serpentinite_slab,
        thing.cat_of_depths,
        thing.owl_of_spirals,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("chapel_calicite", ),
    power_requirements = attributes(edge=14, knock=14),
    stations = (
        altar_ascite,
    ),
)

from ..item import beast, comfort, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Cage
#
# Valentine Dewulf put his only friends in cages. Did he close the cage doors?
cage = station("cage",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            required=condition(co_operative=1, sustenance=1, beverage=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(co_operative=1, sustenance=1, beverage=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Howling Chamber
#
# Great chunks have been torn from the walls of this room. The wind roams the place like a trapped beast, battering to and fro.
# ---
# Gullscry Tower: Eales' Room
#
# Eales Dewulf inherited his father Valentine's madness, and was found unfit to inherit, so his sister Eva held the Isle in his stead. When his fits of violence became uncontrollable, he was confined here in the tower, where his sister would visit him three times a week - until his escape, some time in the late 1720s. Eales's ultimate fate remains unknown.
gullscry_tower_eales_room = room("gullscry_tower_eales_room",
    attributes(baronial_period=1),
    inventory = (
        beast.stymphling,
        comfort.restful_garden_chair,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        wall_art.the_watcher,
    ),
    neighbors = ("gullscry_tower_valentines_room", ),
    power_requirements = attributes(knock=11, sky=11, winter=11),
    stations = (
        cage,
    ),
)

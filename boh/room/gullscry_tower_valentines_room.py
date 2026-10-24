from ..item import beast, comfort, liquid, sustenance, wall_art
from ..model import attributes, condition, room, slot, station


# Gullscry Workbench
#
# Labour solemnly.
gullscry_workbench = station("gullscry_workbench",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, knock=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, knock=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, knock=1, sky=1, winter=1),
        ),
        slot(
            required=condition(made_of_wood=1, wood=1, woven=1, remains=1, tool=1, ductile=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(wood=1, tool=1, remains=1, ductile=1, made_of_wood=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Weeping Chamber
#
# Water trickles like tears from broken pipes in the ceiling, splashing over the cages that hang here. The floor is inches deep in water. The wind flutters mournfully in the cage bars.
# ---
# Gullscry Tower: Valentine's Room
#
# In his youth, Baron Valentine inclined to religion, and he made pilgrimages to holy sites on the Continent. After he made his final pilgrimage - to Fermier Abbey - the dreams began - of blood seeping from the earth; of a vast and pulsing Wheel crushing the temples of men; and, which troubled him most, of twisted birds, shrieking in pain, growing like fruit in the branches of an ancient yew.
gullscry_tower_valentines_room = room("gullscry_tower_valentines_room",
    attributes(baronial_period=1),
    inventory = (
        beast.magnificent_green_cockatoo,
        comfort.painters_stool,
        comfort.soft_blue_sofa,
        liquid.paint_palest_blue,
        liquid.paint_red,
        sustenance.gulls_egg,
        sustenance.outsized_egg,
        wall_art.chac,
        wall_art.departure,
    ),
    neighbors = ("gullscry_loggia", ),
    power_requirements = attributes(forge=10, heart=10, sky=10),
    stations = (
        gullscry_workbench,
    ),
)

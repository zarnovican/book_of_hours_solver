from ..item import beverage, candle, flower, material
from ..model import attributes, condition, room, slot, station


# Catacombs Altar
#
# 'BONE IS THE MEMORY THAT DOES NOT DIE.'
catacombs_altar = station("catacombs_altar",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moon=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moon=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moon=1, scale=1, winter=1),
        ),
        slot(
            required=condition(soul=1, omen=1, remains=1, mark=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, remains=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Rattling Tunnels
#
# The dead do not walk here; but their eyes are upon me. I can quell them, or I can feed them.
# ---
# Catacombs
#
# In the days of honey, those who remembered brought the bones of their dead to the grey rock in the sea. In the time of the Eagles, those who remembered brought the bones of their dead to the grey rock in the sea. In the time of the Bear-king, the clans brought the bones of their dead to the grey rock in the sea. When the Wolf-kings came, those who remembered brought the bones of their dead to the grey rock in the sea. Through all the years of Sun and Bronze, those who remembered brought the bones of their dead to the grey rock in the sea. Much is taken; much abides.
catacombs = room("catacombs",
    attributes(dawn_period=1),
    inventory = (
        beverage.lambig_broceliande_chalice,
        beverage.sacrament_ascite,
        candle.widows_candle,
        candle.widows_candle,
        flower.evas_locks,
        material.atlantic_amber,
        material.sea_glass,
    ),
    neighbors = ("columbic_crypt", ),
    power_requirements = attributes(grail=15, winter=15),
    stations = (
        catacombs_altar,
    ),
)

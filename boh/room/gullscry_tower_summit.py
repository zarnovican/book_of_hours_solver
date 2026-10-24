from ..item import beverage, comfort, leaf, material
from ..model import attributes, condition, room, slot, station


# Tower-Top Prospect
#
# Remember what has passed.
tower_top_prospect = station("tower_top_prospect",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(sky=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(sky=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(sky=1, winter=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, blank=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, pigment=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Screaming Summit
#
# Here the wind's rage is so great that I can barely stand upright. It forces me to retreat back to the stairs. I can hear the voice in the wind now, crying out in sorrow as great as the wind's rage.
# ---
# Gullscry Tower: Summit
#
# In 1721, Valentine fell - or leapt - from the tower top. There were no witnesses, and his body was not found for three days. His daughter Eva was the last to see him alive, and of their last conversation, she would say only that he had begun to fear the sun.
gullscry_tower_summit = room("gullscry_tower_summit",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        comfort.valentines_memorial,
        leaf.potted_avidity,
        material.atlantic_amber,
        material.granite_slab,
    ),
    neighbors = ("gullscry_tower_eales_room", ),
    power_requirements = attributes(rose=12, sky=12, winter=12),
    stations = (
        tower_top_prospect,
    ),
)

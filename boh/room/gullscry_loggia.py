from ..item import beverage, comfort, flower, liquid
from ..model import attributes, condition, room, slot, station


# Loggia Prospect
#
# Take counsel with the seas.
loggia_prospect = station("loggia_prospect",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moon=1, rose=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moon=1, rose=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moon=1, rose=1),
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


# Squawkful Loggia
#
# Birds crowd every corner of this place, glaring at me with malevolent yellow eyes. Guano cakes the walls and feathers drift the floor. Something has drawn them here - it'll need to be dealt with. Once it has, the place will take an awful lot of cleaning.
# ---
# Gullscry Loggia
#
# When Baron Valentine's melancholia and his acusis became too much to bear, he began to take his meals here, with none of those sounds that he found troubling - only the wind, the sea, and the cries of his beloved birds. After the Dewulfs were gone, the Librarians of the Curia would come here when they needed to think in peace.
gullscry_loggia = room("gullscry_loggia",
    attributes(baronial_period=1),
    inventory = (
        beverage.armagnac_dys_bottle,
        beverage.armagnac_dys_glass,
        comfort.comfortable_garden_chair,
        comfort.snug_chair,
        flower.shadowless_silk,
        liquid.asimel,
    ),
    neighbors = ("vestibulum_transitus", ),
    power_requirements = attributes(rose=9, sky=9),
    stations = (
        loggia_prospect,
    ),
)

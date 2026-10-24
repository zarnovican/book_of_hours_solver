from ..item import beverage, flower, liquid
from ..model import attributes, condition, room, station, slot


# Chrysalis
#
# Something might emerge, if it could only be assured of a hospitable History. Until that time, its dreams might be audible to one who presses an ear against its trembling, sky-scented warmth.
chrysalis = station("chrysalis",
    attributes(evolve_via_bosk=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, moth=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, moth=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, moth=1, nectar=1, scale=1),
        ),
        slot(
            required=condition(soul=1, liquid=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, liquid=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Mazed Cell
#
# A leathery burgundy mesentery has spread out of and around the doorway of this cell. Chitin? Fungus? It crumbles beneath my hands, emitting choking fumes. It will be impossible to enter the cell without clearing it.
# ---
# Cell: ?
#
# This was the last prisoner to be admitted to the Gaol, but only the date has been recorded. No record of its origin, crime, or arrest remains. Collers was a man of many secrets. Sometimes, however, he was also a generous man, and he insisted it be provided with a bed and with writing materials, should it ever feel the need for them.
cell_question = room("cell_question",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.rubywise_ruin,
        flower.vase_of_lilies,
        liquid.asimel,
    ),
    neighbors = ("crucible_tower_governors_office", ),
    power_requirements = attributes(grail=14, moth=14, scale=14),
    stations = (
        chrysalis,
    ),
)

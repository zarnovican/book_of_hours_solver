from ..item import beverage, comfort, uncatalogued
from ..model import attributes, condition, room, slot, station


# Telescope
#
# The scholars of the House watched the courses of the stars to determine their pasts and understand their future.
telescope = station("telescope",
    attributes(evolve_via_horomachistry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, moon=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, moon=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, moon=1, rose=1, sky=1),
        ),
        slot(
            required=condition(soul=1, lens=1, tool=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(lens=1, memory=1, tool=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Watchman's Tower: Top Floor
#
# The ceiling bows worryingly under a damp patch. There must be a leak in the observatory. The Sun above knows what state it's in. I should seek help, and enter carefully.
# ---
# Watchman's Tower: Observatory
#
# Thomas Dewulf, second Baron Brancrug, who they called 'Baron Silence', built this observatory in 1576 - by happy coincidence, just in time to observe the passage of the Great Comet in 1577.
watchmans_tower_observatory = room("watchmans_tower_observatory",
    attributes(baronial_period=1),
    neighbors = ("watchmans_tower_first_floor", ),
    inventory = (
        beverage.mist_kissed_water_glass,
        comfort.kittys_armchair,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
    ),
    power_requirements = attributes(grail=2, sky=2),
    stations = (
        telescope,
    ),
)

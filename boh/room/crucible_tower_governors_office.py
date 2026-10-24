from ..item import liquid, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Desk: Governor
#
# A desk as severe and as practical as Collers himself.
desk_governor = station("desk_governor",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, forge=1, lantern=1, moth=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, forge=1, lantern=1, moth=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, forge=1, lantern=1, moth=1),
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


# Smoky Chamber
#
# The room is almost untouched, but little fires still burn here, blithely ignoring the absence of fuel, filling the room with seven years of smoke.
# ---
# Crucible Tower: Governor's Office
#
# The Governor's office - quietly luxurious, at least by the standards of the Cucurbit. Collers was devoted to his cause and his service, but he did insist on his little pleasures.
crucible_tower_governors_office = room("crucible_tower_governors_office",
    attributes(nocturnal_period=1),
    inventory = (
        liquid.catwink,
        thing.quire_of_paper,
        thing.sir_david_greene,
        tool.typewriter,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.genealogical_chart,
    ),
    neighbors = ("staff_room", ),
    power_requirements = attributes(forge=12, heart=12),
    stations = (
        desk_governor,
    ),
)

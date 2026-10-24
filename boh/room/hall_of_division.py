from ..item import flower, thing, wall_art
from ..model import attributes, condition, room, slot, station


# Mirrors
#
# It was often said of Lady Eva, later, that she was always good with mirrors.
mirrors = station("mirrors",
    attributes(evolve_via_nyctodromy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, knock=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, knock=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, knock=1, lantern=1, winter=1),
        ),
        slot(
            required=condition(soul=1, light=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, light=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Silvered Snares
#
# The mirrors in this room teem with watchful spirits and perilous reflections. They can be mollified and banished, but only a fool would attempt a solitary exorcism of a room where all the haunts are doubled.
# ---
# Hall of Division
#
# Eva Dewulf first furnished this as her Hall of Division, holding feasts where the guests were selected by unusual and exacting criteria. Later, Thirza Blake, seventh Librarian, employed the speculist Poemander to add more mirrors. <i>Lots</i> more mirrors.
hall_of_division = room("hall_of_division",
    attributes(curia_period=1),
    inventory = (
        flower.vase_of_amaryllis,
        flower.vase_of_amaryllis,
        thing.hendriks_blade,
        wall_art.eva_and_abraham_1724,
    ),
    neighbors = ("fludd_gallery", ),
    power_requirements = attributes(edge=8, winter=8),
    stations = (
        mirrors,
    ),
)

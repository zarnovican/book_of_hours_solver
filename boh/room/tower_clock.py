from ..item import liquid
from ..model import attributes, condition, room, slot, station


# Great Clock
#
# Every flame has its fuel, and every tick has its tock.
great_clock = station("great_clock",
    attributes(evolve_via_horomachistry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
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
            required=condition(soul=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Stopped Clock
#
# With maniacal but methodical care, someone has disassembled the clock and scattered it round the room. Wheels and parts have been piled and leant on every surface. A W has been marked on the stairs in soot.
# ---
# Tower Clock
#
# George Collers, governor of Brancrug Gaol, oversaw the design and installation of this great clock, with the reluctant help of the Librarian Serena Blackwood. She might have refused outright, had she known how he intended to reuse the horologist's techniques for his so-called 'condignator'.
#
# An inscription on the greatest wheel reads 'STRIKE THE HOURS'.
tower_clock = room("tower_clock",
    attributes(solar_gothic_period=1),
    inventory = (
        liquid.umbrous_oil,
    ),
    neighbors = ("church_tower", ),
    power_requirements = attributes(forge=10, sky=10, winter=10),
    stations = (
        great_clock,
    ),
)

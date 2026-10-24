from ..item import cache, candle, fruit, mark, thing, tool
from ..model import attributes, condition, room, slot, station


# Instrument: Piano
#
# A gift from Kitty Mazarine, who would sometimes pop by of an evening to sing. But her successor Solomon, never one for music, disliked the way its notes would drift up the stairs to the Reading Room, and forbade the staff to play their piano before sunset.
instrument_piano = station("instrument_piano",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            required=condition(soul=1, sound=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Loom
#
# 'And there the golden threads they wove - and in the Moon's House, fast they tied them' - from the Lay of Helgi Hundingsbane
loom = station("loom",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, moth=1, nectar=1, rose=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, moth=1, nectar=1, rose=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, moth=1, nectar=1, rose=1),
        ),
        slot(
            required=condition(fabric_and_fibre=1),
            forbidden=condition(fatigued=1),
            consume_all=True,
        ),
        slot(
            required=condition(fabric_and_fibre=1),
            forbidden=condition(fatigued=1),
            consume_all=True,
        ),
    ),
)


# Ruinous Hall
#
# This place was bright and busy once. It can be again. But it'll be gruelling work to make it so - not suitable work for a Librarian.
# ---
# Servants' Hall
#
# Hendrik Dewulf, 1st Baron Brancrug, was granted Hush House after the dissolution of St Brandan's by 'Old Coppernose', King Henry VIII. In an act of unusual generosity for that tight-fisted King, the grant came with the title of Baron, and rights <i>sicut regale</i> - 'like a king', the quasi-independence traditionally accorded to Marcher Lords. Hendrik was clearly determined to live as befitted his new rank, and he expanded the house accordingly to support sufficient staff.
servants_hall = room("servants_hall",
    attributes(baronial_period=1),
    inventory = (
        cache.contraband_flotsam,
        cache.slim_parcel,
        candle.moth_orchid_scented_candle,
        candle.widows_candle,
        candle.widows_candle,
        fruit.misshapen_fruit,
        mark.midnight_mark,
        thing.inscribed_clock,
        thing.pigeon_statuette,
        thing.warmly_coloured_yarns,
        tool.bronze_knife,
    ),
    neighbors = ("grand_ascent_ground_floor", ),
    power_requirements = attributes(heart=5, scale=5),
    stations = (
        instrument_piano,
        loom,
    ),
)

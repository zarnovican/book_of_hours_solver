from ..model import attributes, condition, room, slot, station


# Instrument: Bells
#
# 'These are the sounds which may answer thunder.'
instrument_bells = station("instrument_bells",
    attributes(evolve_via_ithastry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, sky=1),
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


# Fallen Bells
#
# Someone has smashed the headstocks of the bells so that they fell to the floor here. The stone is cracked beneath them - the noise must have been unbearable. One has fallen against the stairs to the tower top.
# ---
# Bells
#
# Giver, Teller, Shur's Tongue, Lady Janice and Great Paycock are the names of these bells, though they're older than the Abbey itself and those names have certainly been corrupted over the years. By 1915, Shur's Tongue and Lady Janice were too cracked to ring, and the Suppression Bureau paid for them to be recast - Serena Blackwood's <i>quid pro quo</i> for the assistance she gave George Collers with his clock project.
bells = room("bells",
    attributes(solar_gothic_period=1),
    neighbors = ("tower_clock", ),
    power_requirements = attributes(forge=11, heart=11, sky=11),
    stations = (
        instrument_bells,
    ),
)

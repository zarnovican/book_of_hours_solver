from ..item import thing
from ..model import attributes, condition, room, station, slot


# Instrument: Hallowed Drum
#
# Celebrate the god of joy - with your own joy!' - The Bacchae
#
#  [The skin of these drums was the skin of something rare.]
instrument_hallowed_drum = station("instrument_hallowed_drum",
    attributes(evolve_via_preservation=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, sky=1),
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


# Instrument: Grand Piano
#
# 'Simplicity is the final achievement. After one has played a vast quantity of notes and more notes, it is simplicity that emerges as the crowning reward of art.' - Fryderyk Chopin
instrument_grand_piano = station("instrument_grand_piano",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(rose=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(rose=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(rose=1, sky=1),
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


# Instrument: Sunset Harp
#
# 'I have been a string in a harp; disguised for nine years in water, in the foam of the sea.' - The Battle of the Trees
#
#  [This harp is strung with something that glimmers redly as waves at sunset.]
instrument_sunset_harp = station("instrument_sunset_harp",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, evolve_via_birdsong=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moon=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moon=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moon=1, sky=1),
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


# Instrument: Quivering Double Bass
#
# 'The better it gets, the fewer of us know it.' - Ray Brown
#
#  [This instrument is possessed of a restless energy.]
instrument_quivering_double_bass = station("instrument_quivering_double_bass",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, evolve_via_birdsong=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, sky=1),
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


# Reeking Chamber
#
# The room reeks like a rotting reptile. The curtains ripple restlessly with the watchful presences that van Lauren left behind. Perhaps I can find someone to sing them to sleep.
# ---
# Mazarine Room
#
# 'Kitty's pride, and the House's joy.' Kitty Mazarine was better known for her vocal compositions, but she was a versatile musician, and on winter evenings she'd invite visitors and villagers alike to her recitals.
mazarine_room = room("mazarine_room",
    attributes(curia_period=1),
    inventory = (
        thing.kitty_mazarine,
    ),
    neighbors = ("reading_room", ),
    power_requirements = attributes(heart=6, sky=6),
    stations = (
        instrument_grand_piano,
        instrument_hallowed_drum,
        instrument_quivering_double_bass,
        instrument_sunset_harp,
    ),
)

from ..model import attributes, condition, room, slot, station


# Sacred Spring
#
# Here a pilgrim would bathe, make offerings, or drown, as they might prefer.
sacred_spring = station("sacred_spring",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, moon=1, nectar=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, moon=1, nectar=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, moon=1, nectar=1),
        ),
        slot(
            required=condition(soul=1, remains=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, remains=1, pigment=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Wheel-Filled Spring
#
# The pool here is filled with rusting and rotting wheels. Was this some attempt to block it? Or were the wheels thrown down the well above as offerings? In either case, it'll need to be cleaned out, and suitable offerings made to appease the powers to whom this place is holy.
# ---
# Sacred Spring
#
# The Eye marked on the rocks here is not the Watchman's Eye that decorates the church above, but the Eye that marks the Temple of the Wheel in dreams. The priests of the Sun would tell you there was no sight before the rising of the Sun; but those who've drunk from this spring will dream of another sun, one that swung lower in the sky, one that would speak with us, one that would accept friendly gifts of blood from us.
sacred_spring = room("sacred_spring",
    attributes(dawn_period=1),
    neighbors = ("deep_well_descent", ),
    power_requirements = attributes(moon=10, nectar=10),
    stations = (
        sacred_spring,
    ),
)

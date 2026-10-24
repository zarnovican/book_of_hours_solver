from ..model import attributes, condition, room, slot, station


# Exercise Yard
#
# The prisoners in the Cucurbit were permitted to grow neither too strong, nor too weak. Here they were subjected to an exacting regime which developed both their bodies and their souls, in accordance with the Governor's designs.
exercise_yard = station("exercise_yard",
    attributes(evolve_via_ithastry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, heart=1, knock=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, heart=1, knock=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, heart=1, knock=1, winter=1),
        ),
        slot(
            required=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Blackened Yard
#
# A ferocious heat has scorched, even melted, the stones. But as at the bridge, it's only here and there. Horribly, 'here' and 'there' mostly seem to be where people happened to be standing. Charred, cracked bones scatter the yard.
gaol_yard = room("gaol_yard",
    attributes(nocturnal_period=1),
    neighbors = ("lesser_bridge", ),
    power_requirements = attributes(grail=10, heart=10, winter=10),
    stations = (
        exercise_yard,
    ),
)

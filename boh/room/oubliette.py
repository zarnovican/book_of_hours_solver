from ..model import attributes, condition, room, slot, station


# Oubliette Containment
#
# Fire, iron, dusk, air, all wrenched into a configuration designed to confine something very dangerous. That something is long-gone, but the configuration still has its uses.
oubliette_containment = station("oubliette_containment",
    attributes(evolve_via_ithastry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, forge=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, forge=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, forge=1, lantern=1, winter=1),
        ),
        slot(
            required=condition(soul=1, fuel=1, gem=1, remains=1, metal=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(gem=1, memory=1, remains=1, metal=1, fuel=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Incandescent Hollow
#
# Sullen heat still roils below. Its originator must be long gone, but it must be quelled before I can descend safely.
# ---
# Oubliette
#
# Here in a vessel shaped by fire and fate, George Collers confined a flame in human flesh, a blazing shadow of a blazing future, a Name of greed and time. Greene called it 'the Sun's bastard grandchild.' Van Lauren warned of 'the Second Dawn's first spark'. But Collers spoke of it reverently: as 'the Leashed Flame's true heir'.
oubliette = room("oubliette",
    attributes(nocturnal_period=1),
    neighbors = ("gaol_cellar", ),
    power_requirements = attributes(forge=15, knock=15, winter=15),
    stations = (
        oubliette_containment,
    ),
)

from ..model import attributes, condition, room, slot, station


# Altar: St Tentreto
#
# Saint Tentreto of the Deep Door, who is four times winged: for the Scīmafectra-kind; the Glaeterfleoge-kind; the Thritige-kind; for the kind-within.
altar_st_tentreto = station("altar_st_tentreto",
    attributes(evolve_via_horomachistry=1, evolve_via_nyctodromy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(knock=1, moon=1, moth=1, scale=1),
        ),
        slot(
            required=condition(soul=1, memory=1, blank=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, liquid=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Pulsing Darkness
#
# If the Isle had a heart, we would hear its pulse.
# ---
# Shrine to St Tentreto
#
# The Carapace Cross, the hybrid race who in their many kinds were winged, legged, eyed, bright, dark, scaled, feathered, chitinous... and us? The Cross are gone; the Cross were always History; but to their children, their enemies, they leave this hushed legacy.
shrine_to_st_tentreto = room("shrine_to_st_tentreto",
    attributes(dawn_period=1),
    neighbors = ("deeplight_caves", ),
    power_requirements = attributes(moth=15, scale=15),
    stations = (
        altar_st_tentreto,
    ),
)

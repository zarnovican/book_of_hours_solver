from ..item import candle, comfort
from ..model import attributes, condition, room, slot, station


# Shrine: St Januarius
#
# St Januarius is the Name which was wounded; the Name of exceptions; the little god at the door.
shrine_st_januarius = station("shrine_st_januarius",
    attributes(evolve_via_nyctodromy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, knock=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, knock=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, knock=1, rose=1, sky=1),
        ),
        slot(
            required=condition(soul=1, omen=1, mark=1, light=1),
            #required=condition(soul=1, omen=1, mark=1, light=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(fuel=1, memory=1, pigment=1, light=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Shadowed Atrium
#
# This has long been a holy place, but in the absence of prayers, other influences have crept in. I'll need help to purify it, step by step.
# ---
# Atrium
#
# In 1651, Musgrave Dewulf endowed the atrium with a shrine to St Januarius of the Gate. Musgrave was a pious man but also a Puritan, so this grand shrine was a little unusual. St Januarius is also an unusual choice - but he is the patron saint of boundaries, and the Dewulfs were often said in some sense to be 'Marcher Lords' charged with the keeping of boundaries.
atrium = room("atrium",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.aglaophotis_scented_candle,
        candle.aglaophotis_scented_candle,
        candle.watchful_candle,
        candle.watchful_candle,
        comfort.atrium_chair,
    ),
    neighbors = ("grand_ascent_third_floor", ),
    power_requirements = attributes(knock=5, lantern=5),
    stations = (
        shrine_st_januarius,
    ),
)

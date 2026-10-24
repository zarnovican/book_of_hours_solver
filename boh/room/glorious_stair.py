from ..item import candle
from ..model import attributes, condition, room, slot, station


# Shrine: the Madrugad
#
# The Madrugad is the Hour which cannot be unbalanced; which quells and quiets; which comes before the sun.
shrine_the_madrugad = station("shrine_the_madrugad",
    attributes(evolve_via_ithastry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, sky=1, winter=1),
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


# Gloomy Stair
#
# This has long been a holy place, but the Madrugad has withdrawn her favour now, and a chillness waits here where dawn will not touch it. Only once it is pacified can I safely pass.
# ---
# Glorious Stair
#
# Each stair tread is decorated with a quotation from the Book of Suns, so that the congregation might be edified as they ascend. The quotes are worn to half-legibility by the passage of all those worshipful feet, which may be why some of these quotations differ troublingly from any orthodox version.
#
# It has of course been claimed that the Sisterhood of the Knot, who first held the Isle, also held a copy of the long-suppressed Shuritic version of the Book...
glorious_stair = room("glorious_stair",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.snowflake_candle,
        candle.snowflake_candle,
        candle.snowflake_candle,
    ),
    neighbors = ("atrium", ),
    power_requirements = attributes(edge=6, forge=6, winter=6),
    stations = (
        shrine_the_madrugad,
    ),
)

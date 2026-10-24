from ..item import candle, liquid, uncatalogued
from ..model import attributes, condition, room, slot, station


# Shrine: the Chancel
#
# We do not name these Hours, but we acknowledge that together they are the Chancel, the Cruciate, and the Rode.
shrine_the_chancel = station("shrine_the_chancel",
    attributes(evolve_via_horomachistry=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, moth=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, moth=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, moth=1, winter=1),
        ),
        slot(
            required=condition(soul=1, omen=1, mark=1, light=1),
            #required=condition(soul=1, co_operative=1, omen=1, mark=1, light=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(fuel=1, memory=1, pigment=1, light=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Veiled Chamber
#
# This has long been a very holy place - too holy to be left untended safely for this long. There are seventy-seven candles, and each one burns with a chill blue flame, each flame inhabited by a watchful spirit. I should not enter until each flame has been cleansed or extinguished.
# ---
# Chancel of the Abbey Church
#
# The Church of the Unconquered Sun acknowledges only a handful of Hours: the Sun in Rags or Splendour; the Meniscate; the Madrugad; the Watchman; and, reluctantly, the Wolf-Divided. Any other so-called 'Hours' must be lesser powers, wicked impostors, or superstitions.
#
# So the Church denies two of the three Hours of the Chancel. And yet it's the Chancel who are said to determine which of their peers qualify as Hours. That's theology for you.
#
# Abbot Geffrey decreed that all three should be venerated in this holiest of rooms. To avoid actual heresy, he would not permit any of the three to be named. That's theology, too.
chancel_of_the_abbey_church = room("chancel_of_the_abbey_church",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.historywax_candle,
        candle.historywax_candle,
        liquid.ichor_auroral,
        liquid.ichor_vitreous,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
    ),
    neighbors = ("nave_of_the_abbey_church", ),
    power_requirements = attributes(heart=9, lantern=9, moon=9, winter=9),
    stations = (
        shrine_the_chancel,
    ),
)

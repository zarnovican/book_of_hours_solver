from ..item import beverage, liquid, material, tool, uncatalogued
from ..model import attributes, condition, room, slot, station


# Altar: Malachite
#
# Honey, the blood; copper, the heart; yew, the root.
altar_malachite = station("altar_malachite",
    attributes(evolve_via_preservation=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, moth=1, nectar=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, moth=1, nectar=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, moth=1, nectar=1),
        ),
        slot(
            required=condition(soul=1, omen=1, sustenance=1, mark=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(flower=1, memory=1, woven=1, remains=1, root=1, sustenance=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# A Honeyed Forbidding
#
# The air is thick with the scents of honey and yew-berries - enough to daze the heart and mind.
# ---
# Chapel Malachite
#
# The Ring-Yew says: Never speak of this Mystery. When the Thunderskin was mortal he loved me first, and so the Grail destroyed him. Now the Thunderskin delights forever in my succulence. There is always a renewal, and nothing truly ends.
chapel_malachite = room("chapel_malachite",
    attributes(dawn_period=1),
    inventory = (
        beverage.leathy,
        beverage.rubywise_ruin,
        beverage.skinshuck_mead,
        liquid.wolf_snow_ampoule,
        material.beeswax,
        material.curious_seashell,
        material.quartz_chunk,
        tool.mortar_and_pestle,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("chapel_ascite", ),
    power_requirements = attributes(heart=14, nectar=14),
    stations = (
        altar_malachite,
    ),
)

from ..item import beverage, cache, candle, comfort, liquid, material, tool
from ..model import attributes, condition, room, slot, station


# Foundry
#
# Even metal cannot resist these suasions.
station_foundry = station("foundry",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, forge=1, knock=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, forge=1, knock=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, forge=1, knock=1, scale=1),
        ),
        slot(
            required=condition(glass=1, metal=1, stone=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(liquid=1, fuel=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Ravaged Foundry
#
# This room has not only been abandoned, but vandalised. Someone has smashed the place up and scrawled W-signs on the wall in blood and soot. I'll need skilled assistance to return it to use.
# ---
# Foundry
#
# This room was set aside for metalworking by Hendrik Dewulf. There's always been a smithy in Brancrug Village, but Hendrik wanted to make sure he could have his pistol-balls cast and his prisoner-shackles mended, even if the villagers were feeling rebellious. When Ambrose Westcott arrived, he had little use for shackles and less for pistols; he refurbished the place for his metallurgical experiments. A bad place to be in summer, a good one in winter.
foundry = room("foundry",
    attributes(baronial_period=1),
    inventory = (
        beverage.solomons_preparation,
        cache.box_of_oddities,
        cache.box_of_rarities,
        candle.honeyscar_scented_candle,
        candle.widows_candle,
        comfort.librarians_stool,
        liquid.bucket_of_seawater,
        liquid.regensburg_balm,
        material.bucket_of_ashes,
        tool.saw,
        tool.spanners,
        tool.square,
    ),
    neighbors = ("kitchen", ),
    power_requirements = attributes(forge=6, scale=6),
    stations = (
        station_foundry,
    ),
)

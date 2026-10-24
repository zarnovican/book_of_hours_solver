from ..item import cache, candle, comfort, fixed_in_place, flower, liquid, material, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station

# TODO (feature) model disasseble woven into rags, plus other disassemble recipes (wood?)

# Instrument: Hunter's Harp
#
# This was once strung with yeth-hound gut. Those strings must be long gone, but there's still an unusual savagery to the harp's notes.
instrument_hunters_harp = station("instrument_hunters_harp",
    attributes(evolve_via_nyctodromy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(scale=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(scale=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(scale=1, sky=1),
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


# Windlit Workbench
#
# Labour quietly.
windlit_workbench = station("windlit_workbench",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, heart=1, knock=1, lantern=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, heart=1, knock=1, lantern=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, heart=1, knock=1, lantern=1),
        ),
        slot(
            required=condition(made_of_wood=1, wood=1, woven=1, remains=1, tool=1, ductile=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(wood=1, tool=1, remains=1, ductile=1, made_of_wood=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Wind-Prowled Gallery
#
# This has long been a holy place, but the rites have gone too long unperformed. The windows are shattered and only the wind walks here now.
# ---
# Windlit Gallery
#
# In the days of the brethren, every day this gallery would ring with the Liturgy of the Hours. In the times of the Dewulfs and of the Curia, there were services here every Sunday. All those times are long gone. This is a house of echoes now.
windlit_gallery = room("windlit_gallery",
    attributes(solar_gothic_period=1),
    inventory = (
        cache.crate_of_supplies,
        candle.beeswax_candle,
        candle.beeswax_candle,
        comfort.carpenters_stool,
        fixed_in_place.hms_kerisham,
        flower.evas_locks,
        liquid.oscillate_oil,
        material.curious_seashell,
        material.driftwood_fragment,
        material.yew_blank,
        thing.gideon_dewulf,
        tool.spanners,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        wall_art.sol_invictis_symbol,
        wall_art.sol_invictis_symbol,
    ),
    neighbors = ("glorious_stair", ),
    power_requirements = attributes(forge=8, lantern=8, sky=8),
    stations = (
        instrument_hunters_harp,
        windlit_workbench,
    ),
)

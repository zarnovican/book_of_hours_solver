from ..item import beverage, candle, liquid, material, remains, sustenance, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Dispensary
#
# A well-appointed laboratory for a scholar of unconventional therapies.
dispensary = station("dispensary",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, knock=1, moth=1, nectar=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, knock=1, moth=1, nectar=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, knock=1, moth=1, nectar=1),
        ),
        slot(
            required=condition(flower=1, remains=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(fuel=1, liquid=1, remains=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Motley Tower: Second Floor
#
# A nasty theoplasmic miasma hangs around the room above. It's no longer strong, but it'll take years to dissipate to the point of safety. With the right help, I can raise counter-influences.
# ---
# Motley Tower: Dispensary
#
# This room may originally have served as a working dispensary, but some at least of its more eccentric fittings were added by Christopher Illopoly in his time here. By that point he had severed ties with his adoptive father. He'd been using the Illopoly name for years and had no access to the Strathcoyne fortune - but 'Traveling at Night' had sold surprisingly well (much better than his poetry) and he had a little money of his own by then - enough to indulge his preferences.
motley_tower_dispensary = room("motley_tower_dispensary",
    attributes(baronial_period=1),
    inventory = (
        beverage.domaine_raveline_glass,
        beverage.lambig_broceliande_chalice,
        beverage.leathy,
        beverage.leathy,
        beverage.sly_alembic,
        beverage.thirzas_cordials,
        candle.tall_candlestick,
        liquid.catwink,
        liquid.glassfinger_toxin,
        liquid.ichor_auroral,
        liquid.ichor_vitreous,
        liquid.iotic_essence,
        liquid.january_sanguinary,
        liquid.wolf_snow_ampoule,
        material.bitterblack_salts,
        material.desiccated_witchworms,
        material.leathy_lees,
        material.tanglebrag,
        material.westcotts_compounds,
        remains.skaptodon_fang,
        sustenance.viper_egg,
        thing.cranial_tchotchke,
        thing.glinting_cranial_tchotchke,
        tool.mortar_and_pestle,
        tool.serpent_styled_glass,
        tool.shears_of_the_sisterhood,
        tool.snootle_jar,
        tool.spice_scales,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.brazen_clock,
    ),
    neighbors = ("motley_tower_illopolys_nook", ),
    power_requirements = attributes(heart=6, moth=6),
    stations = (
        dispensary,
    ),
)

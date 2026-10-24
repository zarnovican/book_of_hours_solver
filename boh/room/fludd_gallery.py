from ..item import beverage, comfort, liquid, material, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Alchemist's Glassware
#
# Fragile vessels in which new substances are quickened.
alchemists_glassware = station("alchemists_glassware",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, grail=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, grail=1, lantern=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, grail=1, lantern=1, winter=1),
        ),
        slot(
            required=condition(leaf=1, root=1, material=1, remains=1, flower=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(liquid=1, fuel=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Despoiled Laboratory
#
# This was an alchemist's workshop and a picture gallery, but the pictures have been flung down, the vessels overturned, the solvents and reagents spilt. It will be time-consuming and dangerous to repair.
# ---
# Fludd Gallery
#
# Thirza Blake, seventh Librarian of the House, extended this space, decorating it with semi-precious materials and filling it with the finest art Hush House's money could buy. (Of course, after her enthusiasms brought the House to the brink of penury, much of it had to be sold off.)
fludd_gallery = room("fludd_gallery",
    attributes(curia_period=1),
    inventory = (
        beverage.armagnac_dys_bottle,
        beverage.armagnac_dys_glass,
        beverage.rubywise_ruin,
        beverage.sacrament_ascite,
        beverage.sacrament_calicite,
        beverage.sacrament_malachite,
        beverage.solomons_preparation,
        comfort.lumpy_melodic_chair,
        comfort.melodic_chair,
        liquid.glassfinger_toxin,
        liquid.perinculate,
        liquid.stargall_ink,
        liquid.turpentine,
        liquid.wolf_snow_ampoule,
        liquid.xanthotic_essence,
        material.ambergris_chunk,
        material.quartz_chunk,
        thing.eva_dewulf,
        tool.serpent_styled_glass,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        wall_art.a_sacrifice,
        wall_art.as_above_so_below,
        wall_art.crowcross_sands_at_high_tide,
        wall_art.departure,
        wall_art.dr_serena_blackwood,
        wall_art.glorys_gift,
        wall_art.lady_tryphon,
        wall_art.leaves_in_the_wind,
        wall_art.leaves_in_the_wind,
        wall_art.lord_munday,
        wall_art.portrait_of_a_behatted_lady,
        wall_art.the_boy_prays,
        wall_art.the_foundlings,
    ),
    neighbors = ("grand_ascent_third_floor", ),
    power_requirements = attributes(forge=6, winter=6),
    stations = (
        alchemists_glassware,
    ),
)

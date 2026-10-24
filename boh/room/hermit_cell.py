from ..item import beverage, candle, leaf, liquid, material, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Guest Bed: Hermit
#
# A snug nook where absolutely nobody will bother the occupant. [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_hermit = station("guest_bed_hermit", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(moon=1, interested_in_moon=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Hermit's Workbench
#
# Labour in solitude.
hermits_workbench = station("hermits_workbench",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, moon=1, scale=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, moon=1, scale=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, moon=1, scale=1, sky=1),
        ),
        slot(
            required=condition(stone=1, made_of_wood=1, woven=1, remains=1, tool=1, ductile=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(ductile=1, tool=1, remains=1, stone=1, made_of_wood=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Gaping Darkness
#
# Thunder prowls the entrance to this cave - a dying curse, or a capricious storm-spirit? It must be dealt with carefully.
# ---
# Hermit Cell
#
# The words RED WILLIAM are scratched into the wall by the bed-nook. This was the name of the cunning-man who laid a curse on Hendrik Dewulf, that there would be no seventh of his line - the cunning-man that Hendrik Dewulf gelded and imprisoned beneath the House.
#
# But this doesn't look like a cell. There could have been no locks. Perhaps that other story is true - that William was an initiate of the Thunderskin, secretly maintained by Hendrik to prophesy for him 'in the ancient manner.' Who were the Dewulfs, really?
hermit_cell = room("hermit_cell",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.domaine_raveline_bottle,
        beverage.domaine_raveline_bottle,
        beverage.lambig_broceliande_bottle,
        beverage.schloss_jannings_bottle,
        candle.bedside_candleholder,
        leaf.tiny_potted_tree,
        liquid.january_sanguinary,
        liquid.perhibiate,
        liquid.yewgall_ink,
        material.granite_slab,
        thing.quire_of_paper,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("gull_colony", "smugglers_den"),
    power_requirements = attributes(heart=12, moth=12),
    stations = (
        guest_bed_hermit,
        hermits_workbench,
    ),
)

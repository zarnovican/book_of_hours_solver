from ..item import beverage, liquid, material, sustenance, thing, tool
from ..model import attributes, condition, room, slot, station


# Kitchen Range: Gaol
#
# The food served in Brancrug Gaol was unexpectedly hearty and tasty - in keeping with Collers' more humane theories of rehabilitation.
kitchen_range_gaol = station("kitchen_range_gaol",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, lantern=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, lantern=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, lantern=1, nectar=1, scale=1),
        ),
        slot(
            required=condition(leaf=1, beverage=1, flower=1, fuel=1, root=1, cooking_ingredient=1, sustenance=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(leaf=1, beverage=1, flower=1, fuel=1, root=1, cooking_ingredient=1, sustenance=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(kitchenware=1, knife=1),
        ),
    ),
)


# Worm-Gnawed Kitchen
#
# This kitchen has clearly been penetrated and polluted by Worms - the 'parasites of the Sun'. The Worms are long gone. But the kitchen will need scouring, it will need decontaminating, and then it will definitely need all its food throwing out. Even if it's tinned.
# ---
# Gaol Kitchen
#
# 'There are no Hours at Brancrug,' Collers used to say - even before he was Governor of Brancrug Gaol, when he was only Secretary Vigilant of the Curia. By way of reminder, the hands were confiscated from every timepiece within the prison walls. The warders could still rely on the chimes of the great Clock in the abbey spire. But it did make life harder for the cooks.
gaol_kitchen = room("gaol_kitchen",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.dawnlion_coffee_cup,       # beverage.dawnlion_coffee_pot (half-pot)
        beverage.eigengrau,
        beverage.elderflower_cordial,
        beverage.mist_kissed_water_pitcher,
        beverage.skinshuck_mead,
        liquid.cuckoo_honey,
        liquid.honey,
        material.labhitic_tincture,
        sustenance.blackberry_jam,
        sustenance.pickled_pilchards,
        sustenance.rosehip_jam,
        thing.flour,
        tool.kitchen_bowls,
    ),
    neighbors = ("gaol_hall", ),
    power_requirements = attributes(grail=12, heart=12, winter=12),
    stations = (
        kitchen_range_gaol,
    ),
)

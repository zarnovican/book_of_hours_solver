from ..item import beverage, cache, candle, liquid, material, remains, sustenance, tool
from ..model import attributes, room


# Ravaged Cellar
#
# This room too has been visited by Worms, the 'abomination of the relict-kind'... but almost no traces remain.
# ---
# Gaol Cellar
#
# The entrance to the sub-cellar was barred, locked, chained, warded, both physically and otherwise. Whatever was kept down there, they took it extremely seriously.
#
# It looks very much as if the questing Worms broke the seals, drawn by the power below. It looks very much as if they regretted it.
gaol_cellar = room("gaol_cellar",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.elderflower_cordial,
        beverage.schloss_jannings_bottle,
        beverage.sloe_gin_bottle,
        beverage.solomons_preparation,
        cache.abandoned_packages,
        cache.box_of_oddities,
        candle.widows_candle,
        liquid.amethyst_ampoule,
        liquid.kerosene,
        liquid.paraffin,
        liquid.scintillate_oil,
        material.arsenic,
        material.wire_copper,
        remains.essential_periost,
        sustenance.pickled_mushrooms,
        tool.saw,
        tool.serpent_styled_glass,
    ),
    neighbors = ("gaol_kitchen", ),
    power_requirements = attributes(forge=13, scale=13, winter=13),
)

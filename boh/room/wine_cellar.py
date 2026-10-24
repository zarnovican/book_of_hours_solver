from ..item import beverage, cache, candle, comfort, liquid
from ..model import attributes, room


# Infested Wine-Cellar
#
# Something much bigger laired here. The walls and ceiling are smeared with its slimes. It's gone, but its children remain, wriggling in every shadow. We'll have to clear, lure or drive them out.
# ---
# Wine Cellar
#
# Ricardo Milagro, traveller, rascal, Musgrave's gardener, managed a creditable wine from Brancrug grapes. Cornwall has never really been wine country, and the tradition was unevenly maintained, but the Curia of the Isle kept a good cellar.
wine_cellar = room("wine_cellar",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.dandelion_wine,
        beverage.dandelion_wine,
        beverage.domaine_raveline_bottle,
        beverage.lambig_broceliande_bottle,
        beverage.lambig_broceliande_bottle,
        beverage.lambig_broceliande_bottle,
        beverage.roscraggan_whisky_bottle,
        beverage.roscraggan_whisky_glass,
        beverage.schloss_jannings_bottle,
        cache.lost_packages,
        candle.widows_candle,
        comfort.plain_stool,
        liquid.bucket_of_seawater,
    ),
    neighbors = ("kitchen_garden", ),
    power_requirements = attributes(grail=10, moth=10),
)

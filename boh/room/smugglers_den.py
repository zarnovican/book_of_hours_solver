from ..item import beverage, cache, candle, thing
from ..model import attributes, room


# Wing-Haunted Cave
#
# A drunken whirl of bats drives me back! Perhaps literally drunken. There's a faint but definite brandy smell.
# ---
# Smuggler's Den
#
# In the last years of the eighteenth century, the Dewulf line ended and the estate lay empty. Enterprising smugglers spread rumours of the ghosts that walked the Isle, and quietly brought their tea, brandy and tobacco in through the old mines on the seaward side of the Isle. But the remnants here are much newer than the eighteenth century. Perhaps even after the Curia took possession, they permitted the smugglers to use this place. Ambrose Westcott did love his baccy so. Perhaps even the Suppression Bureau found the smugglers useful enough to turn a blind eye.
smugglers_den = room("smugglers_den",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.domaine_raveline_bottle,
        beverage.domaine_raveline_bottle,
        beverage.lambig_broceliande_bottle,
        beverage.schloss_jannings_bottle,
        beverage.schloss_jannings_bottle,
        cache.crate_of_supplies,
        cache.forsaken_packages,
        candle.bottled_candle,
        thing.hurricane_lamp,
    ),
    neighbors = ("our_lady_beneath", ),
    power_requirements = attributes(forge=12, grail=12),
)

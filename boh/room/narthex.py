from ..item import candle, flower, material, sustenance
from ..model import attributes, room


# Slithering Fountain
#
# After all these years, the fountain in this hall is blocked. That's not a surprise. A little more surprising is this: the blockage appears to be mostly snakes; a great many snakes. This, no doubt, is why we have seen so few rats.
# ---
# Narthex
#
# If you were a pilgrim to the Abbey of the White Crow, you'd purify yourself here. You didn't want to track profane Dumnonian mud or alien Mare Britannicum salt into the holy precincts. Or unclean thoughts. Especially not unclean thoughts. The priestesses here were a little more merciful than the Hours they served, but only a little.
narthex = room("narthex",
    attributes(dawn_period=1),
    inventory = (
        candle.aglaophotis_scented_candle,
        candle.widows_candle,
        flower.evas_locks,
        material.atlantic_amber,
        material.sea_glass,
        sustenance.viper_egg,
    ),
    neighbors = ("sacred_spring", ),
    power_requirements = attributes(edge=14, knock=14, scale=14),
)

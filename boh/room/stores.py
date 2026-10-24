from ..item import beverage, cache, candle, comfort, liquid, material, thing, tool
from ..model import attributes, room


# Heart-Haunted Room
#
# The light in this room dims in pulses of sunset red, over and over, in a half-heard heartbeat that matches the crashing of the waves below. It'll need careful exorcism from someone attuned to these influences.
# ---
# Stores
#
# At the time of the Prayer Book Rebellion, in 1549, Hendrik used this room as a prison cell for unfortunate locals - including the cunning-man and rebel ringleader, Red William, who had boasted of the curse he placed on Hendrik's heirs: 'There will be no seventh of his line.'
#
# There is a story told in Brancrug Village that Hendrik came to speak with the imprisoned William in person. 'There will be no <i>second</i> of your line,' he told him - and had him gelded here in this very cell, and cast into the darkness of the caves below the House.
#
# There is another story, that Eva Dewulf once answered an importunate suitor by bringing him here to this room and pointing out a stain upon the stones...
stores = room("stores",
    attributes(baronial_period=1),
    inventory = (
        beverage.eigengrau,
        beverage.isle_water_pitcher,
        beverage.schloss_jannings_bottle,
        beverage.skinshuck_mead,
        cache.box_of_rarities,
        cache.box_of_rarities,
        cache.contraband_jetsam,
        cache.slim_parcel,
        candle.bottled_candle,
        comfort.plain_stool,
        liquid.kerosene,
        liquid.paint_bosk_green,
        liquid.paint_dusk_blue,
        liquid.paint_green,
        liquid.paint_palest_blue,
        liquid.paint_pink,
        liquid.paint_yellow,
        liquid.paraffin,
        liquid.scintillate_oil,
        material.glue,
        material.trn_limited_drinking_cocoa_packet,
        material.wire_steel,
        thing.basket_of_towels,
        thing.bolt_of_moss_green_velvet,
        thing.bolt_of_pale_silk,
        thing.hurricane_lamp,
        tool.cucurbit_burette,
        tool.saw,
    ),
    neighbors = ("refectory", ),
    power_requirements = attributes(grail=8, heart=8, moon=8),
)

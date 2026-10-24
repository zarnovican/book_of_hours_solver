from ..item import candle
from ..model import attributes, room


# Riddling Stair
#
# Half-seen faces mouth half-heard riddles. This is none of van Lauren's work - these defences are much older than the Curia. But the Curia found a way to answer these riddles, and so will we.
# ---
# Whispering Stair
#
# This was the stair that the priestesses walked, in the time that this was the Abbey of the Black Dove. Their carved faces still guard the walls. Their prayers may still be heard when the airs of the Isle are exceptionally still.
whispering_stair = room("whispering_stair",
    attributes(dawn_period=1),
    inventory = (
        candle.widows_candle,
    ),
    neighbors = ("hidden_stair", ),
    power_requirements = attributes(moon=12, rose=12),
)

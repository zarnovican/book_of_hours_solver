from ..item import candle
from ..model import attributes, room


# Rustling Stair
#
# Serpent-scales whisper on stone; serpent-eyes glitter in the pale window-light.
# ---
# Hidden Stair
#
# After Brulleau's retirement in 1861, the Curia found itself short of promising candidates - until the arrival of Willem Harries, a former Dutch Lutheran priest and a sometime correspondent of Stanislav Schaller. He had been a missionary in the Dutch East Indies until his faith was lost or transmuted into a devotion to St Agnes of the Gate, and he was drawn to Hush House.
#
# He won his position by presenting the Curia with a 'key long lost'. That was the key to this very stair, but only the naive would assume the key was a tangible object.
hidden_stair = room("hidden_stair",
    attributes(dawn_period=1),
    inventory = (
        candle.beeswax_candle,
    ),
    neighbors = ("wine_cellar", ),
    power_requirements = attributes(moon=11, scale=11),
)

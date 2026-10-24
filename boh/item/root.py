from ..item import memory
from ..model import attributes, card_type


# Moly
#
# 'Moly the gods call it, and it is hard for mortal men to dig; but with the gods all things are possible.' - Homer
# ---
# Scrutiny
#
# A fluttering in the skull…
moly = card_type("moly",
    attributes(heart=1, moon=2, moth=2, nectar=1, scale=2, thing=1, sustenance=1, root=1, cooking_ingredient=1),
    consider_output = memory.impulse,
)

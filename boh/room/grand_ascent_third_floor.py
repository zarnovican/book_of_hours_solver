from ..item import *
from ..model import attributes, room
from .. import station


# Grand Ascent - Third Floor
#   
# Frost crackles on the window-panes as I ascend, and the light strikes at my eyes like knives. Another of van Lauren's forbiddings.
# ---
# Grand Ascent - Third Floor
#   
# By long tradition, each Baron Brancrug had their image set in a niche in the Grand Ascent. Later, the Curia of the Isle continued the tradition for their Librarians.
grand_ascent_third_floor = room("grand_ascent_third_floor",
    attributes(baronial_period=1),
    inventory = (
        leaf.potted_bamboo,
    ),
    neighbors = ("grand_ascent_second_floor", ),
    power_requirements = attributes(edge=5, forge=4, knock=5, winter=5),
)

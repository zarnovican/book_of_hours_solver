from ..item import leaf
from ..model import attributes, room


# Grand Ascent - First Floor
#   
# The windows are tightly closed, the carpets surprisingly clean, but my skin prickles at the watchful presence in the stairwell. We will need to placate it before we go higher.
# ---
# Grand Ascent - First Floor
#   
# By long tradition, each Baron Brancrug had their image set in a niche in the Grand Ascent. Later, the Curia of the Isle continued the tradition for their Librarians.
grand_ascent_first_floor = room("grand_ascent_first_floor",
    attributes(baronial_period=1),
    inventory = (
        leaf.potted_monstera,
    ),
    neighbors = ("grand_ascent_ground_floor", "physic_garden"),
    power_requirements = attributes(forge=4, heart=4, sky=4, winter=4),
)   

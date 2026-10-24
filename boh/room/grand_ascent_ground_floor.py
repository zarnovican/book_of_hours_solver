from ..item import comfort, wall_art
from ..model import attributes, room


# Grand Ascent - Ground Floor
#
# The stairs here are clear, but the air here is thick with old magics. I should move carefully, and I should not go alone.
#
# Still no sign of any fire. Why then was the House abandoned?
# ---
# Grand Ascent - Ground Floor
#
# The staircase that served as the spine of the House: Baron Walter's great project, executed by the master mason Gregory Wheelock.
grand_ascent_ground_floor = room("grand_ascent_ground_floor",
    attributes(baronial_period=1),
    inventory = (
        comfort.ambroses_favourite_chair,
        comfort.delightful_repose,
        comfort.paradise_palm,
        wall_art.dr_serena_blackwood,
        wall_art.hokobald,
    ),
    neighbors = ("entrance_hall", ),
    power_requirements = attributes(edge=4, heart=4, moon=4, winter=4),
)

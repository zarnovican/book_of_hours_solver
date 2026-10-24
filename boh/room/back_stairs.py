from ..item import wall_art
from ..model import attributes, room


# Blockaded Stairs
#
# Someone has filled these stairs with baulks of timber and broken furniture. They've filled the timber and furniture with signs to bring shadow and despair. Did they want to prevent an intruder from passing, or a resident from leaving? Either way, it'll be difficult and careful work to open the stairs.
# ---
# Back Stairs
#
# The secret artery of the House. All those abbots and barons and all their crowds of retainers needed their chamber pots emptying and their boots cleaning. These are the stairs that the boots and the chamber pots went up and down. They were notoriously cramped and treacherous. It was a rare year some poor scullion didn't crack an ankle. It was the Suppression Bureau, at very long last, who remodelled the stairs and put in electric lights. And people say the Suppression Bureau never did Hush House any good!
back_stairs = room("back_stairs",
    attributes(baronial_period=1),
    inventory = (
        wall_art.lepidoptery_display_grail_centric,
        wall_art.lepidoptery_display_heart_centric,
    ),
    neighbors = ("servants_quarters_north", "stores", "wine_cellar"),
    power_requirements = attributes(heart=9, knock=9, lantern=9, moon=9, rose=9, scale=9),
)

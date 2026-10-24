from ..item import flower
from ..model import attributes, room


# Grand Ascent - Second Floor
#
# It is unexpectedly difficult to raise my foot to the last step before the landing. Leaf-shadows drift across my sight, and the windows hiss and rattle. I have heard that Gervinus van Lauren, last Librarian before me, was skilled at the forbidding of ways.
# ---
# Grand Ascent -Second Floor
#
# By long tradition, each Baron Brancrug had their image set in a niche in the Grand Ascent. Later, the Curia of the Isle continued the tradition for their Librarians.
grand_ascent_second_floor = room("grand_ascent_second_floor",
    attributes(baronial_period=1),
    inventory = (
        flower.vase_of_lilies,
    ),
    neighbors = ("grand_ascent_first_floor", "infirmary"),
    power_requirements = attributes(grail=4, knock=5, nectar=5, winter=5),
)

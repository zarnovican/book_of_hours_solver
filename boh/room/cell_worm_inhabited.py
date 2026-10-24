from ..item import liquid, mark, material
from ..model import attributes, room


# Impermeable Cell
#
# A sign outside this cell reads WARNING: NOT TO BE SPOKEN WITH, NOR LOOKED UPON. The protections that still hang in the air lend force to the injunction.
# ---
# Cell: Worm-Inhabited
#
# The occupant of <i>this</i> cell could not be allowed fresh air and exercise. It could not have reasonably expected to leave this cell ever again, even while it wore human shape. But it could not be confined forever; in the end, somehow, it found its way into the walls.
cell_worm_inhabited = room("cell_worm_inhabited",
    attributes(nocturnal_period=1),
    inventory = (
        liquid.stargall_ink,
        mark.midnight_mark,
        material.desiccated_witchworms,
        material.whispering_sand,
    ),
    neighbors = ("cell_question", ),
    power_requirements = attributes(forge=15, knock=15, sky=15),
)

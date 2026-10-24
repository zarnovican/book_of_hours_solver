from ..item import *
from ..model import attributes, room
from .. import station


# The Atlantic Ocean
#
# Whale-den, moon-road, bone-keeper, ship-breaker.
the_atlantic_ocean = room("the_atlantic_ocean",
    attributes(out_of_bounds=1),
    unlock_at_start = True,
)

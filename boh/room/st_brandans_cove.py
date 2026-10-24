from ..item import *
from ..model import attributes, room
from .. import station


# St Brandan’s Cove
#
# Here the sea ends and the world begins (or the other way around). After storms, the fishermen of Brancrug Village find oddities washed up here.
st_brandans_cove = room("st_brandans_cove",
    attributes(out_of_bounds=1),
    unlock_at_start = True,
)

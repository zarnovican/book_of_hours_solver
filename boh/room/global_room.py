from ..item import *
from ..model import attributes, room
from .. import station


# global_room
global_room = room("global_room",
    attributes(),
    stations = (
        station.consider,
        station.talk,
    ),
    unlock_at_start = True,
)

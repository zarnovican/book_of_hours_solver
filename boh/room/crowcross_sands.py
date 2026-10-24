from ..item import *
from ..model import attributes, room
from .. import station


# Tidal Flats
#
# Brancrug is a tidal island; at low tide you could walk there. Though you probably shouldn't.
# ---
# Crowcross Sands
#
# Look out across the bay. Long long ago, this was a forest.
crowcross_sands = room("crowcross_sands",
    attributes(out_of_bounds=1),
    neighbors = ("st_brandans_cove", ),
    power_requirements = attributes(moon=2, winter=2),
    stations = (
        station.beachcombing,
        station.seas_edge,
    ),
)

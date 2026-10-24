from ..model import attributes, room
from .. import station


# Brancrug Village
#
# Brancrug Village: sanctuary in the storm. I'll need help to climb the cliffs in the dark, and the locals are suspicious of outsiders... more than ever so since the Restoration, and the New King.
# ---
# Brancrug Village
#
# This quiet Cornish fishing village has lain long in the Isle's shadow. It might be as old as Hush House itself. And like Hush House, Brancrug Village has provided sanctuary over the years for its share of misfits and exiles.
brancrug_village = room("brancrug_village",
    attributes(out_of_bounds=1),
    locked_stations = (
        station.mr_and_mrs_kille,
        station.the_post_office,
        station.the_rectory,
        station.the_smithy,
        station.the_sweet_bones,
    ),
    neighbors = ("st_brandans_cove", ),
    stations = (
        station.a_walk_on_the_moor,
    ),
)

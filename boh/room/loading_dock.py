from ..item import cache, memory
from ..model import attributes, condition, room, slot, simple_action, simple_output, station


# Loading Dock Crane
#
# Long ago, this was the route by which provisions entered the gaol, and by which prisoners failed to escape. [Discard objects here, or release beasts.]
loading_dock_crane = station("loading_dock_crane", attributes(),

    simple_actions = (

        simple_action("release",
            output = (
                simple_output( memory.hindsight ),
            ),
            slots = (
                slot(
                    required=condition(beast=1),
                    consume_all=True,
                ),
            ),
        ),

        simple_action("renounce",
            output = (
                simple_output( memory.loss ),
            ),
            slots = (
                slot(
                    required=condition(thing=1),
                    consume_all=True,
                ),
            ),
        ),
    ),

    slots = (
        slot(
            required=condition(beast=1, thing=1),
        ),
    ),
)


# Sagging Dock
#
# The storms have had their way with this since the prison was abandoned. It won't last much longer.
# ---
# Loading Dock
#
# Here the supplies came in, from every continent that the seas touch - from the Bounds, and beyond. Now and then prisoners would try to escape, but the sea is always hungry.
loading_dock = room("loading_dock",
    attributes(nocturnal_period=1),
    inventory = (
        cache.abandoned_luggage,
        cache.crate_of_supplies,
        cache.records_box,
    ),
    neighbors = ("gaol_cellar", ),
    power_requirements = attributes(moon=14, rose=14),
    stations = (
        loading_dock_crane,
    ),
)

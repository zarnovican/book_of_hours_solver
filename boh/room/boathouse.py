from ..item import memory, soul, thing
from ..model import attributes, condition, room, simple_action, simple_output, slot, station


# Brancrug Boathouse
#
# The boat is gone, the Sea remains. That is, of course, the way it usually works. [Discard objects here; release beasts; or go for a swim.]
brancrug_boathouse = station("brancrug_boathouse", attributes(),

    simple_actions = (

        simple_action("a_brisk_swim",
            output = (
                simple_output( memory.salt ),
            ),
            slots = (
                slot(
                    required=condition(one_of=(soul.health, )),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),

        simple_action("a_brisk_swim",
            output = (
                simple_output( memory.salt ),
                simple_output( memory.solace ),
            ),
            slots = (
                slot(
                    required=condition(one_of=(soul.health, )),
                    forbidden=condition(fatigued=1, malady=1),
                ),
                slot(
                    required=condition(one_of=(thing.basket_of_towels, )),
                ),
            ),
        ),

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
            required=condition(soul=1, thing=1, beast=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
    ),
)


# Perilous Path
#
# This route was never safe, even before the last round of storms had their way with it.
boathouse = room("boathouse",
    attributes(open_air=1),
    neighbors = ("hermit_cell", ),
    power_requirements = attributes(moon=13, rose=13),
    stations = (
        brancrug_boathouse,
    ),
)

from ..item import memory, soul, thing
from ..model import attributes, condition, season, simple_action, simple_output, slot, station


# (deadend, soul (not health))
#
# A Brisk Swim?
#
# [Swimming requires an Element of the Soul with Heart and Scale - generally, this means Health.]""",


# Sea's Edge
#
# The Sea is always hungry; the Sea never sleeps; the Sea accepts offerings. [Discard objects here; release beasts; or go for a swim.]
seas_edge = station("seas_edge", attributes(),

    simple_actions = (

        # A Brisk Swim
        #
        # I'll plunge again into the waves...
        # ---
        # A Brisk Swim
        #
        # The waves raise me; the salt stings my eyes; the horizon waits.
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

        # A Brisk Swim
        #
        # I'll plunge again into the waves...
        # ---
        # A Brisk Swim
        #
        # I'll plunge again into the waves... and dry off afterwards.
        # ---
        # A Brisk Swim
        #
        # The waves raise me; the salt stings my eyes; the horizon waits. Afterwards, the towels are clean and soft. [By drying off afterwards, you've gained a Memory: Solace.]
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

        # Release
        #
        # I could release it to the waves, the winds, or the sands, as it prefers.
        # ---
        # Release
        #
        # There were two of us, and now there's one.
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

        # Renounce
        #
        # If I cast an object into the sea, it will be lost, perhaps irretrievably. [Use this to dispose of junk, or of danger.]
        # ---
        # Renounce
        #
        # When something is given to the sea it rarely returns... although, of course, I did.
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

        # Renounce
        #
        # Why? Why not? [Dispose of a stray penny.]
        # ---
        # Renounce
        #
        # And the waves march on.
        simple_action("renounce",
            output = (
                simple_output( memory.impulse,          season=season.spring ),
                simple_output( memory.impulse,          season=season.summer ),
                simple_output( memory.impulse,          season=season.autumn ),
                simple_output( memory.impulse,          season=season.winter ),

                # Renounce
                #
                # To give a coin to the sea at this season - once, this was said to be the toll due to Ys. [Dispose of a stray penny.]
                # ---
                # Renounce
                #
                # And the waves march on to the horizon.
                simple_output( memory.horizon_sight,    season=season.numa ),
            ),
            pennies = 1,
            slots = (),
        ),

        # Renounce
        #
        # To give a coin to the sea at this season - once, this was said to be the toll due to Ys. [Dispose of a stray penny.]
        # ---
        # Renounce
        #
        # And the waves march on to the horizon.
        simple_action("renounce",
            output = (
                simple_output( memory.horizon_sight,    season=season.numa ),
            ),
            pennies = 1,
            slots = (),
        ),
    ),

    slots = (
        slot(
            required=condition(soul=1, thing=1, penny=1, beast=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
    ),
)

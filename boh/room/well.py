from ..item import beverage, memory
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# (action, journal)
# Renounce What Could Be
#
# Do I really want to fling my journal into the well? [THIS WILL DESTROY YOUR JOURNAL, which will make it IMPOSSIBLE TO COMPLETE THE GAME. You'll be stuck! But you can do it if you really want.]
# ---
# Renounce What Could Be
#
# 'Fool of a Librarian!' [It is no longer possible to complete the game.]


# Hush House Well
#
# Here I can draw up water - or drop something in, most likely to be lost forever.
hush_house_well = station("hush_house_well", attributes(),

    simple_actions = (

        # Draw up Water
        #
        # Lower the bucket creaking into the dark.
        # ---
        # Draw up Water
        #
        # A little water sploshes on to the stones of the well to nourish the mosses there.
        simple_action("draw_up_water",
            output = (
                simple_output( beverage.isle_water_pitcher,         season=season.spring ),
                simple_output( beverage.isle_water_pitcher,         season=season.summer ),
                simple_output( beverage.isle_water_pitcher,         season=season.autumn ),
                simple_output( beverage.isle_water_pitcher,         season=season.winter ),
            ),
            slots = (
                slot(
                    essential=condition(soul=1),
                    required=condition(heart=1),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),

        # Draw up Water
        #
        # Mist coils below...
        # ---
        # Draw up Water
        #
        # Water in the season of Numa is almost the same as water in any other season.
        simple_action("draw_up_water",
            output = (
                simple_output( beverage.mist_kissed_water_pitcher,  season=season.numa ),
            ),
            slots = (
                slot(
                    essential=condition(soul=1),
                    required=condition(heart=1),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),

        # Renounce
        #
        # If I drop an object into the well, I'm unlikely to see it again. [Use this to dispose of junk, or of danger.]
        # ---
        # Renounce
        #
        # (Plosh.)
        simple_action("renounce",
            output = (
                simple_output( memory.sound ),
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
        # The smallest of wishes. [Dispose of a stray penny.]
        # ---
        # Renounce
        #
        # (Plip.)
        simple_action("renounce",
            output = (
                simple_output( memory.satisfaction ),
            ),
            pennies = 1,
            slots = (),
        ),
    ),

    slots = (
        slot(
            essential=condition(heart=1, soul=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            required=condition(penny=1, thing=1),
        ),
    ),
)


# Deserted Well
#
# The well is choked and filthy. It'll need to be purified inside and out.
# ---
# Well
#
# There's been a well here since the days of the Sisterhood, and superstitions have gathered around it like leaves in drifts. Its water has a healing virtue if drawn on a night of the new moon. It's ill luck to draw from it if you hear an owl. If you drip the blood of a living enemy into the well, they'll drown. And so on. Certainly, when Numa comes, the mists lie thick here.
well = room("well",
    attributes(open_air=1),
    neighbors = ("foundry", "pantry"),
    power_requirements = attributes(moon=7, nectar=7),
    stations = (
        hush_house_well,
    ),
)

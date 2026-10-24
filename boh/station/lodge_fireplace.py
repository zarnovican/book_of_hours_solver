from ..item import memory
from ..model import attributes, condition, simple_action, simple_output, slot, station


# (incomplete, brewable + <empty>)
#
# Renounce (or Brew?)
#
# If I cast an object into the fire, it will be transformed; destroyed; lost. [If the item is Brewable, add a Soul card to brew it instead of destroying it.]


# (brewing)
#
# Brew over the Fire
#
# Bring water to the boil - permit the potential here to express itself -
# ---
# Brew over the Fire
#
# - steam and scent both rise. It's ready.


# (soul + viper's egg)
#
# Hatch the Egg
#
# The fire's warmth can stir this egg to life - but it'll take a full day.
# ---
# Hatch the Egg
#
# New life!


# Lodge Fireplace
#
# Fire always accepts gifts. And boils the kettle for tea.
lodge_fireplace = station("lodge_fireplace", attributes(),

    simple_actions = (
        # Renounce
        #
        # If I cast an object into the fire, it will be transformed; destroyed; lost. [Use this to dispose of junk, or of danger.]
        # ---
        # Renounce
        #
        # The flames leap up, and die away.
        simple_action("renounce",
            output = (
                simple_output( memory.sight ),
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
            essential=condition(soul=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            required=condition(correspondence=1, thing=1),
        ),
    ),
)

from ..item import beverage, comfort, flower
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# Garden
#
# Catsclaw in spring, trumpeter's lily in summer. Rarer plants might flourish in Numa.
physic_garden_garden = station("physic_garden_garden", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Gather catsclaw carefully. Its mischievous thorns find ways through the thickest gloves.
                simple_output( flower.catsclaw,         season=season.spring ),

                # Gather in Summer
                #
                # In summer, trumpeter's lily flourishes like a shout.
                simple_output( flower.trumpeters_lily,  season=season.summer ),

                # Gather in Autumn
                #
                # In autumn, before the real chill comes, trumpeter's lily still flourishes.
                simple_output( flower.trumpeters_lily,  season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output( ,                       season=season.winter ),

                # Gather in Numa
                #
                # Aglaophotis, the other rose. Only in Numa does it bloom.
                simple_output( flower.aglaophotis,      season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(nectar=1),
        ),
    ),
)


# Weed-Choked Garden
#
# From what I can make out of the garden beyond, it must have been very peaceful - but now it's neglected and overgrown.
# ---
# Physic Garden
#
# The nuns of the Knot planted this garden of healing herbs in the Dawn Period. Natan of Regensburg and Gideon Dewulf both expanded it, and the Curia of the Isle tended it. Even the Branch and the Bureau made use of it in the grim days that Brancrug served as a prison.
physic_garden = room("physic_garden",
    attributes(open_air=1),
    inventory = (
        beverage.roscraggan_whisky_bottle,
        beverage.roscraggan_whisky_glass,
        beverage.roscraggan_whisky_glass,
        comfort.comfortable_garden_chair,
        comfort.comfortable_garden_chair,
        comfort.restful_garden_chair,
    ),
    neighbors = ("entrance_hall", ),
    power_requirements = attributes(heart=3, nectar=3),
    stations = (
        physic_garden_garden,
    ),
)

from ..item import flower
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# Garden
#
# Sea holly in summer, blue crown in winter.
st_brandans_cloister_garden = station("st_brandans_cloister_garden", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # In spring as the days warm, blue crown still blossoms for a little while.
                simple_output( flower.blue_crown,   season=season.spring ),

                # Gather in Summer
                #
                # Gather the spiny florescences of the sea holly.
                simple_output( flower.sea_holly,    season=season.summer ),

                # Gather in Autumn
                #
                # Gather the spiny florescences of the sea holly.
                simple_output( flower.sea_holly,    season=season.autumn ),

                # Gather in Winter
                #
                # Few flowers flourish in the depths of winter. Blue crown is one of those few.
                simple_output( flower.blue_crown,   season=season.winter ),

                # Gather in Numa
                #
                # In Numa, the sea holly returns. Gather it carefully.
                simple_output( flower.sea_holly,    season=season.numa ),
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


# Cloistered Garden
#
# I can make out a green and shaded space, but it's choked with weeds and thorns. I'll need help to clear the space.
# ---
# St Brandan’s Cloister
#
# The sisters and brothers of the Abbey built these gardens in the thirteenth century - at the height of the period we now call Solar Gothic. Walk here a while and breathe the peace they left.
st_brandans_cloister = room("st_brandans_cloister",
    attributes(open_air=1),
    neighbors = ("watchmans_tower_gatehouse", ),
    power_requirements = attributes(lantern=2, nectar=2),
    stations = (
        st_brandans_cloister_garden,
    ),
)

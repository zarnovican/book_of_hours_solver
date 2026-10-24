from ..item import beverage, flower, root, thing
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# Garden
#
# Moth orchids in spring and summer, honeyscar jasmine in autumn.
scent_garden_garden1 = station("scent_garden_garden1", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Moth orchid is soft as velvet to the touch; except when it changes.""",
                simple_output( flower.moth_orchid,          season=season.spring ),

                # Gather in Summer
                #
                # Moth orchid is soft as velvet to the touch; except when it changes.
                simple_output( flower.moth_orchid,          season=season.summer ),

                # Gather in Autumn
                #
                # Honeyscar jasmine, like a dart of sweet fire.
                simple_output( flower.honeyscar_jasmine,    season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                             season=season.winter ),

                # Numa:
                #
                # Honeyscar jasmine, like a dart of sweet fire. Numa brings it back to life.
                simple_output( flower.honeyscar_jasmine,    season=season.numa ),
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


# Garden
#
# Fragrant chalice in summer and autumn, lenten rose in winter. Rarer plants might flourish in Numa.
scent_garden_garden2 = station("scent_garden_garden2", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Pluck the petals of the lenten rose.
                simple_output( flower.lenten_rose,      season=season.spring ),

                # Gather in Summer
                #
                # Gather the scented blossoms of the fragrant chalice.
                simple_output( flower.fragrant_chalice, season=season.summer ),

                # Gather in Autumn
                #
                # Gather the scented blossoms of the fragrant chalice.
                simple_output( flower.fragrant_chalice, season=season.autumn ),

                # Gather in Winter
                #
                # Pluck the petals of the lenten rose.
                simple_output( flower.lenten_rose,      season=season.winter ),

                # Gather in Numa
                #
                # Only in Numa can I follow the white flowers of moly to its potent black root.
                simple_output( root.moly,               season=season.numa ),
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


# Garden
#
# The 'history plant', <i>agave aeterna</i>, flowers here in summer.
scent_garden_garden3 = station("scent_garden_garden3", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                         season=season.spring ),

                # Gather in Summer
                #
                # The History Plant has risen! Gather its blooms!
                simple_output( flower.agave_aeterna,    season=season.summer ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                         season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                         season=season.winter ),

                # TODO (future) 'simple_output()' with 2x cards
                # Gather in Numa
                #
                # The History Plant has risen! Gather its blooms - all the more plentiful in Numa!
                simple_output( flower.agave_aeterna,    season=season.numa ),
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


# Tangle of Thorns
#
# A flower garden, now overrun with thorned weeds and briar rose.
# ---
# Scent Garden
#
# This too dates from the time of the Abbey... but in summer, neither sisters nor brothers were permitted to spend more than a single hour here, lest the 'temptation of savours' overwhelm them.
scent_garden = room("scent_garden",
    attributes(open_air=1),
    inventory = (
        beverage.skinshuck_mead,
        thing.hurricane_lamp,
    ),
    neighbors = ("entrance_hall", "practic_garden", "servants_hall"),
    power_requirements = attributes(grail=4, nectar=4),
    stations = (
        scent_garden_garden1,
        scent_garden_garden2,
        scent_garden_garden3,
    ),
)

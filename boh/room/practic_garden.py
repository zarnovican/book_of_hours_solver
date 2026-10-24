from ..item import fruit
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# Practic Garden Dummy
#
# Since the Napoleonic War, he has been punched, thumped, stabbed and shot by amateurs, by professionals, and by tipsy guests after dinner. No wonder he looks so cross.
practic_garden_dummy = station("practic_garden_dummy",
    attributes(evolve_via_illumination=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, heart=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, heart=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, heart=1, scale=1, winter=1),
        ),
        slot(
            required=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Garden
#
# Sea-Blest Pears in summer and autumn; in Numa, the 'shining pear', <i>pyrus auricalcinus</i>.
practic_garden_garden = station("practic_garden_garden", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                                 season=season.spring ),

                # Gather in Summer
                #
                # Fragrant pears, soft in the hand.
                simple_output( fruit.bowl_of_sea_blest_pears,   season=season.summer ),

                # Gather in Autumn
                #
                # Fragrant pears, soft in the hand.
                simple_output( fruit.bowl_of_sea_blest_pears,   season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                                 season=season.winter ),

                # Numa:
                #
                # <i>Pyrus auricalcinus</i>. In Numa it develops quickly - the boughs of the tree bend with the fruit.
                simple_output( fruit.pyrus_auricalcinus,        season=season.numa ),
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


# Walled Garden
#
# Iron spikes march along the top of the wall. The gate is rusted shut, but what I can see through the bars is as ruinous as I might expect.
# ---
# Practic Garden
#
# In the early days of St Brandan's Abbey, the brothers practiced the arts of war here. So it was that in Baronial times the garden became a favourite of the martial, quarrelsome Dewulfs.
practic_garden = room("practic_garden",
    attributes(open_air=1),
    neighbors = ("st_brandans_cloister", ),
    power_requirements = attributes(edge=4, nectar=4),
    stations = (
        practic_garden_dummy,
        practic_garden_garden,
    ),
)

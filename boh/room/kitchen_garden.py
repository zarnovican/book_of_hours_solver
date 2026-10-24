from ..item import beast, fruit, liquid, material, memory, sustenance
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# Beehive
#
# Bees, like librarians, are not to be trifled with.
beehive = station("beehive", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Honey or beeswax, if I'm careful.
                simple_output( liquid.honey,        probability=67, season=season.spring ),
                simple_output( material.beeswax,    probability=33, season=season.spring ),

                # Gather in Summer
                #
                # Honey or beeswax, if I'm careful.
                simple_output( liquid.honey,        probability=67, season=season.summer ),
                simple_output( material.beeswax,    probability=33, season=season.summer ),

                # Gather in Autumn
                #
                # I'm unlikely to garner much from the hive at this time of year.
                simple_output( memory.regret,       probability=43, season=season.autumn ),
                simple_output( memory.sound,        probability=43, season=season.autumn ),
                simple_output( memory.hives_lament, probability=14, season=season.autumn ),

                # Gather in Winter
                #
                # I'm unlikely to garner much from the hive at this time of year.
                simple_output( memory.regret,       probability=43, season=season.winter ),
                simple_output( memory.sound,        probability=43, season=season.winter ),
                simple_output( memory.hives_lament, probability=14, season=season.winter ),

                # Gather in Numa
                #
                # In Numa, I might gather honey, beeswax, or something unexpected.
                simple_output( liquid.honey,        probability=17, season=season.numa ),
                simple_output( material.beeswax,    probability=17, season=season.numa ),
                simple_output( memory.hives_lament, probability=17, season=season.numa ),
                simple_output( liquid.cuckoo_honey, probability=33, season=season.numa ),
                simple_output( memory.wistful_air,  probability=17, season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(nectar=1, scale=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(nectar=1, scale=1, lyterion=1),
        ),
    ),
)


# TODO (future) model identifing sack of vegetables
# sustenance.sack_of_vegetables + soul
# - sustenance.pale_marrow
# - thing.potatoes
# - sustenance.pumpkin
# - sustenance.basket_of_onions
# - sustenance.basket_of_leeks

# Garden
#
# Nourishing vegetables in summer and autumn.
garden1 = station("kitchen_garden1", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                                  season=season.spring ),

                # Gather in Summer
                #
                # Carrots, tomatoes, marrows, and blessed onions - all the unsung heroes of the stew-pot.
                simple_output( sustenance.sack_of_vegetables,   season=season.summer ),

                # Gather in Autumn
                #
                # Carrots, tomatoes, marrows, and blessed onions - all the unsung heroes of the stew-pot.
                simple_output( sustenance.sack_of_vegetables,   season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                                  season=season.winter ),

                # Gather in Numa
                #
                # Carrots, tomatoes, marrows, and blessed onions - all the unsung heroes of the stew-pot. In Numa they flourish fast, but there is something odd about their taste.
                simple_output( sustenance.sack_of_vegetables,   season=season.numa ),
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
# The gentle climate of Cornwall supports grapevines. Harvest in spring and summer.
garden2 = station("kitchen_garden2", attributes(),

    simple_actions = (
        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Pluck the grapes from the vine.
                simple_output( fruit.bunch_of_grapes,   season=season.spring ),

                # Gather in Summer
                #
                # Pluck the grapes from the vine.
                simple_output( fruit.bunch_of_grapes,   season=season.summer ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                          season=season.autumn ),

                # Quiet Seasons
                #
                # The earth is quiet - not barren, only sleeping. [Harvesting is possible in a different season.]
                #simple_output(                          season=season.winter ),

                # Gather in Numa
                #
                # Do grapes taste different when plucked in Numa? Perhaps we only imagine it.
                simple_output( fruit.bunch_of_grapes,   season=season.numa ),
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


# Overgrown Kitchen Garden
#
# This place has been surrendered to wind and weed. Bees buzz menacingly. Somewhere, something clucks plaintively.
# ---
# Kitchen Garden
#
# In 1652, Musgrave Dewulf caught a travelling pedlar stealing vegetables from this garden - an eccentric wanderer who went by 'Ricardo Milagro'. Musgrave's ancestors would simply have hung the fellow, but Musgrave decreed seven years' service in the garden instead. When the seven years were up, Milagro had proved his worth as a gardener and chose to make Brancrug his home. The grapevines here are cultivated with rootstock he carried in his pack.
kitchen_garden = room("kitchen_garden",
    attributes(open_air=1),
    inventory = (
        beast.terrence_the_chicken,
        beast.tuppence_the_other_chicken,
    ),
    neighbors = ("well", ),
    power_requirements = attributes(grail=9, nectar=9),
    stations = (
        beehive,
        garden1, # 3x
        garden2,
    ),
)

from ..item import beast, mark, material, memory, sustenance
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# The Gull-Colony
#
# Steal eggs from the sea-birds, or find what the sea-birds have stolen.
the_gull_colony = station("the_gull_colony", attributes(),

    simple_actions = (

        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # The birds are furiously vigilant.
                # ---
                # Gather in Spring
                #
                # Scraps from the isle's edge.
                simple_output( sustenance.gulls_egg,        probability=33, season=season.spring ),
                simple_output( memory.sound,                probability=33, season=season.spring ),
                simple_output( material.awakened_feather,   probability=11, season=season.spring ),
                simple_output( beast.orphaned_chick,        probability=22, season=season.spring ),

                # Gather in Summer
                #
                # The sea rolls below.
                # ---
                # Gather in Summer
                #
                # Scraps from the isle's edge.
                simple_output( sustenance.gulls_egg,        probability=33, season=season.summer ),
                simple_output( memory.sound,                probability=33, season=season.summer ),
                simple_output( material.awakened_feather,   probability=11, season=season.summer ),
                simple_output( memory.wind_rumour,          probability=11, season=season.summer ),
                simple_output( beast.orphaned_chick,        probability=11, season=season.summer ),

                # Gather in Autumn
                #
                # Fierce yellow eyes watch my every move.
                # ---
                # Gather in Autumn
                #
                # Scraps from the isle's edge.
                simple_output( sustenance.gulls_egg,        probability=33, season=season.autumn ),
                simple_output( memory.sound,                probability=33, season=season.autumn ),
                simple_output( material.awakened_feather,   probability=11, season=season.autumn ),
                simple_output( memory.wind_rumour,          probability=11, season=season.autumn ),
                simple_output( material.driftwood_fragment, probability=11, season=season.autumn ),

                # Gather in Winter
                #
                # The wind is bitter today.
                # ---
                # Gather in Winter
                #
                # Scraps from the isle's edge.
                simple_output( sustenance.gulls_egg,        probability=33, season=season.winter ),
                simple_output( memory.sound,                probability=33, season=season.winter ),
                simple_output( material.awakened_feather,   probability=11, season=season.winter ),
                simple_output( memory.wind_rumour,          probability=11, season=season.winter ),
                simple_output( material.driftwood_fragment, probability=11, season=season.winter ),

                # Gather in Numa
                #
                # What pilgrims pass in Numa?
                # ---
                # Gather in Numa
                #
                # Much is lost, but much remains...
                simple_output( sustenance.gulls_egg,        probability=14, season=season.numa ),
                simple_output( material.awakened_feather,   probability=14, season=season.numa ),
                simple_output( memory.wind_rumour,          probability=14, season=season.numa ),
                simple_output( sustenance.outsized_egg,     probability=14, season=season.numa ),
                simple_output( memory.horizon_sight,        probability=14, season=season.numa ),
                simple_output( mark.salt_sign,              probability=14, season=season.numa ),
                simple_output( material.tanglebrag,         probability=14, season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(rose=1, scale=1, sky=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(rose=1, scale=1, sky=1),
        ),
    ),
)


# Shrieking Gull-Cloud
#
# The gulls have made this their kingdom, and they have grown intolerant of interlopers. We'll have to pacify or discourage them.
# ---
# Gull Colony
#
# Through all the Isle's long years, the gulls, heedless of our affairs, have taken their due from the sea and returned it to the rocks. Careful where you step.
gull_colony = room("gull_colony",
    attributes(open_air=1),
    neighbors = ("earl_brians_field", ),
    power_requirements = attributes(edge=12, sky=12),
    stations = (
    ),
)

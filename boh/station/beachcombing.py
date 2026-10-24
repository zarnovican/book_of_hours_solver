from ..item import beast, cache, flower, fruit, leaf, mark, material, remains
from ..model import attributes, condition, season, simple_action, simple_output, slot, station


# (gather -> hush house key)
#
# Something Familiar
#
# Something half-buried in the sand...
# ---
# Something Familiar
#
# A familiar iron key has washed up on the beach.


# Beachcombing
#
# Take a long walk along the ocean's side. If I know what to look for, I might find something the ocean has forsaken.
beachcombing = station("beachcombing", attributes(),

    simple_actions = (

        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # What has the sea ceded today?
                # ---
                # Gather in Spring
                #
                # Sea-strewn salt-snared stuff.
                simple_output( material.sand,               probability=13, season=season.spring ),
                simple_output( remains.mackerel,            probability=13, season=season.spring ),
                simple_output( material.whispering_sand,    probability= 7, season=season.spring ),
                simple_output( material.curious_seashell,   probability= 7, season=season.spring ),
                simple_output( flower.evas_locks,           probability= 7, season=season.spring ),
                simple_output( beast.stray_cat,             probability= 7, season=season.spring ),
                simple_output( cache.contraband_flotsam,    probability= 7, season=season.spring ),
                simple_output( cache.contraband_jetsam,     probability= 7, season=season.spring ),
                simple_output( material.driftwood_fragment, probability= 7, season=season.spring ),
                simple_output( material.sea_glass,          probability= 7, season=season.spring ),
                simple_output( leaf.vase_of_rushes,         probability= 7, season=season.spring ),
                simple_output( remains.pilchards,           probability=13, season=season.spring ),

                # Gather in Summer
                #
                # What has the sea ceded today?
                # ---
                # Gather in Summer
                #
                # Sea-strewn salt-snared stuff.
                simple_output( material.sand,               probability=13, season=season.summer ),
                simple_output( remains.mackerel,            probability=13, season=season.summer ),
                simple_output( material.whispering_sand,    probability= 7, season=season.summer ),
                simple_output( material.curious_seashell,   probability= 7, season=season.summer ),
                simple_output( flower.evas_locks,           probability=13, season=season.summer ),
                simple_output( beast.stray_cat,             probability= 7, season=season.summer ),
                simple_output( cache.contraband_flotsam,    probability= 7, season=season.summer ),
                simple_output( material.driftwood_fragment, probability= 7, season=season.summer ),
                simple_output( material.sea_glass,          probability= 7, season=season.summer ),
                simple_output( leaf.vase_of_rushes,         probability= 7, season=season.summer ),
                simple_output( remains.pilchards,           probability=13, season=season.summer ),

                # Gather in Autumn
                #
                # What has the sea ceded today?
                # ---
                # Gather in Autumn
                #
                # Sea-strewn salt-snared stuff.
                simple_output( material.sand,               probability=19, season=season.autumn ),
                simple_output( remains.mackerel,            probability=13, season=season.autumn ),
                simple_output( material.whispering_sand,    probability= 6, season=season.autumn ),
                simple_output( material.curious_seashell,   probability= 6, season=season.autumn ),
                simple_output( flower.evas_locks,           probability=13, season=season.autumn ),
                simple_output( beast.stray_cat,             probability= 6, season=season.autumn ),
                simple_output( cache.contraband_flotsam,    probability= 6, season=season.autumn ),
                simple_output( cache.contraband_jetsam,     probability= 6, season=season.autumn ),
                simple_output( material.driftwood_fragment, probability= 6, season=season.autumn ),
                simple_output( material.sea_glass,          probability= 6, season=season.autumn ),
                simple_output( remains.pilchards,           probability=13, season=season.autumn ),

                # Gather in Winter
                #
                # What has the sea ceded today?
                # ---
                # Gather in Winter
                #
                # Sea-strewn salt-snared stuff.
                simple_output( material.sand,               probability=47, season=season.winter ),
                simple_output( material.whispering_sand,    probability= 7, season=season.winter ),
                simple_output( material.curious_seashell,   probability= 7, season=season.winter ),
                simple_output( flower.evas_locks,           probability= 7, season=season.winter ),
                simple_output( beast.stray_cat,             probability= 7, season=season.winter ),
                simple_output( cache.contraband_flotsam,    probability= 7, season=season.winter ),
                simple_output( cache.contraband_jetsam,     probability= 7, season=season.winter ),
                simple_output( material.driftwood_fragment, probability= 7, season=season.winter ),
                simple_output( material.sea_glass,          probability= 7, season=season.winter ),

                # Gather in Numa
                #
                # The Numa-fog is thick here.
                # ---
                # Gather in Numa
                #
                # Tide-wracked treasures.
                simple_output( remains.mackerel,            probability= 7, season=season.numa ),
                simple_output( material.whispering_sand,    probability=20, season=season.numa ),
                simple_output( material.curious_seashell,   probability=13, season=season.numa ),
                simple_output( beast.stray_cat,             probability= 7, season=season.numa ),
                simple_output( cache.contraband_flotsam,    probability= 7, season=season.numa ),
                simple_output( cache.contraband_jetsam,     probability= 7, season=season.numa ),
                simple_output( remains.pilchards,           probability= 7, season=season.numa ),
                simple_output( material.ambergris_chunk,    probability= 7, season=season.numa ),
                simple_output( fruit.misshapen_fruit,       probability= 7, season=season.numa ),
                simple_output( remains.human_hair,          probability= 7, season=season.numa ),
                simple_output( material.rose_pearl,         probability= 7, season=season.numa ),
                simple_output( beast.savage_relic,          probability= 7, season=season.numa ),
                simple_output( mark.salt_sign,              probability= 7, season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, moon=1, rose=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, moon=1, rose=1),
        ),
    ),
)

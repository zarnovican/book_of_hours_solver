from ..item import beast, cache, fruit, leaf, material, memory, remains, sustenance
from ..model import attributes, condition, season, simple_action, simple_output, slot, station


# A Walk on the Moor
#
# Clamber up into the long reaches of the moors behind the village. Lean into the wind's fluttering fist. If I know what to look for, I might find something among the rocks.
a_walk_on_the_moor = station("a_walk_on_the_moor", attributes(),

    simple_actions = (

        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # The gorse is bright on the land's nape.
                # ---
                # Gather in Spring
                #
                # Unexpected finds in the folds of earth and sky.
                simple_output( material.hawthorn_blank,     probability=12, season=season.spring ),
                simple_output( material.quartz_chunk,       probability=12, season=season.spring ),
                simple_output( material.granite_slab,       probability=12, season=season.spring ),
                simple_output( material.serpentinite_slab,  probability=12, season=season.spring ),
                simple_output( material.yew_blank,          probability=12, season=season.spring ),
                simple_output( beast.stray_dog,             probability= 6, season=season.spring ),
                simple_output( cache.abandoned_luggage,     probability= 6, season=season.spring ),
                simple_output( cache.abandoned_packages,    probability= 6, season=season.spring ),
                simple_output( leaf.vase_of_gorse,          probability= 6, season=season.spring ),
                simple_output( sustenance.viper_egg,        probability=12, season=season.spring ),
                # mushrooms

                # Gather in Summer
                #
                # The wind's almost warm.
                # ---
                # Gather in Summer
                #
                # Unexpected finds in the folds of earth and sky.
                simple_output( material.hawthorn_blank,     probability= 9, season=season.summer ),
                simple_output( material.quartz_chunk,       probability= 9, season=season.summer ),
                simple_output( material.granite_slab,       probability= 9, season=season.summer ),
                simple_output( material.serpentinite_slab,  probability= 9, season=season.summer ),
                simple_output( material.yew_blank,          probability= 9, season=season.summer ),
                simple_output( beast.stray_dog,             probability= 5, season=season.summer ),
                simple_output( cache.abandoned_luggage,     probability= 5, season=season.summer ),
                simple_output( cache.abandoned_packages,    probability= 5, season=season.summer ),
                simple_output( leaf.vase_of_gorse,          probability= 5, season=season.summer ),
                simple_output( beast.wild_viper,            probability= 9, season=season.summer ),
                # mushrooms
                simple_output( fruit.rosehips,              probability= 9, season=season.summer ),
                simple_output( fruit.basket_of_apples,      probability= 9, season=season.summer ),
                simple_output( fruit.blackberries,          probability= 5, season=season.summer ),

                # Gather in Autumn
                #
                # The last leaves toss and scutter.
                # ---
                # Gather in Autumn
                #
                # Unexpected finds in the folds of earth and sky.
                simple_output( material.hawthorn_blank,     probability=11, season=season.autumn ),
                simple_output( material.quartz_chunk,       probability=11, season=season.autumn ),
                simple_output( material.granite_slab,       probability=11, season=season.autumn ),
                simple_output( material.serpentinite_slab,  probability=11, season=season.autumn ),
                simple_output( material.yew_blank,          probability=11, season=season.autumn ),
                simple_output( remains.animal_bones,        probability=11, season=season.autumn ),
                simple_output( beast.stray_dog,             probability= 5, season=season.autumn ),
                # mushrooms                                 5,
                simple_output( fruit.rosehips,              probability= 5, season=season.autumn ),
                simple_output( fruit.basket_of_apples,      probability=11, season=season.autumn ),
                simple_output( fruit.blackberries,          probability=11, season=season.autumn ),

                # Gather in Winter
                #
                # Rime rims the moor-tarns.
                # ---
                # Gather in Winter
                #
                # Unexpected finds in the folds of earth and sky.
                simple_output( material.hawthorn_blank,     probability=15, season=season.winter ),
                simple_output( material.quartz_chunk,       probability=15, season=season.winter ),
                simple_output( material.granite_slab,       probability=15, season=season.winter ),
                simple_output( material.serpentinite_slab,  probability=15, season=season.winter ),
                simple_output( material.yew_blank,          probability=15, season=season.winter ),
                simple_output( remains.animal_bones,        probability=15, season=season.winter ),
                simple_output( beast.stray_dog,             probability= 8, season=season.winter ),

                # Gather in Numa
                #
                # Is it wise to walk on the moors in this season? Let's find out.
                # ---
                # Gather in Numa
                #
                # Much is lost, but much remains...
                simple_output( beast.stray_dog,             probability=20, season=season.numa ),
                simple_output( memory.enduring_reflection,  probability=20, season=season.numa ),
                simple_output( memory.earth_sign,           probability=20, season=season.numa ),
                simple_output( memory.wind_rumour,          probability=20, season=season.numa ),
                simple_output( remains.skaptodon_fang,      probability=20, season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, rose=1, scale=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, rose=1, scale=1),
        ),
    ),
)

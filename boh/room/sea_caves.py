from ..item import cache, flower, mark, material, memory, sustenance
from ..model import attributes, condition, room, season, simple_action, simple_output, slot, station


# The Sea-Caves
#
# Splash cautiously through the shallower tunnels.
the_sea_caves = station("the_sea_caves", attributes(),

    simple_actions = (

        simple_action("gather",
            output = (
                # Gather in Spring
                #
                # Echoes in the endless night...
                # ---
                # Gather in Spring
                #
                # Gleanings from the darkness.
                simple_output( material.phosphorescent_scrapings,   probability=43, season=season.spring ),
                simple_output( memory.fear,                         probability=14, season=season.spring ),
                simple_output( sustenance.outsized_egg,             probability=14, season=season.spring ),
                simple_output( material.driftwood_fragment,         probability=14, season=season.spring ),
                simple_output( material.sand,                       probability=14, season=season.spring ),

                # Gather in Summer
                #
                # Echoes in the endless night...
                # ---
                # Gather in Summer
                #
                # Gleanings from the darkness.
                simple_output( material.phosphorescent_scrapings,   probability=43, season=season.summer ),
                simple_output( memory.fear,                         probability=14, season=season.summer ),
                simple_output( flower.evas_locks,                   probability=29, season=season.summer ),
                simple_output( sustenance.outsized_egg,             probability=14, season=season.summer ),

                # Gather in Autumn
                #
                # Echoes in the endless night...
                # ---
                # Gather in Autumn
                #
                # Gleanings from the darkness.
                simple_output( material.phosphorescent_scrapings,   probability=43, season=season.autumn ),
                simple_output( memory.fear,                         probability=29, season=season.autumn ),
                simple_output( flower.evas_locks,                   probability=29, season=season.autumn ),

                # Gather in Winter
                #
                # Echoes in the endless night...
                # ---
                # Gather in Winter
                #
                # Gleanings from the darkness.
                simple_output( material.phosphorescent_scrapings,   probability=43, season=season.winter ),
                simple_output( memory.fear,                         probability=29, season=season.winter ),
                simple_output( cache.contraband_jetsam,             probability=14, season=season.winter ),
                simple_output( material.sea_glass,                  probability=14, season=season.winter ),

                # Gather in Numa
                #
                # What has Numa brought?
                # ---
                # Gather in Numa
                #
                # Much is lost, but much remains...
                simple_output( material.phosphorescent_scrapings,   probability=50, season=season.numa ),
                simple_output( memory.enduring_reflection,          probability=25, season=season.numa ),
                simple_output( mark.salt_sign,                      probability=25, season=season.numa ),
            ),
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moon=1, scale=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moon=1, scale=1),
        ),
    ),
)


# Submerged Sea-Caves
#
# The sea has claimed these caves. The tide thunders below. I'll need to find some way to lower the water level before I can enter.
# ---
# Sea-Caves
#
# The Curia's last secret. Right under Governor Collers' nose, Levinsen, Blackwood and van Lauren all continued their careful investigations of the Brancrug sea-caves. Many of the species here are unknown to Cornwall. Some have not been seen anywhere under this Sun.
sea_caves = room("sea_caves",
    attributes(dawn_period=1),
    neighbors = ("boathouse", ),
    stations = (
        the_sea_caves,
    ),
)

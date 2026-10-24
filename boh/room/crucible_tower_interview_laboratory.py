from ..item import liquid, material, remains
from ..model import attributes, condition, room, slot, station


# Condignator
#
# The terrible heart of the Governor's terrible project.
condignator = station("condignator",
    attributes(evolve_via_skolekosophy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, forge=1, knock=1, lantern=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, forge=1, knock=1, lantern=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, forge=1, knock=1, lantern=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, fuel=1, memory=1, remains=1, tool=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, fuel=1, memory=1, remains=1, tool=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Charred Chamber
#
# The iron door here stands ajar - but it still glows faintly red, even after all these years. This is not a natural heat, and there is no entirely natural way to quell it.
# ---
# Crucible Tower: Interview Laboratory
#
# When a prisoner resisted all other interventions, Collers would bring them here, to test and refine their worth. His successes might be transferred to Zurich, or turned over to the Légion du Seuil to earn their humanity, or even, at least once, released. But his successes were not numerous.
#
# Here, at last, is where the fire began and where it ended. When the power below the prison was released, it came here to interview Collers. Perhaps it intended to put him in his own device; but it seems there was not nearly enough left of him for that.
crucible_tower_interview_laboratory = room("crucible_tower_interview_laboratory",
    attributes(nocturnal_period=1),
    inventory = (
        liquid.black_sapphire_wash,
        liquid.gideons_soaks,
        liquid.regensburg_balm,
        liquid.wolf_snow_ampoule,
        material.labhitic_tincture,
        material.phosphorescent_scrapings,
        remains.heart_in_a_jar,
    ),
    neighbors = ("crucible_tower_governors_quarters", ),
    power_requirements = attributes(knock=14, moth=14, winter=14),
    stations = (
        condignator,
    ),
)

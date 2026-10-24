from ..model import attributes, card_type, condition, craft_recipe
from ..item import beast, beverage, device, liquid, material, memory, skill


# --- knock 5 ---

# Craft: Amethyst Ampoule
#
# Shape, tint, fill a paradoxical Knock-ampoule. 
#
# [Glassblowing & Vesselcrafting with Prentice-level <sprite name=knock> creates Amethyst Ampoule. Or for a Scholar-level recipe: if I add a Metal, I'll create an exotic alloy.]
# ---
# Craft: Amethyst Ampoule
#
# It has its uses, but none of them are simple and few are safe.
craft_recipe(
    output = liquid.amethyst_ampoule,
    power_requirements = attributes(knock=5),
    skills = (
        skill.glassblowing_and_vesselcrafting,
        skill.lockworks_and_clockworks,
        skill.solutions_and_separations,
        skill.surgeries_and_exsanguinations,
        skill.the_great_signs_and_the_great_scars,
    ),
)

# Craft: Secret Threshold
#
# Employ a complex round of rhymes to establish a new threshold. 
#
# [Preliminal Meter with Prentice-level <sprite name=knock> creates Secret Threshold. Or for a Scholar-level recipe: if I add a Memory, it'll resolve to a Knock-insight.]
# ---
# Craft: Secret Threshold
#
# An opening-opportunity that'll last a little while.
craft_recipe(
    output = memory.secret_threshold,
    power_requirements = attributes(knock=5),
    skills = (
        skill.door_and_wall,
        skill.edicts_liminal,
        skill.horns_and_ivories,
        skill.preliminal_meter,
    ),
)

# --- knock 10 ---

# Craft: Gervinite
#
# Resolve a Knock-alloy.
#
# [Lockworks & Clockworks with Scholar-level <sprite name=knock>, plus Glass, creates Gervinite.]
# ---
# Craft: Gervinite
#
# [With Keeper-level Knock, gervinite is the essential ingredient of a Chronsichord.]
craft_recipe(
    output = material.gervinite,
    power_requirements = attributes(knock=10),
    skills = (
        skill.lockworks_and_clockworks,
    ),
    solution_must_include = condition(glass=1),
)

# Craft: Glassfinger Toxin
#
# Brew a bright and lethal Knock-toxin.
#
# [Door & Wall with Scholar-level <sprite name=knock>, plus Liquid, creates Glassfinger Toxin.]
# ---
# Craft: Glassfinger Toxin
#
# [With Keeper-level Knock, Glassfinger Toxin is the precursor of the Sacrament Ascite.]
craft_recipe(
    output = liquid.glassfinger_toxin,
    power_requirements = attributes(knock=10),
    skills = (
        skill.door_and_wall,
        skill.edicts_liminal,
        skill.solutions_and_separations,
        skill.surgeries_and_exsanguinations,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Wire (Orichalcum)
#
# Use this metal as a base for the fabled Forge-alloy called orichalcum.
#
# [Glassblowing & Vesselcrafting with Scholar-level <sprite name=knock>, plus Metal, creates Wire (Orichalcum).]
# ---
# Craft: Wire (Orichalcum)
#
# [With Keeper-level Forge, orichalcum can catalyse and contain the Azoth.]
craft_recipe(
    output = material.wire_orichalcum,
    power_requirements = attributes(knock=10),
    skills = (
        skill.glassblowing_and_vesselcrafting,
    ),
    solution_must_include = condition(metal=1),
)

# Craft: Chimeric Larva
#
# Hatch an eyeless larva pulsing with Moth-potential.
#
# [Horns & Ivories with Scholar-level <sprite name=knock>, plus Egg, creates Chimeric Larva.]
# ---
# Craft: Chimeric Larva
#
# [With Keeper-level Moth - not Knock - and a more suitable skill, perhaps I could coax this to develop further - as long as it's well-fed.]
craft_recipe(
    output = beast.chimeric_larva,
    power_requirements = attributes(knock=10),
    skills = (
        skill.horns_and_ivories,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Curious Hunch
#
# Knit memories into certainty.
#
# [Preliminal Meter with Scholar-level <sprite name=knock>, plus Memory, creates Curious Hunch.]
# ---
# Craft: Curious Hunch
#
# The Moth's gift? Or mine?
craft_recipe(
    output = memory.curious_hunch,
    power_requirements = attributes(knock=10),
    skills = (
        skill.preliminal_meter,
        skill.the_great_signs_and_the_great_scars,
    ),
    solution_must_include = condition(memory=1),
)

# --- knock 15 ---

# Craft: Chronsichord
#
# Place the gervinite at the heart of a Knock-device.
#
# [The Great Signs and the Great Scars with Keeper-level <sprite name=knock>, plus Gervinite, creates Chronsichord.]
# ---
# Craft: Chronsichord
#
# When a chronsichord is completed, it is fully wound, for the first and only time.
craft_recipe(
    output = device.chronsichord,
    power_requirements = attributes(knock=15),
    skills = (
        skill.glassblowing_and_vesselcrafting,
        skill.glaziery_and_lightsmithing,
        skill.lockworks_and_clockworks,
        skill.preliminal_meter,
        skill.the_great_signs_and_the_great_scars,
    ),
    solution_must_include = condition(one_of=(material.gervinite, )),
)

# Craft: January Sanguinary
#
# Enliven the toxin into something with a greater Heart-aspect.
#
# [Surgeries & Exsanguinations with Keeper-level <sprite name=knock>, plus Glassfinger Toxin, creates January Sanguinary.]
# ---
# Craft: January Sanguinary
#
# Stopper it quickly. Quickly!.
craft_recipe(
    output = liquid.january_sanguinary,
    power_requirements = attributes(knock=15),
    skills = (
        skill.surgeries_and_exsanguinations,
    ),
    solution_must_include = condition(one_of=(liquid.glassfinger_toxin, )),
)

# Craft: Sacrament Ascite
#
# Induce a change in the toxin, to make it more Knock-potent but safer.
#
# [Solutions & Separations with Keeper-level <sprite name=knock>, plus Glassfinger Toxin, creates Sacrament Ascite.]
# ---
# Craft: Sacrament Ascite
#
# In the name of the two blades that are one, of the threshold which has two sides….
craft_recipe(
    output = beverage.sacrament_ascite,
    power_requirements = attributes(knock=15),
    skills = (
        skill.door_and_wall,
        skill.edicts_liminal,
        skill.glassblowing_and_vesselcrafting,
        skill.horns_and_ivories,
        skill.solutions_and_separations,
    ),
    solution_must_include = condition(one_of=(liquid.glassfinger_toxin, )),
)

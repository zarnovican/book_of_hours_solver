from ..model import attributes, card_type, condition, craft_recipe
from ..item import flower, liquid, mark, memory, skill


# --- rose 5 ---

# Craft: Salt-Sign
#
# Use salt to trace a sigil of journeys and returns.
#
# [Path & Pilgrim with Prentice-level <sprite name=rose> creates Salt-Sign. Or for a Scholar-level recipe: if I add a Memory, I can achieve an insight more powerful than this Sign.]
# ---
# Craft: Salt-Sign
#
# Elegant as a footprint.
craft_recipe(
    output = mark.salt_sign,
    power_requirements = attributes(rose=5),
    skills = (
        skill.inks_of_power,
        skill.path_and_pilgrim,
        skill.pearl_and_tide,
        skill.sand_stories,
    ),
)

# Craft: Confounding Parable
#
# Let the wind-sounds gradually recall a subtle memory.
#
# [Sky Stories with Prentice-level <sprite name=rose> creates Confounding Parable. Or for a Scholar-level recipe: if I bring in another Memory, I can conceive a higher insight.]
# ---
# Craft: Confounding Parable
#
# It fits fairly tidily in the mind, as long as you turn it sideways.
craft_recipe(
    output = memory.confounding_parable,
    power_requirements = attributes(rose=5),
    skills = (
        skill.preliminal_meter,
        skill.sky_stories,
    ),
)

# --- rose 10 ---

# Craft: Ichor Auroral
#
# Condense light to a Rose-fluid.
#
# [Sand Stories with Scholar-level <sprite name=rose>, plus Light, creates Ichor Auroral.]
# ---
# Craft: Ichor Auroral
#
# [With Keeper-level  Rose, the Ichor Auroral is a precursor to the Great Ink Porphyrine.]
craft_recipe(
    output = liquid.ichor_auroral,
    power_requirements = attributes(rose=10),
    skills = (
        skill.auroral_contemplations,
        skill.inks_of_power,
        skill.sand_stories,
    ),
    solution_must_include = condition(light=1),
)

# Craft: Enduring Reflection
#
# Refine memory to something of Rose. 
#
# [Path & Pilgrim with Scholar-level <sprite name=rose>, plus Memory, creates Enduring Reflection.]
# ---
# Craft: Enduring Reflection
#
# [With Keeper-level  Rose, an Enduring Reflection can give rise to visions of wilder possibilities...]
craft_recipe(
    output = memory.enduring_reflection,
    power_requirements = attributes(rose=10),
    skills = (
        skill.path_and_pilgrim,
        skill.pearl_and_tide,
        skill.preliminal_meter,
        skill.sky_stories,
    ),
    solution_must_include = condition(memory=1),
)

# --- rose 15 ---

# Craft: Porphyrine
#
# Deepen the ichor into the <i>encaustum terminale</i> Porphyrine.
#
# [Sand Stories with Keeper-level <sprite name=rose>, plus Ichor Auroral, creates Porphyrine.]
# ---
# Craft: Porphyrine
#
# Lift your eyes. That's often good advice, but when we're about this business, it's the best. Lift your eyes, and look around.
craft_recipe(
    output = liquid.porphyrine,
    power_requirements = attributes(rose=15),
    skills = (
        skill.inks_of_power,
        skill.inks_of_revelation,
        skill.sand_stories,
    ),
    solution_must_include = condition(one_of=(liquid.ichor_auroral, )),
)

# Craft: Porphyrine
#
# A little-known secret: use the rose-petals to brew the <i>encaustum terminale</i> Porphyrine.
#
# [Pearl & Tide with Keeper-level <sprite name=rose>, plus Lenten Rose, creates Porphyrine.]
# ---
# Craft: Porphyrine
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.porphyrine,
    power_requirements = attributes(rose=15),
    skills = (
        skill.pearl_and_tide,
    ),
    solution_must_include = condition(one_of=(flower.lenten_rose, )),
)

# Craft: Horizon-Sight
#
# Draw a Rose-vision from this memory.
#
# [Path & Pilgrim with Keeper-level <sprite name=rose>, plus Enduring Reflection, creates Horizon-Sight.]
# ---
# Craft: Horizon-Sight
#
# Lift your eyes. That's often good advice, but when we're about this business, it's the best. Lift your eyes, and look around.
craft_recipe(
    output = memory.horizon_sight,
    power_requirements = attributes(rose=15),
    skills = (
        skill.path_and_pilgrim,
        skill.preliminal_meter,
        skill.sand_stories,
        skill.sky_stories,
    ),
    solution_must_include = condition(one_of=(memory.enduring_reflection, )),
)

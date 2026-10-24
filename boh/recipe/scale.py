from ..model import attributes, card_type, condition, craft_recipe
from ..item import beast, beverage, liquid, mark, memory, skill


# --- scale 5 ---

# Craft: Bisclavret's Knot
#
# Use earth to trace a sigil of the Hill-Children.
#
# [Path & Pilgrim with Prentice-level <sprite name=scale> creates Bisclavret's Knot. Or for a Scholar-level recipe: add a Memory to recall something older and more powerful.]
# ---
# Craft: Bisclavret's Knot
#
# A difficult tangle of lines.
craft_recipe(
    output = mark.bisclavrets_knot,
    power_requirements = attributes(scale=5),
    skills = (
        skill.coil_and_chasm,
        skill.furs_and_feathers,
        skill.hill_and_hollow,
        skill.horns_and_ivories,
        skill.path_and_pilgrim,
        skill.pentiments_and_precursors,
        skill.serpents_and_venoms,
        skill.wolf_stories,
    ),
)

# Craft: Perhibiate
#
# I can brew a minor Ink of Power: a binding ink.
#
# [Inks of Power with Prentice-level <sprite name=scale> creates Perhibiate. Or for a Scholar-level recipe: if I crush in a suitable Leaf, I can make this a deadlier and more potent Ink.]
# ---
# Craft: Perhibiate
#
# Some authorities claim it's difficult to lose a pot of perhibiate ink, but they haven't lived at Hush House.
craft_recipe(
    output = liquid.perhibiate,
    power_requirements = attributes(scale=5),
    skills = (
        skill.inks_of_power,
    ),
)

# Craft: Savage Hymn
#
# Recall the hymns of the hill-cults.
#
# [Drums & Dances with Prentice-level <sprite name=scale> creates Savage Hymn.]
# ---
# Craft: Savage Hymn
#
# Harsh on the tongue.
craft_recipe(
    output = memory.savage_hymn,
    power_requirements = attributes(scale=5),
    skills = (
        skill.drums_and_dances,
        skill.stone_stories,
    ),
)

# --- scale 10 ---

# Craft: Glassfinger Toxin
#
# Brew a bright and lethal Knock-toxin.
#
# [Serpents & Venoms with Scholar-level <sprite name=scale>, plus Liquid, creates Glassfinger Toxin.]
# ---
# Craft: Glassfinger Toxin
#
# [With Serpents & Venoms, and Keeper-level Moon - not Scale -  Glassfinger Toxin is the precursor of the Sacrament Ascite.]
craft_recipe(
    output = liquid.glassfinger_toxin,
    power_requirements = attributes(scale=10),
    skills = (
        skill.serpents_and_venoms,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Perinculate
#
# Brew a notoriously deadly Ink of Power.
#
# [Inks of Power with Scholar-level <sprite name=scale>, plus Leaf, creates Perinculate.]
# ---
# Craft: Perinculate
#
# [With Keeper-level Edge, Perinculate is the precursor to Serpent-Milk.]
craft_recipe(
    output = liquid.perinculate,
    power_requirements = attributes(scale=10),
    skills = (
        skill.inks_of_power,
    ),
    solution_must_include = condition(leaf=1),
)

# Craft: Living Relic
#
# Hatch a Scale-relic from the egg.
#
# [Stone Stories with Scholar-level <sprite name=scale>, plus Egg, creates Living Relic.]
# ---
# Craft: Living Relic
#
# [With Keeper-level Scale, a Living Relic can be induced to help with the production of Houndsgall.]
craft_recipe(
    output = beast.living_relic,
    power_requirements = attributes(scale=10),
    skills = (
        skill.furs_and_feathers,
        skill.hill_and_hollow,
        skill.pentiments_and_precursors,
        skill.stone_stories,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Old Moment
#
# Recall something lost, something Scale-aspected…
#
# [Path & Pilgrim with Scholar-level <sprite name=scale>, plus Memory, creates Old Moment.]
# ---
# Craft: Old Moment
#
# [With Keeper-level Scale, an Old Moment can lead to an Earthquake Name.]
craft_recipe(
    output = memory.old_moment,
    power_requirements = attributes(scale=10),
    skills = (
        skill.coil_and_chasm,
        skill.horns_and_ivories,
        skill.path_and_pilgrim,
        skill.wolf_stories,
    ),
    solution_must_include = condition(memory=1),
)

# --- scale 15 ---

# Craft: Houndsgall
#
# Certain Relic… byproducts… can be repurposed to brew a Scale-ink.
#
# [Path & Pilgrim with Keeper-level <sprite name=scale>, plus Living Relic, creates Houndsgall.]
# ---
# Craft: Houndsgall
#
# I wish I hadn't had to see exactly what I was doing, there….
craft_recipe(
    output = liquid.houndsgall,
    power_requirements = attributes(scale=15),
    skills = (
        skill.horns_and_ivories,
        skill.inks_of_containment,
        skill.path_and_pilgrim,
        skill.pentiments_and_precursors,
    ),
    solution_must_include = condition(one_of=(beast.living_relic, )),
)

# Craft: Serpent-Milk
#
# Enrich the ink to a fluid vibrant with Edge-power.
#
# [Serpents & Venoms with Keeper-level <sprite name=scale>, plus Perinculate, creates Serpent-Milk.]
# ---
# Craft: Serpent-Milk
#
# No Librarian of Hush House has ever died during the preparation of serpent-milk. Thankfully, this was true yesterday and it is still true today.
craft_recipe(
    output = beverage.serpent_milk,
    power_requirements = attributes(scale=15),
    skills = (
        skill.serpents_and_venoms,
    ),
    solution_must_include = condition(one_of=(liquid.perinculate, )),
)

# Craft: Earthquake Name
#
# Discern a potency of Scale.
#
# [Stone Stories with Keeper-level <sprite name=scale>, plus Old Moment, creates Earthquake Name.]
# ---
# Craft: Earthquake Name
#
# Speak half a syllable, and feel the beast stir half a coil....
craft_recipe(
    output = memory.earthquake_name,
    power_requirements = attributes(scale=15),
    skills = (
        skill.coil_and_chasm,
        skill.hill_and_hollow,
        skill.stone_stories,
        skill.wolf_stories,
    ),
    solution_must_include = condition(one_of=(memory.old_moment, )),
)

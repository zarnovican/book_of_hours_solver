from ..model import attributes, card_type, condition, craft_recipe
from ..item import beverage, liquid, material, memory, skill


# --- edge 5 ---

# Craft: Labhitic Tincture
#
# Focus my own and local resources to create a small quantity of a stable Edge ingredient.
#
# [Sickle & Eclipse with Prentice-level <sprite name=edge> creates Labhitic Tincture. Or Scholar-level Edge, plus something with the Leaf aspect, will brew me a dangerous ink.]
# ---
# Craft: Labhitic Tincture
#
# As it clarifies, the Tincture vibrates judderingly. This is called 'growling'.
craft_recipe(
    output = material.labhitic_tincture,
    power_requirements = attributes(edge=5),
    skills = (
        skill.disciplines_of_the_hammer,
        skill.edicts_martial,
        skill.ragged_crossroads,
        skill.sickle_and_eclipse,
    ),
)

# Craft: Torgue's Cleansing
#
# Purge myself of harmonious resonances, accruing some personal Edge. It won't be pleasant.
#
# [Auroral Contemplations with Prentice-level <sprite name=edge> creates Torgue's Cleansing. Or for a Scholar-level recipe: add something with a Memory aspect, and I have the makings of a significant Edge Memory.]
# ---
# Craft: Torgue's Cleansing
#
# The Cleansing has left my skin burning, my teeth throbbing. The Corrivality rumbles beneath the membraneous surfaces of the waking world.
craft_recipe(
    output = memory.torgues_cleansing,
    power_requirements = attributes(edge=5),
    skills = (
        skill.auroral_contemplations,
        skill.disciplines_of_the_scar,
        skill.meniscate_reflections,
        skill.sharps,
    ),
)

# --- edge 10 ---

# Craft: Perinculate
#
# Brew a notoriously deadly Ink of Power.
#
# [Edicts Martial with Scholar-level <sprite name=edge>, plus Leaf, creates Perinculate.]
# ---
# Craft: Perinculate
#
# [With Keeper-level Edge, Perinculate is the precursor to Serpent-Milk.]
craft_recipe(
    output = liquid.perinculate,
    power_requirements = attributes(edge=10),
    skills = (
        skill.disciplines_of_the_scar,
        skill.edicts_martial,
        skill.sickle_and_eclipse,
    ),
    solution_must_include = condition(leaf=1),
)

# Craft: Winning Move
#
# Establish a synthesis of alternatives.
#
# [Meniscate Reflections with Scholar-level <sprite name=edge>, plus Memory, creates Winning Move.]
# ---
# Craft: Winning Move
#
# [With Keeper-level Edge, a Winning Move is the precursor to Invincible Audacity.]
craft_recipe(
    output = memory.winning_move,
    power_requirements = attributes(edge=10),
    skills = (
        skill.auroral_contemplations,
        skill.disciplines_of_the_hammer,
        skill.meniscate_reflections,
        skill.ragged_crossroads,
        skill.sharps,
    ),
    solution_must_include = condition(memory=1),
)

# --- edge 15 ---

# Craft: Serpent-Milk
#
# Enrich the ink to a fluid vibrant with Edge-power.
#
# [Sickle & Eclipse with Keeper-level <sprite name=edge>, plus Perinculate, creates Serpent-Milk.]
# ---
# Craft: Serpent-Milk
#
# No Librarian of Hush House has ever died during the preparation of serpent-milk. Thankfully, this was true yesterday and it is still true today.
craft_recipe(
    output = beverage.serpent_milk,
    power_requirements = attributes(edge=15),
    skills = (
        skill.disciplines_of_the_scar,
        skill.meniscate_reflections,
        skill.sharps,
        skill.sickle_and_eclipse,
    ),
    solution_must_include = condition(one_of=(liquid.perinculate,)),
)

# Craft: Invincible Audacity
#
# Extend your understanding into a more potent Edge-lesson.
#
# [Edicts Martial with Keeper-level <sprite name=edge>, plus Winning Move, creates Invincible Audacity.]
# ---
# Craft: Invincible Audacity
#
# The Colonel's lessons, and the Lionsmith's lessons, have been unkindly, and reductively, rendered as 'stab' versus 'thump'.
craft_recipe(
    output = memory.invincible_audacity,
    power_requirements = attributes(edge=15),
    skills = (
        skill.auroral_contemplations,
        skill.disciplines_of_the_hammer,
        skill.edicts_martial,
    ),
    solution_must_include = condition(one_of=(memory.winning_move,)),
)

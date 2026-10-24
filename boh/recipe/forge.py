from ..model import attributes, card_type, condition, craft_recipe
from ..item import flower, liquid, material, skill


# --- forge 5 ---

# Craft: Bitterblack Salts
#
# Something from the boundaries of the jeweller's art: concentrate smouldering essences into a Forge ingredient.
#
# [Anbary & Lapidary with Prentice-level <sprite name=forge> creates Bitterblack Salts. Or for a Scholar-level recipe:  if I add Liquid, but retain Scholar-level Forge, the essences will take longer to cool, and redden into something more potent.]
# ---
# Craft: Bitterblack Salts
#
# Bitterblack Salts have been used as an ingredient in jeweller's polish, but they have many other purposes.
craft_recipe(
    output = material.bitterblack_salts,
    power_requirements = attributes(forge=5),
    skills = (
        skill.anbary_and_lapidary,
        skill.bells_and_brazieries,
        skill.disciplines_of_the_hammer,
        skill.door_and_wall,
        skill.transformations_and_liberations,
    ),
)

# Craft: Westcott's Compounds
#
# The Reflections include alchemical techniques. I can use those to prepare an odd set of compounds with a variety of uses.
#
# [Meniscate Reflections with Prentice-level <sprite name=forge> creates Westcott's Compounds. Or if I add Liquid to Scholar-level Forge, the essences will take longer to cool, and redden into something more potent.]
# ---
# Craft: Westcott's Compounds
#
# Westcott probably didn't invent all these, but he knew how to make a name stick.
craft_recipe(
    output = material.westcotts_compounds,
    power_requirements = attributes(forge=5),
    skills = (
        skill.meniscate_reflections,
        skill.pyroglyphics,
        skill.spices_and_savours,
    ),
)

# --- forge 10 ---

# Craft: Iotic Essence
#
# Equilibrate this liquid into a ruddy essence of Forge-power.
#
# [Meniscate Reflections with Scholar-level <sprite name=forge>, plus Liquid, creates Iotic Essence.]
# ---
# Craft: Iotic Essence
#
# [With Keeper-level Forge, Iotic Essence is the precursor to the Great Ink called Orpiment Exultant; with Keeper-level Lantern, it can become Xanthotic Essence instead.]
craft_recipe(
    output = liquid.iotic_essence,
    power_requirements = attributes(forge=10),
    skills = (
        skill.anbary_and_lapidary,
        skill.meniscate_reflections,
        skill.pyroglyphics,
        skill.spices_and_savours,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Wire (Orichalcum)
#
# Use this metal as a base for the fabled Forge-alloy called orichalcum.
#
# [Bells & Brazieries with Scholar-level <sprite name=forge>, plus Metal, creates Wire (Orichalcum).]
# ---
# Craft: Wire (Orichalcum)
#
# [With Keeper-level Forge, orichalcum can catalyse and contain the Azoth.]
craft_recipe(
    output = material.wire_orichalcum,
    power_requirements = attributes(forge=10),
    skills = (
        skill.bells_and_brazieries,
        skill.disciplines_of_the_hammer,
        skill.door_and_wall,
    ),
    solution_must_include = condition(metal=1),
)

# --- forge 15 ---

# Craft: Azoth
#
# Use orichalcum to catalyse the ferocious Knock-solvent called the azoth.
#
# [Pyroglyphics with Keeper-level <sprite name=forge>, plus Wire (Orichalcum), creates Azoth.]
# ---
# Craft: Azoth
#
# The orichalcum must be incorporated, very carefully, into the vessel, so that the azoth does not escape. Careless alchemists have to move house frequently.
craft_recipe(
    output = liquid.azoth,
    power_requirements = attributes(forge=15),
    skills = (
        skill.bells_and_brazieries,
        skill.disciplines_of_the_hammer,
        skill.door_and_wall,
        skill.meniscate_reflections,
        skill.purifications_and_exaltations,
        skill.pyroglyphics,
    ),
    solution_must_include = condition(one_of=(material.wire_orichalcum, )),
)

# Craft: Azoth
#
# A little-known secret: when prepared with extraordinary care, Honeyscar Jasmine can catalyse the ferocious Knock-solvent called the Azoth.
#
# [Spices & Savours with Keeper-level <sprite name=forge>, plus Honeyscar Jasmine, creates Azoth.]
# ---
# Craft: Azoth
#
# The jasmine-juices must be prepared very carefully as a coating for the vessel, so that the azoth does not escape. Careless alchemists have to move house frequently.
craft_recipe(
    output = liquid.azoth,
    power_requirements = attributes(forge=15),
    skills = (
        skill.spices_and_savours,
    ),
    solution_must_include = condition(one_of=(flower.honeyscar_jasmine, )),
)

# Craft: Iotic Essence
#
# Transform these salts into a ruddy essence of Forge-power.
#
# [Transformations & Liberations with Keeper-level <sprite name=forge>, plus Bitterblack Salts, creates Iotic Essence.]
# ---
# Craft: Iotic Essence
#
# Red as sunset….
craft_recipe(
    output = liquid.iotic_essence,
    power_requirements = attributes(forge=15),
    skills = (
        skill.disciplines_of_the_hammer,
        skill.meniscate_reflections,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(one_of=(material.bitterblack_salts, )), # TODO (recipe merge) ?
)

# Craft: Iotic Essence
#
# Transform this into a ruddy essence of Forge-power.
#
# [Transformations & Liberations with Keeper-level <sprite name=forge>, plus Xanthotic Essence, creates Iotic Essence.]
# ---
# Craft: Iotic Essence
#
# Red as sunset….
craft_recipe(
    output = liquid.iotic_essence,
    power_requirements = attributes(forge=15),
    skills = (
        skill.disciplines_of_the_hammer,
        skill.meniscate_reflections,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(one_of=(liquid.xanthotic_essence, )),
)

# Craft: Orpiment Exultant
#
# Transform the essence into the <i>encaustum terminale</i> Orpiment Exultant.
#
# [Transformations & Liberations with Keeper-level <sprite name=forge>, plus Iotic Essence, creates Orpiment Exultant.]
# ---
# Craft: Orpiment Exultant
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.orpiment_exultant,
    power_requirements = attributes(forge=15),
    skills = (
        skill.anbary_and_lapidary,
        skill.inks_of_power,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(one_of=(liquid.iotic_essence, )),
)

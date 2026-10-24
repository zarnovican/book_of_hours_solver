from ..model import attributes, card_type, condition, craft_recipe
from ..item import beverage, fruit, liquid, memory, remains, skill


# --- nectar 5 ---

# Craft: Thirza's Cordials
#
# Brew an aromatic miscellany of cordials.
#
# [Herbs & Infusions with Prentice-level <sprite name=nectar> creates Thirza's Cordials. Or for a Scholar-level recipe: if I use this with a Beverage, I'll mix a darker, stronger liquor.]
# ---
# Craft: Thirza's Cordials
#
# Taste with care.
craft_recipe(
    output = beverage.thirzas_cordials,
    power_requirements = attributes(nectar=5),
    skills = (
        skill.coil_and_chasm,
        skill.herbs_and_infusions,
        skill.orchids_and_narcotics,
        skill.spices_and_savours,
        skill.stone_stories,
    ),
)

# Craft: Yewgall Ink
#
# Brew a dark and persistent ink.
#
# [Leaves & Thorns with Prentice-level <sprite name=nectar> creates Yewgall Ink. Or for a Scholar-level recipe: if I steep Wood in the right proportions of the mixture, it'll burst into strange fruit.]
# ---
# Craft: Yewgall Ink
#
# Don't spill it.
craft_recipe(
    output = liquid.yewgall_ink,
    power_requirements = attributes(nectar=5),
    skills = (
        skill.inks_of_containment,
        skill.inks_of_power,
        skill.inks_of_revelation,
        skill.insects_and_nectars,
        skill.leaves_and_thorns,
        skill.rites_of_the_roots,
    ),
)

# Craft: Savage Hymn
#
# Recall the hymns of the hill-cults. 
#
# [Drums & Dances with Prentice-level <sprite name=nectar> creates Savage Hymn. Or for a Scholar-level recipe: use an Instrument to resolve it into a buzzing and more ancient song.]
# ---
# Craft: Savage Hymn
#
# Harsh on the tongue.
craft_recipe(
    output = memory.savage_hymn,
    power_requirements = attributes(nectar=5),
    skills = (
        skill.drums_and_dances,
    ),
)

# --- nectar 10 ---

# Craft: Essential Periost
#
# Awaken the green-dark earth-memories bone-borne.
#
# [Stone Stories with Scholar-level <sprite name=nectar>, plus Remains, creates Essential Periost.]
# ---
# Craft: Essential Periost
#
# [With Keeper-level Nectar, and this skill, Essential Periost can be used to brew the Sacrament Malachite.]
craft_recipe(
    output = remains.essential_periost,
    power_requirements = attributes(nectar=10),
    skills = (
        skill.stone_stories,
    ),
    solution_must_include = condition(remains=1),
)

# Craft: Leathy
#
# Brew a Moth-liquor.
#
# [Herbs & Infusions with Scholar-level <sprite name=nectar>, plus Beverage, creates Leathy.]
# ---
# Craft: Leathy
#
# [With Keeper-level Nectar - not Moon - Leathy is a precursor to the Great Ink Marakat.]
craft_recipe(
    output = beverage.leathy,
    power_requirements = attributes(nectar=10),
    skills = (
        skill.herbs_and_infusions,
        skill.insects_and_nectars,
        skill.orchids_and_narcotics,
        skill.rites_of_the_roots,
    ),
    solution_must_include = condition(beverage=1),
)

# Craft: Pyrus Auricalcinus
#
# Rouse strange fruit, ripe with both Forge and Nectar aspect, to burst from the wood.
#
# [Leaves & Thorns with Scholar-level <sprite name=nectar>, plus Wood, creates Pyrus Auricalcinus.]
# ---
# Craft: Pyrus Auricalcinus
#
# [With Keeper-level Nectar, Pyrus Auricalcinus is a precursor to the Sacrament Malachite.]
craft_recipe(
    output = fruit.pyrus_auricalcinus,
    power_requirements = attributes(nectar=10),
    skills = (
        skill.coil_and_chasm,
        skill.leaves_and_thorns,
        skill.spices_and_savours,
    ),
    solution_must_include = condition(wood=1),
)

# Craft: Hive's Lament
#
# A beating in the heart…
#
# [Drums & Dances with Scholar-level <sprite name=nectar>, plus Instrument, creates Hive's Lament.]
# ---
# Craft: Hive's Lament
#
# A buzzing in the skull…
craft_recipe(
    output = memory.hives_lament,
    power_requirements = attributes(nectar=10),
    skills = (
        skill.drums_and_dances,
    ),
    solution_must_include = condition(instrument=1),
)

# --- nectar 15 ---

# Craft: Marakat
#
# Brew the <i>encaustum terminale</i> called Marakat.
#
# [Insects & Nectars with Keeper-level <sprite name=nectar>, plus Leathy, creates Marakat.]
# ---
# Craft: Marakat
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.marakat,
    power_requirements = attributes(nectar=15),
    skills = (
        skill.inks_of_power,
        skill.insects_and_nectars,
        skill.tridesma_hiera,
    ),
    solution_must_include = condition(one_of=(beverage.leathy, )),
)

# Craft: Sacrament Malachite
#
# This pear can be a basis for a Nectar-sacrament of the deep woods.
#
# [Leaves & Thorns with Keeper-level <sprite name=nectar>, plus Pyrus Auricalcinus, creates Sacrament Malachite.]
# ---
# Craft: Sacrament Malachite
#
# In the name of the roots, of the blood, of the buzzing within….
craft_recipe(
    output = beverage.sacrament_malachite,
    power_requirements = attributes(nectar=15),
    skills = (
        skill.coil_and_chasm,
        skill.drums_and_dances,
        skill.herbs_and_infusions,
        skill.leaves_and_thorns,
        skill.rites_of_the_roots,
        skill.spices_and_savours,
    ),
    solution_must_include = condition(one_of=(fruit.pyrus_auricalcinus, )),
)

# Craft: Sacrament Malachite
#
# From these green-dark earth-memories bone-borne, from these sticks of soul and substance, brew the sacrament which the earth might again claim as blood…
#
# [Stone Stories with Keeper-level <sprite name=nectar>, plus Essential Periost, creates Sacrament Malachite.]
# ---
# Craft: Sacrament Malachite
#
# In the name of the roots, of the blood, of the buzzing within….
craft_recipe(
    output = beverage.sacrament_malachite,
    power_requirements = attributes(nectar=15),
    skills = (
        skill.stone_stories,
    ),
    solution_must_include = condition(one_of=(remains.essential_periost, )),
)

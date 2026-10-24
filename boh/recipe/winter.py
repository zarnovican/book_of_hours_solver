from ..item import beverage, liquid, mark, memory, remains, skill, thing
from ..model import attributes, card_type, condition, craft_recipe


# --- winter 5 ---

# Craft: Eigengrau
#
# Distil a kind of possibility.
#
# [Sights & Sensations with Prentice-level <sprite name=winter> creates Eigengrau. Or for a Scholar-level recipe: crush a Flower in, and mix a pale and chilling draught.]
# ---
# Craft: Eigengrau
#
# The surface of the substance is difficult to resolve - almost as if it weren't there at all.
craft_recipe(
    output = beverage.eigengrau,
    power_requirements = attributes(winter=5),
    skills = (
        skill.inks_of_containment,
        skill.quenchings_and_quellings,
        skill.sights_and_sensations,
    ),
)

# Craft: Yewgall Ink
#
# Brew a dark and persistent ink.
#
# [Putrefactions & Calcinations with Prentice-level <sprite name=winter> creates Yewgall Ink. Or for a Scholar-level recipe: if I crush in a Leaf, I'll brew a more potent, and much more dangerous, ink.]
# ---
# Craft: Yewgall Ink
#
# Don't spill it.
craft_recipe(
    output = liquid.yewgall_ink,
    power_requirements = attributes(winter=5),
    skills = (
        skill.putrefactions_and_calcinations,
    ),
)

# Craft: Bittersweet Certainty
#
# Find a chilly insight in the labyrinths of memory.
#
# [Rhyme & Remembrance with Prentice-level <sprite name=winter> creates Bittersweet Certainty. Or for a Scholar-level recipe: let it guide my hand when I dissect Remains, and I can render something darkly leathery, chillingly powerful.]
# ---
# Craft: Bittersweet Certainty
#
# Hold on to it.
craft_recipe(
    output = memory.bittersweet_certainty,
    power_requirements = attributes(winter=5),
    skills = (
        skill.ouranoscopy,
        skill.ragged_crossroads,
        skill.rhyme_and_remembrance,
        skill.snow_stories,
    ),
)

# --- winter 10 ---

# Craft: Essential Periost
#
# Render a Winter-aspected remnant.
#
# [Rhyme & Remembrance with Scholar-level <sprite name=winter>, plus Remains, creates Essential Periost.]
# ---
# Craft: Essential Periost
#
# [With Keeper-Level Winter, this is a precursor to a Year-Tally.]
craft_recipe(
    output = remains.essential_periost,
    power_requirements = attributes(winter=10),
    skills = (
        skill.rhyme_and_remembrance,
        skill.snow_stories,
    ),
    solution_must_include = condition(remains=1),
)

# Craft: Perinculate
#
# Brew a notoriously deadly Ink of Power.
#
# [Putrefactions & Calcinations with Scholar-level <sprite name=winter>, plus Leaf, creates Perinculate.]
# ---
# Craft: Perinculate
#
# [With Keeper-level Edge, Perinculate is the precursor to Serpent-Milk.]
craft_recipe(
    output = liquid.perinculate,
    power_requirements = attributes(winter=10),
    skills = (
        skill.putrefactions_and_calcinations,
    ),
    solution_must_include = condition(leaf=1),
)

# Craft: Solomon's Preparation
#
# Muddle and mix a wintry preparation.
#
# [Inks of Containment with Scholar-level <sprite name=winter>, plus Flower, creates Solomon's Preparation.]
# ---
# Craft: Solomon's Preparation
#
# [With Keeper-level Winter, Solomon's Preparations are a precursor to the Great Ink Nillycant.]
craft_recipe(
    output = beverage.solomons_preparation,
    power_requirements = attributes(winter=10),
    skills = (
        skill.inks_of_containment,
        skill.quenchings_and_quellings,
        skill.ragged_crossroads,
        skill.sights_and_sensations,
    ),
    solution_must_include = condition(flower=1),
)

# --- winter 15 ---

# Craft: Nillycant
#
# Clarify the preparation into the <i>encaustum terminale</i> Nillycant.
#
# [Inks of Containment with Keeper-level <sprite name=winter>, plus Solomon's Preparation, creates Nillycant.]
# ---
# Craft: Nillycant
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.nillycant,
    power_requirements = attributes(winter=15),
    skills = (
        skill.inks_of_containment,
        skill.sights_and_sensations,
    ),
    solution_must_include = condition(one_of=(beverage.solomons_preparation, )),
)

# Craft: Nillycant
#
# Soften the toxin into the <i>encaustum terminale</i> Nillycant.
#
# [Ragged Crossroads with Keeper-level <sprite name=winter>, plus Glassfinger Toxin, creates Nillycant.]
# ---
# Craft: Nillycant
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.nillycant,
    power_requirements = attributes(winter=15),
    skills = (
        skill.ragged_crossroads,
    ),
    solution_must_include = condition(one_of=(liquid.glassfinger_toxin, )),
)

# Craft: Wyrd-Weft
#
# Draw Winter into a web of little fates.
#
# [Weaving & Knotworking with Keeper-level <sprite name=winter>, plus fabric, creates Wyrd-Weft.]
# ---
# Craft: Wyrd-Weft
#
# Every thread a future, and every other thread a past.
craft_recipe(
    output = thing.wyrd_weft,
    power_requirements = attributes(winter=15),
    skills = (
        skill.stitching_and_binding,
        skill.weaving_and_knotworking,
    ),
    solution_must_include = condition(fabric_and_fibre=1),
)

# Craft: Year-Tally
#
# Draw, very carefully, on an ancient privilege of the House to manifest Winter.
#
# [Snow Stories with Keeper-level <sprite name=winter>, plus Essential Periost, creates Year-Tally.]
# ---
# Craft: Year-Tally
#
# Use with care. The Madrugad, for her own reasons, tolerates the house. Let's not test her tolerance.
craft_recipe(
    output = mark.year_tally,
    power_requirements = attributes(winter=15),
    skills = (
        skill.putrefactions_and_calcinations,
        skill.ragged_crossroads,
        skill.rhyme_and_remembrance,
        skill.snow_stories,
    ),
    solution_must_include = condition(one_of=(remains.essential_periost, )),
)

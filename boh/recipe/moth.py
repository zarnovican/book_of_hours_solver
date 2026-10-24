from ..model import attributes, card_type, condition, craft_recipe
from ..item import beast, beverage, liquid, material, memory, skill


# --- moth 5 ---

# Craft: Paint: Moth-Gold
#
# Mix paint of a wistful golden hue.
#
# [Inks of Revelation with Prentice-level <sprite name=moth> creates Paint: Moth-Gold. Or for a Scholar-level recipe: if I add Liquid, I'll brew a silvery moon-ink.]
# ---
# Craft: Paint: Moth-Gold
#
# Neither bright nor dark.
craft_recipe(
    output = liquid.paint_moth_gold,
    power_requirements = attributes(moth=5),
    skills = (
        skill.inks_of_revelation,
    ),
)

# Craft: Tanglebrag
#
# Weave a token to invite the attention of a Moth-name.
#
# [Weaving & Knotworking with Prentice-level <sprite name=moth> creates Tanglebrag. Or for a Scholar-level recipe: if I work with Memory I'll remember a riddle instead.]
# ---
# Craft: Tanglebrag
#
# Set it down softly, or it might roll away, even uphill.
craft_recipe(
    output = material.tanglebrag,
    power_requirements = attributes(moth=5),
    skills = (
        skill.edicts_liminal,
        skill.resurgences_and_emergences,
        skill.rites_of_the_roots,
        skill.weaving_and_knotworking,
    ),
)

# Craft: Westcott's Compounds
#
# An alchemical trick for rendering the ephemeral into volatile compounds - 'the Moth finds the Flame'.
#
# [Solutions & Separations with Prentice-level <sprite name=moth> creates Westcott's Compounds. Or for a Scholar-level recipe:  if I include a Memory and smoke the preparation while it's fresh, I'll gain a riddlesome insight.]
# ---
# Craft: Westcott's Compounds
#
# Westcott probably didn't invent all these, but he knew how to make a name stick.
craft_recipe(
    output = material.westcotts_compounds,
    power_requirements = attributes(moth=5),
    skills = (
        skill.sacra_limiae,
        skill.solutions_and_separations,
    ),
)

# --- moth 10 ---

# Craft: Asimel
#
# Brew a silvery Moon-ink.
#
# [Inks of Revelation with Scholar-level <sprite name=moth>, plus Liquid, creates Asimel.]
# ---
# Craft: Asimel
#
# [With Keeper-level Moon - not Moth - asimel can deepen to black sapphire.]
craft_recipe(
    output = liquid.asimel,
    power_requirements = attributes(moth=10),
    skills = (
        skill.inks_of_revelation,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Chimeric Larva
#
# Hatch an eyeless larva pulsing with Moth-potential.
#
# [Resurgences & Emergences with Scholar-level <sprite name=moth>, plus Egg, creates Chimeric Larva.]
# ---
# Craft: Chimeric Larva
#
# [With Keeper-level Moth, perhaps I could coax this to develop further - as long as it's well-fed.]
craft_recipe(
    output = beast.chimeric_larva,
    power_requirements = attributes(moth=10),
    skills = (
        skill.resurgences_and_emergences,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Nameday Riddle
#
# Conceive a Mothly riddle.
#
# [Weaving & Knotworking with Scholar-level <sprite name=moth>, plus Memory, creates Nameday Riddle.]
# ---
# Craft: Nameday Riddle
#
# Is this a way to the Wood? But perhaps the Wood is not a suitable place for a Librarian.
craft_recipe(
    output = memory.nameday_riddle,
    power_requirements = attributes(moth=10),
    skills = (
        skill.edicts_liminal,
        skill.rites_of_the_roots,
        skill.sacra_limiae,
        skill.solutions_and_separations,
        skill.weaving_and_knotworking,
    ),
    solution_must_include = condition(memory=1),
)

# --- moth 15 ---

# Craft: Skinshuck Mead
#
# Brew a Moth-liquor with the honey.
#
# [Transformations & Liberations with Keeper-level <sprite name=moth>, plus Cuckoo-Honey, creates Skinshuck Mead.]
# ---
# Craft: Skinshuck Mead
#
# ''One taste to sleep, two to wake, for what are eyelids but the skin of the eyes?'.
craft_recipe(
    output = beverage.skinshuck_mead,
    power_requirements = attributes(moth=15),
    skills = (
        skill.edicts_liminal,
        skill.rites_of_the_roots,
        skill.sacra_limiae,
        skill.solutions_and_separations,
        skill.resurgences_and_emergences,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(one_of=(liquid.cuckoo_honey, )),
)

# Craft: Skinshuck Mead
#
# Brew a Moth-liquor with the honey.
#
# [Solutions & Separations with Keeper-level <sprite name=moth>, plus Honey, creates Skinshuck Mead.]
# ---
# Craft: Skinshuck Mead
#
# ''One taste to sleep, two to wake, for what are eyelids but the skin of the eyes?'.
craft_recipe(
    output = beverage.skinshuck_mead,
    power_requirements = attributes(moth=15),
    skills = (
        skill.edicts_liminal,
        skill.rites_of_the_roots,
        skill.sacra_limiae,
        skill.solutions_and_separations,
    ),
    solution_must_include = condition(one_of=(liquid.honey, )),
)

# Craft: Perilous Imago
#
# Coax the larva to develop into a greater Moth-beast.
#
# [Transformations & Liberations with Keeper-level <sprite name=moth>, plus Chimeric Larva, creates Perilous Imago.]
# ---
# Craft: Perilous Imago
#
# One wet wing, then the other, and then it shakes them dry; and from that point, it will bear watching always.
craft_recipe(
    output = beast.perilous_imago,
    power_requirements = attributes(moth=15),
    skills = (
        skill.resurgences_and_emergences,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(one_of=(beast.chimeric_larva, )),
)

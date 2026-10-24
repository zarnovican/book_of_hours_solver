from ..model import attributes, card_type, condition, craft_recipe
from ..item import beverage, device, liquid, material, memory, skill


# --- lantern 5 ---

# Craft: Dearday Lens
#
# Forge an optical device. 
#
# [Pyroglyphics with Prentice-level <sprite name=lantern> creates Dearday Lens. Or for a Scholar-level recipe: if I add Liquid, I can distil a more potent Lantern-essence.]
# ---
# Craft: Dearday Lens
#
# The Lens is asymmetrical - fragile - unstable. That's what gives it power.
craft_recipe(
    output = device.dearday_lens,
    power_requirements = attributes(lantern=5),
    skills = (
        skill.disciplines_of_the_scar,
        skill.glassblowing_and_vesselcrafting,
        skill.glaziery_and_lightsmithing,
        skill.pyroglyphics,
    ),
)

# Craft: Eigengrau
#
# Distil a kind of possibility.
#
# [Auroral Contemplations with Prentice-level <sprite name=lantern> creates Eigengrau. Or for a Scholar-level recipe: mix in another Liquid to produce an alchemical essence.]
# ---
# Craft: Eigengrau
#
# The surface of the substance is difficult to resolve - almost as if it weren't there at all.
craft_recipe(
    output = beverage.eigengrau,
    power_requirements = attributes(lantern=5),
    skills = (
        skill.auroral_contemplations,
    ),
)

# Craft: Refulgin
#
# Mix a pigment of blinding white, one that the Church used for their rites before the Dissolution.
#
# [Inks of Revelation with Prentice-level <sprite name=lantern> creates Refulgin. Or for a Scholar-level recipe: if I add Glass, I can resolve it into a more potent Lantern-liquid, a precursor of the ink Ashartine.]
# ---
# Craft: Refulgin
#
# Glow, little colour.
craft_recipe(
    output = material.refulgin,
    power_requirements = attributes(lantern=5),
    skills = (
        skill.inks_of_revelation,
        skill.purifications_and_exaltations,
        skill.sacra_solis_invicti,
        skill.transformations_and_liberations,
    ),
)

# Craft: Tanglebrag
#
# Align shadows to invite the attention of a Moth-name.
#
# [Watchman's Paradoxes with Prentice-level <sprite name=lantern> creates Tanglebrag. Or for a Scholar-level recipe: align the shadows through Glass, and gather a Lantern-liquid.]
# ---
# Craft: Tanglebrag
#
# Set it down softly, or it might roll away, even uphill.
craft_recipe(
    output = material.tanglebrag,
    power_requirements = attributes(lantern=5),
    skills = (
        skill.watchmans_paradoxes,
    ),
)

# --- lantern 10 ---

# Craft: Ichor Vitreous
#
# Distil a pale and watchful Lantern-fluid.
#
# [Inks of Revelation with Scholar-level <sprite name=lantern>, plus Glass, creates Ichor Vitreous.]
# ---
# Craft: Ichor Vitreous
#
# [With Keeper-level Lantern, Ichor Vitreous is the precursor of the ink ashartine.]
craft_recipe(
    output = liquid.ichor_vitreous,
    power_requirements = attributes(lantern=10),
    skills = (
        skill.glassblowing_and_vesselcrafting,
        skill.glaziery_and_lightsmithing,
        skill.inks_of_revelation,
        skill.sacra_solis_invicti,
        skill.watchmans_paradoxes,
    ),
    solution_must_include = condition(glass=1),
)

# Craft: Xanthotic Essence
#
# Candesce this liquid to a golden essence of Lantern-power.
#
# [Pyroglyphics with Scholar-level <sprite name=lantern>, plus Liquid, creates Xanthotic Essence.]
# ---
# Craft: Xanthotic Essence
#
# [With Keeper-level Lantern, Xanthotic Essence is the precursor of the Great Ink Uzult.]
craft_recipe(
    output = liquid.xanthotic_essence,
    power_requirements = attributes(lantern=10),
    skills = (
        skill.auroral_contemplations,
        skill.purifications_and_exaltations,
        skill.pyroglyphics,
        skill.transformations_and_liberations,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Old Moment
#
# Recall something lost, something Scale-aspected…
#
# [Disciplines of the Scar with Scholar-level <sprite name=lantern>, plus Memory, creates Old Moment.]
# ---
# Craft: Old Moment
#
# [With Keeper-level Scale - not Lantern - an Old Moment can lead to an Earthquake Name.]
craft_recipe(
    output = memory.old_moment,
    power_requirements = attributes(lantern=10),
    skills = (
        skill.disciplines_of_the_scar,
    ),
    solution_must_include = condition(memory=1),
)

# --- lantern 15 ---

# Craft: Ashartine
#
# Brew the bright ink ashartine from the ichor.
#
# [Glaziery & Lightsmithing with Keeper-level <sprite name=lantern>, plus Ichor Vitreous, creates Ashartine.]
# ---
# Craft: Ashartine
#
# While the vapours of ashartine's making hang in the air, it is very difficult to speak a lie aloud….
craft_recipe(
    output = liquid.ashartine,
    power_requirements = attributes(lantern=15),
    skills = (
        skill.glassblowing_and_vesselcrafting,
        skill.glaziery_and_lightsmithing,
        skill.pyroglyphics,
        skill.watchmans_paradoxes,
    ),
    solution_must_include = condition(one_of=(liquid.ichor_vitreous, )),
)

# Craft: Porphyrine
#
# Deepen the ichor into the <i>encaustum terminale</i> Porphyrine.
#
# [Auroral Contemplations with Keeper-level <sprite name=lantern>, plus Ichor Auroral, creates Porphyrine.]
# ---
# Craft: Porphyrine
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.porphyrine,
    power_requirements = attributes(lantern=15),
    skills = (
        skill.auroral_contemplations,
    ),
    solution_must_include = condition(one_of=(liquid.ichor_auroral, )),
)

# Craft: Uzult
#
# Brighten the essence into the <i>encaustum terminale</i> Uzult.
#
# [Inks of Revelation with Keeper-level <sprite name=lantern>, plus Xanthotic Essence, creates Uzult.]
# ---
# Craft: Uzult
#
# [This is an <i>encaustum terminale</i>: one of the Great Inks. Use it with your journal to record a History and fulfil your reason for coming to Hush House… if you so choose.].
craft_recipe(
    output = liquid.uzult,
    power_requirements = attributes(lantern=15),
    skills = (
        skill.anbary_and_lapidary,
        skill.glaziery_and_lightsmithing,
        skill.inks_of_revelation,
        skill.sacra_solis_invicti,
        skill.watchmans_paradoxes,
    ),
    solution_must_include = condition(one_of=(liquid.xanthotic_essence, )),
)

# TODO verify with wiki
# Craft: Xanthotic Essence
#
# Exalt this liquid into a golden essence of Lantern-power.
#
# [Purifications & Exaltations with Scholar-level <sprite name=lantern>, plus Liquid, creates Xanthotic Essence.]
# ---
# Craft: Xanthotic Essence
#
# [With Keeper-level Lantern, Xanthotic Essence is the precursor of the Great Ink Uzult.]
craft_recipe(
    output = liquid.xanthotic_essence,
    power_requirements = attributes(lantern=15),
    skills = (
        skill.purifications_and_exaltations,
    ),
    solution_must_include = condition(one_of=(material.bitterblack_salts, liquid.xanthotic_essence)),
)

# Craft: Earthquake Name
#
# Discern a potency of Scale.
#
# [Disciplines of the Scar with Keeper-level <sprite name=lantern>, plus Old Moment, creates Earthquake Name.]
# ---
# Craft: Earthquake Name
#
# Speak half a syllable, and feel the beast stir half a coil....
craft_recipe(
    output = memory.earthquake_name,
    power_requirements = attributes(lantern=15),
    skills = (
        skill.disciplines_of_the_scar,
    ),
    solution_must_include = condition(one_of=(memory.old_moment, )),
)

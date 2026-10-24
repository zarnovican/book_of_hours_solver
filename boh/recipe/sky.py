from ..model import attributes, card_type, condition, craft_recipe
from ..item import beast, device, liquid, material, mark, memory, remains, skill, tool


# --- sky 5 ---

# Craft: Awakened Feather
#
# Spark a life-current in an abandoned feather.
#
# [Anbary & Lapidary with Prentice-level <sprite name=sky> creates Awakened Feather. Or for a Scholar-level recipe: spark those energies in a Liquid, curdling it into an alchemical essence.]
# ---
# Craft: Awakened Feather
#
# A smooth sweep of quill alert with life.
craft_recipe(
    output = material.awakened_feather,
    power_requirements = attributes(sky=5),
    skills = (
        skill.anbary_and_lapidary,
        skill.furs_and_feathers,
        skill.lockworks_and_clockworks,
        skill.sacra_limiae,
        skill.sights_and_sensations,
        skill.stitching_and_binding,
    ),
)

# Craft: Dearday Lens
#
# Craft an optical device.
#
# [Glassblowing & Vesselcrafting with Prentice-level <sprite name=sky> creates Dearday Lens. Or for a Scholar-level recipe: if I add Glass, I can distil a potent Lantern-liquid.]
# ---
# Craft: Dearday Lens
#
# The Lens is asymmetrical - fragile - unstable. That's what gives it power.
craft_recipe(
    output = device.dearday_lens,
    power_requirements = attributes(sky=5),
    skills = (
        skill.glassblowing_and_vesselcrafting,
        skill.glaziery_and_lightsmithing,
    ),
)

# Craft: Stargall Ink
#
# Brew a bright and persistent ink.
#
# [Inks of Revelation with Prentice-level <sprite name=sky> creates Stargall Ink.]
# ---
# Craft: Stargall Ink
#
# Don't spill it.
craft_recipe(
    output = liquid.stargall_ink,
    power_requirements = attributes(sky=5),
    skills = (
        skill.inks_of_containment,
        skill.inks_of_power,
        skill.inks_of_revelation,
    ),
)

# Craft: Confounding Parable
#
# Muse on tradition, recall contradiction.
#
# [Applebright Euphonies with Prentice-level <sprite name=sky> creates Confounding Parable. Or for a Scholar-level recipe: if I use an Instrument, I can set this contradiction to music.]
# ---
# Craft: Confounding Parable
#
# It fits fairly tidily in the mind, as long as you turn it sideways.
craft_recipe(
    output = memory.confounding_parable,
    power_requirements = attributes(sky=5),
    skills = (
        skill.applebright_euphonies,
        skill.sacra_solis_invicti,
    ),
)

# Craft: Torgue's Cleansing
#
# Purge myself of earthly influences, accruing some personal Edge through the savagery of the process.
#
# [Purifications & Exaltations with Prentice-level <sprite name=sky> creates Torgue's Cleansing. Or for a Scholar-level recipe: if I use an Instrument, I can use the experience as an inspiration for Sky-focused music.]
# ---
# Craft: Torgue's Cleansing
#
# The Cleansing has left my eyes dazzled, my skin burning. The Corrivality manifests even in the operations of the Sun.
craft_recipe(
    output = memory.torgues_cleansing,
    power_requirements = attributes(sky=5),
    skills = (
        skill.purifications_and_exaltations,
    ),
)

# Craft: Wistful Air
#
# Recall a sweet and sorrowful song.
#
# [Sky Stories with Prentice-level <sprite name=sky> creates Wistful Air. Or for a Scholar-level recipe: use an Instrument to raise it to a greater music.]
# ---
# Craft: Wistful Air
#
# Let it rise in head and heart.
craft_recipe(
    output = memory.wistful_air,
    power_requirements = attributes(sky=5),
    skills = (
        skill.bells_and_brazieries,
        skill.ouranoscopy,
        skill.sky_stories,
        skill.strings_and_songs,
        skill.watchmans_paradoxes,
    ),
)

# --- sky 10 ---

# Craft: Gervinite
#
# Resolve a Knock-alloy.
#
# [Glaziery & Lightsmithing with Scholar-level <sprite name=sky>, plus Metal, creates Gervinite.]
# ---
# Craft: Gervinite
#
# [With Keeper-level Knock, gervinite is the essential ingredient of a Chronsichord.]
craft_recipe(
    output = material.gervinite,
    power_requirements = attributes(sky=10),
    skills = (
        skill.glaziery_and_lightsmithing,
    ),
    solution_must_include = condition(metal=1),
)

# Craft: Ichor Auroral
#
# Condense light to a Rose-fluid.
#
# [Sights & Sensations with Scholar-level <sprite name=sky>, plus Light, creates Ichor Auroral.]
# ---
# Craft: Ichor Auroral
#
# [With Keeper-level  Rose - not Sky - the Ichor Auroral is a precursor to the Great Ink Porphyrine.]
craft_recipe(
    output = liquid.ichor_auroral,
    power_requirements = attributes(sky=10),
    skills = (
        skill.sights_and_sensations,
        skill.watchmans_paradoxes,
    ),
    solution_must_include = condition(light=1),
)

# Craft: Ichor Vitreous
#
# Distil a pale and watchful Lantern-fluid.
#
# [Glassblowing & Vesselcrafting with Scholar-level <sprite name=sky>, plus Glass, creates Ichor Vitreous.]
# ---
# Craft: Ichor Vitreous
#
# [With Keeper-level Sky, Ichor Vitreous is the precursor of the ink ashartine.]
craft_recipe(
    output = liquid.ichor_vitreous,
    power_requirements = attributes(sky=10),
    skills = (
        skill.glassblowing_and_vesselcrafting,
    ),
    solution_must_include = condition(glass=1),
)

# Craft: Mazarine Fife
#
# Carve a Sky-aspected instrument.
#
# [Sacra Solis Invicti with Scholar-level <sprite name=sky>, plus Wood, creates Mazarine Fife.]
# ---
# Craft: Mazarine Fife
#
# [With Keeper-level Sky, a Mazarine Fife is an essential tool to conjure a Wind-in-Waiting.]
craft_recipe(
    output = tool.mazarine_fife,
    power_requirements = attributes(sky=10),
    skills = (
        skill.ouranoscopy,
        skill.sacra_limiae,
        skill.sacra_solis_invicti,
    ),
    solution_must_include = condition(wood=1),
)

# Craft: Wire (Orichalcum)
#
# Use this metal as a base for the fabled Forge-alloy called orichalcum.
#
# [Lockworks & Clockworks with Scholar-level <sprite name=sky>, plus Metal, creates Wire (Orichalcum).]
# ---
# Craft: Wire (Orichalcum)
#
# [With Keeper-level Forge, orichalcum can catalyse and contain the Azoth.]
craft_recipe(
    output = material.wire_orichalcum,
    power_requirements = attributes(sky=10),
    skills = (
        skill.lockworks_and_clockworks,
    ),
    solution_must_include = condition(metal=1),
)

# Craft: Xanthotic Essence
#
# Energise this liquid into a golden essence of Lantern-power.
#
# [Anbary & Lapidary with Scholar-level <sprite name=sky>, plus Liquid, creates Xanthotic Essence.]
# ---
# Craft: Xanthotic Essence
#
# [With Keeper-level Lantern - not Sky -  Xanthotic Essence is the precursor of the Great Ink Uzult.]
craft_recipe(
    output = liquid.xanthotic_essence,
    power_requirements = attributes(sky=10),
    skills = (
        skill.anbary_and_lapidary,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Living Relic
#
# Hatch a Scale-relic from the egg.
#
# [Stitching & Binding with Scholar-level <sprite name=sky>, plus Egg, creates Living Relic.]
# ---
# Craft: Living Relic
#
# [With Keeper-level Scale - not Sky - a Living Relic can be induced to help with the production of Houndsgall.]
craft_recipe(
    output = beast.living_relic,
    power_requirements = attributes(sky=10),
    skills = (
        skill.stitching_and_binding,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Ascendant Harmony
#
# Conjure bright Sky-music.
#
# [Applebright Euphonies with Scholar-level <sprite name=sky>, plus Instrument, creates Ascendant Harmony.]
# ---
# Craft: Ascendant Harmony
#
# [With Keeper-level Sky, an Ascendant Harmony might conjure a Didumos.]
craft_recipe(
    output = memory.ascendant_harmony,
    power_requirements = attributes(sky=10),
    skills = (
        skill.applebright_euphonies,
        skill.bells_and_brazieries,
        skill.furs_and_feathers,
        skill.purifications_and_exaltations,
        skill.sky_stories,
        skill.strings_and_songs,
    ),
    solution_must_include = condition(instrument=1),
)

# --- sky 15 ---

# Craft: Ashartine
#
# Brew the bright ink ashartine from the ichor.
#
# [Anbary & Lapidary with Keeper-level <sprite name=sky>, plus Ichor Vitreous, creates Ashartine.]
# ---
# Craft: Ashartine
#
# While the vapours of ashartine's making hang in the air, it is very difficult to speak a lie aloud….
craft_recipe(
    output = liquid.ashartine,
    power_requirements = attributes(sky=15),
    skills = (
        skill.anbary_and_lapidary,
        skill.glassblowing_and_vesselcrafting,
    ),
    solution_must_include = condition(one_of=(liquid.ichor_vitreous, )),
)

# Craft: Chronsichord
#
# Use a little-known technique to craft a Knock-device from silver.
#
# [Lockworks & Clockworks with Keeper-level <sprite name=sky>, plus Wire (Silver), creates Chronsichord.]
# ---
# Craft: Chronsichord
#
# When a chronsichord is completed, it is fully wound, for the first and only time.
craft_recipe(
    output = device.chronsichord,
    power_requirements = attributes(sky=15),
    skills = (
        skill.lockworks_and_clockworks,
    ),
    solution_must_include = condition(one_of=(material.wire_silver, )),
)

# Craft: Year-Tally
#
# Craft a remedy against age from the celestial influence-trace that striate these remnants.
#
# [Ouranoscopy with Keeper-level <sprite name=sky>, plus Essential Periost, creates Year-Tally.]
# ---
# Craft: Year-Tally
#
# Use with care. The Madrugad, for her own reasons, tolerates the house. Let's not test her tolerance.
craft_recipe(
    output = mark.year_tally,
    power_requirements = attributes(sky=15),
    skills = (
        skill.ouranoscopy,
    ),
    solution_must_include = condition(one_of=(remains.essential_periost, )),
)

# Craft: Didumos
#
# Evoke a chilly Sky-influence.
#
# [Ouranoscopy with Keeper-level <sprite name=sky>, plus Ascendant Harmony, creates Didumos.]
# ---
# Craft: Didumos
#
# The dream of a star is not apparent to the human eye; but its presence, once felt, could not be mistaken for anything else.
craft_recipe(
    output = memory.didumos,
    power_requirements = attributes(sky=15),
    skills = (
        skill.applebright_euphonies,
        skill.bells_and_brazieries,
        skill.ouranoscopy,
        skill.sacra_limiae,
        skill.sights_and_sensations,
    ),
    solution_must_include = condition(one_of=(memory.ascendant_harmony, )),
)

# Craft: Wind-in-Waiting
#
# Secure a wind's promise from the Sky.
#
# [Strings & Songs with Keeper-level <sprite name=sky>, plus Mazarine Fife, creates Wind-in-Waiting.]
# ---
# Craft: Wind-in-Waiting
#
# One last pipe-shrill, and the wind is still.
craft_recipe(
    output = memory.wind_in_waiting,
    power_requirements = attributes(sky=15),
    skills = (
        skill.furs_and_feathers,
        skill.sacra_solis_invicti,
        skill.sky_stories,
        skill.strings_and_songs,
    ),
    solution_must_include = condition(one_of=(tool.mazarine_fife, )),
)

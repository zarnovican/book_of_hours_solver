from ..model import attributes, card_type, condition, craft_recipe
from ..item import beast, beverage, fruit, liquid, mark, memory, remains, skill


# --- moon 5 ---

# Craft: Catwink
#
# Brew an ink that will rouse regret in rats.
#
# [Sand Stories with Prentice-level <sprite name=moon> creates Catwink. Or for a Scholar-level recipe: if I add an Egg to the soak, I'll hatch something mischievous and silvery.]
# ---
# Craft: Catwink
#
# Dark and pungent.
craft_recipe(
    output = liquid.catwink,
    power_requirements = attributes(moon=5),
    skills = (
        skill.edicts_inviolable,
        skill.inks_of_containment,
        skill.putrefactions_and_calcinations,
        skill.sand_stories,
        skill.sickle_and_eclipse,
    ),
)

# Craft: Eigengrau
#
# Distil a kind of possibility.
#
# [Pearl & Tide with Prentice-level <sprite name=moon> creates Eigengrau. Or for a Scholar-level recipe: add Liquid to strengthen it into a silvery Ink of Revelation.]
# ---
# Craft: Eigengrau
#
# The surface of the substance is difficult to resolve - almost as if it weren't there at all.
craft_recipe(
    output = beverage.eigengrau,
    power_requirements = attributes(moon=5),
    skills = (
        skill.maggephene_mysteries,
        skill.pearl_and_tide,
    ),
)

# Craft: Midnight Mark
#
# Concentrate nocturnal resonances with a careful sigil. 
#
# [Desires & Dissolutions with Prentice-level <sprite name=moon> creates Midnight Mark. Or for a Scholar-level recipe: if I trace the mark on Wood, it'll burst into strange fruit.]
# ---
# Craft: Midnight Mark
#
# The Mark shouldn't be exposed to sunlight, but that's mostly because it looks surprisingly ugly in sunlight.
craft_recipe(
    output = mark.midnight_mark,
    power_requirements = attributes(moon=5),
    skills = (
        skill.desires_and_dissolutions,
        skill.insects_and_nectars,
        skill.rhyme_and_remembrance,
        skill.serpents_and_venoms,
        skill.sharps,
        skill.snow_stories,
        skill.wolf_stories,
    ),
)

# Craft: Salt-Sign
#
# Use salt to trace a sigil of wave-song and night-travel.
#
# [Sea Stories with Prentice-level <sprite name=moon> creates Salt-Sign. Or for a Scholar-level recipe: if I hallow a Liquid with this sign, it will clarify into an Ink of Revelation.]
# ---
# Craft: Salt-Sign
#
# Elegant as a wave.
craft_recipe(
    output = mark.salt_sign,
    power_requirements = attributes(moon=5),
    skills = (
        skill.sea_stories,
        skill.hill_and_hollow,
    ),
)

# Craft: Bittersweet Certainty
#
# Find a chilly insight in moonlight.
#
# [Ouranoscopy with Prentice-level <sprite name=moon> creates Bittersweet Certainty. Or for a Scholar-level recipe: add a Lens and focus that moonlight into a silvery Ink of Revelation.]
# ---
# Craft: Bittersweet Certainty
#
# Hold on to it.
craft_recipe(
    output = memory.bittersweet_certainty,
    power_requirements = attributes(moon=5),
    skills = (
        skill.ouranoscopy,
    ),
)

# Craft: Confounding Parable
#
# Employ the Sisterhood's invocations to bring a subtle memory to mind.
#
# [Tridesma Hiera with Prentice-level <sprite name=moon> creates Confounding Parable. Or for a Scholar-level recipe: if I pronounce these invocations over an Egg, it'll hatch into something silvery and mischievous.]
# ---
# Craft: Confounding Parable
#
# It fits fairly tidily in the mind, as long as you turn it sideways.
craft_recipe(
    output = memory.confounding_parable,
    power_requirements = attributes(moon=5),
    skills = (
        skill.tridesma_hiera,
    ),
)

# Craft: Old Wound
#
# Explore an old wound to awaken the violent resonances within.
#
# [Edicts Martial with Prentice-level <sprite name=moon> creates Old Wound. Or for a Scholar-level recipe: add a Memory and find an even bitterer dream.]
# ---
# Craft: Old Wound
#
# Move gingerly while the pain lasts.
craft_recipe(
    output = memory.old_wound,
    power_requirements = attributes(moon=5),
    skills = (
        skill.edicts_martial,
    ),
)

# --- moon 10 ---

# Craft: Asimel
#
# Brew a silvery Moon-ink.
#
# [Putrefactions & Calcinations with Scholar-level <sprite name=moon>, plus Liquid, creates Asimel.]
# ---
# Craft: Asimel
#
# [With Keeper-level Moon, asimel can deepen to black sapphire.]
craft_recipe(
    output = liquid.asimel,
    power_requirements = attributes(moon=10),
    skills = (
        skill.pearl_and_tide,
        skill.putrefactions_and_calcinations,
        skill.sea_stories,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Asimel
#
# Focus the light of the heavens to enliven a silvery Moon-ink.
#
# [Ouranoscopy with Scholar-level <sprite name=moon>, plus Lens, creates Asimel.]
# ---
# Craft: Asimel
#
# [With Keeper-level Moon, asimel sigils can evoke a celestial influence.]
craft_recipe(
    output = liquid.asimel,
    power_requirements = attributes(moon=10),
    skills = (
        skill.ouranoscopy,
    ),
    solution_must_include = condition(lens=1),
)

# Craft: Essential Periost
#
# Render a Winter-aspected remnant.
#
# [Sickle & Eclipse with Scholar-level <sprite name=moon>, plus Remains, creates Essential Periost.]
# ---
# Craft: Essential Periost
#
# [With Keeper-Level Winter - not Moon -  this is a precursor to a Year-Tally.]
craft_recipe(
    output = remains.essential_periost,
    power_requirements = attributes(moon=10),
    skills = (
        skill.sharps,
        skill.sickle_and_eclipse,
        skill.wolf_stories,
    ),
    solution_must_include = condition(remains=1),
)

# Craft: Leathy
#
# Brew a Moth-liquor.
#
# [Inks of Containment with Scholar-level <sprite name=moon>, plus Beverage, creates Leathy.]
# ---
# Craft: Leathy
#
# [With Keeper-level Nectar - not Moon - Leathy is a precursor to the Great Ink Marakat.]
craft_recipe(
    output = beverage.leathy,
    power_requirements = attributes(moon=10),
    skills = (
        skill.inks_of_containment,
   ),
    solution_must_include = condition(beverage=1),
)

# Craft: Pyrus Auricalcinus
#
# Rouse strange fruit, ripe with both Forge and Nectar aspect, to burst from the wood.
#
# [Desires & Dissolutions with Scholar-level <sprite name=moon>, plus Wood, creates Pyrus Auricalcinus.]
# ---
# Craft: Pyrus Auricalcinus
#
# [With Keeper-level Nectar - not Moon - Pyrus Auricalcinus is a precursor to the Sacrament Malachite.]
craft_recipe(
    output = fruit.pyrus_auricalcinus,
    power_requirements = attributes(moon=10),
    skills = (
        skill.desires_and_dissolutions,
    ),
    solution_must_include = condition(wood=1),
)

# Craft: Solomon's Preparation
#
# Muddle and mix a wintry preparation.
#
# [Edicts Inviolable with Scholar-level <sprite name=moon>, plus Flower, creates Solomon's Preparation.]
# ---
# Craft: Solomon's Preparation
#
# [With Keeper-level Winter - not Moon - Solomon's Preparations are a precursor to the Great Ink Nillycant.]
craft_recipe(
    output = beverage.solomons_preparation,
    power_requirements = attributes(moon=10),
    skills = (
        skill.edicts_inviolable,
        skill.maggephene_mysteries,
    ),
    solution_must_include = condition(flower=1),
)

# Craft: Chimeric Larva
#
# Hatch an eyeless larva pulsing with Moth-potential.
#
# [Hill & Hollow with Scholar-level <sprite name=moon>, plus Egg, creates Chimeric Larva.]
# ---
# Craft: Chimeric Larva
#
# [With Keeper-level Moth - not Moon - and a more suitable skill, perhaps I could coax this to develop further - as long as it's well-fed.]
craft_recipe(
    output = beast.chimeric_larva,
    power_requirements = attributes(moon=10),
    skills = (
        skill.hill_and_hollow,
        skill.insects_and_nectars,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Stymphling
#
# Hatch a mischievous Moon-thing from the egg.
#
# [Serpents & Venoms with Scholar-level <sprite name=moon>, plus Egg, creates Stymphling.]
# ---
# Craft: Stymphling
#
# [With Keeper-level Moon, stymphlings can produce Wormwood Dreams.]
craft_recipe(
    output = beast.stymphling,
    power_requirements = attributes(moon=10),
    skills = (
        skill.rhyme_and_remembrance,
        skill.sand_stories,
        skill.serpents_and_venoms,
        skill.snow_stories,
        skill.tridesma_hiera,
    ),
    solution_must_include = condition(egg=1),
)

# Craft: Wormwood Dream
#
# Recall a forgotten crime of Moon and Winter.
#
# [Edicts Martial with Scholar-level <sprite name=moon>, plus Memory, creates Wormwood Dream.]
# ---
# Craft: Wormwood Dream
#
# Let's hope it's equally possible to forget this again.
craft_recipe(
    output = memory.wormwood_dream,
    power_requirements = attributes(moon=10),
    skills = (
        skill.edicts_martial,
    ),
    solution_must_include = condition(memory=1),
)

# --- moon 15 ---

# Craft: Black Sapphire Wash
#
# Darken the asimel into a potent Moon-pigment.
#
# [Putrefactions & Calcinations with Keeper-level <sprite name=moon>, plus Asimel, creates Black Sapphire Wash.]
# ---
# Craft: Black Sapphire Wash
#
# Whence came the light in the House of the Moon? We still don't know; but perhaps this colour is its darkness.
craft_recipe(
    output = liquid.black_sapphire_wash,
    power_requirements = attributes(moon=15),
    skills = (
        skill.desires_and_dissolutions,
        skill.pearl_and_tide,
        skill.putrefactions_and_calcinations,
        skill.sea_stories,
        skill.tridesma_hiera,
    ),
    solution_must_include = condition(one_of=(liquid.asimel, )),
)

# Craft: Sacrament Ascite
#
# Induce a change in the toxin, to make it more Knock-potent but safer.
#
# [Serpents & Venoms with Keeper-level <sprite name=moon>, plus Glassfinger Toxin, creates Sacrament Ascite.]
# ---
# Craft: Sacrament Ascite
#
# In the name of the two blades that are one, of the threshold which has two sides….
craft_recipe(
    output = beverage.sacrament_ascite,
    power_requirements = attributes(moon=15),
    skills = (
        skill.serpents_and_venoms,
    ),
    solution_must_include = condition(one_of=(liquid.glassfinger_toxin, )),
)

# Craft: Skinshuck Mead
#
# Brew a Moth-liquor with the honey.
#
# [Insects & Nectars with Keeper-level <sprite name=moon>, plus Cuckoo-Honey, creates Skinshuck Mead.]
# ---
# Craft: Skinshuck Mead
#
# ''One taste to sleep, two to wake, for what are eyelids but the skin of the eyes?'.
craft_recipe(
    output = beverage.skinshuck_mead,
    power_requirements = attributes(moon=15),
    skills = (
        skill.insects_and_nectars,
    ),
    solution_must_include = condition(one_of=(liquid.cuckoo_honey, )),
)

# Craft: Perilous Imago
#
# Beneath the auspices of dusk, coax the larva to develop into a greater Moth-beast.
#
# [Insects & Nectars with Keeper-level <sprite name=moon>, plus Chimeric Larva, creates Perilous Imago.]
# ---
# Craft: Perilous Imago
#
# One wet wing, then the other, and then it shakes them dry; and from that point, it will bear watching always.
craft_recipe(
    output = beast.perilous_imago,
    power_requirements = attributes(moon=15),
    skills = (
        skill.insects_and_nectars,
    ),
    solution_must_include = condition(one_of=(beast.chimeric_larva, )),
)

# Craft: Didumos
#
# Draw the moon-ink sigils that will bring a star's chilly dream to earth.
#
# [Ouranoscopy with Keeper-level <sprite name=moon>, plus Asimel, creates Didumos.]
# ---
# Craft: Didumos
#
# The dream of a star is not apparent to the human eye; but its presence, once felt, could not be mistaken for anything else.
craft_recipe(
    output = memory.didumos,
    power_requirements = attributes(moon=15),
    skills = (
        skill.ouranoscopy,
    ),
    solution_must_include = condition(one_of=(liquid.asimel,)),
)

# Craft: Forbidden Epic
#
# Elaborate the parable into a potent Edge-epic.
#
# [Edicts Martial with Keeper-level <sprite name=moon>, plus Confounding Parable, creates Forbidden Epic.]
# ---
# Craft: Forbidden Epic
#
# The Colonel's lessons, and the Lionsmith's lessons, have been unkindly, and reductively, rendered as 'stab' versus 'thump'.
craft_recipe(
    output = memory.forbidden_epic,
    power_requirements = attributes(moon=15),
    skills = (
        skill.edicts_martial,
    ),
    solution_must_include = condition(one_of=(memory.confounding_parable,)),
)

# Craft: Wormwood Dream
#
# Interpret the stymphling's hisses into a crime-prophecy of Moon and Winter.
#
# [Snow Stories with Keeper-level <sprite name=moon>, plus Stymphling, creates Wormwood Dream.]
# ---
# Craft: Wormwood Dream
#
# Let's hope it's equally possible to forget this again.
craft_recipe(
    output = memory.wormwood_dream,
    power_requirements = attributes(moon=15),
    skills = (
        skill.edicts_inviolable,
        skill.rhyme_and_remembrance,
        skill.sickle_and_eclipse,
        skill.snow_stories,
        skill.wolf_stories,
    ),
    solution_must_include = condition(one_of=(beast.stymphling, )),
)

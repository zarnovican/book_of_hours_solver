from ..model import attributes, card_type, condition, craft_recipe
from ..item import beverage, device, memory, skill


# --- grail 5 ---

# Craft: Witching Tisane
#
# Here where the sea sounds, I can mix a tide-touched tisane.
#
# [Sea Stories with Prentice-level <sprite name=grail> creates Witching Tisane. Or for a Scholar-level recipe: if I soak Fabric in the brew, I can twist it into a Grailful little cloth doll.]
# ---
# Craft: Witching Tisane
#
# It's best when it's warm; but it'll keep.
craft_recipe(
    output = beverage.witching_tisane,
    power_requirements = attributes(grail=5),
    skills = (
        skill.desires_and_dissolutions,
        skill.leaves_and_thorns,
        skill.orchids_and_narcotics,
        skill.sea_stories,
        skill.the_great_signs_and_the_great_scars,
    ),
)

# Craft: Beguiling Melody
#
# Conceive or recall a delightful little music.
#
# [Resurgences & Emergences with Prentice-level <sprite name=grail> creates Beguiling Melody. Or for a Scholar-level recipe: if I add Fabric, I can hum the faintest life into a little cloth doll.]
# ---
# Craft: Beguiling Melody
#
# I'll be humming this for a while. And so will anyone else who happens by.
craft_recipe(
    output = memory.beguiling_melody,
    power_requirements = attributes(grail=5),
    skills = (
        skill.applebright_euphonies,
        skill.pentiments_and_precursors,
        skill.resurgences_and_emergences,
        skill.tridesma_hiera,
    ),
)

# --- grail 10 ---

# Craft: Pale Mommet
#
# Invest Grail-power in an almost-living doll.
#
# [The Great Signs and the Great Scars with Scholar-level <sprite name=grail>, plus Fabric, creates Pale Mommet.]
# ---
# Craft: Pale Mommet
#
# [With Keeper-level Grail, a Pale Mommet is a precursor to a Flushed Mommet.]
craft_recipe(
    output = device.pale_mommet,
    power_requirements = attributes(grail=10),
    skills = (
        skill.pentiments_and_precursors,
        skill.resurgences_and_emergences,
        skill.sea_stories,
        skill.the_great_signs_and_the_great_scars,
        skill.tridesma_hiera,
    ),
    solution_must_include = condition(fabric_and_fibre=1),
)

# Craft: Rubywise Ruin
#
# Brew a Grail-liquor.
#
# [Desires & Dissolutions with Scholar-level <sprite name=grail>, plus Flower, creates Rubywise Ruin.]
# ---
# Craft: Rubywise Ruin
#
# [With Keeper-level Grail, Rubywise Ruin is a precursor to the Sacrament Calicite.]
craft_recipe(
    output = beverage.rubywise_ruin,
    power_requirements = attributes(grail=10),
    skills = (
        skill.applebright_euphonies,
        skill.desires_and_dissolutions,
        skill.leaves_and_thorns,
        skill.orchids_and_narcotics,
    ),
    solution_must_include = condition(flower=1),
)

# --- grail 15 ---

# Craft: Flushed Mommet
#
# With Grail-essence, the mommet will redden into something more potent.
#
# [The Great Signs and the Great Scars with Keeper-level <sprite name=grail>, plus Pale Mommet, creates Flushed Mommet.]
# ---
# Craft: Flushed Mommet
#
# Drink it in, little one. Drink it in….
craft_recipe(
    output = device.flushed_mommet,
    power_requirements = attributes(grail=15),
    skills = (
        skill.desires_and_dissolutions,
        skill.furs_and_feathers,
        skill.pentiments_and_precursors,
        skill.resurgences_and_emergences,
        skill.the_great_signs_and_the_great_scars,
    ),
    solution_must_include = condition(one_of=(device.pale_mommet, )),
)

# Craft: Sacrament Calicite
#
# Use this liquor as a base for a Grail-sacrament.
#
# [Leaves & Thorns with Keeper-level <sprite name=grail>, plus Rubywise Ruin, creates Sacrament Calicite.]
# ---
# Craft: Sacrament Calicite
#
# In the name of the Hour that gives life; of the Hour that takes life; of the Hour that is not sated….
craft_recipe(
    output = beverage.sacrament_calicite,
    power_requirements = attributes(grail=15),
    skills = (
        skill.applebright_euphonies,
        skill.leaves_and_thorns,
        skill.orchids_and_narcotics,
        skill.sea_stories,
        skill.tridesma_hiera,
    ),
    solution_must_include = condition(one_of=(beverage.rubywise_ruin,)),
)

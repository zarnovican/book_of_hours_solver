from ..model import attributes, card_type, condition, craft_recipe
from ..item import device, liquid, memory, skill, thing


# --- heart 5 ---

# Craft: Perhibiate
#
# Not all knots are physical. I can brew an ink which ties the naming to the named.
#
# [Weaving & Knotworking with Prentice-level <sprite name=heart> creates Perhibiate. Or for a Scholar-level recipe: if I add Fabric, I can weave the stained fibres into a greater binding.]
# ---
# Craft: Perhibiate
#
# Some authorities claim it's difficult to lose a pot of perhibiate ink, but they haven't lived at Hush House.
craft_recipe(
    output = liquid.perhibiate,
    power_requirements = attributes(heart=5),
    skills = (
        skill.stitching_and_binding,
        skill.weaving_and_knotworking,
    ),
)

# Craft: Regensburg Balm
#
# Brew a herbal palliative.
#
# [Herbs & Infusions with Prentice-level <sprite name=heart> creates Regensburg Balm. Or for a Scholar-level recipe: if I add a suitably aspected Liquid, I'll brew something more potent.]
# ---
# Craft: Regensburg Balm
#
# Medicine should smell like this: reassuringly offputting.
craft_recipe(
    output = liquid.regensburg_balm,
    power_requirements = attributes(heart=5),
    skills = (
        skill.edicts_inviolable,
        skill.herbs_and_infusions,
        skill.maggephene_mysteries,
        skill.quenchings_and_quellings,
        skill.surgeries_and_exsanguinations,
    ),
)

# Craft: Cheerful Ditty
#
# Conceive or recall a rousing, catchy tune.
#
# [Strings & Songs with Prentice-level <sprite name=heart> creates Cheerful Ditty. Or for a Scholar-level recipe: if I work at an Instrument, I can elevate it to something more powerful.]
# ---
# Craft: Cheerful Ditty
#
# Tiddly tiddly tum ti diddle. Tum!
craft_recipe(
    output = memory.cheerful_ditty,
    power_requirements = attributes(heart=5),
    skills = (
        skill.strings_and_songs,
        skill.drums_and_dances,
    ),
)

# --- heart 10 ---

# Craft: Frith-Weft
#
# Perform a peace-weaving to manifest Heart-aspect.
#
# [Stitching & Binding with Scholar-level <sprite name=heart>, plus Fabric, creates Frith-Weft.]
# ---
# Craft: Frith-Weft
#
# [With Keeper-level Heart, a Frith-Weft is a precursor to Swaddled Thunder.]
craft_recipe(
    output = thing.frith_weft,
    power_requirements = attributes(heart=10),
    skills = (
        skill.stitching_and_binding,
        skill.weaving_and_knotworking,
    ),
    solution_must_include = condition(fabric_and_fibre=1),
)

# Craft: Gideon's Soaks
#
# Brew healing Heart-soaks.
#
# [Herbs & Infusions with Scholar-level <sprite name=heart>, plus Liquid, creates Gideon's Soaks.]
# ---
# Craft: Gideon's Soaks
#
# [With Keeper-level Heart, the Soaks are the precursor to January Sanguinary.]
craft_recipe(
    output = liquid.gideons_soaks,
    power_requirements = attributes(heart=10),
    skills = (
        skill.edicts_inviolable,
        skill.herbs_and_infusions,
        skill.maggephene_mysteries,
        skill.quenchings_and_quellings,
        skill.surgeries_and_exsanguinations,
    ),
    solution_must_include = condition(liquid=1),
)

# Craft: Thunderskin's Paean
#
# Drum up a Heart-music.
#
# [Drums & Dances with Scholar-level <sprite name=heart>, plus Instrument, creates Thunderskin's Paean.]
# ---
# Craft: Thunderskin's Paean
#
# [With Keeper-level Heart, the Paean is the precursor to Swaddled Thunder.]
craft_recipe(
    output = memory.thunderskins_paean,
    power_requirements = attributes(heart=10),
    skills = (
        skill.drums_and_dances,
        skill.strings_and_songs,
    ),
    solution_must_include = condition(instrument=1),
)

# --- heart 15 ---

# Craft: January Sanguinary
#
# Enliven the soaks into something with a greater Heart-aspect.
#
# [Surgeries & Exsanguinations with Keeper-level <sprite name=heart>, plus Gideon's Soaks, creates January Sanguinary.]
# ---
# Craft: January Sanguinary
#
# Stopper it quickly. Quickly!.
craft_recipe(
    output = liquid.january_sanguinary,
    power_requirements = attributes(heart=15),
    skills = (
        skill.edicts_inviolable,
        skill.herbs_and_infusions,
        skill.maggephene_mysteries,
        skill.surgeries_and_exsanguinations,
    ),
    solution_must_include = condition(one_of=(liquid.gideons_soaks, )),
)

# Craft: Swaddled Thunder
#
# Draw storm-potential into the weft, to capture more Heart-aspect.
#
# [Stitching & Binding with Keeper-level <sprite name=heart>, plus Frith-Weft, creates Swaddled Thunder.]
# ---
# Craft: Swaddled Thunder
#
# Sleep, o thou tempest; for now, bow thy head….
craft_recipe(
    output = device.swaddled_thunder,
    power_requirements = attributes(heart=15),
    skills = (
        skill.quenchings_and_quellings,
        skill.stitching_and_binding,
        skill.weaving_and_knotworking,
    ),
    solution_must_include = condition(one_of=(thing.frith_weft, )),
)

# Craft: Swaddled Thunder
#
# Drum storm-potential into the weft, to capture more Heart-aspect.
#
# [Drums & Dances with Keeper-level <sprite name=heart>, plus Thunderskin's Paean, creates Swaddled Thunder.]
# ---
# Craft: Swaddled Thunder
#
# Sleep, o thou tempest; for now, bow thy head….
craft_recipe(
    output = device.swaddled_thunder,
    power_requirements = attributes(heart=15),
    skills = (
        skill.drums_and_dances,
        skill.strings_and_songs,
    ),
    solution_must_include = condition(one_of=(memory.thunderskins_paean, )),
)

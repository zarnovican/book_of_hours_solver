from ..item import beverage, cache, leaf, liquid, material, remains, sustenance, thing
from ..model import attributes, room


# Wrecked Pantry
#
# Smashed glass and shattered timber. This room can be restored, and there'll be salvageable provisions tucked away in the wreckage, but I'll need someone with strong arms and a patient heart.
# ---
# Pantry
#
# This room is close to the roots of the House; and so it had a troubled reputation with the servantry, who late at night might hear the pulse of an unseen drum, the buzzing of flies, voices crying out in tongues unknown... and so the servants would trade favours not to be the one to fetch spices for his Lordship's posset after dark.
pantry = room("pantry",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.domaine_raveline_bottle,
        beverage.eigengrau,
        beverage.elderflower_cordial,
        beverage.schloss_jannings_bottle,
        beverage.scrumpy,
        beverage.sloe_gin_bottle,
        cache.box_of_oddities,
        cache.contraband_jetsam,
        cache.tall_parcel,
        leaf.ch_second_flush_assam_packet,
        leaf.veiled_goddess_lapsang_souchong_packet,
        liquid.cuckoo_honey,
        liquid.cuckoo_honey,
        liquid.gideons_soaks,
        material.beeswax,
        material.cinnabar,
        material.dawnlion_coffee_packet,
        material.dawnlion_coffee_packet,
        material.evening_isles_coffee_packet,
        material.phosphorescent_scrapings,
        material.rose_pearl,
        material.trn_limited_drinking_cocoa_packet,
        remains.canned_ham,
        remains.essential_periost,
        remains.mackerel,
        sustenance.basket_of_vegetables,
        sustenance.blackberry_jam,
        sustenance.blackberry_jam,
        sustenance.golden_marrow,
        sustenance.pale_marrow,
        sustenance.pickled_mushrooms,
        sustenance.pickled_pilchards,
        sustenance.pickled_pilchards,
        sustenance.pumpkin,
        sustenance.rosehip_jam,
        sustenance.soft_amber_pumpkin,
        thing.flour,
    ),
    neighbors = ("kitchen", ),
    power_requirements = attributes(heart=7, nectar=7),
)

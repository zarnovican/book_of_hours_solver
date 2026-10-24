from ..item import beverage, memory
from ..model import attributes, card_type


# Ambergris Chunk
#
# Never, never, never call it 'whale vomit'.
# ---
# Scrutiny
#
# Were I being polite, I would call the scent 'musky'.
ambergris_chunk = card_type("ambergris_chunk",
    attributes(moon=2, scale=2, thing=1, material=1, gem=1),
    consider_output = memory.scent,
)


# Arsenic
#
# A poison sometimes known as 'the Message of the Swan'.
# ---
# Scrutiny
#
# Careful…
arsenic = card_type("arsenic",
    attributes(edge=1, lantern=1, winter=1, thing=1, material=1),
    consider_output = memory.fear,
)


# Atlantic Amber
#
# Sunset's colours, pine's blood.
# ---
# Scrutiny
#
# The tree, the sea, then nothing.
atlantic_amber = card_type("atlantic_amber",
    attributes(lantern=3, thing=1, material=1, gem=1),
    consider_output = memory.revelation,
)


# Awakened Feather
#
# Alive to every draught and spark.
# ---
# Scrutiny
#
# Something on the wind… [There are Prentice-level Sky recipes which can create one of these.]
awakened_feather = card_type("awakened_feather",
    attributes(scale=1, sky=2, thing=1, material=1, remains=1),
    consider_output = memory.cheerful_ditty,
)


# Beeswax
#
# It begins as a flower. [Beeswax can be used to make candles, if you have a skill with the Chandlery aspect.]
# ---
# Scrutiny
#
# Smooth on the fingers.
beeswax = card_type("beeswax",
    attributes(moth=1, scale=1, thing=1, material=1, fuel=1),
    consider_output = memory.scent,
)


# Bitterblack Salts
#
# Bitter as chicory, dark as secrets, but the first rung of the traditional alchemical ascent.
# ---
# Scrutiny
#
# There's a brightness locked within. Keeper-level Forge or Lantern might transform these into a more potent essence. [And Prentice-level Forge can be used with certain recipes to create more Salts.]
bitterblack_salts = card_type("bitterblack_salts",
    attributes(forge=1, thing=1, material=1, pigment=1),
    consider_output = memory.foresight,
)


# Bucket of Ashes
#
# Long cold, but they faintly remember the fire.
# ---
# Scrutiny
#
# Fingers stained grey…
bucket_of_ashes = card_type("bucket_of_ashes",
    attributes(forge=1, comfort=1, material=1),
    consider_output = memory.touch,
)


# Cinnabar
#
# A bright scarlet powder with a silvery brilliance locked within.
# ---
# Scrutiny
#
# Don't inhale…
cinnabar = card_type("cinnabar",
    attributes(forge=1, thing=1, material=1),
    consider_output = memory.touch,
)


# Curious Seashell
#
# Brancrug is said to lie in the Bounds where the world ends. Odd creatures have made their dying way to the beach.
# ---
# Scrutiny
#
# Now powder.
curious_seashell = card_type("curious_seashell",
    attributes(moon=1, scale=1, thing=1, material=1),
    consider_output = memory.regret,
)


# Dawnlion Coffee (Packet)
#
# Coffee from beyond the great deserts.
# ---
# Scrutiny
#
# Better brewed.
dawnlion_coffee_packet = card_type("dawnlion_coffee_packet",
    attributes(forge=1, lantern=1, scale=1, thing=1, material=1, brewable=1),
    brew_into = beverage.dawnlion_coffee_pot,
    consider_output = memory.scent,
)


# Desiccated Witchworms
#
# Nasty little things, but almost safe when they're this dead.
# ---
# Scrutiny
#
# Rinse them carefully away.
desiccated_witchworms = card_type("desiccated_witchworms",
    attributes(knock=2, scale=2, thing=1, material=1, remains=1),
    consider_output = memory.sight,
)


# Driftwood Fragment
#
# Long ago there was a forest between the waves of Brancrug Bay. This driftwood is not nearly that old, but it's shared salt with its lost forerunners…
# ---
# Scrutiny
# 
# Fragments…
driftwood_fragment = card_type("driftwood_fragment",
    attributes(moon=1, nectar=1, thing=1, material=1, wood=1, fuel=1),
    consider_output = memory.touch,
)


# Evening Isles Coffee (Packet)
#
# Coffee from beyond the sunset sea.
# ---
# Scrutiny
#
# Better brewed.
evening_isles_coffee_packet = card_type("evening_isles_coffee_packet",
    attributes(forge=1, lantern=1, rose=1, thing=1, material=1, brewable=1),
    brew_into = beverage.evening_isles_coffee_pot,
    consider_output = memory.scent,
)


# Gervinite
#
# An alloy equivalent in some respects to the clockmaker's invar - but instead of a constant weight, it retains the same origin in every history.
# ---
# Scrutiny
#
# Whatever that means, it meant it. [There is a Scholar-level Knock recipe that can craft this with glass, and a Scholar-level Sky recipe that can craft it with metal.]
gervinite = card_type("gervinite",
    attributes(knock=4, rose=2, thing=1, material=1, metal=1),
    consider_output = memory.horizon_sight,
)


# Glue
#
# A substance that ensures the continued proximity of things to other things.
# ---
# Scrutiny
#
# Oooops.
glue = card_type("glue",
    attributes(forge=1, nectar=1, thing=1, material=1),
    consider_output = memory.touch,
)


# Granite Slab
#
# Long-cold volcano-blood.
# ---
# Scrutiny
#
# Crushed.
granite_slab = card_type("granite_slab",
    attributes(forge=1, scale=1, thing=1, material=1, stone=1),
    consider_output = memory.touch,
)


# Hawthorn Blank
#
# A wood favoured by the Horned-Axe.
# ---
# Scrutiny
#
# Shattered.
hawthorn_blank = card_type("hawthorn_blank",
    attributes(knock=1, thing=1, material=1, fuel=1, wood=1),
    consider_output = memory.touch,
)


# Labhitic Tincture
#
# A much more potent preparation can be extracted from the remains of a labhite, but labhites generally frown on this technique.
# ---
# Scrutiny
#
# Scattered. [There are Prentice-level Edge recipes which can be used to create more.]
labhitic_tincture = card_type("labhitic_tincture",
    attributes(edge=2, lantern=1, thing=1, material=1),
    consider_output = memory.sight,
)


# Leathy Lees
#
# The dark aftermath of a dark drink.
# ---
# Scrutiny
#
# Exhausted.
leathy_lees = card_type("leathy_lees",
    attributes(grail=1, moth=2, nectar=1, scale=1, thing=1, material=1),
    consider_output = memory.taste,
)


# Lignum Vitae Blank
#
# The hardest of all woods.
# ---
# Scrutiny
#
# In Brancrug Village, they tell of Thirza Blake's boast that she crossed an ocean in the Bounds by clinging to a broom of lignum vitae after a shipwreck. The pedant Strathcoyne points out that lignum vitae sinks in water. 'An ocean of mercury,' Thirza replies, and then, to provide a suitable punchline, clouts him on the head with her broom. Much later, Governor Collers speculated that this might be a sly alchemical parable...
lignum_vitae_blank = card_type("lignum_vitae_blank",
    attributes(edge=3, nectar=3, scale=3, thing=1, material=1, wood=1, fuel=1),
    consider_output = memory.gossip,
)


# Phosphorescent Scrapings
#
# Rendered inert, but still luminous.
# ---
# Scrutiny
#
# Dissipated.
phosphorescent_scrapings = card_type("phosphorescent_scrapings",
    attributes(moon=2, nectar=2, thing=1, material=1, remains=1),
    consider_output = memory.sight,
)


# Quartz Chunk
#
# Ice, rock, winking light.
# ---
# Scrutiny
#
# Powdered.
quartz_chunk = card_type("quartz_chunk",
    attributes(rose=1, thing=1, material=1, gem=1),
    consider_output = memory.touch,
)


# Rags
#
# Scraps of fabric. Possibly useful as fuel.
# ---
# Scrutiny
#
# Sort through the scraps… nothing of use.
rags = card_type("rags",
    attributes(forge=1, heart=1, winter=1, thing=1, material=1, fuel=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# Refulgin
#
# A white so pure that it remains visible even in utter darkness, like the moon, or an insistent cat.
# ---
# Scrutiny
#
# Shiny! Ish. [There are Prentice-level Lantern recipes which can craft this.]
refulgin = card_type("refulgin",
    attributes(lantern=2, thing=1, material=1, pigment=1),
    consider_output = memory.revelation,
)


# Rose-Pearl
#
# Surprisingly common in these waters.
# ---
# Scrutiny
#
# In one folktale, the Witch prophesied to the Sister that the sea would drink her blood; the Sister prophesied to the Witch that the sea would never harm her. When they came ashore by Brancrug, she gave her a shell to catch rainwater in, and the sharp edge shed her blood on the white sand. That blood we know as rose-pearls.
rose_pearl = card_type("rose_pearl",
    attributes(heart=1, thing=1, material=1, gem=1),
    consider_output = memory.solace,
)


# Sand
#
# An hourglass, of course, is sand contained by sand.
# ---
# Scrutiny
#
# It's time.
sand = card_type("sand",
    attributes(lantern=1, moon=1, thing=1, material=1, glass=1),
    consider_output = memory.salt,
)


# Sea-Glass
#
# Smooth as an egg, frosted like a winter window.
# ---
# Scrutiny
#
# What's lost.
sea_glass = card_type("sea_glass",
    attributes(lantern=1, moon=1, thing=1, material=1, glass=1),
    consider_output = memory.touch,
)


# Serpentinite Slab
#
# The grey-green root-rock of the Cornish coast.
# ---
# Scrutiny
#
# Crushed.
serpentinite_slab = card_type("serpentinite_slab",
    attributes(knock=1, scale=1, thing=1, material=1, stone=1),
    consider_output = memory.touch,
)


# Tanglebrag
#
# A clot of wood, leaves and feathers that might draw the attention of the entity called Knotwingknot.
# ---
# Scrutiny
#
# Not a knot… [There are Prentice-level Moth recipes - and one Lantern recipe - that can craft this.]
tanglebrag = card_type("tanglebrag",
    attributes(lantern=1, moth=2, nectar=1, scale=1, thing=1, material=1),
    consider_output = memory.impulse,
)


# T.R.N. Limited Drinking Cocoa (Packet)
#
# T.R.N.'s Spices and Savours Department markets this as 'the Secret Sacrament of the Last Inca!'
# ---
# Scrutiny
#
# Not <i>exactly</i> edible.
trn_limited_drinking_cocoa_packet = card_type("trn_limited_drinking_cocoa_packet",
    attributes(grail=2, heart=1, thing=1, material=1, brewable=1),
    brew_into = beverage.trn_limited_drinking_cocoa_pot,
    consider_output = memory.scent,
)


# Westcott's Compounds
#
# Reagents and activants to enhance alchemical operations, or the flavour of one's pipe tobacco.
# ---
# Scrutiny
#
# Scattered. [There are Prentice-level Forge and Moth recipes which can be used to create more.]
westcotts_compounds = card_type("westcotts_compounds",
    attributes(forge=2, grail=1, lantern=1, moth=1, nectar=1, thing=1, material=1),
    consider_output = memory.sight,
)


# Whispering Sand
#
# White-silver sand in which the voice of the waves lingers...
# ---
# Scrutiny
#
# The voice of the waves lingers no longer.
whispering_sand = card_type("whispering_sand",
    attributes(lantern=1, moon=2, thing=1, material=1, glass=1),
    consider_output = memory.salt,
)


# Wire (Copper)
#
# The Malachite's metal.
# ---
# Scrutiny
#
# Finished.
wire_copper = card_type("wire_copper",
    attributes(forge=2, nectar=1, sky=1, thing=1, material=1, metal=1),
    consider_output = memory.touch,
)


# Wire (Orichalcum)
#
# A metal which alters its estate in every age, but in every age can be used to catalyse the azoth.
# ---
# Scrutiny
#
# There is a sunset song which tells how in sea-stolen Ys, all the water-ewers were orichalcum, and all the window-panes were amber… [There are Scholar-level Forge recipes which can be used to craft this from another metal.]
wire_orichalcum = card_type("wire_orichalcum",
    attributes(forge=4, lantern=1, thing=1, material=1, metal=1),
    consider_output = memory.regret,
)


# Wire (Silver)
#
# The Meniscate's metal.
# ---
# Scrutiny
#
# There is a rare alloy called gervinite which is used for potent Knock-devices. It has some of the properties of silver. Would it be possible, perhaps, to use silver wire instead? It would be a Keeper-level recipe…
wire_silver = card_type("wire_silver",
    attributes(forge=2, moon=1, thing=1, material=1, metal=1),
    consider_output = memory.touch,
)


# Wire (Steel)
#
# The Colonel's metal.
# ---
# Scrutiny
#
# Finished.
wire_steel = card_type("wire_steel",
    attributes(edge=1, forge=2, thing=1, material=1, metal=1),
    consider_output = memory.touch,
)


# Wire (Tin)
#
# The white metal of the Sun-in-Rags.
# ---
# Scrutiny
#
# Finished.
wire_tin = card_type("wire_tin",
    attributes(forge=2, winter=1, thing=1, material=1, metal=1),
    consider_output = memory.touch,
)


# Yew Blank
#
# A wood sacred to the Malachite, who is also called the Ring-Yew; but also the tree that the Dead pass in the dark.
# ---
# Scrutiny
#
# Finished.
yew_blank = card_type("yew_blank",
    attributes(nectar=2, winter=1, thing=1, material=1, wood=1, fuel=1),
    consider_output = memory.touch,
)

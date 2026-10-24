from ..item import memory
from ..model import attributes, card_type


# Chimeric Larva
#
# Approaching the chrysalis crossroads.
# ---
# Scrutiny
#
# An undulating bundle of possibilities… [Certain Scholar-level recipes will hatch this from an Egg in the presence of sufficient Moth - or sometimes Moon.]
chimeric_larva = card_type("chimeric_larva",
    attributes(knock=2, moon=2, moth=4, beast=1, comfort=1, co_operative=1),
    consider_output = memory.fear,  # TODO (verify) consider output mismatch
)


# Hungry Gull
#
# Squawking urgently.
# ---
# Scrutiny
#
# Why would it fly free, when it can get free food?
hungry_gull = card_type("hungry_gull",
    attributes(moon=1, sky=1, beast=1, comfort=1),
    consider_output = memory.touch,
)


# Hungry Viper
#
# Inclined to strike, although sluggishly, until fed.
# ---
# Scrutiny
#
# Ware fingers…
hungry_viper = card_type("hungry_viper",
    attributes(knock=1, scale=1, beast=1, comfort=1),
    consider_output = memory.touch,
)


# Living Relic
#
# Few of these have been seen in the world under <i>this</i> sun.
# ---
# Scrutiny
#
# Its sigils evolve with age… but it ages so very slowly.
living_relic = card_type("living_relic",
    attributes(heart=1, scale=4, sky=2, beast=1, comfort=1, co_operative=1),
    consider_output = memory.touch,
)


# Magnificent Green Cockatoo
#
# On numerous occasions, this wonderful bird has remained almost entirely inaudible.
# ---
# Scrutiny
#
# This proud bird strongly resembles a painting in the Gullscry Tower. But that painting is two hundred years old. Cockatoos are long-lived birds, but not that long; and they can be difficult to tell apart.
magnificent_green_cockatoo = card_type("magnificent_green_cockatoo",
    attributes(grail=2, heart=2, sky=2, beast=1, comfort=1, co_operative=1),
    consider_output = memory.sound,
)


# Orphaned Chick
#
# A peeping little thing, its mother is dead or flown.
# ---
# Scrutiny
#
# Fragile as a feathered petal.
orphaned_chick = card_type("orphaned_chick",
    attributes(moon=1, sky=2, beast=1, comfort=1),
    consider_output = memory.sight,
)


# Perilous Imago
#
# It's come so far. Release it, and it could fly farther.
# ---
# Scrutiny
#
# If this had developed very differently, we might call it Carapace Cross… [There are Keeper-level recipes that can develop this from a Chimeric Larva, in the presence of sufficient Moon or Moth.]
perilous_imago = card_type("perilous_imago",
    attributes(knock=2, moon=2, moth=6, scale=2, beast=1, comfort=1, co_operative=1),
    consider_output = memory.sight,
)


# Pet Gull
#
# As noisy and demanding as it was in its youth. But much bigger.
# ---
# Scrutiny
#
# Why would it fly free, when it can get free food?
pet_gull = card_type("pet_gull",
    attributes(moon=1, sky=2, beast=1, comfort=1, co_operative=1),
    consider_output = memory.sound,
)


# Pleading Tuppence
#
# Cluck. …cluck?
# ---
# Scrutiny
#
# Tuppence, in her uncertainty.
pleading_tuppence = card_type("pleading_tuppence",
    attributes(scale=2, sky=1, beast=1, comfort=1),
    consider_output = memory.sound,
)


# Resentful Terrence
#
# Cluck. CLUCK.
# ---
# Scrutiny
#
# Terrence, in her magnificence.
resentful_terrence = card_type("resentful_terrence",
    attributes(scale=3, sky=1, beast=1, comfort=1),
    consider_output = memory.sound,
)


# Savage Relic
#
# A shrieking little bundle of primordial ill-temper.
# ---
# Scrutiny
#
# Its sigils evolve with age… but it ages so very slowly.
savage_relic = card_type("savage_relic",
    attributes(heart=1, scale=4, sky=1, beast=1, comfort=1),
    consider_output = memory.touch,
)


# Stray Cat
#
# Feed some animals and earn their loyalty. Feed this one, and earn its patience.
# ---
# Scrutiny
#
# Elegant, inscrutable, indefatigable.
stray_cat = card_type("stray_cat",
    attributes(grail=2, heart=2, moth=2, beast=1, comfort=1),
    consider_output = memory.sight,
)


# Stray Dog
#
# Lost, frightened, eager.
# ---
# Scrutiny
#
# Something noble in its ancestry; and something else.
stray_dog = card_type("stray_dog",
    attributes(edge=2, heart=2, scale=2, beast=1, comfort=1),
    consider_output = memory.touch,
)


# Stymphling
#
# Eva Dewulf taught her father Valentine how to hatch these silvery little villains, but he never learnt to like them.
# ---
# Scrutiny
#
# A distant cousin of salamanders, and of moonlight. [Certain Scholar-level recipes will hatch this from an egg in the presence of sufficient Moon.]
stymphling = card_type("stymphling",
    attributes(moon=3, scale=3, beast=1, comfort=1, co_operative=1),
    consider_output = memory.touch,
)


# Tame Viper
#
# An avid student of warm fireplace stones, warm mice, and warm milk.
# ---
# Scrutiny
#
# Ware fingers…
tame_viper = card_type("tame_viper",
    attributes(knock=2, scale=2, beast=1, comfort=1, co_operative=1),
    consider_output = memory.touch,
)


# Terrence, the Chicken
#
# Was this magnificent and indomitable beast named for the rector's indomitable and magnificent housekeeper? Best not to inquire too closely.
# ---
# Scrutiny
#
# Terrence, in her magnificence.
terrence_the_chicken = card_type("terrence_the_chicken",
    attributes(scale=3, sky=1, beast=1, comfort=1, co_operative=1),
    consider_output = memory.sound,
)


# Tuppence, the Other Chicken
#
# Tuppence's most notable quality, all observers will agree, is that she is not Terrence.
# ---
# Scrutiny
#
# Tuppence, in her uncertainty.
tuppence_the_other_chicken = card_type("tuppence_the_other_chicken",
    attributes(scale=2, sky=1, beast=1, comfort=1, co_operative=1),
    consider_output = memory.sound,
)


# Wild Viper
#
# Don't make any sudden moves.
# ---
# Scrutiny
#
# Ware fingers…
wild_viper = card_type("wild_viper",
    attributes(knock=2, scale=2, beast=1, comfort=1),
    consider_output = memory.sight,
)

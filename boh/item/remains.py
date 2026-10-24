from ..item import memory
from ..model import attributes, card_type


# Animal Bones
#
# What remains?
# ---
# Scrutiny
#
# I recall a prophecy of war: 'a war in which each flame will find its fuel.' Or was the prophecy mine?
animal_bones = card_type("animal_bones",
    attributes(scale=2, winter=1, thing=1, remains=1),
    consider_output = memory.fear,
)


# Canned Ham
#
# The taste will remain reliably unchanged for many years to come; which is, in some respects, an advantage.
# ---
# Scrutiny
#
# Salty and savoury.
canned_ham = card_type("canned_ham",
    attributes(heart=2, scale=1, thing=1, sustenance=1, remains=1, cooking_ingredient=1),
    consider_output = memory.solace,
)


# Essential Periost
#
# What happens when you boil and scrape us down to our utter fundamentals.
# ---
# Scrutiny
#
# This was something left from before any of us were born - from a time when the sun swung red and low -   [There are Nectar, Moon and Winter recipes which can be used to craft this from mortal remains.]
essential_periost = card_type("essential_periost",
    attributes(moon=2, nectar=4, scale=4, winter=4, thing=1, remains=1),
    consider_output = memory.old_moment,
)


# Heart in a Jar
#
# An offering, or an exhibit?
# ---
# Scrutiny
#
# One very final beat.
heart_in_a_jar = card_type("heart_in_a_jar",
    attributes(heart=2, winter=1, thing=1, remains=1),
    consider_output = memory.fear,
)


# Human Hair
#
# Of interest to wig-makers, cushion-stuffers, and crude sorcerers.
# ---
# Scrutiny
#
# Torn.
human_hair = card_type("human_hair",
    attributes(moth=1, thing=1, fabric_and_fibre=1, remains=1),
    consider_output = memory.touch,
)


# Mackerel
#
# Eat it while it's fresh or keep it while it's salted.
# ---
# Scrutiny
#
# Healthful and slippery.
mackerel = card_type("mackerel",
    attributes(heart=1, moon=2, scale=1, thing=1, cooking_ingredient=1, raw=1, remains=1, sustenance=1),
    consider_output = memory.taste,
)


# Pilchards
#
# [Pickle them alone; or they're pretty good on toast.]
# ---
# Scrutiny
#
# They're just really big sardines. Or sardines are really small pilchards. This is the mystery.
pilchards = card_type("pilchards",
    attributes(heart=1, moon=2, scale=1, thing=1, cooking_ingredient=1, raw=1, remains=1, sustenance=1),
    consider_output = memory.scent,
)


# Skaptodon Fang
#
# It is rare for the Lionsmith to make skaptodons, now; but they are difficult to kill, and they live a very long time.
# ---
# Scrutiny
#
# Potent.
skaptodon_fang = card_type("skaptodon_fang",
    attributes(edge=2, scale=2, thing=1, remains=1),
    consider_output = memory.foresight,
)


# Urn of Ashes
#
# Some poor soul who probably won't mind if they're repurposed for a worthy experiment. I probably wouldn't.
# ---
# Scrutiny
#
# I recall a prophecy of war: 'a war in which each flame will find its fuel.' Or was the prophecy mine?
urn_of_ashes = card_type("urn_of_ashes",
    attributes(winter=3, thing=1, remains=1),
    consider_output = memory.fear,
)

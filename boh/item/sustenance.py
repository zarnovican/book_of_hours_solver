from ..item import memory
from ..model import attributes, card_type


# Basket of Leeks
#
# The mark of St David's triumph. And very good in soup.
# ---
# Scrutiny
#
# That wasn't what you'd call easy on the palate.
basket_of_leeks = card_type("basket_of_leeks",
    attributes(edge=1, heart=1, nectar=2, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.regret,
)

# Basket of Onions
#
# The <i>prima materia</i> of cooking. This may be why the cosmos is shaped so like an onion.
# ---
# Scrutiny
#
# That wasn't what you'd call easy on the palate.
basket_of_onions = card_type("basket_of_onions",
    attributes(edge=1, heart=1, nectar=2, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.regret,
)


# Basket of Vegetables
#
# Gifts from the garden.
# ---
# Scrutiny
#
# Fresh and hearty.
basket_of_vegetables = card_type("basket_of_vegetables",
    attributes(heart=1, nectar=1, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.solace,
)


# Blackberry Jam
#
# Plucked from hedgerows.
# ---
# Scrutiny
#
# Sweet and tasty.
blackberry_jam = card_type("blackberry_jam",
    attributes(grail=1, heart=1, nectar=1, rose=1, thing=1, sustenance=1, cooking_ingredient=1),
    consider_output = memory.solace,
)


# Dark Marrow
#
# In Brancrug, they take marrows seriously. This is a marrow with secrets.
# ---
# Scrutiny
#
# The secrets in this marrow are not identifiable to the tongue.
dark_marrow = card_type("dark_marrow",
    attributes(heart=1, moon=1, nectar=2, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.solace,
)


# Golden Marrow
#
# In Brancrug, they take marrows seriously. This is accounted a beauty among its kind.
# ---
# Scrutiny
#
# This marrow's magnificence is not manifest in the mouth.
golden_marrow = card_type("golden_marrow",
    attributes(heart=1, lantern=1, nectar=2, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.solace,
)


# Gull's Egg
#
# 'At Brancrug, even the Hours are kind, and the years are kinder.' This egg might stay viable quite a while yet.
# ---
# Scrutiny
#
# When it cracks, a craze of lines, the tiniest sound, and then a joyous freedom for potentially delicious goo.
gulls_egg = card_type("gulls_egg",
    attributes(scale=1, thing=1, sustenance=1, egg=1, brewable=1),
    consider_output = memory.touch,
)


# Hen's Egg
#
# Delicious when cooked, alarming when dropped.
# ---
# Scrutiny
#
# When it cracks, a craze of lines, the tiniest sound, and then a joyous freedom for potentially delicious goo.
hens_egg = card_type("hens_egg",
    attributes(heart=1, scale=1, thing=1, sustenance=1, egg=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Outsized Egg
#
# An ostrich egg? A crocodile egg? Surely neither.
# ---
# Scrutiny
#
# The faintest scratching within…
outsized_egg = card_type("outsized_egg",
    attributes(scale=3, thing=1, sustenance=1, egg=1, brewable=1),
    consider_output = memory.sound,
)


# Pale Marrow
#
# In Brancrug, they take marrows seriously. This is a marrow redolent of sorrow.
# ---
# Scrutiny
#
# Eating it raw only accentuates the sorrow.
pale_marrow = card_type("pale_marrow",
    attributes(heart=1, nectar=2, winter=1, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Pickled Mushrooms
#
# You'll learn to like them.
# ---
# Scrutiny
#
# I might have learnt to like them.
pickled_mushrooms = card_type("pickled_mushrooms",
    attributes(edge=1, heart=1, moon=1, nectar=2, thing=1, sustenance=1, first_course=1, side_dish=1),
    consider_output = memory.taste,
)


# Pickled Pilchards
#
# An acquired, and unforgettable, taste.
# ---
# Scrutiny
#
# How does one know when one has acquired a taste?
pickled_pilchards = card_type("pickled_pilchards",
    attributes(edge=1, heart=1, moon=2, scale=1, thing=1, sustenance=1, first_course=1, side_dish=1),
    consider_output = memory.taste,
)


# Pillas-Oat Bread
#
# Gritty bread made with the hardy, ancient oats that grow at Land's End.
# ---
# Scrutiny
#
# Gritty, but good.
pillas_oat_bread = card_type("pillas_oat_bread",
    attributes(forge=1, heart=1, nectar=1, rose=1, thing=1, sustenance=1, first_course=1, bread=1, cooking_ingredient=1),
    consider_output = memory.sight,
)


# Pumpkin
#
# Mash it, eat it, hide forbidden documents in it.
# ---
# Scrutiny
#
# Better cooked.
pumpkin = card_type("pumpkin",
    attributes(heart=1, nectar=1, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Rosehip Jam
#
# Plucked from wild roses.
# ---
# Scrutiny
#
# Florally sweet.
rosehip_jam = card_type("rosehip_jam",
    attributes(heart=1, nectar=1, rose=2, thing=1, sustenance=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Sack of Vegetables
#
# Stew-in-waiting.
# ---
# Scrutiny
#
# Fresh and hearty.
sack_of_vegetables = card_type("sack_of_vegetables",
    attributes(heart=1, nectar=1, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Soft Amber Pumpkin
#
# A lovely golden gourd grown beside the soft sea.
# ---
# Scrutiny
#
# The pumpkin bears the marks of intrusion. It's been filled with something sticky and unexpected.
# ---
# Scrutiny
#
# Not bad… for a raw pumpkin.
soft_amber_pumpkin = card_type("soft_amber_pumpkin",
    attributes(heart=1, lantern=1, nectar=1, thing=1, sustenance=1, raw=1, cooking_ingredient=1),
    #consider_output = xxx .. morph
)


# Viper Egg
#
# A serpent in waiting.
# ---
# Scrutiny
#
# Poor thing: coiled like a forbidden thought, never to see day.
viper_egg = card_type("viper_egg",
    attributes(scale=1, thing=1, sustenance=1, egg=1, brewable=1),
    consider_output = memory.taste,
)

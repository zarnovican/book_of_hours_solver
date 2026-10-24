from ..item import memory
from ..model import attributes, card_type


# Basket of Apples
#
# Notoriously hard to take just one bite.
# ---
# Scrutiny
#
# Sweet, crunchy, satisfying.
basket_of_apples = card_type("basket_of_apples",
    attributes(grail=1, heart=1, nectar=1, thing=1, sustenance=1, fruit=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Blackberries
#
# Berries promised by darkness.
# ---
# Scrutiny
#
# Sweet and tangy. [If you're looking for more Blackberries, they can sometimes be found on the Moor in summer and autumn.]
blackberries = card_type("blackberries",
    attributes(heart=1, nectar=1, thing=1, sustenance=1, fruit=1, first_course=1, cooking_ingredient=1),
    consider_output = memory.satisfaction,
)


# Bowl of Sea-Blest Pears
#
# Smooth as butter and wonderfully juicy.
# ---
# Scrutiny
#
# Thirza Blake developed this variety by - she claimed - hybridising with orchard rootstock of Ys-beyond-the-wave. [Add Dough and spices to bake a pie.]
bowl_of_sea_blest_pears = card_type("bowl_of_sea_blest_pears",
    attributes(grail=1, moon=1, nectar=1, thing=1, sustenance=1, fruit=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Bunch of Grapes
#
# A juicy blush-purple.
# ---
# Scrutiny
#
# On this southern tip of Britain, grapes do grow. They might even make creditable wine.
bunch_of_grapes = card_type("bunch_of_grapes",
    attributes(nectar=1, thing=1, sustenance=1, cooking_ingredient=1, fruit=1),
    consider_output = memory.taste,
)


# Misshapen Fruit
#
# Salvaged windfalls, lumpy but tasty.
# ---
# Scrutiny
#
# Lumpy, but tasty. Tasty, but lumpy. Lumpy.
misshapen_fruit = card_type("misshapen_fruit",
    attributes(heart=1, moth=1, nectar=1, thing=1, sustenance=1, fruit=1),
    consider_output = memory.taste,
)


# Pyrus Auricalcinus
#
# A peculiar pear, with coppery skin that barely dints under the pressure of fingers.
# ---
# Scrutiny
#
# In our History, this grows only on the uncanny hybrids we call 'Mare-blest' trees. [Although there are Scholar-level Nectar recipes that can force it to burst from dead wood.]
pyrus_auricalcinus = card_type("pyrus_auricalcinus",
    attributes(forge=4, nectar=4, thing=1, sustenance=1, fruit=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Rosehips
#
# Berries that promise roses.
# ---
# Scrutiny
#
# Tangy and tart.[If you're looking for more Rosehips, they can sometimes be found on the Moor in summer and autumn.]
rosehips = card_type("rosehips",
    attributes(heart=1, nectar=1, rose=1, thing=1, sustenance=1, fruit=1, first_course=1, cooking_ingredient=1),
    consider_output = memory.satisfaction,
)

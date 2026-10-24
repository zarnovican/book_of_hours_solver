from ..item import memory
from ..model import attributes, card_type


# Bisclavret's Knot
#
# The <i>bisclavret</i> is the half-human hill-child of these parts, and this is its sign.
# ---
# Scrutiny
#
# The wind howls… [Certain Prentice-level Scale recipes are used to tie the Knot.]
bisclavrets_knot = card_type("bisclavrets_knot",
    attributes(moth=1, scale=2, thing=1, mark=1),
    consider_output = memory.sight,
)


# Midnight Mark
#
# A blemish left on a page (or a skin) by a careful incision (or a judicious sting) to preserve a little of the power of night.
# ---
# Scrutiny
#
# A little loss of night. [Certain Prentice-level Moon recipes can be used to make the Mark.]
midnight_mark = card_type("midnight_mark",
    attributes(moon=2, moth=1, thing=1, mark=1),
    consider_output = memory.sight,
)


# Salt-Sign
#
# Too bad it won't last. But then again, what does?
# ---
# Scrutiny
#
# It didn't last. [Certain Prentice-level Rose and Moon recipes which can be used to create this.]
salt_sign = card_type("salt_sign",
    attributes(moon=2, rose=2, thing=1, mark=1),
    consider_output = memory.regret,
)


# Year-Tally
#
# A chitty worth an additional year of life, scrupulously obtained through carefully balanced thaumaturgic attention to the Cindered Tally of the Madrugad.
# ---
# Scrutiny
#
# Somewhere, perhaps, someone has won an extra year. [Certain Keeper-level Winter recipes can be used to craft this from Essential Periost.]
year_tally = card_type("year_tally",
    attributes(winter=6, thing=1, mark=1),
    consider_output = memory.old_moment,
)

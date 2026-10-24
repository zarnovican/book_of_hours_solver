from ..item import memory, weather
from ..model import attributes, card_type


# Chronsichord
#
# A music-box that only performs once; a typewriter that can only send one message; a clock that can only strike Now.
# ---
# Scrutiny
#
# A whirl of motion; a series of clicks; then silence. [There are Keeper-level Knock recipes that can craft this from Gervinite.]
chronsichord = card_type("chronsichord",
    attributes(forge=3, knock=6, sky=3, winter=3, thing=1, tool=1, device=1, ink=1),
    consider_output = memory.pattern,
)


# Dearday Lens
#
# A fiendishly simple - and wretchedly fragile - optical device.
# ---
# Scrutiny
#
# Inspired by one half of the notorious Edge dyad and developed by the Librarian Brulleau; useful for starting fires and inciting headaches, among other things. [There are Prentice-level Lantern recipes which can create one of these.]
dearday_lens = card_type("dearday_lens",
    attributes(edge=1, forge=1, lantern=2, sky=2, thing=1, tool=1, device=1, lens=1, glass=1),
    consider_output = memory.regret,
)


# Flushed Mommet
#
# A crimson-stained little cloth doll with merry button eyes and a frill of twitching ribbons.
# ---
# Scrutiny
#
# It's not alive - or not very. It is hungry - but not very. [There are Keeper-level Grail recipes which can develop a Pale Mommet into one of these.]
flushed_mommet = card_type("flushed_mommet",
    attributes(grail=6, heart=3, moth=3, thing=1, tool=1, device=1, inert=1, woven=1),
    consider_output = memory.regret,
)


# Pale Mommet
#
# A gently twitching little cloth doll with melancholy button eyes and a frill of coloured ribbons.
# ---
# Scrutiny
#
# It's cold. It's always cold. It's grateful for my warmth… [There are Scholar-level Grail recipes which can craft one of these from fabric.]
pale_mommet = card_type("pale_mommet",
    attributes(grail=4, heart=2, moth=2, thing=1, tool=1, device=1, inert=1, woven=1),
    consider_output = memory.sight,
)


# Swaddled Thunder
#
# A storm swathed in subtle threads, ready to be released with a few judicious snips.
# ---
# Scrutiny
#
# The thread parts - the weave is empty - the skies cry out! [There are Keeper-level Heart recipes that can craft this from a Frith-Weft or a Thunderskin's Paean.]
swaddled_thunder = card_type("swaddled_thunder",
    attributes(heart=6, sky=4, thing=1, tool=1, device=1, fabric_and_fibre=1),
    consider_output = weather.storm,
)

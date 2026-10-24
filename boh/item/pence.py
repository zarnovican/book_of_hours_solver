from ..model import attributes, card_type


# Crown
#
# Five shillings; one-quarter of a pound.""",
crown = card_type("crown",
    attributes(pence=60),
)


# Five Pound Note
#
# 'I promise to pay the Bearer on Demand the Sum of Five Pounds'. The Bearer never does demand, though.
five_pound_note = card_type("five_pound_note",
    attributes(pence=1200),
)


# Florin
#
# A shilling per side.""",
florin = card_type("florin",
    attributes(pence=24),
)


# Half Crown
#
# Two and a half shillings. Obviously.""",
half_crown = card_type("half_crown",
    attributes(pence=30),
)


# One Pound Note
#
# A noble paper in soothing green. Britannia lounges on her throne, flaming hammer propped insouciantly across her knee.
one_pound_note = card_type("one_pound_note",
    attributes(pence=240),
)


# Penny
#
# The smallest denomination coin, except for the smaller ones.""",
penny = card_type("penny",
    attributes(pence=1),
)


# Seven Pound Note
#
# Swirls and curlicues in solemn hues. Until recently, one could exchange bank notes for gold in the banks of the capital. A seven-pound note can still be exchanged for rarer metals in rarer places.
seven_pound_note = card_type("seven_pound_note",
    attributes(pence=1680),
)


# Shilling
#
# Twelve pence or, if you prefer, one-twentieth of a pound.""",
shilling = card_type("shilling",
    attributes(pence=12),
)


# Sixpence
#
# The silver coin of least value - but silver, nonetheless.""",
sixpence = card_type("sixpence",
    attributes(pence=6),
)


# Ten Shilling Note
#
# Half a pound; but not half a note. A recent innovation.""",
ten_shilling_note = card_type("ten_shilling_note",
    attributes(pence=120),
)


# Threepence
#
# Or 'thruppence', or a 'thruppenny bit'. Like twopence, but more so.""",
threepence = card_type("threepence",
    attributes(pence=3),
)


# Twopence
#
# Or, if you prefer, 'tuppence'. A sort of Janus of pennies.""",
twopence = card_type("twopence",
    attributes(pence=2),
)

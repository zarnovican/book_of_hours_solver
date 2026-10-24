from ..item import memory
from ..model import attributes, card_type


# Aglaophotis-Scented Candle
#
# A candle scented with aglaophotis.
# ---
# Scrutiny
#
# The air clears, and my thoughts likewise.
aglaophotis_scented_candle = card_type("aglaophotis_scented_candle",
    attributes(heart=2, knock=2, lantern=2, rose=2, thing=1, candle=1, light=1),
    consider_output = memory.revelation,
)


# Bedside Candleholder
#
# To comfort you through the dark hours.
# ---
# Scrutiny
#
# A clear and gentle light.
bedside_candleholder = card_type("bedside_candleholder",
    attributes(lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.solace,
)


# Beeswax Candle
#
# Simple and bright.
# ---
# Scrutiny
#
# A clear and fragrant light.
beeswax_candle = card_type("beeswax_candle",
    attributes(lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.sight,
)


# Bottled Candle
#
# An admirable combination of two utterly disparate elements. Quiet genius.
# ---
# Scrutiny
#
# Traces of a paper label: DO… RAV….18…
bottled_candle = card_type("bottled_candle",
    attributes(grail=1, lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.scent,
)


# Chalice Candle
#
# A candle scented with fragrant chalice.
# ---
# Scrutiny
#
# The scent is rich as roses.
chalice_candle = card_type("chalice_candle",
    attributes(grail=2, lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.satisfaction,
)


# Historywax Candle
#
# A candle made with the oils of the 'history plant', <i>agave aeterna</i>.
# ---
# Scrutiny
#
# The flame flickers, and the Histories ripple.
historywax_candle = card_type("historywax_candle",
    attributes(lantern=3, thing=1, candle=1, light=1),
    consider_output = memory.wild_surmise,
)


# Honeyscar-Scented Candle
#
# A candle scented with honeyscar jasmine.
# ---
# Scrutiny
#
# A roaring orange flame, a coppery sweetness.
honeyscar_scented_candle = card_type("honeyscar_scented_candle",
    attributes(forge=2, rose=1, thing=1, candle=1, light=1),
    consider_output = memory.foresight,
)


# Moth-Orchid-Scented Candle
#
# A candle scented with moth orchid.
# ---
# Scrutiny
#
# A scent like evening.
moth_orchid_scented_candle = card_type("moth_orchid_scented_candle",
    attributes(knock=2, moth=1, thing=1, candle=1, light=1),
    consider_output = memory.a_stolen_secret,
)


# Small Candlestick
#
# Simple elegance.
# ---
# Scrutiny
#
# Fraser Strathcoyne gave Solomon Husher a much nicer set of silver ones. Thirza Blake sold all those off bought brass ones instead, but they've lasted pretty well.
small_candlestick = card_type("small_candlestick",
    attributes(forge=1, lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.sight,
)


# Snowflake Candle
#
# A silver candle soft as snow.
# ---
# Scrutiny
#
# A chilly light.
snowflake_candle = card_type("snowflake_candle",
    attributes(winter=1, thing=1, candle=1, light=1),
    consider_output = memory.regret,
)


# Tall Candlestick
#
# Elegant simplicity.
# ---
# Scrutiny
#
# Fraser Strathcoyne gave Solomon Husher a much nicer set of silver ones. Thirza Blake sold all those off bought brass ones instead, but they've lasted pretty well.
tall_candlestick = card_type("tall_candlestick",
    attributes(lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.sight,
)


# Watchful Candle
#
# A little portable clarity.
# ---
# Scrutiny
#
# A bright clear light.
watchful_candle = card_type("watchful_candle",
    attributes(lantern=1, thing=1, candle=1, light=1),
    consider_output = memory.foresight,
)


# Weighty Bedside Candleholder
#
# To comfort you through the dark hours.
# ---
# Scrutiny
#
# A clear and gentle light.
# ---
# Scrutiny
#
# The candle is much heavier than it should be. Something has been sealed into the wax…
weighty_bedside_candleholder = card_type("weighty_bedside_candleholder",
    attributes(lantern=1, thing=1, candle=1, light=1),
    #consider_output = xxx    # ..and morph
)


# Widow's Candle
#
# Light it in remembrance.
# ---
# Scrutiny
#
# At the sea-air's current, the candle-flame bows its head…
widows_candle = card_type("widows_candle",
    attributes(moon=1, thing=1, candle=1, light=1),
    consider_output = memory.salt,
)

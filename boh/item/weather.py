from ..model import attributes, card_type


# Clouds
#
# In this country the sky is rarely clear. The Sun goes courteously cloaked.
clouds = card_type("clouds",
    attributes(moon=1, moth=1, weather=1, memory=1),
)


# Fog
#
# Coastal fog - moon-mared, sea-dulling.
fog = card_type("fog",
    attributes(knock=3, moon=3, weather=1, memory=1),
)


# Gale
#
# Trees bend, walls creak, travellers bend low against the blast.
gale = card_type("gale",
    attributes(heart=3, sky=3, weather=1, memory=1),
)


# Hail
#
# Ice raps on the roofs and tree-tops.
hail = card_type("hail",
    attributes(edge=3, sky=3, weather=1, memory=1),
)


# Nume-Brume
#
# Numa's brumous vapours.
nume_brume = card_type("nume_brume",
    attributes(knock=5, moon=5, rose=5, winter=5, weather=1, memory=1),
)


# Rain
#
# Soft rain brings life.
rain = card_type("rain",
    attributes(grail=2, nectar=2, weather=1, memory=1),
)


# Snow
#
# The world is pale today. 'The White is west of the world, and winter does not wait forever', Solomon Husher once said.
snow = card_type("snow",
    attributes(sky=3, winter=3, weather=1, memory=1),
)


# Storm
#
# Thunder-roaring, lightning-lashed skies.
storm = card_type("storm",
    attributes(heart=4, sky=4, weather=1, memory=1),
)


# Sunny
#
# The Sun is not what it was, but today he is smiling.
sunny = card_type("sunny",
    attributes(lantern=2, sky=2, weather=1, memory=1),
)

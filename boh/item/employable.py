from ..model import attributes, card_type


# Skulking Nearby: a Fugitive
#
# Someone's taken a room upstairs for the night. He hasn't shown his face, but the village is abuzz with gossip... [The Fugitive provides <sprite name=scale>, <sprite name=edge>, and <sprite name=heart> assistance. Talk to him before he leaves if you want to use his services.]""",
skulking_nearby_a_fugitive = card_type("skulking_nearby_a_fugitive",
    attributes(employable=1, fee=24),
)


# On an Unusual Pilgrimage: an Unusual Nun
#
# Nuns don't usually travel alone. This one does. [The Sister of the Triple Knot provides <sprite name=knock>, <sprite name=moon>, and <sprite name=grail> assistance. Talk to her before she leaves if you want to use her services.].""",
on_an_unusual_pilgrimage_an_unusual_nun = card_type("on_an_unusual_pilgrimage_an_unusual_nun",
    attributes(employable=1, fee=24),
)


# Passing By: a Consulting Engineer?
#
# A consulting engineer has stopped by the Sweet Bones on the way home. [The Consulting Engineer provides <sprite name=forge>, <sprite name=sky> and <sprite name=lantern> assistance. Talk to her before she leaves if you want to use her services.].""",
passing_by_a_consulting_engineer = card_type("passing_by_a_consulting_engineer",
    attributes(employable=1, fee=24),
)


# Passing By: a Musician
#
# A musician is entertaining the patrons of the Sweet Bones for pennies... not very many pennies. He'd jump at a better-paid opportunity. [The Travelling Musician provides <sprite name=sky>, <sprite name=rose>, and <sprite name=nectar> assistance. Talk to him before he leaves if you want to use his services.].""",
passing_by_a_musician = card_type("passing_by_a_musician",
    attributes(employable=1, fee=24),
)


# Passing By: a Poet
#
# A poet has come to the Sweet Bones seeking inspiration, which mostly seems to mean 'drinking' but also 'complaining'. [The Elegiac Poet provides <sprite name=winter>, <sprite name=moth>, and <sprite name=sky> assistance. Talk to him before he leaves if you want to use his services.].""",
passing_by_a_poet = card_type("passing_by_a_poet",
    attributes(employable=1, fee=24),
)


# Passing By: a Surrealist Painter
#
# A painter has come to Cornwall for the famous light of the region's afternoons... [The Surrealist Painter provides <sprite name=grail>, <sprite name=moth>, and <sprite name=rose> assistance. Talk to her before she leaves if you want to use her services.].""",
passing_by_a_surrealist_painter = card_type("passing_by_a_surrealist_painter",
    attributes(employable=1, fee=24),
)

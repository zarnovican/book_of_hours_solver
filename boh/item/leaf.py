from ..item import beverage, memory
from ..model import attributes, card_type


# C&H Second Flush Assam  (Packet)
#
# Tea from the land of the <i>real</i> unicorn, imported by Cater & Hero.
# ---
# Scrutiny
#
# A wonderfully full-bodied taste, bright as morning.
ch_second_flush_assam_packet = card_type("ch_second_flush_assam_packet",
    attributes(edge=1, knock=1, lantern=1, thing=1, leaf=1, brewable=1),
    brew_into = beverage.ch_second_flush_assam_pot,
    consider_output = memory.scent,
)


# Potted Avidity
#
# A lush and hungry ornament.
# ---
# Scrutiny
#
# Concerning.
potted_avidity = card_type("potted_avidity",
    attributes(grail=2, nectar=1, thing=1, leaf=1),
    consider_output = memory.scent,
)


# Potted Bamboo
#
# Water it, and you can almost hear it growing.
# ---
# Scrutiny
#
# Lush.
potted_bamboo = card_type("potted_bamboo",
    attributes(nectar=1, thing=1, leaf=1),
    consider_output = memory.scent,
)


# Potted Dragon Tree
#
# A determined, spiky little survivor.
# ---
# Scrutiny
#
# (Ow.)
potted_dragon_tree = card_type("potted_dragon_tree",
    attributes(scale=1, thing=1, leaf=1),
    consider_output = memory.touch,
)


# Potted Fern
#
# A pleasantly primitive plant.
# ---
# Scrutiny
#
# A faint mist of spores rises…
potted_fern = card_type("potted_fern",
    attributes(nectar=2, thing=1, leaf=1),
    consider_output = memory.touch,
)

# Potted Monstera
#
# A defiant plant.
# ---
# Scrutiny
#
# Beware?
potted_monstera = card_type("potted_monstera",
    attributes(nectar=1, thing=1, leaf=1),
    consider_output = memory.touch,
)


# Potted Snake Plant
#
# A sturdy sun-loving relic from a warmer place.
# ---
# Scrutiny
#
# Lush.
potted_snake_plant = card_type("potted_snake_plant",
    attributes(scale=1, thing=1, leaf=1),
    consider_output = memory.sight,
)


# Tiny Potted Tree
#
# Tiny as a ship in a bottle.
# ---
# Scrutiny
#
# Adorable.
tiny_potted_tree = card_type("tiny_potted_tree",
    attributes(nectar=1, thing=1, leaf=1),
    consider_output = memory.scent,
)


# Vase of Gorse
#
# As Cornish a plant as any.
# ---
# Scrutiny
#
# (Ow.)
vase_of_gorse = card_type("vase_of_gorse",
    attributes(forge=1, nectar=1, thing=1, leaf=1),
    consider_output = memory.touch,
)


# Vase of Rushes
#
# A subtle ornament.
# ---
# Scrutiny
#
# Charming.
vase_of_rushes = card_type("vase_of_rushes",
    attributes(moon=1, nectar=1, thing=1, leaf=1),
    consider_output = memory.sight,
)


# Veiled Goddess Lapsang Souchong (Packet)
#
# Named for an enigmatic minor deity whose charge is the healing of burns.
# ---
# Scrutiny
#
# Smoky and astringent, like pine-scented dragon's breath.
veiled_goddess_lapsang_souchong_packet = card_type("veiled_goddess_lapsang_souchong_packet",
    attributes(forge=1, sky=1, thing=1, leaf=1, brewable=1),
    brew_into = beverage.veiled_goddess_lapsang_souchong_pot,
    consider_output = memory.taste,
)

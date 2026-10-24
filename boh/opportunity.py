from .item import memory
from .model import attributes, card_type, condition, opportunity


# Art: It's Educational!!
#
# Possible inspiration from a relevant painting, or other Wall Art
opportunity.register_opportunity("art_its_educational", condition(wall_art=1))


# Awen
#
# Divine inspiration? Or just the right breath of air at the right moment? [This mood increases certain aspects.]
opportunity.register_mood("awen", memory.awen)


# Comfort: Relevant Furniture
#
# Possible inspiration from relevant furniture, or other Comforts.
opportunity.register_opportunity("comfort_relevant_furniture", condition(comfort=1))


# Duende
#
# 'The duende is a force not a labour, a struggle not a thought. - Lorca [This mood increases certain aspects.]
opportunity.register_mood("duende", memory.duende)


# Epiphany
#
# 'It was for the man of letters to record these epiphanies with extreme care, seeing that they themselves are the most delicate and evanescent of moments.' - Joyce [This mood increases certain aspects.]
opportunity.register_mood("epiphany", memory.epiphany)


# Extra Effort: Soul
#
# An opportunity to add a Soul Element. [Beware: failure might cause Maladies.]
opportunity.register_opportunity("extra_effort_soul", condition(soul=1))


# Only Connect: Memory
#
# An opportunity to add a Memory - which will be used up.
opportunity.register_opportunity("only_connect_memory", condition(memory=1))


# Stuff: also Things
#
# Possible inspiration from a relevant Thing.
opportunity.register_opportunity("stuff_also_things", condition(thing=1))


# The Right Skies: Weather
#
# An opportunity to use a Weather card.
opportunity.register_opportunity("the_right_skies_weather", condition(weather=1))


# 'Ubi Sunt'?
#
# 'Where are my kindred? Where is the giver of treasure? Where are the benches to bear us? Joys of the hall to bring us together?' [This mood increases certain aspects.]
opportunity.register_mood("ubi_sunt", memory.ubi_sunt)

from ..item import memory
from ..model import attributes, card_type, condition, talking


speak_to_an_assistant = (
    # Speak to an Assistant
    #
    # I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.]
    # ---
    # Speak to an Assistant
    #
    # I've learnt something - or perhaps just remembered it.
    ( memory.gossip,            24 ),
    ( memory.solace,            18 ),
    ( memory.a_stolen_secret,    6 ),
    ( memory.fear,               6 ),
    ( memory.foresight,          6 ),
    ( memory.hindsight,          6 ),
    ( memory.impulse,            6 ),
    ( memory.intuition,          6 ),
    ( memory.regret,             6 ),
    ( memory.revelation,         6 ),
    ( memory.satisfaction,       6 ),
    ( memory.storm,              6 ),
)


# Barber's Assistance
#
# The itinerant barbers of the south country will keep you clean and kempt, make sure you don't miss out on any news or gossip, and arrange matters so you aren't too troubled by vermin. Snip snip.
barber = card_type("barber",
    attributes(moth=2, rose=1, assistance=1, an_introduction=1),
)
talking.register(barber, output=speak_to_an_assistant)


# Blacksmith's Assistance
#
# Denzil the blacksmith will lend me his strength for the day. [Make use of the Blacksmith's help before dawn.]
blacksmith = card_type("blacksmith",
    attributes(edge=2, forge=2, assistance=1, an_introduction=1),
    unique_collabotation = condition(metal=1),
)
talking.register(blacksmith, output = (
    # Speak to Denzil
    #
    # He might even reply. [Add something to enhance Denzil's effectiveness for the day, or just talk. Unlike some assistants, Denzil can make use of Metal.]
    # ---
    # Speak to Denzil
    #
    # He does a lot with silence, this man.
    ( memory.fear,              21 ),
    ( memory.foresight,         21 ),
    ( memory.hindsight,         21 ),
    ( memory.a_stolen_secret,    5 ),
    ( memory.impulse,            5 ),
    ( memory.intuition,          5 ),
    ( memory.regret,             5 ),
    ( memory.revelation,         5 ),
    ( memory.solace,             5 ),
    ( memory.storm,              5 ),
))


# Coffinmaker's Assistance
#
# A tamer of trees, a worker of woods, a consigner of cadavers. He has also been known to try his hand, very diffidently, at poetry. [Make use of the Coffinmaker's help before dawn.]
coffinmaker = card_type("coffinmaker",
    attributes(sky=1, winter=2, assistance=1, an_introduction=1),
    unique_collabotation = condition(wood=1),
)
talking.register(coffinmaker, output = (
    ( memory.foresight,         24 ),
    ( memory.gossip,            24 ),
    ( memory.a_stolen_secret,    6 ),
    ( memory.fear,               6 ),
    ( memory.hindsight,          6 ),
    ( memory.impulse,            6 ),
    ( memory.intuition,          6 ),
    ( memory.regret,             6 ),
    ( memory.revelation,         6 ),
    ( memory.solace,             6 ),
    ( memory.storm,              6 ),
))


# Consulting Engineer's Assistance
#
# A consulting engineer can find plenty of work in the mines and towns of the region. But Hush House represents an unusual and interesting challenge.
consulting_engineer = card_type("consulting_engineer",
    attributes(forge=4, lantern=4, sky=4, assistance=1, an_introduction=1, fee=24),
    unique_collabotation = condition(fuel=1),
)
talking.register(consulting_engineer, output=speak_to_an_assistant)


# Elegiac Poet's Assistance
#
# Poets, they say, never do the washing up. This one hasn't brushed his hair either. But he has his uses and his talents.
elegiac_poet = card_type("elegiac_poet",
    attributes(moth=4, sky=4, winter=4, assistance=1, an_introduction=1, fee=24),
    unique_collabotation = condition(flower=1),
)
talking.register(elegiac_poet, output=speak_to_an_assistant)


# Fisherman's Assistance
#
# Fishermen in this part of the world have a reputation as smugglers, and worse than smugglers. Those days are past, mostly, and mostly they just catch pilchards now. But they still remember the words spoken in silence to the Moon and the Sea.
fisherman = card_type("fisherman",
    attributes(moon=2, sky=1, assistance=1, an_introduction=1),
)
talking.register(fisherman, output=speak_to_an_assistant)


# Fisherman's Assistance
#
# A fisherman from Brancrug village! He can guide me up the cliff path - if he trusts me. [The Aspects below tell you more about how and where you can use this card. Mouse over them to learn more - or to see what other things also have these Aspects.]
fisherman_reluctant = card_type("fisherman_reluctant",
    attributes(moon=1, sky=1, assistance=1, reluctant=1),
)


# Fisherman's Assistance
#
# A fisherman from Brancrug village! He can guide me up the cliff path - if he trusts me. [The Aspects below tell you more about how and where you can use this card. Mouse over them to learn more - or to see what other things also have these Aspects.]
fisherman_sceptical = card_type("fisherman_sceptical",
    attributes(moon=1, sky=1, sceptical=1, assistance=1, reluctant=1),
)


# Fugitive's Assistance
#
# 'Hold your noise!' called a terrible voice, as a man started up from among the graves at the side of the church porch. [...] A fearful man, all in coarse grey, with a great iron on his leg. A man with no hat, and with broken shoes, and with an old rag tied around his head.' - Dickens
fugitive = card_type("fugitive",
    attributes(edge=4, heart=4, scale=4, assistance=1, an_introduction=1, fee=24),
)
talking.register(fugitive, output=speak_to_an_assistant)


# Midwife's Assistance
#
# As somber as autumn, as kind as autumn. She also likes her beer. [Make use of the Midwife's help before dawn.]
midwife = card_type("midwife",
    attributes(grail=2, heart=1, assistance=1, an_introduction=1),
    unique_collabotation = condition(fabric_and_fibre=1),
)
talking.register(midwife, output = (
    # Talk to Mrs Kille
    #
    # Mrs Kille has seen more of the world than she usually lets on. Conversations with her yield the occasional surprise. [Add something to enhance Mrs Kille's effectiveness for the day, or just talk. Unlike some assistants, Mrs Kille can make use of Fabric.]""",
    # ---
    # Talk to Mrs Kille
    #
    # 'There tis, and can't be no tizzer.' Mrs Kille, as every local gossip knows, came from France to marry Mr Kille. But there's scant trace of the Continent in her accent now.""",
    ( memory.gossip,            17 ),
    ( memory.regret,            17 ),
    ( memory.satisfaction,      17 ),
    ( memory.solace,            17 ),
    ( memory.a_stolen_secret,    4 ),
    ( memory.fear,               4 ),
    ( memory.foresight,          4 ),
    ( memory.hindsight,          4 ),
    ( memory.impulse,            4 ),
    ( memory.intuition,          4 ),
    ( memory.revelation,         4 ),
    ( memory.storm,              4 ),
))


# Miner's Assistance
#
# 'Thus they more or less ruled themselves, with the help of their wild Celtic temperament, made wilder by the hardness of their lives and the truly ghastly conditions under which they worked [...] with all this it is not to be wondered that the tinners acquired the reputation of being scarcely human. But it must be remembered that among them at all times were those whose characters could stand comparison with the best of men.' - L. Russell Muirhead
miner = card_type("miner",
    attributes(forge=1, moon=1, scale=2, assistance=1, an_introduction=1),
)
talking.register(miner, output=speak_to_an_assistant)


# Nun's Assistance
#
# The Sisters of the Triple Knot are long gone from this corner of the world... aren't they?
nun = card_type("nun",
    attributes(grail=4, knock=4, moon=4, assistance=1, an_introduction=1, fee=24),
    unique_collabotation = condition(omen=1),
)
talking.register(nun, output=speak_to_an_assistant)


# Orchard-Keeper's Assistance
#
# 'In Cornwall, it is quite possible to take a stride from the richest vegetation into the abomination of desolation. It has been said in mockery that Cornwall does not grow wood enough to make coffins for the people.' - Sabine Baring-Gould
orchard_keeper = card_type("orchard_keeper",
    attributes(heart=1, nectar=2, assistance=1, an_introduction=1),
)
talking.register(orchard_keeper, output=speak_to_an_assistant)


# Rector's Assistance
#
# Reverend Timothy, Rector of Brancrug, ordained by the Church of the Unconquered Sun. A learned man, blessed in the Tally, the Gate, and the Light. [Make use of the Rector's help before dawn.]
rector = card_type("rector",
    attributes(knock=1, lantern=2, assistance=1, an_introduction=1),
    unique_collabotation = condition(candle=1),
)
talking.register(rector, output = (
    # Speak with Reverend Timothy
    #
    # Reverend Timothy is always, always happy to chat. [Add an Element of the Soul to enhance Reverend Timothy's effectiveness for the day, or just talk. Unlike some assistants, Timothy can make use of Candles.]
    # ---
    # Speak with Reverend Timothy
    #
    # I don't need to listen to everything Reverend Timothy says. He doesn't really even expect me to. But I'm often glad when I do.
    ( memory.gossip,            17 ),
    ( memory.hindsight,         17 ),
    ( memory.revelation,        17 ),
    ( memory.solace,            17 ),
    ( memory.a_stolen_secret,    4 ),
    ( memory.fear,               4 ),
    ( memory.foresight,          4 ),
    ( memory.impulse,            4 ),
    ( memory.intuition,          4 ),
    ( memory.regret,             4 ),
    ( memory.storm,              4 ),
))


# Surrealist Painter's Assistance
#
# What painter worth their pigments wouldn't want to spend a day at Hush House?
surrealist_painter = card_type("surrealist_painter",
    attributes(grail=4, moth=4, rose=4, assistance=1, an_introduction=1, fee=24),
    unique_collabotation = condition(pigment=1),
)
talking.register(surrealist_painter, output=speak_to_an_assistant)


# Travelling Musician's Assistance
#
# 'I'm just some irritating, lying, ginger kid from Cornwall who should have been locked up [...] I just managed to escape and blag it into music.' - Richard James
travelling_musician = card_type("travelling_musician",
    attributes(nectar=4, rose=4, sky=4, assistance=1, an_introduction=1, fee=24),
)
talking.register(travelling_musician, output=speak_to_an_assistant)

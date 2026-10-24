from ..model import attributes, card_type


# An Old Friend's Address
#
# Denzil is the blacksmith of Brancrug Village. I remember him from the War. If he remembers me, I can find shelter beneath his roof - <b>once I've reached Brancrug Village</b>.""",
blacksmith = card_type("blacksmith",
    attributes(forge=1, an_introduction=1),
)

# An Old Friend's Address
#
# Mr Kille is the coffinmaker of Brancrug Village. I once wrote kindly of his poetry. His home is always open to me (though he's asked me never to mention poetry in front of Mrs Kille). I can find shelter for tonight under their roof - <b>once I've reached Brancrug Village</b>. """,
mr_kille = card_type("mr_kille",
    attributes(winter=1, an_introduction=1),
)

# An Old Friend's Address
#
# Mrs Kille is the handywoman - the midwife - of Brancrug village. I knew her long ago in Paris, when her surname was not 'Kille' but 'Raveline', and her sister was a viscountess. Her home is always open to me (though she's asked me not to bring up the title thing when Mr Kille's around).  I can find shelter for tonight under their roof  - <b>once I've reached Brancrug Village</b>. """,
mrs_kille = card_type("mrs_kille",
    attributes(grail=1, an_introduction=1),
)

# An Old Friend's Address
#
# I first heard of Brancrug through its Rector, Reverend Timothy. For years now I've been exchanging letters with him. I can find shelter for tonight under his roof - <b>once I've reached Brancrug Village</b>. [The Rector can also introduce you to other villagers.]""",
rector = card_type("rector",
    attributes(lantern=1, an_introduction=1),
)

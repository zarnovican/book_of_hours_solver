from ..model import attributes, card_type


# A Matter of Counterfeit Memory
#
# In Numa, visitors will be concerned with the tricks and strategems that might have been used in secret by the Hours. [As long as this card remains, Numatic visitors will have an interest in <sprite name=moon> Mysteries. Their needs will usually be more exacting than visitors who come during more traditional seasons.]
a_matter_of_counterfeit_memory = card_type("a_matter_of_counterfeit_memory",
    attributes(relevance_moon=1, from_numa=1, incident=1),
)


# A Matter of Knot and Tangle
#
# In Numa, visitors will be concerned with the Hours honoured by the Sisterhood of the Knot. [As long as this card remains, Numatic visitors will have an interest in <sprite name=grail> or <sprite name=nectar> Mysteries. Their needs will usually be more exacting than visitors who come during more traditional seasons.]
a_matter_of_knot_and_tangle = card_type("a_matter_of_knot_and_tangle",
    attributes(relevance_grail=1, relevance_nectar=1, from_numa=1, incident=1),
)


# A Matter of the Feasting Few
#
# In Numa, visitors will be concerned with questions of appetite, of blood, and of their attendant dangers. [Numatic visitors will have an interest in <sprite name=grail> Mysteries. Their needs will usually be more exacting than visitors who come during more traditional seasons.]
a_matter_of_the_feasting_few = card_type("a_matter_of_the_feasting_few",
    attributes(relevance_grail=1, from_numa=1, incident=1),
)


# The Affair of the Grunewald Provision
#
# After the dissolution of Grunewald's Permanent Circus, its assets were disposed of by the Bureau. That was during one of the Bureau's occasional funding crises, and the 'Grunewald Provision' sanctioned the sale of the Circus' assets for cash, bypassing some of the usual checks for oneiric hazard. In hindsight, this has started to look like a mistake. [Visitors with an interest in <sprite name=heart> or <sprite name=winter> Mysteries will want to talk about this.]
the_affair_of_the_grunewald_provision = card_type("the_affair_of_the_grunewald_provision",
    attributes(heart=1, winter=1, incident=1),
)


# The Affair of the Oriflamme Heist
#
# Oriflamme's Auction House is never robbed. But what if it has been? What if, somehow, priceless treasures have been replaced with pricey forgeries? How could we even be sure? [Visitors with an interest in <sprite name=knock> or <sprite name=forge> Mysteries will want to talk about this.]
the_affair_of_the_oriflamme_heist = card_type("the_affair_of_the_oriflamme_heist",
    attributes(forge=1, knock=1, incident=1),
)


# The Affair of the Other Horizon
#
# Sailors have a term for the compass-whirl phenomenon which occurs before sightings of the city Ys. They say a compass has caught 'the giddy horizons'. There is something of a giddy epidemic in the North Sea this year. [Visitors with an interest in <sprite name=rose> Mysteries will want to talk about this.]
the_affair_of_the_other_horizon = card_type("the_affair_of_the_other_horizon",
    attributes(rose=1, incident=1),
)


# The Affair of the Rising While
#
# Across the inner sea, across the desert sands, someone styling herself the Oracle of the Rising While has set up a tent-town where she preaches 'the truth of nearly now' to her followers. This would be of no obvious interest to the students of the invisible arts... except that although she has pitched her tents in the shadow of the Temple of Seven Coils, nothing appears to have eaten anyone. [Visitors with an interest in <sprite name=moon> or <sprite name=scale> Mysteries will want to talk about this.]
the_affair_of_the_rising_while = card_type("the_affair_of_the_rising_while",
    attributes(moon=1, scale=1, incident=1),
)


# The Affair of the Royal Endeavour
#
# The New King has sanctioned the use of the Crown's wealth to fund a visionary new industrial project - one that will transform our economy, and furnish the kingdom with a sense of patriotic mission. Parliament, dazzled, has already passed the Royal Endeavour Act, mandating the construction of the necessary facilities, although the details remain in some respects vague. [Visitors with an interest in <sprite name=forge> or <sprite name=lantern> Mysteries will want to talk about this.]
# ---
# (Mme Olympe Bechet)
# On the Royal Endeavour
#
# 'This Royal Endeavour. I wonder what you think. No, don't tell me! I don't want us to get in trouble - either of us.' [Try a book with as much Mystery: <sprite name=forge> as their <sprite name=forge> Interest.]
# ---
# On the Royal Endeavour
#
# 'No, I am no believer. But my mother, she believed; and she used to talk of the Second Dawn. Of course I did not take it seriously. But now the King's project. So strange. I would like to see what I can find in your collection...' [Try a book with as much Mystery: <sprite name=forge> as their <sprite name=forge> Interest.]
# ---
# On the Royal Endeavour
#
# 'Truly it might mean a Second Dawn. Or a war. I would prefer the Dawn. But then it might be both… thank you, Librarian. Keep my visit between us two only, for now, if you don't mind.'
# ---
# (Magister Hokobald)
# On the Royal Endeavour
#
# 'You are aware what the King is at? I suppose it will do well enough.' [Try a book with as much Mystery: <sprite name=forge> as their <sprite name=forge> Interest.]
# ---
# On the Royal Endeavour
#
# 'I have a general idea of what the Royal Endeavour entails, of course, but I would like to refresh my understanding of a few minor details.' [Try a book with as much Mystery: <sprite name=forge> as their <sprite name=forge> Interest.]
# ---
# On the Royal Endeavour
#
# 'Yes, this has been quite satisfactory, especially considering the sad state of affairs which persists in this House. I make no complaint; good day.'
# ---
# (Lt Arthur Thomas Moore (Ret.))
# On the Royal Endeavour
#
# 'I abandoned the Empire's service long ago. That was not an easy choice. But some ties, I find even harder to loose.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'My blood - the son of my nephew - is bound up somehow with the New King's Endeavour. My family and I have parted ways and I will not remind them of the shame of my desertion. But I cannot rest until I understand this business better.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'What is happening here - I think it is no more perilous than any line in the Sun's Plan. And it is much grander. We all make our choices - my choice, now, is to be proud of my kin and his part in the work. Thank you, Librarian. I hope that you will keep this matter between us alone.'
# ---
# (Sr. Corso Reverte)
# On the Royal Endeavour
#
# 'The New King's got a lot of Continental powers nervous, Librarian. So a friend of a friend has asked me to drop by and do a little reassuring research.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'I'm not a <i>spy</i>. Spies don't go to libraries. Just a paid researcher. Doing my bit for world peace. Mind if I take a look around?' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'I'll be honest, Librarian, I don’t think anything I've found will reassure our foreign friends. Well, if they don't start a war, I won't either. Good luck with your New King.'
# ---
# (DI Douglas Moore)
# On the Royal Endeavour
#
# 'Detective-Illuminate Douglas Moore, on special assignment to the High Executive for the Royal Endeavour. Get me. 'Ope you're impressed.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'Anyone builds something important, there's always someone trying to break into it or blow it up. That's the job. Funny to see a pack of <i>vicars</i> getting involved with something like that, though. Spose it's what they call 'doctrinal differences'. Here to look into that.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'Thanks for that. Got a much better idea of who might need arresting. Mrs M's going to like that. No time at all for the Church, Mrs M. Proper freethinker. 'Never mind all them poor mediums,' says she, 'lock up a bishop or two, save all that money on silly hats.' Told her once if we locked people up for spending too much on millinery, she'd need to watch out. Had to eat my dinner in the garden shed that evening. Anyway, ta ta.'
# ---
# (Mr Fraser Strathcoyne)
# On the Royal Endeavour
#
# 'The High Executive for the Royal Endeavour has approached me for assistance with some of their more esoteric requirements…' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'I can provide what they need. But some of their requests have piqued my curiosity. I would like to refresh my memory on the, hm, 'solar context'.' [Try a book with as much Mystery:  <sprite name=lantern> as their <sprite name=lantern> Interest.]
# ---
# On the Royal Endeavour
#
# 'Battleships; aerostats; locomotives. What do all these things have in common, Librarian? I'll tell you: names. Thank you. Good day.'
# ---
# (Dr Serena Blackwood)
# On the Royal Endeavour
#
# 'The New King… I have some concerns. I am certain it is a coincidence that he came to the throne so soon after the fire here at the House. An unlucky time. But it's a coincidence I have always disliked.' [Try a book with as much Mystery: <sprite name=forge> or Mystery: <sprite name=lantern> as their matching Interest.]
# ---
# On the Royal Endeavour
#
# 'I hope I might find something in the collection here to allay my concerns. Or to crystallise them.' [Try a book with as much Mystery: <sprite name=forge> or Mystery: <sprite name=lantern> as their matching Interest.]
# ---
# On the Royal Endeavour
#
# 'My concerns remain. This is a Solar project, no doubt of it. Everything is doctrinally acceptable… everything goes back to Light… but this sunset business. You know, I have always believed the Chandler to be Sunset Celia's. No, it shouldn't be possible, but the Chandler shouldn't be possible either. Keep this to yourself. Thank you.'
the_affair_of_the_royal_endeavour = card_type("the_affair_of_the_royal_endeavour",
    attributes(forge=1, lantern=1, incident=1),
)


# The Affair of the Sandalwood Saint
#
# An odd little image in a church in Strasbourg has become a locus for wild claims of healing and haunting. When it comes to the attention of the Church hierarchy, they'll rule it miraculous or heretical… unless someone takes a hand before then. [Visitors with an interest in <sprite name=nectar> or <sprite name=scale> Mysteries will want to talk about this.]
the_affair_of_the_sandalwood_saint = card_type("the_affair_of_the_sandalwood_saint",
    attributes(nectar=1, scale=1, incident=1),
)


# The Affair of the Second Skin
#
# Immortals change more slowly than most of us - but even immortals change sometimes. In the city of Marrakech, the labhite Abecassis has begun a dramatic and dangerous metamorphosis - one that's alarming friends and enemies alike… [Visitors with an interest in <sprite name=edge> or <sprite name=scale> Mysteries will want to talk about this.]
the_affair_of_the_second_skin = card_type("the_affair_of_the_second_skin",
    attributes(edge=1, scale=1, incident=1),
)


# The Affair of the Unfettered Eye
#
# Messana: a prosperous little desert village that has become, in recent years, a place of pilgrimage. There have been peculiar manifestations there of late - villagers gifted with sight, or struck blind. The Church has despatched its representatives to investigate. [Visitors with an interest in <sprite name=lantern> Mysteries will want to talk about this.]
the_affair_of_the_unfettered_eye = card_type("the_affair_of_the_unfettered_eye",
    attributes(lantern=1, incident=1),
)


# The Affair of the Forgivable Debt
#
# Like many criminal enterprises, Reckoners offer loans to the desperate and unwary - but Reckoners can offer loans not only of cash, but of allotted years of life. They usually keep a low profile, but now two Reckoner mobs have gone to war in the unremarkable Lithuanian city of Kaunas. Why? What's in Kaunas? [Visitors with an interest in <sprite name=moon> or <sprite name=edge> Mysteries will want to talk about this.]
the_affair_of_the_forgivable_debt = card_type("the_affair_of_the_forgivable_debt",
    attributes(incident=1),
    #attributes(relevance_edge=1, relevance_moon=1, incident=1), # TODO (wish) relevance_ attributes not mapped
)

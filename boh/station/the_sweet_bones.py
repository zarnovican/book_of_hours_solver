from ..item import assistance, journal, soul, thing
from ..model import attributes, condition, season, simple_action, simple_output, slot, station


# unlock inn with 12p
(
    """A Wary Welcome at the Inn

In the time of the Heptarchy, a ring-giver was accounted generous. In this bright and civilised century, a beer-buyer enjoys the same regard.""",
    """A Wary Welcome at the Inn

I bought a round for everyone. And another. And one more for luck. And thus was I accounted 'not so bad for a foreigner'. I'll find a warmer welcome here next time.""",
)

# unlock inn with rector
(
    """Introductions

I haven't come alone. Reverend Timothy's presence demands respect.""",
    """Introductions

Eventually, the other patrons unbend enough to let me buy them a pint, and let me listen to them complain about the weather. I'll find a warmer welcome here next time.""",
)


# journal.a_drowned_book_fet_phost
(
    """Dry Out a Book

The clock ticks in the snug; a distant wireless crackles musically; carefully, page by page, I dry the book.""",
)


# (soul.fet | soul.trist -> 2p)
#
# Fortune-Telling
#
# <sprite name=moth> I've garnered enough mystique to tell fortunes for pennies. Undignified, perhaps, for the Librarian of Hush House, but times are hard. [Or add a coin to find visitors seeking employment.]
# Fortune-Telling
#
# The fortunes I tell may be true, and they may be real. The money, at least, is real.


# (soul.phost | soul.wist -> 6p)
#
# Help with Letters
#
# <sprite name=lantern> I could offer help with correspondence and arithmetic. There's no school in Brancrug, and not everyone here knows their letters. [Or add a coin to find visitors seeking employment.]
# ---
# Help with Letters
#
#An afternoon spent profitably, reading newspapers to the curious, writing affectionate letters for the lonely, steering farmers through the requirements of the Ministry of Agriculture.


# (soul.ereb -> memory.fear | memory.gossip | ..)
#
# A Little Respect
#
# <sprite name=edge> I am the Librarian of Hush House. I will question the villagers of Brancrug, and I will add whatever they tell me to my store of knowledge. [Or add a coin to find visitors seeking employment.]
# ---
# A Little Respect
#
# I've learnt something. Something useful? Too early to tell.


# (soul.mettle | soul.shapt -> 6p)
#
# Fixing and Mending
#
# <sprite name=forge> There's not much work on offer in Brancrug, but I can find sixpence worth of odd jobs. [Or add a coin to find visitors seeking employment.]
# ---
# Fixing and Mending
#
# As they used to say in my youth, 'The day is done, and so am I; but I've earned my pay.'


# (soul.chor | soul.health -> 6p)
#
# Manual Labour
#
# <sprite name=heart> There's not much work on offer in Brancrug, but I can find sixpence worth of odd jobs. [Or add a coin to find visitors seeking employment.] 
# ---
# Manual Labour
#
# As they used to say in my youth, 'The day is done, and so am I; but I've earned my pay.'


# fatigued soul + 0p
(
    """Rest and Refreshment

Tuppence will buy me a hearty meal and a quiet place where I can rest and gather my thoughts.""",
    """Rest and Refreshment

No tuppence, no beer.""",
)


# fatigued soul + 2p (spring)
(
    """Rest and Refreshment

Tuppence will buy me a hearty meal and a quiet place where I can rest and gather my thoughts.""",
    """Rest and Refreshment: Spring

It is Spring; and the landlady has served me a slice of her starygazy pie, with the pilchard-heads poking cheekily through the hot crust.""",
    """Rest and Refreshment: Spring

Better now.""",
)


# fatigued soul + 2p (summer)
(
    """Rest and Refreshment

Tuppence will buy me a hearty meal and a quiet place where I can rest and gather my thoughts.""",
    """Rest and Refreshment: Summer

It is Summer; I am sitting on the bench outside the Sweet Bones, eating crumbly cheese in nettle wrappings and good black rye bread, soaking up the sun.""",
    """Rest and Refreshment: Summer

Better now.""",
)


# fatigued soul + 2p (autumn)
(
    """Rest and Refreshment

Tuppence will buy me a hearty meal and a quiet place where I can rest and gather my thoughts.""",
    """Rest and Refreshment: Autumn

It is Autumn when the leaves rustle. The silent landlady has served me apple pie with steamed cream in the window-nook.""",
    """Rest and Refreshment: Autumn

Better now.""",
)


# fatigued soul + 2p (winter)
(
    """Rest and Refreshment

Tuppence will buy me a hearty meal and a quiet place where I can rest and gather my thoughts.""",
    """Rest and Refreshment: Winter

It is Winter and the storms have tightened the seas. I am sitting before the fire in the Sweet Bones with a beef and potato pasty in one hand, and a hot ale posset in the other.""",
    """Rest and Refreshment: Winter

Better now.""",
)


# (fatigued soul + 2p, in numa)
#
# The Refreshments of the Labyrinth Season
#
# The inn is crowded with Numa's heralds and pilgrims. Their meat is unfamiliar; their drink is unknown. As I linger at the window, an electric bulb flares like a marsh-light: a guest raises her glinting eyes and sees me. She beckons me in with a gloved hand.
# ---
# The Refreshments of the Labyrinth Season
#
# I have eaten, I have drunk. A cloying taste lingers. My lips are stained with grey.


# (soul, in numa)
#
# Uncanny Labours
#
# The inn is crowded with Numa's heralds and pilgrims. They will be gone by morning. Until then, I could offer my services for payment. I might regret it.
# ---
# Uncanny Labours
#
# Afterwards I don't remember what work I performed, except in scents and sensations - leaf-mould, a rhythmic musical clicking like melodious castanets, soft blue flame like antique gaslight. And cold; I remember that where we went, it was cold.


# basket_of_dirty_laundry + 12p
(
    """Have Something Cleaned at the Sweet Bones

For a shilling, the Sweet Bones will take care of my laundry...""",
    """Have Something Cleaned at the Sweet Bones

The Sweet Bones is taking care of my laundry.""",
    """Have Something Cleaned at the Sweet Bones

Fresh, clean, dry.""",
)


# The Sweet Bones [Locked]
#
# After the Restoration of 1930, the New King's agents came looking for his enemies in these parts... and they weren't gentle about it. Since those days, the locals are suspicious of foreigners. No-one in the Sweet Bones will talk to me.""",
# ---
# The 'Sweet Bones'
#
# The 'Sweet Bones' has been the public house in Brancrug since Cromwell's time. Its history is notable; its beer is not. Guests looking for discreet employment, or for discreet assistance, congregate in the snug.
the_sweet_bones = station("the_sweet_bones", attributes(),

    simple_actions = (

        # Seek Unusual Help
        #
        # What visitors might be passing through? [Find out what unusual passersby might be looking for employment.]
        # ---
        # Seek Unusual Help
        #
        # Here's an opportunity.
        simple_action("seek_unusual_help",
            output = (
                simple_output( assistance.consulting_engineer, probability=20 ),
                simple_output( assistance.elegiac_poet,        probability=20 ),
                simple_output( assistance.fugitive,            probability=10 ),
                simple_output( assistance.nun,                 probability=10 ),
                simple_output( assistance.surrealist_painter,  probability=20 ),
                simple_output( assistance.travelling_musician, probability=20 ),
            ),
            pennies = 24,
            slots = (
                slot(
                    required=condition(soul=1),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),

        simple_action("assistance_from",
            output = (
                # Assistance from a Travelling Barber
                #
                # In summer, the barber comes by to keep the villagers kempt. A shilling will buy his services. [Barbers offer <sprite name=moth> and a little <sprite name=rose>. Alternatively, add a Soul card to find any rarer guests who might be seeking employment...]""",
                simple_output( assistance.barber,         season=season.summer ),

                # Assistance from a Fisherman
                #
                # In winter when the storms close the seas, the fishermen will offer their services for a shilling a day. [Fishermen will offer <sprite name=moon> and a little <sprite name=sky>. Alternatively, add a Soul card to find any rarer guests who might be seeking employment...]""",
                simple_output( assistance.fisherman,      season=season.winter ),

                # Assistance from a Miner
                #
                # In spring, the local miners often travel to the Feast of Lights Below. If one breaks his journey at the Sweet Bones, a shilling will buy his labour for a day. [Miners offer <sprite name=scale>, <sprite name=forge>, and a little <sprite name=moon>. Alternatively, add a Soul card to find any rarer guests who might be seeking employment...]""",
                simple_output( assistance.miner,          season=season.spring ),

                # Assistance from an Orchard-Keeper
                #
                # In autumn, the orchard-keepers come to sell their wares at Brancrug. A shilling will buy one's help. [Orchard-keepers offer <sprite name=nectar> and a little <sprite name=heart>. Alternatively, add a Soul card to find any rarer guests who might be seeking employment...]""",
                simple_output( assistance.orchard_keeper, season=season.autumn ),
            ),
            pennies = 12,
            slots = (),
        ),
    ),

    slots = (
        slot(
            required=condition(soul=1),
            forbidden=condition(malady=1),
        ),
        slot(
            required=condition(pence=1, soiled=1, soaked=1),
        ),
    ),
)

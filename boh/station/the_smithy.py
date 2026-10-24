from ..item import assistance, journal, tally
from ..model import attributes, condition, simple_action, simple_output, slot, station


# unlock with miner
(
    """A Firelit Doorway

A mutual acquaintance will introduce me to Denzil the Smith. I might get six or even ten words out of him if I'm patient.""",
    """A Firelit Doorway

Denzil is a surprising source of practical advice. [The Smithy is now available.]""",
)


# soul + soaked journal
(
    """Speak with Denzil

Denzil will talk about practical matters, though he prefers to sit in silence. A shilling will buy his help for a day. [If you give him occult coinage, he will perform the Service of Division instead.]""",
    """Dry Out a Book

Denzil watches with grave interest as I dry the book in the warmth of his forge-fire. He provides wads of cotton to put between the pages, but otherwise he keeps his distance. He is wary of the written word. I am beginning to suspect he cannot read. I do not expect he will ever tell me.""",
)


# soul + bronze spintria -> 2x iron spintria
(
    """Speak with Denzil

Denzil will talk about practical matters, though he prefers to sit in silence. A shilling will buy his help for a day. [If you give him occult coinage, he will perform the Service of Division instead.]""",
    """Divide Bronze

Since the time of the Curia, the smiths of Brancrug have performed 'the service of division' for them. [This will break your spintria into more manageable coinage.]""",
    """Divide Bronze

Denzil ushers me silently from the room while he does his work. I do not hear the sound of his hammer; perhaps he only keeps a secret cache of spintria. But when he comes out to hand me the coins, they are almost too hot to touch.""",
)


# soul + iron spintria -> nothing
(
    """Speak with Denzil

Denzil will talk about practical matters, though he prefers to sit in silence. A shilling will buy his help for a day. [If you give him occult coinage, he will perform the Service of Division instead.]""",
    """'Iron is Iron'

Since the time of the Curia, the smiths of Brancrug have performed 'the service of division' for the Librarian. But Denzil only shakes his head. 'Iron is iron,' is all he says.""",
)


# The Smithy [Locked]
#
# Denzil Smith has more work than he needs, and he rarely opens his door to strangers.
# [You need an Introduction, or a mutual acquaintance marked with Edge, Forge, or Heart - someone in a similar trade, or someone who can appeal to his secret passion for saffron cake.]""",
# ---
# The Smithy
#
# Denzil Smith, strong as oak, blackened by smoke. He will never surpass his father, and he is no longer a soldier. But he still has his craft.
the_smithy = station("the_smithy", attributes(),

    simple_actions = (
        # Speak with Denzil
        #
        # Denzil will talk about practical matters, though he prefers to sit in silence. A shilling will buy his help for a day. [If you give him occult coinage, he will perform the Service of Division instead.]
        # ---
        # Assistance from Denzil the Blacksmith
        #
        # 'What d'you need?'
        simple_action("speak_with_denzil",
            output = (
                simple_output( assistance.blacksmith ),
            ),
            pennies = 12,
            slots = None,   # same as station slots
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, forge=1, heart=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
    ),
)

from ..item import notype, tally
from ..model import attributes, condition, simple_action, slot, station


# unlock with journal
(
    """Something for me?

The Postmistress regards me with the chilly gaze of a goddess-image in an ancient hill-shrine. 'The Librarian,' says she, 'yes. I have something for you. Wait here, please.'""",
    """Something for me?

The Postmistress returns with an envelope addressed to 'The Librarian, Hush House, Brancrug Isle' - postmarked in Wales a week ago.""",
)


# bronze spintria -> 120p
(
    """Sell a Bronze Spintria

Spintriae are not legal tender. But no law prevents the Postmistress from purchasing them from me. Perhaps she collects them. [This is worth ten shillings.]""",
    """Sell a Bronze Spintria

The Postmistress scrutinises the design on the spintria.'Fire warms,' she says softly, 'night ends.' She hands me a ten shilling note.""",
)


# iron spintria -> 60p
(
    """Sell an Iron Spintria

Spintriae are not legal tender. But no law prevents the Postmistress from purchasing them from me. Perhaps she collects them. [This is worth five shillings.]""",
    """Sell an Iron Spintria

The Postmistress scrutinises the design on the spintria. 'And they say that <i>speech</i> is a sword,' she remarks. She hands me a coin.""",
)


# ready_to_post + 1p
(
    """A King-Marked Stamp

Stamp, envelope, send!""",
    """A King-Marked Stamp

The Postmistress examines the letter, and deems it sufficient. 'It'll go with the next post,' she assures me.""",
    """In the Post

Now I can expect visitors, correspondence, and a stipend from the Trust every spring.""",
)


# 60p -> 30,24,6
(
    """Break a Crown

The Postmistress will accept the offering and bestow upon me the appropriate change.""",
    """Break a Crown

A crown broken into a muted rainbow of silver.""",
)

# 24p -> 12,6,3,2,1
(
    """Break a Florin

The Postmistress will accept the offering and bestow upon me the appropriate change.""",
    """Break a Florin

I surrender the florin and receive an unruly handful of lesser coins""",
)


# 30p -> 24,6
(
    """Break a Half Crown

The Postmistress will accept the offering and bestow upon me the appropriate change.""",
    """Break a Half Crown

A pedant, or a poet, might suggest that a half crown cannot ever have been whole, and so might not be broken. They wouldn't suggest it to the Postmistress, though..""",
)


# 12p -> 6,3,2,1
(
    """Break a Shilling

The Postmistress will accept the offering and bestow upon me the appropriate change. (This is the smallest coin she will deign to change.)""",
    """Break a Shilling

Surrender silver, collect copper.""",
)


# 120p -> 60,30,24,6
(
    """Break a Ten-Shilling Note

The Postmistress will accept the offering and bestow upon me the appropriate change.""",
    """Break a Ten-Shilling Note

Ten shillings, discarnated into lesser coins.""",
)


# Post Office
#
# The Postmistress keeps the gate to the wider world. In her left hand is the lightning (which is to say, the telegraph) and in her right, the thunder (which is to say, the only telephone in Brancrug). Before her lies the cash-register, which accepteth the greater currency and returneth its lesser children.
the_post_office = station("the_post_office", attributes(),

    nonleaf_description = (
        # locked incomplete, <empty>
        """The Post Office [Locked]

The postmistress may have something for me - once I know what to ask for.""",
        # deadend, coin (pence<12)
        """Too Petty Cash

The Postmistress will break larger currency into change, but don't tempt her anger with so mean and small a coin as this.""",
        # incomplete, ready_to_post
        """Post Office

Patience. Thus the mountain awaits the fall of the snow; thus Monday awaits the death of the week-end; thus the Postmistress waits for me to purchase the necessary stamp.""",
    ),

    slots = (
        slot(
            required=condition(pence=1, ready_to_post=1, tally=1),
        ),
    ),
)

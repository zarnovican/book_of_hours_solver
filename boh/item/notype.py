from ..model import attributes, card_type


# A Letter to the Librarian
#
# A letter to me from St Rhonwen's Trust. The Trust's connection with Hush House is probably benevolent, but persistently obscure.""",
# ---
# The Letter Reads...
#
# St Rhonwen's Trust wishes to congratulate me on my appointment as Librarian of Hush House. The Trust assures me that it will provide the promised stipend each spring... but reminds me that its resources are limited, and suggests I seek local assistance in restoring the premises. 'Let us know when you're all set up and ready to receive visitors,' the letter concludes. It's signed simply 'the Trustees'.""",
a_letter_to_the_librarian = card_type("a_letter_to_the_librarian",
    attributes(readable=1, correspondence=1),
)


# A Reply to the Trust
#
# I can take this to the Post Office to be dispatched to St Rhonwen's Trust. Once they know I've arrived, they'll send more funds... I hope.
# ---
# (cannot consider)
# ---
# A King-Marked Stamp
#
# Stamp, envelope, send!
# ---
# A King-Marked Stamp
#
# The Postmistress examines the letter, and deems it sufficient. 'It'll go with the next post,' she assures me.
# ---
# In the Post
#
# Now I can expect visitors, correspondence, and a stipend from the Trust every spring.
a_reply_to_the_trust = card_type("a_reply_to_the_trust",
    attributes(moth=1, ready_to_post=1),
)


# Order Form: Cater & Hero
#
# Cater & Hero has offices almost everywhere. Not in this misty limb of the kingdom - but they will, at least, deliver here. [Use Ink to order items of interest - a few lines on an order form won't consume the Ink. When your delivery arrives, it'll contain a new order form.]
order_form_cater_and_hero = card_type("order_form_cater_and_hero",
    attributes(readable=1),
)

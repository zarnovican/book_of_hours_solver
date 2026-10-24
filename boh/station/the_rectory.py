from ..item import assistance, journal
from ..model import attributes, condition, simple_action, simple_output, slot, station


# (locked incomplete, an introduction + <empty>)
#
# A Clergyman Distrait?
#
# The door opens a few cautious inches. 'Who's there? I say, who's there?  [The storm-wind plucks at you, plucks at the door, shakes the trees around the house...]


# (unlock with an_introduction + health)
# 
# A Clergyman Distrait
#
# The Reverend staggers back as if he'd received a blow, and then he's bombarding me with terrified, delighted questions before I'm even through the door.
# ---
# A Clergyman Distrait
#
# Timothy ushers me into the bright hall, casting about for his housekeeper, and asking questions the whole time. 'How did you come here? Was it the wreck? Terrence! Terrence, do fetch towels!'
# ---
# Take Shelter at the Rectory
#
# Reverend Timothy flutters fussily while Terrence the Housekeeper busies herself with practicalities. She shows me to a warm room at the top of the house where a fire is already made up.
# ---
# Take Shelter at the Rectory
#
# Reverend Timothy is touchingly excited to meet his correspondent in person. I am still too exhausted to hold up my end of the conversation, and Terrence is not a talkative woman, but the Reverend can talk for three. At last however he suddenly realises how exhausted I am, and lets me sleep.


# (phost + soaked journal)
#
# Speak with Reverend Timothy
#
# Reverend Timothy's door is always open to me. [Timothy will offer help for free, as a friend.]
# ---
# Dry Out a Book
#
# Reverend Timothy is not a man to miss an opportunity for conversation, so the whole business takes longer than it might... but he's anxious to help.


# The Rectory [Locked]
#
# Reverend Timothy is a hospitable soul, but Terrence, his housekeeper, guards her employer fiercely. She doesn't want his innocent theological enthusiasms getting him in trouble with the New King's men.
# [You need an Introduction, or a mutual acquaintance marked with Lantern, Knock, or Sky -  perhaps someone who shares his interests in theology or poetry.]""",
# ---
# The Rectory
#
# Reverend Timothy's words always run ahead of him, but his thoughts always catch up.
the_rectory = station("the_rectory", attributes(),

    simple_actions = (
        # Speak with Reverend Timothy
        #
        # Reverend Timothy's door is always open to me. [Timothy will offer help for free, as a friend.]
        # ---
        # Assistance from Reverend Timothy
        #
        # Reverend Timothy always jumps at the offer of my company.
        simple_action("speak_with_reverend_timothy",
            output = (
                simple_output( assistance.rector ),
            ),
            pennies = 0,    # TODO (future) implement cost for old friend
            slots = None,   # same as station
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(knock=1, lantern=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
    ),
)

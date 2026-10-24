from ..item import assistance, journal
from ..model import attributes, condition, simple_action, simple_output, slot, station


# (unlock with miner)
#
# Cradles and Coffins
#
# A mutual acquaintance has induced the Killes to invite me for a fish supper.  If I'm lucky, 'fish supper' may mean Mrs Kille's celebrated galettes.
# ---
# Cradles and Coffins
#
# Mr Kille pumps my hand. 'Just me and thee and the Mrs tonight! Eh, well, there's a client in the back, but if thee don't bother he, he won't bother thee.'[The Killes household is now available.]


# Mrs and Mr Kille [Locked]
#
# Mrs Kille the midwife is tall and gloomy. Mr Kille the undertaker is slight and wry. In these troubled times, both are wary of strangers. [You need a suitably marked Introduction; check the slot.]""",
# ---
# Mrs and Mr Kille
#
# Mrs Kille the midwife is tall and gloomy. Mr Kille the undertaker is slight and wry. For ten years she has drawn villagers into the world and he has shaped cradles for their departure. But she can also whittle, and he can also paint.
mr_and_mrs_kille = station("mr_and_mrs_kille", attributes(),

    simple_actions = (
        # Speak with Mr Kille
        #
        # Mr Kille likes conversations about endings. (His wife prefers to talk about beginnings.)  A shilling will buy his help for a day.
        # ---
        # Assistance from Mr Kille
        #
        # 'Let's to it!'
        simple_action("speak_with_mr_kille",
            output = (
                simple_output( assistance.coffinmaker ),
            ),
            pennies = 12,
            slots = (
                slot(
                    essential=condition(soul=1),
                    required=condition(grail=1),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),

        # Speak with Mrs Kille
        #
        # Mrs Kille likes conversations about beginnings. (Her husband prefers to talk about endings.) A shilling will buy her help for a day.
        # ---
        # Assistance from Mrs Kille
        #
        # 'A day's work is a night's dreaming.'
        simple_action("speak_with_mrs_kille",
            output = (
                simple_output( assistance.midwife ),
            ),
            pennies = 12,
            slots = (
                slot(
                    essential=condition(soul=1),
                    required=condition(grail=1),
                    forbidden=condition(fatigued=1, malady=1),
                ),
            ),
        ),
    ),

    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, winter=1),
            forbidden=condition(fatigued=1, malady=1),
        ),
    ),
)

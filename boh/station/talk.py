from ..item import assistance, soul
from ..model import attributes, condition, simple_action, slot, station


# assistance.fisherman_sceptical + an_introduction.rector
(
    """Allaying Suspicion

'Be someone that'll speak for 'ee?'

(Of course. Since 1930 and the Restoration, the locals have grown ever more suspicious of foreigners. But there is someone in Brancrug I know...)""",
    """Allaying Suspicion

'I'll take 'ee by the cliffs, then.' [This gentleman is no longer Sceptical. Use him to unlock Brancrug Village.]""",
)


# collaborate_chor
(
    """Collaborate: Chor

Everything goes easier with a song. [Boosts Heart and Grail]""",
    """Collaborate: Chor

My assistant and I are both a little merrier.""",
)


# (assistance + soul.ereb)
# Collaborate: Ereb
#
# My pride will find an echo in theirs. [Boosts Grail and Edge]
# ---
# Collaborate: Ereb
#
# Eagerly, we anticipate our work.


# collaborate_fet
(
    """Collaborate: Fet

Perhaps we shared a dream. [Boosts Rose and Moth]""",
    """Collaborate: Fet

My assistant and I have an unspoken understanding.""",
)


# collaborate_health
(
    """Collaborate: Health

I'm ready to lend my limbs. [Boosts Heart, Scale, Nectar]""",
    """Collaborate: Health

We'll work alongside each other.""",
)


# collaborate_mettle
(
    """Collaborate: Mettle

Inspiration and determination. [Boosts Forge and Edge]""",
    """Collaborate: Mettle

Our course is fixed.""",
)


# collaborate_phost
(
    """Collaborate: Phost

Together, we'll be watchful. [Boosts Lantern and Sky]""",
    """Collaborate: Phost

My assistant and I are vigilant.""",
)


# (assistance + soul.shapt)
# Collaborate: Shapt
#
# Education, or beguilement? [Boosts Knock and Forge]
# ---
# Collaborate: Shapt
#
# My assistant and I fall easily into conversation.


# collaborate_trist
(
    """Collaborate: Trist

Secret sorrows may join our strengths. [Boosts Moth and Moon]""",
    """Collaborate: Trist

What comes? Neither of us knows yet, but we will.""",
)


# (assistance + soul.wist)
# Collaborate: Wist
#
# We'll watch for what lies ahead. [Boosts Winter and Lantern]
# ---
# Collaborate: Wist
#
# My assistant and I will be prudent.


# exalt_with_a_memory
(
    """Exalt with a Memory

I can discuss a Memory with my assistant. [This will use up the Memory, but boost the assistant's abilities for the rest of the day.]""",
    """Exalt with a Memory

Memories don't last as long outside books. But it's made a difference for the day.""",
)


# exalt_with_a_weather
(
    """Talk about the Weather

More useful than one might expect. Especially in Britain. [The influences of the turning skies can boost an assistant's abilities for the rest of the day.]""",
)


# exalt with flower
(
    """'To put thy pale, lost lilies out of mind'

Fading flowers may provide inspiration. [This will increase their Aspects.]""",
    """'To put thy pale, lost lilies out of mind'

'I cried for madder music and for stronger wine...' [This has improved their Aspects appropriately.]""",
)


# exalt with tool
(
    """Proffer a Tool

I can lend my assistant something to help, increasing their abilities. [You'll still be able to use the Tool.]""",
    """Proffer a Tool

[The tool's boosted their Aspects appropriately.]"""
)


# exalt with metal
(
    """Additional Supplies

I can offer my assistant metals - mundane, or exotic. [This will increase their Aspects. They'll keep any of the metal that's left over.]""",
    """Additional Supplies

Let it clutter up <i>their</i> shelves. [This has improved their Aspects appropriately.]""",
)


# exalt with fuel
(
    """Fuelling their Efforts

I can offer my assistant fuel for light, or for heat. [This will increase their Aspects. They'll keep any fuel that might be left over.]""",
    """Fuelling their Efforts

'Each flame has its fuel.' [This has improved their Aspects appropriately.]""",
)


# soul.fet
(
    """Déjà Vu?

Did I dream of this beach and this wind?  If I did, I might remember the path I took in that dream -  a path which brought me light.""",
    """Déjà Vu?

At last, the light of a hurricane lamp bobbing in the dark. As it approaches, a face looms out of the night.""",
)


# hire_a_visitor - employable + 24p
(
    """Hire a Visitor

I'll hire this one for a day.""",
    """Hire a Visitor

Hired.""",
)


# <autorun>
(
    """Shelter?

Brancrug Village must be nearby. But it's hard going, dragging my soaked body across the soaked sand in the teeth of this wind. Which way?""",
)


# fugitive
(
    """Speak to an Assistant

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.]""",
    """Speak to an Assistant

I've learnt something - or perhaps just remembered it.""",
)


# speak_to_a_nun
(
    """Speak to a Nun

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk. A Nun may have a particular interest in Omens.]""",
    """Speak to a Nun

I've learnt something - or perhaps just remembered it.""",
)


# speak_to_a_poet
(
    """Speak to a Poet

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.  Unlike some assistants, a Poet has a use for Flowers.]""",
    """Speak to a Poet

I've learnt something - or perhaps just remembered it.""",
)


# speak_to_an_artist
(
    """Speak to an Artist

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.  Unlike most assistants, a Painter can make use of Pigments.]""",
    """Speak to an Artist

I've learnt something - or perhaps just remembered it.""",
)


# speak_to_an_engineer
(
    """Speak to an Engineer

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.  Unlike some assistants, an Engineer can make use of Fuels.]""",
    """Speak to an Engineer

I've learnt something - or perhaps just remembered it.""",
)


# speak_to_travelling_musician
(
    """Speak to an Assistant

I could encourage my assistant; work with them; for a little while, exalt them. Or I could just listen to whatever they might have to say. [Add something to enhance your assistant's effectiveness for the day, or just talk.]""",
    """Speak to an Assistant

I've learnt something - or perhaps just remembered it.""",
)


# assistance + sustenance
(
    """Offer Something to Eat

I can offer my assistant something to eat. This will increase their Aspects. It's also just friendly.""",
    """Offer Something to Eat

[The sustenance has boosted their Aspects appropriately.]""",
)


# assistance + candle
(
    """A Light for Dark Places

I can offer my assistant a candle. [This will increase their Aspects. They'll keep any candle-stumps that might be left over.]""",
    """A Light for Dark Places

'Every candle has its shadow.' [This has improved their Aspects appropriately.]""",
)


# assistance + beverage
(
    """A Nice Drop

I can offer my assistant something to drink. [This will increase their Aspects. They'll also be glad of the refreshment.]""",
    """A Nice Drop

Down to the grushans. [This has boosted their Aspects appropriately.]""",
)


# assistance + fabric_and_fibre
(
    """The Threads Converge

This assistant may be able to make use of fabrics and other woven things. [This will increase their Aspects. They'll keep whatever might be left over.]""",
    """The Threads Converge

Let it clutter up <i>their</i> shelves. [This has improved their Aspects appropriately.]""",
)


# assistance + pigment
(
    """Exotic Pigments

I can offer them something to brighten their canvas. [This will increase the assistant's Aspects. And more art is always good.]""",
    """Exotic Pigments

'Interesting...' [This has improved their Aspects appropriately.]""",
)


# (assistance + wood)
# Additional Supplies
#
# I can offer my assistant any suitable timber I have lying around. [This will increase their Aspects. They'll keep any of the wood that's left over.]
# ---
# Additional Supplies
#
# Let it clutter up <i>their</i> shelves. [This has improved their Aspects appropriately.]


# feed the beastie
(
    """Feed the Beastie

Satisfy this creature's appetite. [Food will make a hungry beast, or a wild one, co-operative.]""",
    """Feed the Beastie

A full belly makes a helpful friend. [This beastie is now inclined to co-operate.]""",
)


# nun + omen
(
    """An Apposite Auspice

I can offer them an omen that may provide useful guidance. [This will increase their Aspects.]""",
    """An Apposite Auspice

'Before Moon, Dusk; before Dusk, Dawn; before Dawn, Stone.' [This has improved their Aspects appropriately.]""",
)


# visitor.mr_fraser_strathcoyne + book with matching interest -> tally.iron_spintria
(
    """A Conversation with Fraser Strathcoyne

'Librarian. I have urgent business with you.' [If there's an Incident card active, you can discuss it - or just leave the slot empty and offer a Consultation.]""",
    """A Conversation with Fraser Strathcoyne

I can identify my visitor's interests, and satisfy them with an appropriate book. Alternatively, if they know a language I'd like to learn, I can offer payment. [Untrustworthy visitors might occasionally abscond with a book.]""",
    """Lantern: Suitable Reading

My visitor is in search of revelations. The answers can be found in my collection.""",
    """Lantern: Suitable Reading

'How enlightening.' [You've satisfied your visitor and earnt a reward. But the more they learn, the harder they'll be to satisfy in future.]""",
)


# visitor.mr_fraser_strathcoyne + book without matching interest / or no book
(
    """A Conversation with Fraser Strathcoyne

My visitor has learnt nothing.""",
)


# visitor.mr_zachary_wakefield + book with matching interest -> tally.iron_spintria
(
    """A Conversation with Wakefield

'Librarian. I can see you.' [If there's an Incident card active, you can discuss it - or just leave the slot empty and offer a Consultation.]""",
    """A Conversation with Wakefield

I can identify my visitor's interests, and satisfy them with an appropriate book. Alternatively, if they know a language I'd like to learn, I can offer payment. [Untrustworthy visitors might occasionally abscond with a book.]""",
    """Knock: Suitable Reading

My visitor needs something sealed... or unsealed. My collection can help.""",
    """Knock: Suitable Reading

'How promising.' [You've satisfied your visitor and earnt a reward. But the more they learn, the harder they'll be to satisfy in future.]""",
)


# visitor + tally -> skill
(
    """Tutoring: Cracktrack

My visitor can teach me the rudiments of the primal language that we rather underwhelmingly call 'Cracktrack' - because there is no name for that language in that language. [After tutoring you, the visitor will leave, even if they arrived on other business.]""",
    """Tutoring: Cracktrack

I've learnt enough to puzzle out books in this language, though it might be slow going. [You can also use and improve this like any other skill.]""",
)


# visitor.mr_fraser_strathcoyne + tally -> skill
(
    """Tutoring: Ramsund

My visitor can teach me the rudiments of this lively language. [After tutoring you, the visitor will leave, even if they arrived on other business.]""",
    """Tutoring: Ramsund

I've learnt enough to puzzle out books in this language, though it might be slow going. [You can also use and improve this like any other skill.]""",
)


# tame viper -> hungry viper + earth-sign
(
    """Time with the Beastie

Offer this beast my company. Who knows? Perhaps it will offer something in return.""",
    """Time with the Beastie

And now, it suggests, a meal would be welcome.""",
)


# Talk
#
# Speak to visitors, assistants, strangers, friends...
talk = station("talk", attributes(),

    nonleaf_description = (
        # prologue incomplete, <empty>
        """Help?

Above me, atop the cliffs, lies Brancrug Village. I'll never reach it in this storm, but if I can only muster my remaining strength to find help... [Clicking a slot will highlight cards and objects which can go there.]""",
        # talk incomplete, sceptical fisherman + <empty>
        """Allaying Suspicion?

'Come no closer! What's thy business?'""",
        # talk incomplete, non-sceptical fisherman + <empty>
        """Suspicion Allayed, Already

'Ar?' [The gentleman wishes you to understand that he's talked enough and that he would like to get out of the rain now, please and thank you. Use him to unlock the path up the cliffs.]""",
        # talk incomplete, employable + <empty>
        """Hire a Visitor?

If I meet their price, I can hire them for a day.""",
        # incomplete: beast + <empty>
        """Feed the Beastie?

Use a Soul card and suitable Sustenance. [Food will make a hungry beast, or a wild one, co-operative.]""",
        # visitor.fr_stanislav_john_schaller + <empty>
        """A Conversation with Father Stanislav

'Bless you; and bless the House you serve.' [If there's an Incident card active, you can discuss it - or just leave the slot empty and offer a Consultation.]"""
        # visitor.mr_fraser_strathcoyne + <empty>
        """A Conversation with Fraser Strathcoyne

'Librarian. I have urgent business with you.' [If there's an Incident card active, you can discuss it - or just leave the slot empty and offer a Consultation.]""",
        # visitor.mr_zachary_wakefield + <empty>
        """A Conversation with Wakefield

'Librarian. I can see you.' [If there's an Incident card active, you can discuss it - or just leave the slot empty and offer a Consultation.]""",
    ),

    slots = (
        slot(
            required=condition(assistance=1, employable=1, beast=1, visitor=1),
        ),
    ),
)

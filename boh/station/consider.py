from ..item import journal, notype, thing, uncatalogued
from ..model import attributes, condition, simple_action, slot, station


# (journal.scaled_book + soul)
#
# A Journal?
#
# <i>My</i> journal? That softly scaled cover is familiar - but the storm so scattered my thoughts...
# ---
# A Journal?
#
# My journal - I'm sure of it. The storm scattered my thoughts, but each page I turn is familiar. I begin to recall now why I came here - to finish my masterwork - my last map. [More about your origin, and your aspirations, in your journal. You can now also access the Tree of Wisdoms from the top of the screen.]


# (journal.a_drowned_book_fet_phost)
#
# Consider
#
# I should dry this book out before trying to read it.
# ---
# Consider
#
# I can't glean anything from this book until I've dried it out - carefully! To do that, I'll need to find somewhere warmer. Much warmer.


# (journal.a_drowned_book + memory.storm)
#
# I Remember...
#
# There was a storm. It smashed the ship like an egg. But I seized this book as the sea seized me... then the sea brought me here to Brancrug.
# ---
# I Remember...
#
# There was a storm. It smashed the ship like an egg. But I seized this book as the sea seized me... then the sea brought me here to Brancrug. And Brancrug is where I wanted to be. But it's hard to remember why. What else did I lose in the storm?


# (<autorun>)
#
# The cold comes first
#
# Thunder growling. Waves pounding...
# ---
# The cold comes first
#
# Thunder growling. Waves pounding... and finally me, sprawled on the sodden sand of the beach. There's something in my hand.


# (journal.a_drowned_book + memory.fet_question)
#
# What Remains of Me? Dreams?
#
# The human soul has nine parts. <i>Fet</i> is that part of the soul that dreams. Is my <i>fet</i> strong? [Recover this. The other two possibilities will be lost to the sea... for now.]
# ---
# What Remains of Me? Dreams?
#
# This is the coast where Brancrug Isle lies. I've seen it in my dreams, night after night. I know there's no way I can cross to the isle in these seas. I'll need to find shelter for the night.


# (journal.a_drowned_book + memory.chor_question)
#
# What Remains of Me? Instinct?
#
# The human soul has nine parts. Exuberance, enthusiasm, instinct all rise from that part of the soul we call <i>chor</i>. Is my <i>chor</i> strong? [Recover this. The other two possibilities will be lost to the sea... for now.]
# ---
# What Remains of Me? Instinct?
#
# This is the coast where Brancrug Isle lies. It wasn't easy to come here... but I don't give up easily. Even so, I know there's no way I can cross to the isle in these seas. I'll need to find shelter for the night.


# (journal.a_drowned_book_fet + memory.wist_question)
#
# What Remains of Me? Knowledge?
#
# <i>Wist</i> is the soul's memory, the true name scratched on its cornerstone, what remains after the rest has passed. [Choose a strong <i>wist</i>, and a past where you sought voices that had fallen silent. The waves will wash away the others... for now.]
# ---
# What Remains of Me? Knowledge?
#
# There are still things I don't remember. But I <i>do</i> remember there's someone in the village who will give me sanctuary - if I can get there.
#
# [Mysteries have been added to your Journal. You can begin to investigate them when you and your journal are both dry.]


# (journal.a_drowned_book_fet + memory.phost_question)
#
# What Remains of Me? Light?
#
# <i>Phost</i> is the light within: sight, perception, inspiration. [Choose a strong <i>phost</i>, and a past with a pursuer who can see the light within you. The waves will wash away the others... for now.]
# ---
# What Remains of Me? Light?
#
# Perhaps here I'll find safety from what follows me. But what was that, exactly?
#
# First things first. I remember there's someone in the village who will give me sanctuary - if I can get there.
#
# [Mysteries have been added to your Journal. You can begin to investigate them when you and your journal are both dry.]


# (journal.a_drowned_book_fet + memory.mettle_question)
#
# What Remains of Me? My strength of character?
#
# <i>Mettle</i> is the soul's tempering - will; self-discipline; that part of us which makes the right choice. [Choose a strong <i>mettle</i>, and a past where you made mistakes. The waves will wash away the others... for now.]
# ---
# What Remains of Me? My strength of character?
#
# Perhaps here I can atone for all I've done. But what was that, exactly?
#
# First things first. I remember there's someone in the village who will give me sanctuary - if I can get there.
#
# [Mysteries have been added to your Journal. You can begin to investigate them when you and your journal are both dry.]


# (journal.a_drowned_book_fet + memory.ereb_question)
#
# What Remains of Me? Passion?
#
# <i>Ereb</i> is the shadow in the soul's cellar: pride, fear, hatred, compassion. [Choose a strong <i>ereb</i>, and a past where your passions were paramount. The waves will wash away the others... for now.]
# ---
# What Remains of Me? Passion?
#
# I wanted something I didn't have. I don't have very much at all now, do I? I suppose that should make it easier.
#
# First things first. I remember there's someone in the village who will give me sanctuary - if I can get there.
#
# [Mysteries have been added to your Journal. You can begin to investigate them when you and your journal are both dry.]


# (journal.a_drowned_book + memory.shapt_question)
#
# What Remains of Me? Words?
#
# The human soul has nine parts. Eloquence and understanding rise from that part of the soul we call <i>shapt</i>. Is my <i>shapt</i> strong? [Recover this. The other two possibilities will be lost to the sea... for now.]
# ---
# What Remains of Me? Words?
#
# This is the coast where Brancrug Isle lies. My sources briefed me thoroughly about the place, and I know there's no way I can cross to the isle in these seas. I'll need to find shelter for the night.


# (journal.serpentskin_journal + soul.fet + memory.foresight)
#
# Lantern: Revelations!
#
# I can master this mystery. [Enough Lantern to match Mystery: Lantern.]


# (consider lesson)
#
# Acquire Path & Pilgrim
#
# Use this Lesson to acquire a new Skill.
# ---
# Acquire Path & Pilgrim
#
# Another leaf on the Tree of Wisdoms.


# (consider skill + soul + lesson + memories)
#
# Consider
#
# There's always more to learn. [Improve this skill to level 2. This will increase its Aspects, which'll help with crafting; and make it suitable for higher branches in the Tree of Wisdoms, if you haven't already committed it.]
# ---
# Consider
#
# [This skill is now level 2. Its Power aspects have also increased.


# (consider cache)
#
# Something Rare
#
# Crack open the container, delight in your discovery.


# (consider beast)
#
# Inspect
#
# Inspect this beast. [It can be more rewarding to Talk with a beast, though.]
# ---
# Inspect
#
# What have I learnt?


# (skill level 2+ + soul, in numa)
#
# In Numa...
#
# That brightness in the mist - is it the Sun? It might be unwise to gaze into it.[You can choose to forget almost everything you have learnt of this Skill - since you haven't yet committed it to the Tree of Wisdoms. You'll gain 8 Many-Faceted Lessons, one fewer than you spent to get this far... for though much abides, something is always taken. Many-Faceted Lessons can be used to upgrade any Skill, but always disappear at dawn.]
# ---
# In Numa...
#
# [This skill is now level 1. Use your Many-Faceted Lessons wisely.]

# (skill level 1 + soul, in numa)
#
# In Numa...
#
# This mist will pass. What will pass with it?[You can choose to forget everything you know of this Skill - since you haven't yet committed it to the Tree of Wisdoms. You'll gain a Many-Faceted Lesson, which can be used to upgrade any other skill, but which always disappears at dawn - and which cannot be used to regain your lost skill.]
# ---
# In Numa...
#
# [Use your Many-Faceted Lesson wisely.]

# consider
consider = station("consider", attributes(),

    mastering_slots = (
        slot(
            required=condition(readable=1),
            forbidden=condition(reel_of_film=1, phonograph_record=1, fixed_in_place=1),
        ),
        slot(
            required=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(required=condition(skill=1)),
        slot(required=condition(memory=1)),
    ),

    nonleaf_description = (
        # prologue incomplete, <empty>
        """Remember

What do I have left to work with?""",
        # prologue deadend, memory
        """Scattered Memories

I can't get my thoughts straight. But there's something in my hand... [Your single remaining possession is in a Belongings slot at the top.]""",
        # prologue deadend, half-drowned health
        """Alive, Approximately

I'm soaked, I'm freezing, but as far as I can tell, I'm still alive. [You still have some Health. Don't lose it. You need it, if you want to be alive. What else do you have? Your single remaining possession is in a Belongings slot at the top.]""",
        # prologue incomplete, soaked journal
        """I Remember...?

Perhaps this book can help me put the pieces together.""",
        # prologue deadend, soaked journal + half-drowned health
        """Freezing Fingers

The book's in bad shape, and I'm not much better. We're both in need of a warm dry safe place, and soon.""",
        # prologue deadend, soul
        """I've begun to remember -

This element of my soul is strong. What else? [Choose another Memory, and recover another Element of the Soul.]""",
        # consider incomplete, <empty>
        """Consider

Examine; appreciate; catalogue.""",
        # consider incomplete, journal + <empty>
        """The Soul's Labours

'Some books are to be tasted, others to be swallowed, and some few to be chewed and digested.' - Bacon 

 [Studying requires effort; you'll always need a <i>suitable</i> Soul card first.] """,
        # incomplete, mastered journal + soul
        """The Next Page?

I could add something to this journal... if I could lay my hands on a suitable ink.""",
        # incomplete, skill + soul + lesson
        """Consider

[You'll need to fill every slot with Memories which match a Power aspect - including at least one Lesson.]""",
    ),

    slots = (
        slot(
            required=condition(skill=1, readable=1, lesson=1, cache=1),
            forbidden=condition(reel_of_film=1, phonograph_record=1, fixed_in_place=1),
        ),
    ),
)

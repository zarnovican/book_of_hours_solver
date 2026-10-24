from ..item import memory
from ..model import attributes, card_type


# Shuritic Book of Suns
#
# A radically different text from any of the other versions of the Book of Suns, attributed to Hagar, Queen of Shur, Mother of Wolves. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# 'Set down with reverence before the Intercalate, by one who understood what would come to pass…'
# ---
# I've Read...
#
# Apocryphal chapters foretell the means by which the Sun-in-Splendour and the Forge might circumvent the impossibility of their joining, through proxies that are in some sense themselves…
shuritic_book_of_suns = card_type("shuritic_book_of_suns",
    attributes(tally_price=8, written_in_deep_mandaic=1, mystery_sky=10, readable=1, thing=1, subject_sacra_solis_invicti=1, dawn_period=1, scroll=1),
    lessons=2,
    provides=memory.the_great_counterfeit,
)


# The Fire-Circle Tantra
#
# The one known extant copy of this in Western Europe was stolen from the British Library in 1892. One Harvey Hattington confessed to the crime and claimed to have eaten it, with butter and garlic, in a moment of ungovernable whimsy.
# ---
# I'm Reading...
#
# Herein the Great Hooded Princes are shown beseeching the Wood to rise and devour an invading Timurid army. The 'Dapple-King', the 'Honey-Tree' and the 'Sea-Twins' all deny their request, until they enlist the help of a burrowing secret-keeper...
# ---
# I've Read...
#
# Armed with blackmail material from the 'burrowing secret-keeper', the Great Hooded Princes petition the powers of the Wood for a second time, and are successful. One quarter of the Timurid army is devoured by bees, one quarter drowns themselves, and one quarter 'disrobe themselves until nothing remains'.
the_fire_circle_tantra = card_type("the_fire_circle_tantra",
    attributes(tally_price=2, mystery_moth=8, written_in_sanskrit=1, readable=1, thing=1, scroll=1, curia_period=1, subject_solutions_and_separations=1),
    lessons=2,
    provides=memory.intuition,
)


# The Flayed Tantra
#
# This Tantra is recorded as being spoken by an enigmatic individual identified as 'Peel', with many of the qualities of the mythological naga. The Flayed Tantra played a notable part in Alexander Sparrow's paranoid pamphleteering.
# ---
# I'm Reading...
#
# 'Peel' was numbered among the Great Hooded Princes, but it breaks with its brethren and followed the Thunderskin in the endless dance.
# ---
# I've Read...
#
# Once Peel had peeled itself, it had the ink it needed to write the Tantra. It had to face the wrath of its fellows. Here is the invocation it used to fend them off.
the_flayed_tantra = card_type("the_flayed_tantra",
    attributes(tally_price=2, mystery_heart=8, written_in_sanskrit=1, readable=1, thing=1, subject_maggephene_mysteries=1, scroll=1, curia_period=1),
    lessons=2,
    provides=memory.storm,
)


# The Incandescent Tantra
#
# Michael Blockley, the eccentric iron magnate, was fond of quoting from this tantra. Blockley died in a factory fire.
# ---
# I'm Reading...
#
# Dialogues with an entity called the Crucible Prince. The Prince warns about the appetites of his mistress, the Burning Queen, and the peril of the naked desire she shares with the Sun, but professes his loyalty nevertheless.
# ---
# I've Read...
#
# 'A rite which changes is necessarily a rite which destroys. But a great change requires a destruction of savage extent.'
the_incandescent_tantra = card_type("the_incandescent_tantra",
    attributes(tally_price=2, mystery_forge=8, written_in_sanskrit=1, readable=1, thing=1, scroll=1, curia_period=1, subject_transformations_and_liberations=1),
    lessons=2,
    provides=memory.foresight,
)


# The Leonine Tantra
#
# In the most notorious translation of the Leonine Tantra, Ashley Phillips is listed as the translator, but their existence is explicitly denied in the prologue. This confusion is characteristic of books which mention the Great Hooded Princes.
the_leonine_tantra = card_type("the_leonine_tantra",
    attributes(tally_price=2, mystery_edge=8, written_in_sanskrit=1, readable=1, thing=1, subject_edicts_martial=1, scroll=1, curia_period=1),
    lessons=2,
    provides=memory.fear,
)


# The Sun Disfigured
#
# A scroll of anthropoderm parchment, written in the golden ink called Uzult. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# The author of the text calls herself 'the Elagabaline'. Sometimes she seems to be Sunset Celia, the Watchman's Name; sometimes she seems to be Lady Tryphon, the Grail-long. It is unclear whether these are separate entities or the same person - it may be unclear even to the writer.
# ---
# I've Read...
#
# The flaws in the Sun's Plan are elucidated. The Sun's Plan itself is never entirely clear, but it is a project of some kind to enter, possess, or surrender to the Glory - the pure light above the Mansus. This book suggests ways in which that Plan might fail.
the_sun_disfigured = card_type("the_sun_disfigured",
    attributes(tally_price=8, written_in_cracktrack=1, mystery_grail=10, readable=1, thing=1, dawn_period=1, subject_applebright_euphonies=1, scroll=1),
    lessons=2,
    provides=memory.the_suns_weakness,
)


# The Thirsting Tantra
#
# C.G. Burial, the temperance campaigner, published elements of this in a pamphlet, which had to be withdrawn and destroyed after it became popular.
# ---
# I'm Reading...
#
# A disquisition on the many varieties of thirst, their uses and their effects.
# ---
# I've Read...
#
# The tantra describes how the satisfaction of thirsts may allow a mortal to rise into the service of the Thirsting Power, but warns of the consequences of rejecting those rarer thirsts for common ones.“A man who thirsts, O Mighty One, whose mind clings to actions in this world, will return to this world of action from that other place.”
the_thirsting_tantra = card_type("the_thirsting_tantra",
    attributes(tally_price=2, mystery_grail=8, written_in_sanskrit=1, readable=1, thing=1, subject_orchids_and_narcotics=1, curia_period=1, scroll=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Watchful Tantra
#
# Notorious for its involvement in the deaths of Dafydd Jones and Meredith Blaine, two early physicists who each claimed to have the only copy and who ultimately fought a duel over it in 1840.
# ---
# I'm Reading...
#
# The Tantra describes processes of occult illumination, including a formula which may show the way from the 'Hunter's Gate' to the 'Serpent Gate' - which in the West is usually called the Spider's Door.
# ---
# I've Read...
#
# The Sun passes through the House at the appointed time. Since the Sun's division, the time has become uncertain.'
the_watchful_tantra = card_type("the_watchful_tantra",
    attributes(tally_price=2, mystery_lantern=8, written_in_sanskrit=1, readable=1, thing=1, scroll=1, curia_period=1, subject_purifications_and_exaltations=1),
    lessons=2,
    provides=memory.revelation,
)

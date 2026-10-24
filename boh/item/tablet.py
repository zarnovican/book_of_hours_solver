from ..item import memory
from ..model import attributes, card_type


# Amiranis Beteli
#
# A fragment of iron-alloy meteorite carefully inscribed and polished. [This object houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# 'Who gave us fire? Who gave us steel? What is the sound of dusk? Of what alloy is wind forged?'
# ---
# I've Read...
#
# Esoteric secrets of metallurgy and resonance are revealed - including directions towards the creation of a terrible Bell.
amiranis_beteli = card_type("amiranis_beteli",
    attributes(tally_price=8, mystery_forge=10, written_in_fucine=1, readable=1, thing=1, tablet=1, subject_bells_and_brazieries=1, dawn_period=1),
    lessons=2,
    provides=memory.the_bells_of_ys,
)


# Kopralith Omphalos
#
# What is this? A tufted fossil of silken fibre, big as a child. [This object houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# Something consumed, and something was consumed. If we interpret its interweavings, we might understand.
# ---
# I've Read...
#
# The meaning of this object isn't something that one reads, but rather something that one follows, until at last one has passed three times around it, and one finds the meaning waiting at one's shoulder.
kopralith_omphalos = card_type("kopralith_omphalos",
    attributes(tally_price=8, written_in_killasimi=1, mystery_moth=10, readable=1, thing=1, dawn_period=1, subject_weaving_and_knotworking=1, tablet=1),
    lessons=2,
    provides=memory.weaving_the_world,
)


# Serpent-Root
#
# A mass of root-stock, shiny with age but still somehow viable. Tiny spidery scratchings, marked with embedded egg-shell shards, encode a cryptic message. [This object houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# Sea-born, tide-drawn, Meniscate-sister, Witch-lover. The House of the Moon will always have its messenger, though its messenger is different each time, in eye and flesh and heart…'
# ---
# I've Read...
#
# Feits, feats, posterns, loopholes, set down against the advent of Eternity by powers favouring imperfection and impermanence.
serpent_root = card_type("serpent_root",
    attributes(tally_price=8, written_in_cracktrack=1, mystery_nectar=10, readable=1, thing=1, dawn_period=1, tablet=1, subject_rites_of_the_roots=1),
    lessons=2,
    provides=memory.loopholes,
)


# The Sun's Design
#
# A scorched slab of black corundum, minutely scratched on every side with intricate ideoglyphs. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# In the city of Emesa, beneath the Church of the Holy Belt, in a sarcophagus of black corundum, Elagabalus lies: accursed of Janus, neither Long nor mortal, neither man nor woman, neither a liar nor a speaker of truth, neither real nor imagined. On his light-suffused skin is made manifest the Sun-in-Splendour's grand design...
# ---
# I've Read...
#
# Elagabalus is the source of one-half of this text. The source of the other-half is obscure, but its power is evident. It is impossible to be certain if the Sun really planned for us to enter Eternity. It is impossible to be sure if the Grail, the Vagabond, and the Forge, stole this birthright from us, or saved us from it. But there is a great secret here.
the_suns_design = card_type("the_suns_design",
    attributes(tally_price=8, written_in_cracktrack=1, mystery_lantern=10, readable=1, thing=1, subject_watchmans_paradoxes=1, dawn_period=1, tablet=1),
    lessons=2,
    provides=memory.the_paths_of_the_sun,
)

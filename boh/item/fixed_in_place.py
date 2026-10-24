from ..model import attributes, card_type


# Aspect of the Axe: Xenodice Half-Faced
#
# One of the more enigmatic aspects of the Horned-Axe: Xenodice Half-Faced, who welcomes or slays strangers at the threshold. Xenodice is sister sometimes to owl and cat, sometimes to bull and butterfly, sometimes to dove and serpent. This hybrid nature suggests a link with the prehuman Carapace Cross - but that's not so surprising in a Name of the Axe.
aspect_of_the_axe_xenodice_half_faced = card_type("aspect_of_the_axe_xenodice_half_faced",
    attributes(knock=2, fixed_in_place=1),
)


# Aspect of the Grail: Lagiah, the Queen Unsated
#
# One of the crueller aspects of the Red Grail: Lagiah, the Queen Unsated, devouring mother, sister-lover of Antaios. One tradition has it that Lagiah took animal form so that she could satisfy her craving to devour her own children, and go unpunished - another that the animal form was the punishment for her incest. The Grail has often been tolerant of contradictions. Perhaps her part in the Intercalate really was, after all, a long and subtle move to undermine Eternity. Or perhaps she's just not to be trusted.
aspect_of_the_grail_lagiah_the_queen_unsated = card_type("aspect_of_the_grail_lagiah_the_queen_unsated",
    attributes(grail=2, fixed_in_place=1),
)


# Aspect of the Malachite: Mylissa, Queen and Palace
#
# One of the kinder aspects of the Malachite: Mylissa, both Queen and Palace, who feeds all comers, whose body is the house in which her children dwell. Mylissa was not always a Name of the Malachite. She may have been a Name of another Hour - she may even have begun among the Carapace Cross, before she chose Eternity over History.
aspect_of_the_malachite_mylissa_queen_and_palace = card_type("aspect_of_the_malachite_mylissa_queen_and_palace",
    attributes(nectar=2, fixed_in_place=1),
)


# Dartboard
#
# The THOCK of the darts punctuated the long evenings and drifted down the corridor to the grilled doors of the cells. (The ex-Tragulari always won, and rather soon, none of the other guards would play with them unless they agreed to a blindfold.)
dartboard = card_type("dartboard",
    attributes(edge=1, moth=1, sky=1, fixed_in_place=1),
)


# HMS Kerisham
#
# A fourth-rate ship of the line captained by Sebastian Dewulf in the Battle of Quiberon Bay. Lost with all hands.
hms_kerisham = card_type("hms_kerisham",
    attributes(edge=1, moon=1, winter=1, fixed_in_place=1),
)


# Key Hooks
#
# All the keys of all the cells still hang here. I can unlock them all at my leisure… but the most significant cells of the Cucurbit were protected by more than locks. (The Least Cells I shouldn't trouble with. The keys to the Most Cells are labelled: ADEPT; LONG; W.I.; and, unhelpfully, ?)
key_hooks = card_type("key_hooks",
    attributes(knock=1, fixed_in_place=1),
)


# Stained Glass Window: the Madrugad
#
# THAT WHICH IS NOT NEEDED, THAT SHALL BE QUENCHED
stained_glass_window_the_madrugad = card_type("stained_glass_window_the_madrugad",
    attributes(forge=1, fixed_in_place=1),
)


# Stained Glass Window: the Meniscate
#
# WHAT IS WITHIN, WITHOUT; WHAT IS WITHOUT, WITHIN
stained_glass_window_the_meniscate = card_type("stained_glass_window_the_meniscate",
    attributes(moon=1, fixed_in_place=1),
)


# Stained Glass Window: the Sun-in-Rags
#
# WHEN IT ENDS, IT WILL BE A BEAUTIFUL ENDING
stained_glass_window_the_sun_in_rags = card_type("stained_glass_window_the_sun_in_rags",
    attributes(winter=1, fixed_in_place=1),
)


# Stained Glass Window: the Watchman
#
# THE WAY IS LIT FOR THE WILLING AND FOR THE UNWILLING
stained_glass_window_the_watchman = card_type("stained_glass_window_the_watchman",
    attributes(lantern=1, fixed_in_place=1),
)

from ..item import candle, fixed_in_place, material, remains, tool
from ..model import attributes, condition, room, slot, station


# Altar of the Knot
#
# History is woven; a knot is a testament.
altar_of_the_knot = station("altar_of_the_knot",
    attributes(evolve_via_bosk=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, moon=1, moth=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, moon=1, moth=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, moon=1, moth=1),
        ),
        slot(
            required=condition(soul=1, omen=1, material=1, mark=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(woven=1, memory=1, material=1, flower=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Abandoned Church
#
# This is a holy place of the Sisterhood of the Triple Knot. The Hours they worshipped are not worshipped now, but those Hours are not dead, nor even sleeping. I should not enter this place without pouring out a sufficient offering.
# ---
# Our Lady Beneath
#
# Who is 'Our Lady'? The Red Grail, which gives life, which takes life, which is not sated? The Horned-Axe, who bears two blades, who waits at the threshold, who sunders that which should not be joined? The Ring-Yew, who is succulent, who is renewed, who encompasseth? Or a fourth, who is always signified but never named?
#
# A Librarian might phrase the question differently: who was first?
our_lady_beneath = room("our_lady_beneath",
    attributes(dawn_period=1),
    inventory = (
        candle.moth_orchid_scented_candle,
        candle.widows_candle,
        candle.widows_candle,
        fixed_in_place.aspect_of_the_axe_xenodice_half_faced,
        fixed_in_place.aspect_of_the_grail_lagiah_the_queen_unsated,
        fixed_in_place.aspect_of_the_malachite_mylissa_queen_and_palace,
        material.ambergris_chunk,
        material.beeswax,
        material.gervinite,
        material.lignum_vitae_blank,
        material.quartz_chunk,
        remains.human_hair,
        tool.mortar_and_pestle,
        tool.shears_of_the_sisterhood,
    ),
    neighbors = ("whispering_stair", "narthex"),
    stations = (
        altar_of_the_knot,
    ),
)

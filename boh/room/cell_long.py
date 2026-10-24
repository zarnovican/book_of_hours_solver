from ..item import uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Long Cell
#
# A bunk-bed constructed for two immortals who could neither be together, nor apart. [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_long_cell = station("guest_bed_long_cell", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(edge=1, interested_in_edge=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Trapped Cell
#
# A sign outside this cell reads WARNING: DO NOT ENTER WHILE SAFETY MEASURES ARE ARMED.
# ---
# Cell: Long
#
# The few Long at Brancrug were kept in cells triple-buttressed with silver and steel and sanctioned spells. The Bureau knew their weaknesses, but never relied upon them. This cell last housed <i>two</i> immortals - an Edge-long dyad. This would have required not only ferocious and eternal vigilance, but also frequent replacement of shattered furniture.
cell_long = room("cell_long",
    attributes(nocturnal_period=1),
    inventory = (
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.bokken_captain_torgue_and_mistress_dearday,
        wall_art.bokken_captain_torgue_and_mistress_dearday,
        wall_art.cudgels_dyddgu_and_st_twrog,
        wall_art.cudgels_dyddgu_and_st_twrog,
        wall_art.wasters_darling_dear_and_father_turk,
        wall_art.wasters_darling_dear_and_father_turk,
    ),
    neighbors = ("cell_adepts", ),
    power_requirements = attributes(edge=13, knock=13),
    stations = (
        guest_bed_long_cell,
    ),
)

from ..item import comfort, liquid, material, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# desk: trist|health + a_letter_to_the_librarian + ink
# An enigmatic Reply to St Rhonwen's Trust
#
#'The sea remains; the House remains; what else remains, we shall learn in time. I am something new, and in time I will learn what that means...'


# desk: mettle + a_letter_to_the_librarian + ink
# A Pragmatic Reply to St Rhonwen's Trust
#
# 'The journey was not straightforward, but here I am. Hush House is empty and peaceful. Nothing walks these halls. If something once did, seven years ago... the fire must have purged it.'


# desk: phost + a_letter_to_the_librarian + ink
# An Inquisitive Reply to St Rhonwen's Trust
#
# 'I am here, but my situation is precarious, and there is so much I do not yet know. Is there anything more you can tell me? Of the House, the locals, their pasts? ...


# Desk: Eva
#
# A magnificent eighteenth-century secretary desk commissioned for Lady Eva Dewulf, last of the Brancrug Dewulfs.
desk_eva = station("desk_eva",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, grail=1, moon=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, grail=1, moon=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, grail=1, moon=1, winter=1),
        ),
        slot(
            required=condition(readable=1, blank=1),
            forbidden=condition(phonograph_record=1, reel_of_film=1),
        ),
        slot(
            required=condition(tool=1, ink=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Gatehouse Stairs
#
# The stairs to the room above are blocked with debris, and the plaster is peeling from the walls. I'll need help from the village to clear and restore the place.
# ---
# Watchman's Tower: First Floor
#
# The notorious Eva Dewulf, first and last Baroness Brancrug, liked this room. Because this side of the house carried fewest memories of her poor father Valentine? So she could eavesdrop on the conversations of visitors waiting below? Or just because of how the pale light slanted through the windows in the last days of winter?
watchmans_tower_first_floor = room("watchmans_tower_first_floor",
    attributes(baronial_period=1),
    inventory = (
        comfort.nightsky_chair,
        comfort.starstrewn_chair,
        liquid.yewgall_ink,
        material.gervinite,
        thing.quire_of_paper,
        thing.walter_dewulf,
        tool.baron_silences_astrolabe,
        tool.mirrorscope,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        wall_art.as_above_so_below,
    ),
    neighbors = ("watchmans_tower_gatehouse", ),
    power_requirements = attributes(forge=2, lantern=2),
    stations = (
        desk_eva,
    ),
)

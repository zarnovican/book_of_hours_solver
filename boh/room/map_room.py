from ..item import comfort, flower, liquid, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Desk: Vagabond
#
# An elegant relic, repurposed by Greene for his small and secret war.
desk_vagabond = station("desk_vagabond",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, knock=1, rose=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, knock=1, rose=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, knock=1, rose=1, scale=1),
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


# Web-Snared Room
#
# The cobwebs here are thick as ivy, clinging to the walls and furniture. Black-furred bodies rustle stickily. Van Lauren was creative here. Many of the spiders are probably only seemings, but the webs are real, and it'll be long and tiresome work clearing away the webs.
# ---
# Map Room
#
# At the turn of the century, Sir David Greene - eighth librarian and former Nocturnal Branch superintendent - had this room refurnished to plan his explorations, and to manage the operations of his many agents.
map_room = room("map_room",
    attributes(curia_period=1),
    inventory = (
        comfort.greenes_red_chair,
        flower.vase_of_roses,
        liquid.catwink,
        thing.hallowed_anthropoderm,
        tool.lunar_globe,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        wall_art.a_sacrifice,
        wall_art.caer_ys,
    ),
    neighbors = ("westcott_room", ),
    power_requirements = attributes(heart=6, rose=6, sky=6),
    stations = (
        desk_vagabond,
    ),
)

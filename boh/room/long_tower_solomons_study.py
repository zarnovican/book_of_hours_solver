from ..item import candle, liquid, material, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Desk: Pale
#
# Solomon Husher himself commissioned this from Lockwood Fen bog-yew, blackened and half-fossilised by centuries underwater. Here at this desk he wrote his doomy allegory of Winter and its romance with the sun. When he blotted the last word on his manuscript and rose from his work, the timber had turned pale as fresh-cut maple. Or so the story goes.
desk_pale = station("desk_pale",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(lantern=1, scale=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(lantern=1, scale=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(lantern=1, scale=1, sky=1, winter=1),
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


# Long Tower: First Floor
#
# The Long Tower looks like it's been abandoned much longer than seven years. In the Nocturnal Period, the inhabitants probably spent most of their time on the seaward side of the Isle. I'll need help to restore the room above.
# ---
# Long Tower: Solomon's Study
#
# In 1818, the Very Reverend Solomon Husher became third Librarian of the Curia of the Isle. He took rooms in the Long Tower as his quarters. Husher's tastes were spartan; although the Curia generally liked a little more luxury, no-one ever quite dared to redecorate the place after his disappearance.
long_tower_solomons_study = room("long_tower_solomons_study",
    attributes(baronial_period=1),
    inventory = (
        candle.chalice_candle,
        candle.widows_candle,
        candle.widows_candle,
        liquid.perinculate,
        material.whispering_sand,
        thing.nivine_parchment,
        thing.solomon_husher,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
    ),
    neighbors = ("st_brandans_cloister", ),
    power_requirements = attributes(lantern=3, winter=3),
    stations = (
        desk_pale,
        # station "fireplace" not mapped on purpose
    ),
)

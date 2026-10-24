from ..item import beverage, candle, comfort, flower, liquid, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Desk: Ambrose
#
# Ambrose did most of his work downstairs in the foundry and kitchen, or upstairs in the laboratory that later became the Fludd Gallery, but it was at this desk that he composed 'The Temptations of Architecture' and wrote long cross letters to the Times about the flaws of the British constitution.
desk_ambrose = station("desk_ambrose",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, knock=1, lantern=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, knock=1, lantern=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, knock=1, lantern=1, sky=1),
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


# Smoking-Room
#
# A tarnished brass sign on the door clearly reads 'SMOKING-ROOM'. Rags of very old smoke sway restlessly, hazing the room beyond: what remains of the protections van Lauren once placed on it. (And yet, still, no sign of a fire.)
# ---
# Westcott Room
#
# 'By God, Sir, we shall have no Cigars in the Library, and we shall have no House without a Smoking-Room.' Dr Ambrose Westcott (1734-1797)
westcott_room = room("westcott_room",
    attributes(curia_period=1),
    inventory = (
        beverage.domaine_raveline_glass,
        candle.small_candlestick,
        candle.small_candlestick,
        candle.tall_candlestick,
        comfort.ambroses_favourite_chair,
        comfort.inviting_footstool,
        flower.vase_of_carnations,
        liquid.ashartine,
        thing.ambrose_westcott,
        thing.cranial_tchotchke,
        thing.cyprians_lamp,
        thing.quire_of_paper,
        thing.strategists_lamp,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        wall_art.finnian,
        wall_art.philemon,
        wall_art.tavish,
        wall_art.the_mansus,
    ),
    neighbors = ("grand_ascent_first_floor", ),
    power_requirements = attributes(forge=5, lantern=5),
    stations = (
        desk_ambrose,
    ),
)

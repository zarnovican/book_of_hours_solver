from ..item import beverage, candle, comfort, liquid, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Desk: Reading Room
#
# The bookwheel is a Dewulf heirloom - a gift to Eva Dewulf from her admirer, the adept Franklin Bancroft. The desk and lectern are much more recent. Steel plaques on both read 'TO GERVINUS VAN LAUREN - IN GRATITUDE FOR HIS ASSISTANCE IN THE CLOSING OF THE WINDING STAIR - E. ABNEY-HASTINGS, NOCTURNAL SECRETARY, 1928'
desk_reading_room = station("desk_reading_room",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, lantern=1, moon=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, lantern=1, moon=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, lantern=1, moon=1, sky=1),
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


# Dimly Lit Chamber
#
# Van Lauren's old protections hang heavy in the air here, clotting the air with shadows. I'll need counter-influences to unwind them.
# ---
# Reading Room
#
# Visitors were usually permitted this far into the House, and no further. In the days when the Librarians commanded the services of the Fine-Takers, visitors were sometimes even left unsupervised.
reading_room = room("reading_room",
    attributes(curia_period=1),
    inventory = (
        beverage.veiled_goddess_lapsang_souchong_cup,
        beverage.veiled_goddess_lapsang_souchong_pot,
        candle.watchful_candle,
        comfort.grand_reading_armchair,
        comfort.imposing_reading_armchair,
        comfort.moon_footstool,
        comfort.moon_footstool,
        comfort.moon_stool,
        comfort.reading_lamp,
        liquid.houndsgall,
        thing.quire_of_paper,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
    ),
    neighbors = ("grand_ascent_ground_floor", ),
    power_requirements = attributes(lantern=5, rose=5),
    stations = (
        desk_reading_room,
    ),
)

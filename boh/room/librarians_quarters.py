from ..item import beverage, candle, codex, comfort, flower, leaf, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Librarian's Quarters
#
# Librarians are prone to back-ache, and the mattress here has always been a hard one, even in Westcott's time.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_librarians_quarters = station("guest_bed_librarians_quarters", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(lantern=1, interested_in_lantern=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Abandoned Librarian's Quarters
#
# A bright haven on the House's seaward side, innocent of protections and menacing influences - though it'll take some work to set it right and clean it.
# ---
# Librarian's Quarters
#
# When the Curia of the Isle acquired the deed to the abandoned Dewulf estate, Ambrose Westcott became first Librarian, and had this cosy nook constructed above the north wing to fit his preferences. His successor Kitty preferred the room next door (she lamented that the reek of Westcott's pipe remained long after his death) and her successor, Solomon Husher, preferred the Long Tower for his own chilly reasons. But most Librarians have enjoyed the peace and the sea view.
librarians_quarters = room("librarians_quarters",
    attributes(curia_period=1),
    inventory = (
        beverage.witching_tisane,
        candle.watchful_candle,
        codex.journal_of_sir_david_greene,
        comfort.librarians_armchair,
        comfort.librarians_footstool,
        flower.pot_of_malachite_daisies,
        flower.potted_pink_orchid,
        flower.potted_white_orchid,
        leaf.potted_avidity,
        leaf.potted_bamboo,
        leaf.potted_fern,
        tool.watering_can,
        thing.fringed_lamp,
        thing.half_faceless_face,
        thing.inscribed_stone,
        thing.librarians_glasses,
        thing.librarians_timepiece,
        thing.pale_bust,
        thing.twinned_fish_stone,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        wall_art.gods_return,
    ),
    neighbors = ("pale_chamber", ),
    power_requirements = attributes(forge=3, heart=3, lantern=3, scale=3),
    stations = (
        guest_bed_librarians_quarters,
        # .. and fireplace
    ),
)

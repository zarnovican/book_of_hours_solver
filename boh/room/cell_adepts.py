from ..item import candle, comfort, thing, tool, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Adept Cell
#
# A bed stamped with sigils to discourage access to the Mansus in dream. [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_adept_cell = station("guest_bed_adept_cell", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(scale=1, interested_in_scale=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Sealed Cell
#
# A sign outside this cell reads WARNING: DO NOT INSERT KEYS WITHOUT FIRST INVOKING ADEQUATE AUTHORISATION. The key is in the Staff-Room, but I shouldn't turn it without invoking powers to provide a reasonable facsimile of authorisation.
# ---
# Cell: Adepts
#
# Seventy-seven days in the Cucurbit was considered enough to soften the passions of the most unrepentant adept. After that, they were usually charged and tried in closed court; very occasionally released; sometimes taken upstairs for one of Collers' experimental interviews.
cell_adepts = room("cell_adepts",
    attributes(nocturnal_period=1),
    inventory = (
        candle.bottled_candle,
        comfort.prison_stool,
        thing.quire_of_paper,
        tool.silent_typewriter,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.aliis_licet_tibi_non_licet,
        wall_art.julian_coseley,
    ),
    neighbors = ("staff_room", ),
    power_requirements = attributes(forge=12, knock=12),
    stations = (
        guest_bed_adept_cell,
    ),
)

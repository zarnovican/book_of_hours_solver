from ..item import beverage, candle, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Solomon
#
# Julian Coseley and Solomon Husher - both great sages of Winter - slept in this bed. Although not simultaneously. No-one, the story runs, has ever managed a serene night's sleep in it since.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_solomon = station("guest_bed_solomon", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(winter=1, interested_in_winter=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Long Tower: Second Floor
#
# Freezing air - even tendrils of fog - drift from the tower top. I should probably seek help from someone who knows the local traditions for dealing with restless spirits.
# ---
# Long Tower: Solomon's Quarters
#
# Generally reckoned the chilliest room in the House. The Long Tower was usually called the Winter Tower until Julian Coseley - magus, epistler, reputed Long - dwelt here briefly in the seventeenth century. Solomon Husher was the second known to sleep in the room. Evidently they didn't mind the cold.
long_tower_solomons_quarters = room("long_tower_solomons_quarters",
    attributes(baronial_period=1),
    inventory = (
        beverage.isle_water_glass,
        candle.widows_candle,
        candle.widows_candle,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        wall_art.the_foundation_of_the_sun,
    ),
    neighbors = ("long_tower_solomons_study", ),
    power_requirements = attributes(lantern=4, winter=4),
    stations = (
        guest_bed_solomon,
    ),
)

from ..item import beverage, cache, candle, comfort, flower, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Servant's Quarters
#
# Narrow, but comfortable. [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_servants_quarters = station("guest_bed_servants_quarters", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(heart=1, interested_in_heart=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Wounded Room
#
# Blood drips from wet-edged cracks in the ceiling here, pooling on the floor. Another rage-fuelled presence that I could use help to lay.
# ---
# Servants' Quarters - North
#
# This was once the private chamber of the formidable Ernestine Peterhans, Seneschale of Brancrug. Baron Hendrik, and afterwards his son Thomas, would both descend the back stairs to visit her in person. For counsel, most said; for prayers, others insisted. Only the very foolish ever suggested there was any improper motive for their visits.
servants_quarters_north = room("servants_quarters_north",
    attributes(baronial_period=1),
    inventory = (
        beverage.dawnlion_coffee_cup,
        beverage.isle_water_glass,
        cache.investigators_suitcase,
        candle.bedside_candleholder,
        candle.weighty_bedside_candleholder,
        candle.widows_candle,
        candle.widows_candle,
        comfort.severe_chair,
        flower.shadowless_silk,
        thing.bolt_of_buttercup_linen,
        uncatalogued.uncatalogued_book_baronial,
        wall_art.shaving_mirror,
    ),
    neighbors = ("kitchen_garden", "servants_quarters_south"),
    power_requirements = attributes(heart=8, knock=8),
    stations = (
        guest_bed_servants_quarters, # 2x
    ),
)

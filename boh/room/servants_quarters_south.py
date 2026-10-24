from ..item import cache, candle, thing
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


# Maze-Crazed Room
#
# Wires are strung tightly and crazily through this room, snaring the bed-legs to the window-latches, the window-latches to the wardrobe-handles. Every movement brings a ripple of musical <i>pings</i>. It'll need time and patience to unravel.
# ---
# Servants' Quarters - South
#
# When Hendrik Dewulf left behind the life of a mercenary, he appointed his quartermaster as head of his new household. This would have drawn little comment, except that his quartermaster was a woman - the soft-spoken, steely-willed Ernestine Peterhans. For more than five decades, these rooms were her unchallenged domain. Even in her eightieth year, she still walked her rounds every day, and the servants would fall silent at the distant jingle of her keys.
servants_quarters_south = room("servants_quarters_south",
    attributes(baronial_period=1),
    inventory = (
        cache.contraband_jetsam,
        cache.slim_parcel,
        candle.widows_candle,
        thing.basket_of_clean_linen,
    ),
    neighbors = ("pantry", ),
    power_requirements = attributes(heart=8, rose=8),
    stations = (
        guest_bed_servants_quarters,
    ),
)

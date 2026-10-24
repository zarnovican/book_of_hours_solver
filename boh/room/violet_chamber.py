from ..item import beverage, candle, comfort, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Violet Chamber
#
# Six generations of Dewulf heirs were born in this room. It would have been seven, but Hafren Waters had the ill grace to give birth to Baron Walter in (family legend has it) a cow-byre outside Kerisham.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_violet_chamber = station("guest_bed_violet_chamber", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(knock=1, interested_in_knock=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Serpent-Haunted Bedroom
#
# Bright-scaled, watchful snakes lie coiled on every surface. I think some of them might be real.
# ---
# Violet Chamber
#
# In the days of the Dewulfs, this chamber was reserved for the lady of the House. Later, the Librarians Willem Harries and Gervinus van Lauren both preferred it to the Librarian's Quarters. Harries established a little shrine to St Agnes in the far corner, and there it remained for many years until van Lauren ordered it to be removed.
violet_chamber = room("violet_chamber",
    attributes(curia_period=1),
    inventory = (
        beverage.strathcoyne_whisky_bottle,
        beverage.strathcoyne_whisky_glass,
        candle.bedside_candleholder,
        candle.watchful_candle,
        comfort.chair_of_challenges,
        comfort.chaise_longue_of_conclusions,
        comfort.violet_stool,
        wall_art.mlle_matutine,
        wall_art.the_first_birth,
    ),
    neighbors = ("severn_chamber", ),
    power_requirements = attributes(knock=6, scale=6),
    stations = (
        guest_bed_violet_chamber,
    ),
)

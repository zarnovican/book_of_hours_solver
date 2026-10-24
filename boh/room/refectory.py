from ..item import candle, flower, thing, wall_art
from ..model import attributes, room


# Rose-Haunted Hall
#
# The room is rife with climbing roses, tangled in the lamps, sprawled across the table. The blossoms are a deep, deep red - one of those colours not often seen in waking life - and their perfume makes my head swim. Another of van Lauren's protections? Or something else? In any case, it'll be arduous, careful work to clear it.
# ---
# Refectory
#
# Here, the whole Curia used to meet - the Librarian, and the Secretaries Salvant, Vigilant and Enigmatic. Sometimes even the Secretary Nunciant, though the duties of that office usually kept him away from the House. But there has only ever been one Secretary Persistent, and she has never liked to eat in company.
#
# That was in the good times of the Curia's heyday. In later years, the Governor of the Gaol would sit at one end, the Librarian at the other, and the clock would tick away the long silences between their words.
refectory = room("refectory",
    attributes(curia_period=1),
    inventory = (
        candle.tall_candlestick,
        candle.tall_candlestick,
        flower.vase_of_lilies,
        flower.vase_of_lilies,
        thing.masquewatch_clock,
        wall_art.night_mirror,
        wall_art.portrait_of_a_behatted_lady,
        wall_art.the_hatching,
    ),
    neighbors = ("mazarine_room", ),
    power_requirements = attributes(grail=7, nectar=7),
    stations = (
        # fireplace
    ),
)

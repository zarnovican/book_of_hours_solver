from ..item import candle, remains, tool
from ..model import attributes, room


# Creeper-Crowded Descent
#
# Leaves, flowers, and thorns. Especially thorns. Could I clear them, I might find something beneath.
# ---
# Well Descent
#
# Rungs line the well's side. This must lead down to the oldest part of the Isle, to the shrines of the Sisterhood. It may be that the servants of the Dewulf family still came here in secret, even while they paid lip service to the rites of the Unconquered Sun.
well_descent = room("well_descent",
    attributes(baronial_period=1),
    inventory = (
        candle.aglaophotis_scented_candle,
        remains.animal_bones,
        tool.shears_of_the_sisterhood,
    ),
    neighbors = ("well", ),
    power_requirements = attributes(moon=8, nectar=8, scale=8),
)

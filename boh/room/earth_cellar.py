from ..item import *
from ..model import attributes, room


# Collapsed Cellar
#
# The roof has fallen in. We'll need to dig it out.
# ---
# Earth Cellar
#
# In the time of the Abbey, this was a shrine to St Lucia the Eyeless. Since the heresies of the Intercalate, the Church of the Unconquered Sun considers her an aspect of the Hour called Meniscate, but back then she was just the patron saint of stained-glass workers and eye doctors. The tree in Earl Brian's Field outside was traditionally hung with stained-glass ornaments on St Lucia's day.
#
# Since the dissolution of the Abbey, though, it's mostly been vegetables in here.
earth_cellar = room("earth_cellar",
    attributes(baronial_period=1),
    inventory = (
        sustenance.basket_of_leeks,
        sustenance.basket_of_onions,
        sustenance.basket_of_vegetables,
        sustenance.basket_of_vegetables,
    ),
    neighbors = ("stair_tenebrous", "wine_cellar"),
    power_requirements = attributes(heart=11, nectar=11, scale=11),
)

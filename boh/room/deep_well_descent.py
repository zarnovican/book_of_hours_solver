from ..item import cache, material
from ..model import attributes, room


# Root-Thronged Descent
#
# The roots here are a labyrinth of years. How long is it since anyone passed this way?
# ---
# Deep Well Descent
#
# Each of the great roots here carries a garden of fruiting fungus. Great black bumblebees buzz improbably between them, gathering spores, droning peace.
deep_well_descent = room("deep_well_descent",
    attributes(baronial_period=1),
    inventory = (
        material.atlantic_amber,
        material.sand,
        cache.tall_parcel,
    ),
    neighbors = ("well_descent", ),
    power_requirements = attributes(heart=9, nectar=9, scale=9),
)

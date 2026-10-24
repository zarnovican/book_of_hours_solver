from ..item import beverage, comfort, device, flower, thing, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Infirmary
#
# Clean white sheets and the unmistakable military <i>ping</i> of a steel bed-frame. [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_infirmary = station("guest_bed_infirmary", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(heart=1, interested_in_heart=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Infirmary
#
# Careless visitors have tracked in mud through the door, and the windows have been open to the elements for years.
# ---
# Infirmary
#
# In the fifteenth century, Natan of Regensburg came to Brancrug. The brothers of St Brandan's granted sanctuary, but they would not permit a Jew - and his family! - to live on abbey grounds. Still they built this tower for him to dwell in and practice his healing arts. It has changed greatly since that time, but a place of healing it remains.
infirmary = room("infirmary",
    attributes(baronial_period=1),
    inventory = (
        beverage.mist_kissed_water_pitcher,
        beverage.rubywise_ruin,
        beverage.serpent_milk,
        beverage.trn_limited_drinking_cocoa_cup,
        beverage.trn_limited_drinking_cocoa_cup,
        beverage.trn_limited_drinking_cocoa_pot,
        comfort.pale_stool,
        comfort.watchful_potted_plant,
        comfort.wicker_chair,
        device.pale_mommet,
        flower.vase_of_lilies,
        thing.basket_of_towels,
        thing.musgrave_dewulf,
        wall_art.the_sister_and_witch,
        wall_art.the_thunderskin,
        wall_art.the_velvet,
        wall_art.the_witch_and_sister,
    ),
    neighbors = ("physic_garden", ),
    power_requirements = attributes(heart=4, rose=4),
    stations = (
        guest_bed_infirmary,
    ),
)

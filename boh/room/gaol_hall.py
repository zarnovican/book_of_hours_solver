from ..item import beverage, comfort, thing, tool, uncatalogued
from ..model import attributes, room


# Worm-Eaten Hall
#
# This place bears the unmistakable traces of Worms - the 'serpents which are no serpents'. They are almost certainly gone... but we'll take no chances. Worms are difficult to evict from buildings, but much harder to evict from people.
# ---
# Gaol Hall
#
# Here the guards and the prisoners would take their meals. Sometimes Collers, too, would descend from his tower and discuss philosophy with poisoners, ethics with Antaians, theology with labhites. Afterwards he would generally burn his notes.
gaol_hall = room("gaol_hall",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.dawnlion_coffee_cup,
        beverage.dawnlion_coffee_cup,
        beverage.isle_water_glass,
        beverage.isle_water_glass,
        beverage.isle_water_pitcher,
        comfort.spartan_chair,
        thing.lacquered_bone_chess_set,
        tool.mop_and_bucket,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
    ),
    neighbors = ("gaol_yard", ),
    power_requirements = attributes(forge=11, moth=11, winter=11),
)

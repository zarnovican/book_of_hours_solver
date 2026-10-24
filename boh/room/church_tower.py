from ..item import beverage, comfort, tool, uncatalogued
from ..model import attributes, room


# Ill-Omened Tower
#
# The stairway has been chained off - more than chained off. The whole thing is wrapped or swathed in chains. Authoritative sigils forbid entry.
# ---
# Church Tower
#
# The bells in this tower rang every Sunday, even in Solomon Husher's time, until Thirza Blake finally cancelled services so she could save money by sacking the priest. This brought a deputation of angry locals from Brancrug Village, where there was a fearful superstition that when the bells of Brancrug fell silent, the bells of Ys would be heard.
church_tower = room("church_tower",
    attributes(solar_gothic_period=1),
    inventory = (
        beverage.veiled_goddess_lapsang_souchong_cup,
        beverage.veiled_goddess_lapsang_souchong_pot,
        comfort.bell_tower_chair,
        tool.mop_and_bucket,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
    ),
    neighbors = ("windlit_gallery", ),
    power_requirements = attributes(forge=9, lantern=9, sky=9),
)

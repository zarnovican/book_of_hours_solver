import boh
from boh.item import *
from boh.state import state


def test_count():
    s = state()

    s.inventory_add(
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
        beverage.isle_water_glass,
    )
    s.inventory_remove(beverage.ch_second_flush_assam_cup)
    s.inventory_add(
        beverage.isle_water_glass,
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
    )
    s.inventory_remove(beverage.isle_water_glass)
    s.inventory_add(beverage.isle_water_glass)
    s.inventory_remove(beverage.ch_second_flush_assam_cup)
    s.inventory_add(beverage.isle_water_glass)

    assert s.inventory_card_count(beverage.ch_second_flush_assam_cup) == 2
    assert s.inventory_card_count(beverage.isle_water_glass) == 3

from ..item import candle, comfort, flower, leaf, mark, material, thing, uncatalogued, wall_art
from ..model import attributes, room


# Glaring Room
#
# This has long been a holy place, but now the Sun-in-Rags has withdrawn his peace from it, and the light here cannot be borne. In the day the sun's light dazzles, in the night the moon's light freezes. Only once a peace has been laid on the room will I be able to enter safely.
# ---
# Solarium
#
# This room was once for the meditation of favoured visionaries. Here White Matilda prophesied the victory of the Iron King in the Wars of the Roads, much as it would occur three hundred years later. (She got his name wrong, though.)
solarium = room("solarium",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.tall_candlestick,
        candle.tall_candlestick,
        comfort.contemplative_seat,
        comfort.paradise_palm,
        comfort.restful_seat,
        flower.potted_pink_orchid,
        leaf.potted_bamboo,
        leaf.potted_snake_plant,
        mark.bisclavrets_knot,
        material.awakened_feather,
        thing.ninewink_clock,
        thing.willem_harries,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        wall_art.sol_invictis_symbol,
    ),
    neighbors = ("church_tower", ),
    power_requirements = attributes(heart=10, lantern=10, winter=10),
)

from ..item import candle, comfort, fixed_in_place, flower, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Instrument: Organ
#
# 'One must practice slowly, then more slowly, and finally slowly.'' - Camille Saint-Saens
instrument_organ = station("instrument_organ",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1, instrument=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, sky=1),
        ),
        slot(
            required=condition(soul=1, sound=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Solar Altar
#
# The Sun-in-Splendour is the Hour which was sundered; the Hour which is not conquered; the Hour from which proceed all the other Hours of the day. Or so the Church teaches.
solar_altar = station("solar_altar",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(lantern=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(lantern=1, sky=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(lantern=1, sky=1, winter=1),
        ),
        slot(
            required=condition(soul=1, omen=1, mark=1, light=1),
            #required=condition(soul=1, omen=1, mark=1, light=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(pigment=1, lens=1, gem=1, memory=1, light=1, fuel=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Darkened Church
#
# This has long been a holy place, but shadows are the only worshippers here now. The windows have been painted black, the pews overturned, the organ hung with black ribbons.
# ---
# Nave of the Abbey Church
#
# For a thousand years the Unconquered Sun has been worshipped here in all his Aspects - though since the heresies of the Intercalate, many of those aspects are considered distinct Hours in their own right, and the Sun's death and birth are both now celebrated.
#
# The Abbey Church used to be more golden, but many of the valuables were lost at the Abbey's dissolution, including the original stained glass. These magnificent windows are of recent manufacture, financed by the eighth Librarian, Greene, who was a believer of the Second Dawn variety.
nave_of_the_abbey_church = room("nave_of_the_abbey_church",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.small_candlestick,
        candle.small_candlestick,
        candle.small_candlestick,
        candle.small_candlestick,
        candle.small_candlestick,
        candle.small_candlestick,
        comfort.uncomfortable_seat,
        comfort.uncomfortable_seat,
        comfort.uncomfortable_seat,
        fixed_in_place.stained_glass_window_the_madrugad,
        fixed_in_place.stained_glass_window_the_meniscate,
        fixed_in_place.stained_glass_window_the_sun_in_rags,
        fixed_in_place.stained_glass_window_the_watchman,
        flower.vase_of_amaryllis,
        flower.vase_of_lilies,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        wall_art.sol_invictis_symbol,
    ),
    neighbors = ("atrium", ),
    power_requirements = attributes(heart=6, lantern=6),
    stations = (
        instrument_organ,
        solar_altar,
    ),
)

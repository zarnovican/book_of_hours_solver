from ..item import beverage, candle, liquid, material, thing, remains, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Nocturnary
#
# Constructed by Thirza for her own murky purposes; maintained by the Suppression Bureau for its murkier ones; and available, now, for mine.
nocturnary = station("nocturnary",
    attributes(evolve_via_skolekosophy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, moon=1, nectar=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, moon=1, nectar=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, moon=1, nectar=1, winter=1),
        ),
        slot(
            required=condition(soul=1, wood=1, pigment=1, device=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, liquid=1, remains=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Shrouded Space
#
# If the wards on this place were real, they would be heavy curtains of black velvet that stung the grazing hand. They aren't real in any meaningful sense of the word. I'll still need to dispose of them before I can enter safely.
# ---
# Night Gallery
#
# In the 1850s, and in deep secrecy, Natalia Brulleau built the Night Gallery into the foundations of the Gullscry Tower. Behind this heavy steel door the Curia, and later the Suppression Bureau, kept treasures too difficult for common view, but too relevant to consign to a deeper vault. If anything difficult might, hypothetically, have been inclined to creep up the stairs from below, it would also have been discouraged by that door.
night_gallery = room("night_gallery",
    attributes(curia_period=1),
    inventory = (
        beverage.leathy,
        beverage.thirzas_cordials,
        candle.honeyscar_scented_candle,
        liquid.gideons_soaks,
        material.arsenic,
        material.rose_pearl,
        material.whispering_sand,
        remains.urn_of_ashes,
        thing.thomas_dewulf,
        uncatalogued.uncatalogued_book_curia,
        wall_art.a_bargain,
        wall_art.as_above_so_below,
        wall_art.chac,
        wall_art.crowcross_sands_at_high_tide,
        wall_art.leaves_in_the_wind,
        wall_art.our_benefactor,
        wall_art.our_benefactress,
        wall_art.the_boy_prays,
        wall_art.the_first_answer,
        wall_art.the_first_end,
        wall_art.the_wheel_still_turns,
    ),
    neighbors = ("vestibulum_transitus", ),
    power_requirements = attributes(moon=10, winter=10),
    stations = (
        nocturnary,
    ),
)

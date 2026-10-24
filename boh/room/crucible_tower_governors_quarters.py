from ..item import beverage, codex, comfort, material, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Governor's Phonograph
#
# Collers generally preferred his devices to be as gleamingly modern as possible, but he preferred phonograph cylinders over the newer gramophone records. The cylinder, like the records, exemplified ingenuity and reliably repeated the desired sounds, but they also could be consigned neatly to a cubbyhole without causing any sort of fuss.
governors_phonograph = station("governors_phonograph",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, rose=1, scale=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, rose=1, scale=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, rose=1, scale=1, sky=1),
        ),
        slot(
            required=condition(phonograph_record=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Sculptor's Bench
#
# Labour seriously.
sculptors_bench = station("sculptors_bench",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, knock=1, lantern=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, knock=1, lantern=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, knock=1, lantern=1, scale=1),
        ),
        slot(
            required=condition(stone=1, made_of_wood=1, woven=1, remains=1, tool=1, ductile=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(ductile=1, tool=1, remains=1, stone=1, made_of_wood=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Stifling Chamber
#
# No fires are visible, no scorch marks, no smoke, but this room pulses with sultry heat. My head swims as I approach the threshold.
# ---
# Crucible Tower: Governor's Quarters
#
# In this room, the Governor was Collers the artist, Collers the dreamer. It was a side of him that almost no-one saw, especially when, after the death of his wife, he grew so much more solitary. That said, there is a connection to be drawn between his enthusiasm for sculpture, and his ambitions for his human subjects.
crucible_tower_governors_quarters = room("crucible_tower_governors_quarters",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.armagnac_dys_glass,
        codex.towards_a_fundamental_aesthetic,
        comfort.librarians_stool,
        material.arsenic,
        thing.gervinus_van_lauren,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.lady_tryphon,
    ),
    neighbors = ("crucible_tower_governors_office", ),
    power_requirements = attributes(forge=13, winter=13),
    stations = (
        governors_phonograph,
        sculptors_bench,
    ),
)

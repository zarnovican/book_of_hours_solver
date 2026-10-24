from ..item import comfort, liquid, material, remains, uncatalogued
from ..model import attributes, condition, room, slot, station


# Necropsy Table
#
# A hygienic place for scrupulous examination of whatever might remain.
necropsy_table = station("necropsy_table",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, knock=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, knock=1, scale=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, knock=1, scale=1, winter=1),
        ),
        slot(
            required=condition(carcass=1, tool=1, material=1, remains=1),
            #forbidden=condition(fatigued=1),   # TODO (???) yeth_hound_horns (carcass+wall_art) is consumed in necropsy table slot.. but only one! (random?)
            forbidden=condition(fatigued=1, wall_art=1),
        ),
        slot(
            required=condition(carcass=1, tool=1, material=1, remains=1),
            #forbidden=condition(fatigued=1),
            forbidden=condition(fatigued=1, wall_art=1),
        ),
    ),
)


# Gloomy Room
#
# The window of this room is coated thickly with black paint. A little light seeps through. Otherwise, the room is dark. Very faintly, I can still smell rotting meat.
# ---
# Examination Room
#
# Hendrik Dewulf evicted the family of the healer Natan from the Barber's Tower - as it was then called. ('I have rooted out the barber's brood,' he is recorded to have gloated.) But his great-great-grandson Gideon - 'the Motley Baron', for his brindled hair - restored the Tower and made it a place of healing again.
#
# Of course the equipment in this room dates from the current century. But Gideon's other nickname was 'the Cutter'. It was rumoured that he bought corpses for dissection - even that he was a vivisectionist. The latter was probably a slander, but one way or another, scholars have been cutting up corpses in here for a very long time.
examination_room = room("examination_room",
    attributes(baronial_period=1),
    inventory = (
        comfort.morgue_boots,
        liquid.bucket_of_seawater,
        material.phosphorescent_scrapings,
        material.serpentinite_slab,
        remains.essential_periost,
        remains.heart_in_a_jar,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
    ),
    neighbors = ("grand_ascent_third_floor", "infirmary", "patients_lounge"),
    power_requirements = attributes(edge=5, heart=5),
    stations = (
        necropsy_table,
    ),
)

from ..item import beverage, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Projector
#
# Governor Collers had this installed in the 20s, as a treat for prisoners allowed to recover in the infirmary. Or so he said. Rumour had it he was a secret Keaton fan, and didn't want to motor all the way up to Exeter to see the latest feature.
projector = station("projector",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(forge=1, grail=1, lantern=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, grail=1, lantern=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(forge=1, grail=1, lantern=1, sky=1),
        ),
        slot(
            required=condition(reel_of_film=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Neglected Room
#
# The room above might once have been some sort of lounge, but the furniture and equipment has been smashed and overturned; the walls are streaked with mildew. An unlovely smell wafts from further up.
# ---
# Patients' Lounge
#
# In this room, the accursed of the Great War gathered to recuperate - those who had suffered something no more horrible, but somewhat more mysterious, than the War's usual wounds to body and spirit - an irruption of Worms, perhaps, or the risks at the military end of Suppression Bureau activities. Among them were minor luminaries of the invisible world - Christopher Illopoly, Zachary Wakefield, Harvey Hattington. But not Brian Levinsen, who had been ninth Librarian, and under whose tenure the Infirmary had flourished. He enlisted; he served for a time as a medical officer on the Western Front; his body was never found.
patients_lounge = room("patients_lounge",
    attributes(baronial_period=1),
    inventory = (
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_cup,
        beverage.ch_second_flush_assam_pot,
        thing.lacquered_bone_chess_set,
        uncatalogued.uncatalogued_book_nocturnal,
    ),
    neighbors = ("infirmary", ),
    power_requirements = attributes(grail=5, heart=5),
    stations = (
        projector,
    ),
)

from ..item import comfort, material, thing, wall_art
from ..model import attributes, room


# Entrance Hall
#
# The beginning of the House proper. The Curia used to issue gloves and slippers of soft leather to protect the books and premises. Visitors were often asked to remove their shoes. Pause a moment and listen to the Histories.
# ---
# The First True Threshold
#
# I have reached the threshold of the House proper. The Librarians of the Curia were scholars of note - some were potent adepts. From here I should proceed carefully, observing the proper forms, making the appropriate offerings. The villagers and other locals know the ways of the earth and sea hereabouts. Their assistance will be invaluable.
entrance_hall = room("entrance_hall",
    attributes(baronial_period=1),
    inventory = (
        comfort.authority,
        comfort.lady_de_braose,
        comfort.lady_rowena,
        material.lignum_vitae_blank,
        thing.abbot_geffrey,
        thing.abbot_thomas,
        thing.hendrik_dewulf,
        thing.sister,
        thing.st_melancthe,
        thing.valentine_dewulf,
        wall_art.crowcross_sands_at_high_tide,
        wall_art.leaves_in_the_wind,
        wall_art.leaves_in_the_wind,
        wall_art.the_boy_prays,
    ),
    neighbors = ("st_brandans_cloister", ),
    power_requirements = attributes(knock=3, rose=3),
)

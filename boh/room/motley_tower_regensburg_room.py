from ..item import cache, candle, comfort, material, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Desk: Natan
#
# It's an apothecary's desk, all right, but it dates from at least a hundred years after Natan of Regensburg came here. Of course his son, his grandson, and his great-grand-son were all Natans too…
desk_natan = station("desk_natan",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, knock=1, moth=1, rose=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, knock=1, moth=1, rose=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, knock=1, moth=1, rose=1),
        ),
        slot(
            required=condition(readable=1, blank=1),
            forbidden=condition(phonograph_record=1, reel_of_film=1),
        ),
        slot(
            required=condition(tool=1, ink=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Guest Bed: Motley
#
# An exile slept here, long ago.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_motley = station("guest_bed_motley", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(moth=1, interested_in_moth=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Motley Tower: Third Floor
#
# The theoplasmic miasma that hung around the room below is a little stronger here, and a little different, with a rotten, musky scent that suggests a decaying reptile house. Perhaps something laired here after the inhabitants departed; perhaps the inhabitants dreamed unwisely. In any case, the right counter-influences will dispel it.
# ---
# Motley Tower: Regensburg Room
#
# The physician Natan lived here in the fifteenth century - and his family after that, tolerated by the monks - until King Henry dissolved the foundation and granted the Isle to Hendrik. Hendrik turfed them out of the tower and furnished the place more to his own taste. But when Christopher Illopoly moved in four hundred years later, he restored what he could. Illopoly wrote at the time of his sympathy, as a rootless foundling, for the outcast Natan: <i>'I don't know what I am, but I don't think I'm English.'</i>
motley_tower_regensburg_room = room("motley_tower_regensburg_room",
    attributes(baronial_period=1),
    inventory = (
        cache.bag_of_tricks,
        candle.weighty_bedside_candleholder,
        comfort.wine_dark_chair,
        material.gervinite,
        thing.quire_of_paper,
        thing.reference_image,
        thing.regensburg_menorah,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        wall_art.our_benefactor,
        wall_art.our_benefactress,
        wall_art.storm_tossed_mirror,
    ),
    neighbors = ("motley_tower_dispensary", ),
    power_requirements = attributes(heart=6, sky=6),
    stations = (
        desk_natan,
        guest_bed_motley,
    ),
)

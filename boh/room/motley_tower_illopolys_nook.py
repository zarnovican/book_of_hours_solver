from ..item import comfort, leaf, liquid, remains, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station


# Barber's Chair
#
# No-one emerges unchanged from a barber's chair. Perhaps they'll just be a little bit more beautiful.
barbers_chair = station("barbers_chair",
    attributes(evolve_via_preservation=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, grail=1, moth=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, grail=1, moth=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, grail=1, moth=1),
        ),
        slot(
            required=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Motley Tower: First Floor
#
# The door jams half-open, but the room above is a bright oasis after the dreary neglect of the lower tower. The previous occupant has probably left some sort of protections in place. I'll find somebody suitably qualified to deal with them.
# ---
# Motley Tower: Illopoly's Nook
#
# Christopher Illopoly - poet, painter, archivist, ruiner of seances - stayed on for a while at Hush House after the Great War. The Librarian, Serena Blackwood, arranged rooms for Illopoly in the Motley Tower, ostensibly so he could help with the collection, but perhaps also because she saw a potential ally against the Governor of the Cucurbit... relations between the Cucurbit and the House were badly strained at the time.
motley_tower_illopolys_nook = room("motley_tower_illopolys_nook",
    attributes(baronial_period=1),
    inventory = (
        comfort.elegant_sunburst_lamp,
        comfort.russet_couch,
        leaf.vase_of_rushes,
        liquid.holiest_hemolymph,
        liquid.perhibiate,
        remains.urn_of_ashes,
        thing.fraser_strathcoyne,
        thing.red_lotus_vase,
        thing.twilight_pot,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.again_at_night,
        wall_art.love_in_a_quiet_place,
        wall_art.red_blue,
        wall_art.sedona_not_yet,
        wall_art.to_be_fruitful,
        wall_art.to_hear_those_voices,
    ),
    neighbors = ("patients_lounge", ),
    power_requirements = attributes(heart=5, moth=5),
    stations = (
        barbers_chair,
    ),
)

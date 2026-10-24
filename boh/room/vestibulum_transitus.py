from ..item import leaf, mark, remains, uncatalogued
from ..model import attributes, room


# Rattling Bridge
#
# Each time the wind makes its rounds, the whole bridge shakes. On its threshold, there's a serpentine knot-mark in browned blood. The mark is fading, but it still trembles with the power of the spirit that waits in it - a great servant of the old House, perhaps the last of the Fine-Takers themselves. I must pacify it with a suitable offering before I can pass.
# ---
# Vestibulum Transitus
#
# 'Vestibulum Transitus' was the wry name the Curia gave this structure. Before that it was 'Valentine's Bridge', the sheltered crossing beyond which Baron Valentine's solitude was assured.
vestibulum_transitus = room("vestibulum_transitus",
    attributes(baronial_period=1),
    inventory = (
        leaf.vase_of_gorse,
        leaf.vase_of_gorse,
        mark.year_tally,
        remains.urn_of_ashes,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
        uncatalogued.uncatalogued_book_solar,
    ),
    neighbors = ("duelling_hall", ),
)

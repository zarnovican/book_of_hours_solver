from ..item import beverage, candle, codex, comfort, flower, leaf, material, sustenance, thing, uncatalogued, wall_art
from ..model import attributes, condition, room, slot, station
from .. import station as station_module


# bed: soul.health
# Camp
#
# I'll make this my lodgings for the time being. [Move your belongings into this room; you can then use this bed to rest Soul cards and recover Maladies.]
# ---
# Camp
#
# This is a safe place for me now... to the extent that dreams are safe.


# bed: soul.health
# Decamp
#
# Hush House is a mansion of many rooms. I'll move to a different one. [Or add other cards if you'd like to try something else.]
# ---
# Decamp
#
# Gathered my belongings, refreshed the sheets for any guests I might have. Ready to move on.


# bed: memory
# Dream on a Memory
#
# Now that night has fallen, I can rest - and perhaps dream on the day's doings. [Dreaming on a Memory will preserve it past Dawn, allowing you to keep it until the following day.]""",
# ---
# Dream on a Memory
#
# I've carried a Memory like a flambeau safe through the mazes of night. [This will complete once dawn has come.]""",


# bed: fatigued soul + beverage|restorative
# Rest
#
# A quick nap in a warm bed with something comforting to drink, while the winds chase the clouds and the clouds chase the sun. [Restore a fatigued Soul card.]
# ---
# Rest
#
# I deserved a little quiet time.


# bed: malady soul + skill + restorative
# Cure my Malady
#
# [You've supplied enough Heart.]
# ---
# Cure my Malady
#
# Time, peace, recovery.


# Guest Bed: Lodge
#
# Stout, rustic, snug.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_lodge = station("guest_bed_lodge", attributes(),
    # TODO (bed model) powers (scale, forge, knock, heart)
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(heart=1, interested_in_heart=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Lodge at the Gate
#
# A cottage where Hush House's groundskeeper lived - until the fire. If I can get into the place and make it habitable, I can use it as a base for reclaiming more of the House.
# ---
# Keeper's Lodge
#
# For five hundred years - in the times we call Baronial, Curia, Nocturnal - there was always a keeper to watch the ways, weed the gardens, mend the roof when the sun was shining. There is no keeper now, but the Lodge's roof still weathers the storms of Brancrug Bay.
keepers_lodge = room("keepers_lodge",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        candle.honeyscar_scented_candle,
        codex.travelling_at_night_vol_1,
        codex.travelling_at_night_vol_2,
        comfort.straw_cushioned_chair,
        flower.shadowless_silk,
        leaf.ch_second_flush_assam_packet,
        leaf.potted_dragon_tree,
        material.dawnlion_coffee_packet,
        sustenance.pillas_oat_bread,
        thing.basket_of_clean_linen,
        thing.hush_house_key,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_nocturnal,
        wall_art.fractured_mirror,
        wall_art.shaving_mirror,
    ),
    neighbors = ("cucurbit_bridge", ),
    power_requirements = attributes(forge=2, heart=1, knock=1),
    stations = (
        guest_bed_lodge,
        station_module.lodge_fireplace,
        station_module.serve_here,
    ),
)

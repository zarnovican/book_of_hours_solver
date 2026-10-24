from ..item import beverage, candle, comfort, liquid, thing, uncatalogued
from ..model import attributes, condition, room, slot, station


# Guest Bed: Severn Chamber
#
# For those who prefer their mattresses soft.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_severn_chamber = station("guest_bed_severn_chamber", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(grail=1, interested_in_grail=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Thirza's Phonograph
#
# Thirza Blake invited a nameless friend (or according to Brancrug tradition, her sister) to Hush House to recover from an illness. Thirza was uncharacteristically secretive about the whole business, perhaps because her own solicitude embarrassed her. She cooked her guest's meals herself; read to her in the afternoons; and purchased this phonograph so her guest could listen to Viennese opera.
thirzas_phonograph = station("thirzas_phonograph",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(heart=1, knock=1, moon=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(heart=1, knock=1, moon=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(heart=1, knock=1, moon=1, sky=1),
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


# Abandoned Bedroom
#
# A crooning whisper haunts this room. It must once have been luxurious, and will be again once I have it restored, but I will need help to lay the restless presence that drifts here.
# ---
# Severn Chamber
#
# In the days of the Dewulfs, this chamber was reserved for the heir of the House - though it was originally furnished for Hafren, the woman of 'uncertain lineage' who became Baron Walter's mother and bequeathed her unusual pale eyes and hair to Walter and his descendants.
severn_chamber = room("severn_chamber",
    attributes(curia_period=1),
    inventory = (
        beverage.veiled_goddess_lapsang_souchong_cup,
        candle.bedside_candleholder,
        candle.moth_orchid_scented_candle,
        comfort.nighted_chair,
        liquid.ashartine,
        thing.abduction_salvation,
        thing.fringed_lamp,
        thing.fringed_lamp,
        uncatalogued.uncatalogued_book_baronial,
        uncatalogued.uncatalogued_book_curia,
        uncatalogued.uncatalogued_book_curia,
    ),
    neighbors = ("grand_ascent_second_floor", ),
    power_requirements = attributes(moon=5, rose=5),
    stations = (
        guest_bed_severn_chamber,
        thirzas_phonograph,
    ),
)

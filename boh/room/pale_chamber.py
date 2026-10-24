from ..item import beverage, comfort, flower, thing, wall_art
from ..model import attributes, condition, room, slot, station


# Guest Bed: Pale
#
# Seven generations of Dewulfs slept here… as did Kitty Mazarine, who never cared much for tradition.  [Use a matching Soul card to move your belongings in and make this your bed; or place a matching Visitor card to encourage them to stay a little longer.]
guest_bed_pale = station("guest_bed_pale", attributes(),
    slots = (
        slot(
            essential=condition(occupant=1),
            required=condition(sky=1, interested_in_sky=1),
            forbidden=condition(fatigued=1, malady=1, from_numa=1),
        ),
    ),
)


# Icy Bedroom
#
# A thick and freezing murk, like a clinging black mist, roils at floor level. Not theoplasma exactly - the ragged remnants of some chilly Wood-thing? Or a good old-fashioned ghost, decayed to half-elemental energies? Some local will probably know.
# ---
# Pale Chamber
#
# In the time of the Dewulfs, this magnificent bedroom was reserved for the Baron... or in Lady Eva's time, the Baroness. Eva had the whole room decorated in black as a gesture of permanent mourning for her father Valentine (or, according to ribald rumours, to set off her own paleness for her lovers). It was Kitty Mazarine, much later, who freshened the furnishings and made it the Pale Chamber.
pale_chamber = room("pale_chamber",
    attributes(curia_period=1),
    inventory = (
        flower.vase_of_golden_bulrushes,
        flower.vase_of_golden_bulrushes,
        thing.daybreak_clock,
        beverage.armagnac_dys_bottle,
        comfort.sea_green_sofa,
        wall_art.self_born,
        thing.thirza_blake,
    ),
    neighbors = ("violet_chamber", ),
    power_requirements = attributes(moth=7, winter=7),
    stations = (
        guest_bed_pale,
        # ..plus fireplace
    ),
)

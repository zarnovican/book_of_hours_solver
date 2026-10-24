from ..model import attributes, condition, room, slot, station


# Pumps: Lower Level
#
# These machines are of different and newer manufacture than the ones above. They include something like a generator, too. But they're in even worse condition. I'll need to provide suitable materials and fuel - and I'll need Scholar-level of Forge to jury-rig them.
pumps_lower_level = station("pumps_lower_level",
    attributes(scholar_level_challenges=1),
    slots = (
        slot(
            essential=condition(skill=1),
            required=condition(forge=1, knock=1),
        ),
        slot(
            essential=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            essential=condition(liquid=1, fuel=1, logical_and=True),
        ),
        slot(
            essential=condition(metal=1),
        ),
        slot(
            essential=condition(metal=1),
        ),
    ),
)


# Flooded Level
#
# Gleaming black water, still as bone. I'll need to find some way to lower the water level before I can descend.
# ---
# Lower Pump Room
#
# The Curia installed these pumps when the lower levels of the Sisterhood's holy place were already dry. Why? What were they looking for? What lies beneath Brancrug Isle that even the Sisterhood never found?
lower_pump_room = room("lower_pump_room",
    attributes(dawn_period=1),
    neighbors = ("upper_pump_room", ),
    stations = (
        pumps_lower_level,
    ),
)

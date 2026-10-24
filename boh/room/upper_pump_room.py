from ..model import attributes, condition, room, slot, station


# Pumps: Upper Level
#
# The Curia installed these pumps to drain the lower levels - but they installed them in the late nineteenth century. I'll need to provide suitable materials and fuel - and I'll need a Prentice-level of Forge to jury-rig them.
pumps_upper_level = station("pumps_upper_level",
    attributes(prentice_level_challenges=1),
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


# Room of Rusts
#
# The ceiling has collapsed. Rusting machinery pokes out here and there through the rubble.
# ---
# Upper Pump Room
#
# See the pickaxe marks on the walls. Before the Sisterhood came to the Isle, the Romans or the Phoenicians dug these tunnels, scratching in the ground for tin and for gold. For centuries those pumps kept the sea at bay, driven by slaves or votaries who saw the sun one day in nine. When those pumps fell silent, the sea crept in - until, much later, the Curia brought in their own machines to open up the lower levels again.
upper_pump_room = room("upper_pump_room",
    attributes(dawn_period=1),
    neighbors = ("sacred_spring", ),
    power_requirements = attributes(forge=11, scale=11),
    stations = (
        pumps_upper_level,
    ),
)

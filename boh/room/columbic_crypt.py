from ..model import attributes, condition, room, slot, station


# Columbic Sarcophagus
#
# 'Sarcophagus': the eater of flesh. No bones remain, but the marble is chilly with power.
columbic_sarcophagus = station("columbic_sarcophagus",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moth=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moth=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moth=1, winter=1),
        ),
        slot(
            required=condition(soul=1, remains=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, remains=1, pigment=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Fluttering Crypt
#
# The darkness here beats with wings. Bats? The sound is more like birds, but there is a timpani quality that suggests more bones than feathers. One more step, and I sense the possibility of talons.
# ---
# Columbic Crypt
#
# <i>St Columba, with twelve companions, brought the word of the Unconquered Sun to Scotland, where he founded a monastery on the blessed isle of Iona. There he died and there his bones remained until the Northmen came.
#
# But in Cornwall they speak of his thirteenth companion, a 'hybrid beauty' called Rowena who was perhaps his tutor, perhaps his seducer, or perhaps his daughter. At his death, the monks sought to stone her for her impurities. She bore Columba's bones away so the monks would not have them - substituting, out of tact or mischief, the bones of a horse. She brought the bones to a hidden Isle, where she made a double foundation of nuns and monks, and became its first abbess: but she would admit none to her order who was a virgin, nor innocent of any crime. Since then, the Isle has been a refuge for all the world might consider impure.</i>
columbic_crypt = room("columbic_crypt",
    attributes(dawn_period=1),
    neighbors = ("lower_pump_room", ),
    power_requirements = attributes(moon=15, winter=15),
    stations = (
        columbic_sarcophagus,
    ),
)

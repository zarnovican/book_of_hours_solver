from ..model import attributes, condition, room, slot, station


# Rowenarium

# Rowena the Ligeian, protectress of the House, holds the Mare's Key of worm-stone, which opens the door to Nowhere. Now and then, she has lent it unwisely. But only once has she lent it to Ys.
rowenarium_station = station("rowenarium",
    attributes(evolve_via_skolekosophy=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, moth=1, rose=1, winter=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, moth=1, rose=1, winter=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, moth=1, rose=1, winter=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, remains=1, omen=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, key=1, remains=1, pigment=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Crystallised Chamber
#
# My path is blocked by shining surfaces like curdled light. Dark shapes shift beneath. We can tap away the crystal if we're careful. But we must, we must be careful.
# ---
# Rowenarium
#
# <i>Once there was a brother and sister who loved each other greatly. They resolved that they were one soul split into two bodies, and their greatest wish was to become one. They found the hidden isle where the Twins, the Sister-and-Witch, had arrived when they crossed the great ocean, and a sacred pool on which the moon shone only once a year. There they spoke with the Twins in dreams, and they learnt how they might become conjoined as one flesh, and immortal.
#
#
# Now the brother's resolution failed him, and though he loved his sister, he could not choose to spend eternity joined in one flesh. The sister could not persuade him, and she would not abandon him or force him. So they used their arts to live long lives, close but separate, and they made a double foundation of monks and nuns, as chaste as they had always been, but each nun had her brother-twin and none could enter alone.
#
# In time, the sister found her own immortality, and to this day she walks the world by moonlight. The brother died, and his bones are buried in the room beneath the well. But his children live on.</i>
rowenarium = room("rowenarium",
    attributes(dawn_period=1),
    neighbors = ("upper_pump_room", ),
    power_requirements = attributes(rose=13, winter=13),
    stations = (
        rowenarium_station,
    ),
)

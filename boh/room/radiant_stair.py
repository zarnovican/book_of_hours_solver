from ..item import candle
from ..model import attributes, condition, room, slot, station


# Shrine: the Watchman
#
# The Watchman is the Hour which navigates; which illuminates; which is not compassionate.
shrine_the_watchman = station("shrine_the_watchman",
    attributes(evolve_via_illumination=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(lantern=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(lantern=1, rose=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(lantern=1, rose=1, sky=1),
        ),
        slot(
            required=condition(soul=1, omen=1, mark=1, light=1),
            #required=condition(soul=1, omen=1, mark=1, light=1, co_operative=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(pigment=1, lens=1, gem=1, memory=1, light=1, fuel=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Shrouded Stair
#
# This has long been a holy place, but the Meniscate has withdrawn her favour now. Someone has shattered a mirror on the floor. The shards wink from the gloom - something half-seen flits from shard to shard, avoiding my gaze, unseen no matter how quickly I turn my head. Only once it's pacified will I be able to pass safely.
# ---
# Radiant Stair
#
# The Watchman's shrine here is decorated with the Eye Elagabaline - a controversial variant of the Watchman's Eye. The Elagabaline rites have always had a shaky doctrinal status. It would not often have been seen, of course. These stairs were reserved for the choir monks who sang the liturgy of the Hours, the only ones permitted to enter the Chancel. Still, it is a little surprising that the Eye was allowed to remain, when the monastery was dissolved and the Isle given to the Dewulfs.
radiant_stair = room("radiant_stair",
    attributes(solar_gothic_period=1),
    inventory = (
        candle.beeswax_candle,
        candle.beeswax_candle,
        candle.beeswax_candle,
    ),
    neighbors = ("windlit_gallery", "chancel_of_the_abbey_church"),
    power_requirements = attributes(edge=6, forge=6, knock=6, lantern=6),
    stations = (
        shrine_the_watchman,
    ),
)

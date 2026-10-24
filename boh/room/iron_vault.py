from ..item import cache, codex, tablet
from ..model import attributes, room


# Sealed Vault
#
# A heavy iron door sealed with black wax; a triple lock of unornamented iron.
# ---
# Iron Vault
#
# Where did the Curia of the Isle come from? Across the western ocean from Noon, where the Ordo Limiae made their home? That would raise more questions than it answered. But this vault would seem to be of their making, and it would also seem to reference the oath called the Iron Chain, which binds every resident of Noon, to remain hidden from the world, 'so that the Calyptra might not look upon us, so that the Chancel might not hear our names, so that the Hours might not devour us.'
iron_vault = room("iron_vault",
    attributes(curia_period=1),
    inventory = (
        cache.coppery_casket,
        cache.hive_casket,
        cache.morbid_casket,
        codex.a_childs_treasury_of_golden_afternoons,
        tablet.amiranis_beteli,
    ),
    neighbors = ("catacombs", ),
    power_requirements = attributes(edge=16, knock=16),
)

from ..item import cache, codex, tablet
from ..model import attributes, room


# Sealed Vault
#
# A heavy granite door sealed with white wax; a triple lock ornamented with ivory and black nephrite.
# ---
# Ivory Vault
#
# How did the Curia of the Isle begin? There is no evidence they began with the House of Lethe, that society of unseen immortals bound by three oaths. But this vault - much newer than the tunnels above - does seem to reference the oath called the Ivory Chain, which forbade commerce with the Hours - except, sometimes, with the winter Hour known as the Elegiast, or the Ivory Dove. Solomon Husher remarked that this might be considered less an oath of rejection of the Hours, and more an oath of loyalty to the Elegiast. But Solomon, of course, vanished into the snow.
ivory_vault = room("ivory_vault",
    attributes(curia_period=1),
    inventory = (
        cache.attache_case,
        cache.imperial_casket,
        cache.ironclad_casket,
        cache.records_box,
        cache.scaled_casket,
        cache.scarred_casket,
        codex.the_sky_in_the_scar,
        tablet.kopralith_omphalos,
    ),
    neighbors = ("columbic_crypt", ),
    power_requirements = attributes(knock=14, scale=14),
)

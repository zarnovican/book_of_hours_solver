from ..item import cache, codex, scroll, uncatalogued
from ..model import attributes, room


# Sealed Vault
#
# A heavy marble door sealed with red wax; a triple lock chased with silver.
# ---
# Silver Vault
#
# Did the Curia of the Isle construct this vault? They were not Long - most of them were not Long. So they were not the Obliviates, that society of unseen immortals bound by three oaths. But this vault does seem to reference the oath called the Silver Chain, which forbade men to lie with woman, or women with men: 'for what may come is not always the Crime of the Sky, yet that is a furious danger.'
silver_vault = room("silver_vault",
    attributes(curia_period=1),
    inventory = (
        cache.ambered_casket,
        cache.mottled_casket,
        cache.royal_casket,
        codex.the_turquoise_hand,
        scroll.shuritic_book_of_suns,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("rowenarium", ),
    power_requirements = attributes(grail=14, knock=14),
)

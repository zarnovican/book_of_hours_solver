from ..item import comfort, leaf, thing, wall_art
from ..model import attributes, room


# The great gate of the House
#
# The walls of the House tower above me. I had been told that it was abandoned after a fire - but there is no sign of any such thing. The building will no doubt need restoration, but it's in better shape than I'd feared.
#
# 'BOOKS ARE THE MEMORY THAT DOES NOT DIE', reads the inscription above the gate.
# ---
# Watchman's Tower: Gatehouse
#
# Back in the eleventh century, Brian of Brittany built the Tower and its gate to protect St Brandan's Abbey - as Hush House was then known. Later, the Barons Dewulf strengthened the gate against their many enemies. But it's a long time now since Hush House was any kind of fortress... and by the time the scholars of the Curia took possession, this place had long been a comfortable waiting room for visitors to the House too minor to merit immediate attention.
watchmans_tower_gatehouse = room("watchmans_tower_gatehouse",
    attributes(baronial_period=1),
    neighbors = ("keepers_lodge", ),
    inventory = (
        comfort.expansive_chair,
        comfort.expansive_chair,
        comfort.lingering_repose,
        comfort.treasury_of_shelters,
        leaf.vase_of_gorse,
        thing.serena_blackwood,
        wall_art.raveline_summer,
        wall_art.red_deer_antlers,
        wall_art.the_tattered_outlaw,
        wall_art.yeth_hound_horns,
        wall_art.yeth_hound_horns,
    ),
)

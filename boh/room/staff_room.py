from ..item import beverage, comfort, fixed_in_place, leaf
from ..model import attributes, room


# Blackened Staff-Room
#
# The same story as the yard below - seared bones, blackened walls, furniture half-consumed by fierce fire. But much of the room remains untouched.
# ---
# Staff-Room
#
# The warders at Brancrug were a cut above your usual prison warder - former Bureau constables, repentant Know, turncoat Tragulari, veterans of the Légion du Seuil. When the end came, none of that mattered. But here, for a while, when the winter storms battered the walls, they hunkered close to this glowing stove to share tea and comradeship and stories of their very different lives.
staff_room = room("staff_room",
    attributes(nocturnal_period=1),
    inventory = (
        beverage.dawnlion_coffee_cup,
        beverage.dawnlion_coffee_cup,
        beverage.dawnlion_coffee_pot,
        comfort.severe_chair,
        comfort.staff_armchair,
        fixed_in_place.dartboard,
        fixed_in_place.key_hooks,
        leaf.tiny_potted_tree,
    ),
    neighbors = ("gaol_yard", ),
    power_requirements = attributes(grail=11, heart=11),
    stations = (
        # stove intentionally left out
    ),
)

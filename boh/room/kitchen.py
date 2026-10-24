from ..item import beverage, fruit, liquid, liquid, leaf, material, sustenance, tool
from ..model import attributes, condition, room, slot, station


# Kitchen Range: Servants
#
# It's good luck for the villagers to bring little gifts of food to the Librarian. That's already become a tradition. But sometimes the Librarian wants a hot meal, and, these days, the Librarian is the only entity in the house that can cook.
kitchen_range_servants = station("kitchen_range_servants",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(grail=1, heart=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(grail=1, heart=1, nectar=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(grail=1, heart=1, nectar=1, scale=1),
        ),
        slot(
            required=condition(leaf=1, beverage=1, flower=1, fuel=1, root=1, cooking_ingredient=1, sustenance=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(leaf=1, beverage=1, flower=1, fuel=1, root=1, cooking_ingredient=1, sustenance=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(kitchenware=1, knife=1),
        ),
    ),
)


# Ruined Kitchen
#
# Finally, signs of a fire - but it looks as if, fortunately the chimney-breast collapsed before it could spread too far. It can't be why the House was abandoned. In any case, the kitchen will need skilled labour to restore it to a usable state.
# ---
# Kitchen
#
# 'Kingsluck pie' - a beef pie with pears and cinnamon and secret ingredients - is the traditional dish of the House. It was first cooked, they say, for King Henry, when in great secrecy on St Piran's Day he came to Cornwall seeking the 'King's Metal', tin, to 'restore his Alloy'. It probably didn't happen. But the pie did.
kitchen = room("kitchen",
    attributes(baronial_period=1),
    inventory = (
        beverage.dandelion_wine,
        beverage.isle_water_pitcher,
        beverage.lambig_broceliande_bottle,
        beverage.schloss_jannings_bottle,
        fruit.bunch_of_grapes,
        liquid.cuckoo_honey,
        liquid.honey,
        liquid.honey,
        liquid.honey,
        leaf.ch_second_flush_assam_packet,
        material.labhitic_tincture,
        sustenance.hens_egg,
        sustenance.pickled_mushrooms,
        tool.kitchen_bowls,
    ),
    neighbors = ("servants_hall", ),
    power_requirements = attributes(forge=6, sky=6),
    stations = (
        kitchen_range_servants,
    ),
)

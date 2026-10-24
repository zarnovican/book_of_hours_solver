from ..item import beverage, candle, liquid, material, tool, uncatalogued
from ..model import attributes, condition, room, slot, station


# Hearth: Hall of Voices
#
# Here, the priestesses prepared those meals which they would not, or could not, entrust to their servants.
hearth_hall_of_voices = station("hearth_hall_of_voices",
    attributes(prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, grail=1, moon=1, nectar=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, grail=1, moon=1, nectar=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, grail=1, moon=1, nectar=1),
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


# Silent Hall
#
# The hearth is cold, the floor thick with dust, the walls streaked with nitre. Old invocations and forbiddings squeak and whisper like rats.
# ---
# Hall of Voices
#
# Here the higher initiates of the Threefold Mysteries would meet to manage the affairs of the Black Dove and to resolve its disputes. Here they voted to blind and expel the Chorates of the Thunderskin, who had trespassed in the inner chambers and spied on the Mysteries. From that time on, the rites of the Thunderskin were not permitted on the Isle, and the sacred drums fell silent. But the waves still beat in the bones of the rock. Even now that slow pulse comes.
hall_of_voices = room("hall_of_voices",
    attributes(dawn_period=1),
    inventory = (
        beverage.lambig_broceliande_chalice,
        candle.widows_candle,
        liquid.black_sapphire_wash,
        liquid.holiest_hemolymph,
        material.leathy_lees,
        tool.mortar_and_pestle,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
        uncatalogued.uncatalogued_book_dawn,
    ),
    neighbors = ("upper_pump_room", ),
    power_requirements = attributes(moth=15, rose=15),
    stations = (
        hearth_hall_of_voices,
    ),
)

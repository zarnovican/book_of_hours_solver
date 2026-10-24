from ..item import thing, uncatalogued
from ..model import attributes, room


# Shadowed Stair
#
# The shadow here is a sentinel. To enter it unprepared is to risk dissolution. I must bear a memory, like a torch in the dark.
# ---
# Stair Tenebrous
#
# There were shadows here in the earth, long before the foundations of the House were laid. They retreated before the Romans' burrowings, they quailed before the sun-hymns of the brethren, they slunk away before the blades and pistols of the Barons Dewulf. Over all those centuries they shrank, until at last when the Curia of the Isle sunk this stair, they could recruit one as a watch-dog.
stair_tenebrous = room("stair_tenebrous",
    attributes(curia_period=1),
    inventory = (
        thing.the_velvet,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
        uncatalogued.uncatalogued_book_nocturnal,
    ),
    neighbors = ("night_gallery", ),
)

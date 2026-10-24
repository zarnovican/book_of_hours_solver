from ..model import attributes, condition, room, slot, station


# The Earl's Yew
#
# Since the Conquest, this has been waiting for you. The irreverent might even call it a <i>you tree</i>.
the_earls_yew = station("the_earls_yew",    # TODO (wish) model The Earl's Yew
    attributes(),
    slots = (
        slot(
            essential=condition(soul=1),
        ),
        slot(
            required=condition(journal=1),
        ),
    ),
)


# Mist-Sunk Meadow
#
# There's grass beneath my feet and a mingle of wildflower scents, but above all the damp salt vapours of a thick sea-fog. Somewhere in the fog I think I hear a distant bell - far away - as it were beneath the sea...
#
# Perhaps this can be blown away, perhaps sung away, if I bring the right powers and the right assistance.
# ---
# Earl Brian's Field
#
# 'Brian' is another one of those leitmotif names that recur all through Brancrug's long histories. This one was Brian of Brittany, who is named Earl of Cornwall by King William after the Conquest. In 1068, the sons of the deposed King Harold mount raids on Cornwall and Brian funds the construction of a fortified gate and the Watchman's Tower - initially in wood - to protect the abbey. In return, the Abbey 'gives shelter' to a yew tree he's brought from Brittany, that flowers in 'divers colours'. This is that tree, hollow now and rotting slowly from within, taking its time to die gracefully.
#
# It has not flowered in living memory and the colours of its flowers cannot now be told; but Brian's brothers were called Alan the Red and Alan the Black.
earl_brians_field = room("earl_brians_field",
    attributes(open_air=1),
    neighbors = ("earth_cellar", ),
    power_requirements = attributes(nectar=11, rose=11, sky=11),
    stations = (
        the_earls_yew,
    ),
)

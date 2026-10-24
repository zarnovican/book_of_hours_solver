from ..model import attributes, room


# Broken Bridge
#
# The gaol bridge still stands, but charred and twisted. It groans dangerously in the wind. A fire, then, but what fire does this? It's as if someone had trailed a match-flame along a bridge of wax.
#
# On the far side, the gate stands wide. When the bridge is repaired, I can enter the gaol.
# ---
# Lesser Bridge
#
# Brancrug Gaol: built in 1896 at the behest of Nocturnal Branch, to contain 'troubles unseemly and occult'. A mere six years later, after the Ortucchio Incident, the Branch came itself to be considered 'unseemly and occult', and its functions were absorbed into the Suppression Bureau. But the Gaol still stands.
#
# Over the gate is the Bureau's motto: ALIIS SI LICET, TIBI NON LICET, commonly rendered as IT IS PERMITTED TO US; IT IS NOT PERMITTED TO YOU.
lesser_bridge = room("lesser_bridge",
    attributes(nocturnal_period=1),
    neighbors = ("night_gallery", ),
    power_requirements = attributes(edge=9, forge=9, knock=9),
)

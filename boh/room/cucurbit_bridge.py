from ..model import attributes, room


# Mist-Cloaked Bridge
#
# Every so often, someone builds a bridge to the Isle; each bridge lasts a hundred years, or two hundred; then the sea disposes of it. This was built in the 1890s, and that makes it the newest bridge - but that doesn't mean it's new.
# ---
# Cucurbit Bridge
#
# Hush House has been many things over the centuries - including, in the Nocturnal Period of 1896-1929, a gaol. No-one remembers that period fondly, but at least it meant Nocturnal Branch paid for a new bridge.
cucurbit_bridge = room("cucurbit_bridge",
    attributes(out_of_bounds=1),
    neighbors = ("brancrug_village", ),
    power_requirements = attributes(forge=1, lantern=1, sky=1),
)

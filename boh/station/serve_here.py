from ..model import attributes, condition, slot, station


# Serve Here
#
# Plates, cups and glasses, so that if I want to offer someone wine, I needn't give them the whole bottle.
serve_here = station("serve_here", attributes(),
    slots = (
        slot(
            essential=condition(to_serve=1),
        ),
    ),  
)

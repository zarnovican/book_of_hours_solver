from ..model import attributes, card_type


# Receding Waters
#
# Once more, the waters are in retreat in the lower levels of the House.
receding_waters = card_type("receding_waters",
    attributes(forge=3, knock=3, circumstance=1),
)


# Uncovered Depths
#
# Once more, the sea has withdrawn from the caves of the Isle.
uncovered_depths = card_type("uncovered_depths",
    attributes(moon=3, scale=3, circumstance=1),
)

from ..model import attributes, card_type


# Bronze Spintria
#
# Occult treasures are purchased with occult coin: spintriae. Bronze spintriae usually display the act of shaping on their reverse side.
bronze_spintria = card_type("bronze_spintria",
    attributes(forge=2, ductile=1, tally=2),
)


# Gold Spintria
#
# Occult treasures are purchased with occult coin: spintriae. Gold spintriae display scenes that are not visible to mortal eyes on their reverse side.
gold_spintria = card_type("gold_spintria",
    attributes(lantern=5, ductile=1, tally=5),
)


# Iron Spintria
#
# Occult treasures are purchased with occult coin: spintriae. Iron spintriae are the lowest denomination, and display scenes of murder on their reverse side.
iron_spintria = card_type("iron_spintria",
    attributes(edge=1, ductile=1, tally=1),
)


# Silver Spintria
#
# Occult treasures are purchased with occult coin: spintriae. Silver spintriae are more valuable, and usually display scenes of debauchery on their reverse side.
silver_spintria = card_type("silver_spintria",
    attributes(grail=4, ductile=1, tally=4),
)


# Tin Spintria
#
# Occult treasures are purchased with occult coin: spintriae. Tin spintriae usually display a wild face on their reverse side: shouting, screaming, or singing?
tin_spintria = card_type("tin_spintria",
    attributes(heart=3, ductile=1, tally=3),
)

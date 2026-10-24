from ..model import attributes, card_type


# Uncatalogued Book (Baronial)
#
# [Catalogue this to learn more]
# ---
# Catalogue a Baronial Period book
#
# This book was probably written around the time of Hush House's Baronial Period - roughly 1500s to 1700s. If I examine it, I can learn more about what knowledge it might contain. [Books from this period are only rarely contaminated.]
# ---
# Catalogue a Baronial Period book
#
# Now I have an idea of the book's nature, and its contents.
uncatalogued_book_baronial = card_type("uncatalogued_book_baronial",
    attributes(thing=1, uncatalogued=1, readable=1),
    period="baronial",
)


# Uncatalogued Book (Curia)
#
# [Catalogue this to learn more]
# ---
# Catalogue a Curia Period book
#
# This book was probably written around the time of Hush House's Curia Period - roughly 1700s to 1800s. If I examine it, I can learn more about what knowledge it might contain. [Books from this period are only rarely contaminated.]
# ---
# Catalogue a Curia Period book
#
# Now I have an idea of the book's nature, and its contents.
uncatalogued_book_curia = card_type("uncatalogued_book_curia",
    attributes(thing=1, uncatalogued=1, readable=1),
    period="curia",
)


# Uncatalogued Book (Dawn)
#
# [Catalogue this to learn more]
# ---
# Catalogue a Dawn Period book
#
# This book was probably written around the time of Hush House's Dawn Period - some time before the end of the first millennium, commonly reckoned. If I examine it, I can learn more about what knowledge it might contain. [Books from this period are sometimes contaminated.]
# ---
# Catalogue a Dawn Period book
#
# Now I have an idea of the book's nature, and its contents.
uncatalogued_book_dawn = card_type("uncatalogued_book_dawn",
    attributes(thing=1, uncatalogued=1, readable=1),
    period="dawn",
)


# Uncatalogued Book (Nocturnal)
#
# [Catalogue this to learn more]
# ---
# Catalogue a Nocturnal Period book
#
# This book was probably written around the time of Hush House's Nocturnal Period - after the turn of the century. If I examine it, I can learn more about what knowledge it might contain. [Books from this period are almost never contaminated.]
# ---
# Catalogue a Nocturnal Period book
#
# Now I have an idea of the book's nature, and its contents.
uncatalogued_book_nocturnal = card_type("uncatalogued_book_nocturnal",
    attributes(thing=1, uncatalogued=1, readable=1),
    period="nocturnal",
)


# Uncatalogued Book (Solar)
#
# [Catalogue this to learn more]
# ---
# Catalogue a Solar Period book
#
# This book was probably written around the time of Hush House's Solar Gothic Period - roughly, between the 1000s and the 1500s. If I examine it, I can learn more about what knowledge it might contain. [Books from this period are occasionally contaminated.]
# ---
# Catalogue a Solar Period book
#
# Now I have an idea of the book's nature, and its contents.
uncatalogued_book_solar = card_type("uncatalogued_book_solar",
    attributes(thing=1, uncatalogued=1, readable=1),
    period="solar_gothic",
)

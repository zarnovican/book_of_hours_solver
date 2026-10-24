from ..model import attributes, journal


# A Drowned Book
#
# The one possession I kept from the shipwreck. It must be important to me. [The Aspects below tell you more about how and where you can use this item. Mouse over them to learn more.]
a_drowned_book = journal("a_drowned_book",
    attributes(thing=1, readable=1, journal=1, soaked=1),
)

# A Drowned Book
#
# The one possession I kept from the shipwreck. It must be important to me. [The Aspects below tell you more about how and where you can use this item. Mouse over them to learn more.]
a_drowned_book_fet = journal("a_drowned_book_fet",
    attributes(rose=1, thing=1, readable=1, journal=1, soaked=1),
)

# A Drowned Book
#
# The one possession I kept from the shipwreck. It must be important to me. [The Aspects below tell you more about how and where you can use this item. Mouse over them to learn more.]
a_drowned_book_fet_phost = journal("a_drowned_book_fet_phost",
    attributes(rose=1, mystery_lantern=1, thing=1, readable=1, journal=1, soaked=1),
)

# Scaled Book
#
# The scaled binding has survived the soaking well enough.
scaled_book = journal("scaled_book",
    attributes(rose=1, mystery_lantern=1, thing=1, uncatalogued=1, readable=1, journal=1),
)

# Serpentskin Journal
#
# I am the Librarian of Hush House, and this journal will be my Perpetual Map. [The Cartographer's dearest wish, when they came to the House, was to chart a new History in which their impossible map would be possible; but you can complete the game by recording any History. You might wish to begin your studies with the Nyctodromy Wisdom.]
serpentskin_journal = journal("serpentskin_journal",
    attributes(rose=1, mystery_lantern=1, memories_the_cartographer=1, readable=1, thing=1, journal=1),
)
serpentskin_journal_mastered = journal("serpentskin_journal_mastered",
    attributes(rose=1, mystery_lantern=1, memories_the_cartographer=1, mastery_lantern=1, readable=1, thing=1, journal=1),
)

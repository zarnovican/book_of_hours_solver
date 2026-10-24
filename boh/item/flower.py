from ..item import memory
from ..model import attributes, card_type


# Agave Aeterna
#
# <i>agave aeterna</i>, the 'history plant', unlike its cousin the century plant, blooms every year. Perhaps it will do so forever.
# ---
# Scrutiny
#
# <i>Aguamiel</i> sweet as nostalgia's dawn. [A previous librarian was said to sweeten lapsang tea with historied honey from this plant.]
agave_aeterna = card_type("agave_aeterna",
    attributes(lantern=2, nectar=1, winter=1, thing=1, flower=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Aglaophotis
#
# The rosy colour of good memories; but not the colour of the rose.
# ---
# Scrutiny
#
# A potent protection in many troubles.
aglaophotis = card_type("aglaophotis",
    attributes(heart=2, knock=2, lantern=2, nectar=1, rose=2, thing=1, flower=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Blue Crown
#
# The sky-coloured petals of blue crown are always cold as frost.
# ---
# Scrutiny
#
# Solomon Husher often used this in his preparations.
blue_crown = card_type("blue_crown",
    attributes(nectar=1, sky=2, winter=2, thing=1, flower=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Catsclaw
#
# Watch the thorns.
# ---
# Scrutiny
#
# Its caustic juices can be used to make the unsanctioned ink called perinculate.
catsclaw = card_type("catsclaw",
    attributes(edge=2, heart=1, nectar=1, thing=1, leaf=1, flower=1),
    consider_output = memory.scent,
)


# Eva's Locks
#
# A pale wrack washed up on the beach by Brancrug.
# ---
# Scrutiny
#
# Named for Lady Eva, who drowned herself with her grandchildren after the death of Sebastian her nephew. Her motives were never clear; her body, and the bodies of her grandchildren, were never found.
evas_locks = card_type("evas_locks",
    attributes(rose=1, winter=1, thing=1, leaf=1, flower=1),
    consider_output = memory.scent,
)


# Fragrant Chalice
#
# A glorious globe of wine-coloured flowers.
# ---
# Scrutiny
#
# When pressed, it's a good source for the intoxicating cordial called <i>rubywise ruin</i>.
fragrant_chalice = card_type("fragrant_chalice",
    attributes(grail=2, nectar=1, thing=1, flower=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Honeyscar Jasmine
#
# Sweet-scented, night-blooming.
# ---
# Scrutiny
#
# Ambrose Westcott found a way to scent his pipe tobacco with honeyscar. Kitty Mazarine made jam. And Gervinus van Lauren, it is said, found a Keeper-level recipe which somehow uses it as the basis for the azoth...
honeyscar_jasmine = card_type("honeyscar_jasmine",
    attributes(forge=2, nectar=1, rose=1, thing=1, flower=1, cooking_ingredient=1),
    consider_output = memory.scent,
)


# Lenten Rose
#
# Pretty; poisonous; no true rose.
# ---
# Scrutiny
#
# There's a story that Serena Blackwood took a specimen of this rose to the Invisible Serapeum when she left. There's another story that it's the unexpected component of a secret Keeper-level recipe for the Great Ink Porphyrine...
lenten_rose = card_type("lenten_rose",
    attributes(grail=1, nectar=1, rose=2, thing=1, flower=1),
    consider_output = memory.scent,
)


# Moth Orchid
#
# The 'true moth', the flower that opens as it changes.
# ---
# Scrutiny
#
# Traditionally, the flower of the library called the Tomb of Lies - 'where truth yet lives'.
moth_orchid = card_type("moth_orchid",
    attributes(knock=2, moth=1, nectar=1, thing=1, flower=1),
    consider_output = memory.scent,
)


# Pot of Malachite Daisies
#
# Thomas Dewulf was fond of these. It's not what you'd expect from Thomas Dewulf.
# ---
# Scrutiny
#
# The scent is crushed moss and old sun…
pot_of_malachite_daisies = card_type("pot_of_malachite_daisies",
    attributes(nectar=2, thing=1, flower=1),
    consider_output = memory.scent,
)


# Potted Pink Orchid
#
# A little smudge of dawn.
# ---
# Scrutiny
#
# There is a story that the Hour called Madrugad loved these in the days when she was gentler. No serious scholar believes the Madrugad was ever gentler.
potted_pink_orchid = card_type("potted_pink_orchid",
    attributes(rose=1, thing=1, flower=1),
    consider_output = memory.scent,
)


# Potted White Orchid
#
# A little smudge of snow.
# ---
# Scrutiny
#
# Rowena, Eva, Hafren… How many pale ladies have passed the doors of the House?
potted_white_orchid = card_type("potted_white_orchid",
    attributes(nectar=1, winter=1, thing=1, flower=1),
    consider_output = memory.scent,
)


# Sea Holly
#
# Umbelled spiny flowers, the steel-blue of a winter afternoon.
# ---
# Scrutiny
#
# Traditionally, this was the flower of Hush House. Sometimes you find it along the dunes and cliff-tops hereabouts.
sea_holly = card_type("sea_holly",
    attributes(moon=1, nectar=1, winter=1, thing=1, flower=1),
    consider_output = memory.scent,
)


# Shadowless Silk
#
# A variant of the Persian silk tree, golden as the Shadowless Kings.
# ---
# Scrutiny
#
# The Shadowless Kings are gone. This is the nature of kings; although the New King would have it otherwise.
shadowless_silk = card_type("shadowless_silk",
    attributes(lantern=1, thing=1, flower=1),
    consider_output = memory.scent,
)


# Trumpeter's Lily
#
# A glorious efflorescence of sunset orange.
# ---
# Scrutiny
#
# Traditionally, the flower of the western Library named Crossrow, where the Watchman, the Vagabond, and Sunset Celia are all celebrated.
trumpeters_lily = card_type("trumpeters_lily",
    attributes(heart=1, nectar=1, sky=2, thing=1, flower=1),
    consider_output = memory.scent,
)


# Vase of Amaryllis
#
# A soft-flowered ornament.
# ---
# Scrutiny
#
# Favoured in summer.
vase_of_amaryllis = card_type("vase_of_amaryllis",
    attributes(grail=1, nectar=1, thing=1, flower=1),
    consider_output = memory.sight,
)


# Vase of Carnations
#
# A bright-flowered ornament.
# ---
# Scrutiny
#
# Favoured in spring.
vase_of_carnations = card_type("vase_of_carnations",
    attributes(heart=1, nectar=1, thing=1, flower=1),
    consider_output = memory.sight,
)


# Vase of Golden Bulrushes
#
# It won't need watering.
# ---
# Scrutiny
#
# Gathered along the river's edge, touched still by the river's memory.
vase_of_golden_bulrushes = card_type("vase_of_golden_bulrushes",
    attributes(moon=1, moth=1, nectar=1, thing=1, flower=1),
    consider_output = memory.sight,
)


# Vase of Lilies
#
# An elegant ornament.
# ---
# Scrutiny
#
# For the dead; but not only for the dead.
vase_of_lilies = card_type("vase_of_lilies",
    attributes(nectar=1, winter=1, thing=1, flower=1),
    consider_output = memory.sight,
)


# Vase of Roses
#
# A proud ornament.
# ---
# Scrutiny
#
# 'Should this fair rose offend thine eye/Raised to the troubled air/'Twill blush to find itself less white/And turn Lancastrian there.' - Somerville, approximately
vase_of_roses = card_type("vase_of_roses",
    attributes(grail=1, nectar=1, thing=1, flower=1),
    consider_output = memory.scent,
)

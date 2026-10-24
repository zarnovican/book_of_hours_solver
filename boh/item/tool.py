from ..item import memory
from ..model import attributes, card_type


# Baron Silence's Astrolabe
#
# Thomas Dewulf used this armillary - a spherical astrolabe - in his calculations, but it's much older than he was.
# ---
# Scrutiny
#
# The base is marked with the wave-and-bell of the proscribed city, Ys…
baron_silences_astrolabe = card_type("baron_silences_astrolabe",
    attributes(sky=1, comfort=1, tool=1),
    consider_output = memory.touch,
)


# Bronze Knife
#
# A long knife of age-darkened metal with a teak handle inlaid with bone. It could be a hunting knife, although it's certainly no older than the nineteenth century, and it's not clear why anyone might have chosen to make a hunting knife out of bronze in the nineteenth century.
# ---
# Scrutiny
#
# The tang is engraved with the letters T.B. The bone has absorbed a dark stain that might be old blood. Or it might be old strawberries.
bronze_knife = card_type("bronze_knife",
    attributes(edge=1, grail=1, nectar=2, winter=1, thing=1, knife=1, tool=1),
    consider_output = memory.touch,
)


# Cucurbit Burette
#
# A vessel with an ambiguous history.
# ---
# Scrutiny
#
# Something from one of Collers' experiments, no doubt…
cucurbit_burette = card_type("cucurbit_burette",
    attributes(edge=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Kitchen Bowls
#
# CAKE TIME.
# ---
# Scrutiny
#
# It is not yet time for cake.
kitchen_bowls = card_type("kitchen_bowls",
    attributes(heart=1, nectar=1, thing=1, kitchenware=1, tool=1),
    consider_output = memory.sight,
)


# Lunar Globe
#
# It's the Earth; but silvered like the Moon, unlabelled, and pocked with craters.
# ---
# Scrutiny
#
# There are no cities and no nations marked, but I find one label - a speck in the Western Ocean marked NOON.
lunar_globe = card_type("lunar_globe",
    attributes(moon=1, rose=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Mazarine Fife
#
# Whittled according to Kitty Mazarine's patient, eccentric instructions.
# ---
# Scrutiny
#
# To be used carefully; just in case of storms. [Crafted from wood with certain Scholar-level Sky recipes.]
mazarine_fife = card_type("mazarine_fife",
    attributes(sky=3, thing=1, tool=1, instrument=1),
    consider_output = memory.sound,
)


# Mirrorscope
#
# Bewildering and occasionally useful.
# ---
# Scrutiny
#
# Faint dents on the obverse suggest someone has taken out their impatience on this thing.
mirrorscope = card_type("mirrorscope",
    attributes(lantern=1, thing=1, tool=1),
    consider_output = memory.sight,
)


# Mop and Bucket
#
# Galvanised steel, enriched with the stains of a dozen years of methodical mopping.
# ---
# Scrutiny
#
# Very, very, very faintly, even after all these years, the unmistakable yeasty marshy odour of Prophet-slime.
mop_and_bucket = card_type("mop_and_bucket",
    attributes(heart=1, comfort=1, tool=1),
    consider_output = memory.sight,
)


# Mortar & Pestle
#
# CRUSH.
# ---
# Scrutiny
#
# CRUSH CRUSH.
mortar_and_pestle = card_type("mortar_and_pestle",
    attributes(forge=1, nectar=1, thing=1, tool=1),
    consider_output = memory.sight,
)


# Saw
#
# Eternally useful, though not for most librarians most of the time.
# ---
# Scrutiny
#
# What's tangled in these teeth?
saw = card_type("saw",
    attributes(edge=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Serpent-Styled Glass
#
# Carved snakes writhe down the frame. A prominent inscription reads TO THE LIBRARIAN GERVINUS IN EARNEST OF OUR WAGER.
# ---
# Scrutiny
#
# The inscription is repeated on the base of the sand-glass, in Sanskrit. And, indeed, the style is Eastern - though, I think, somewhere farther than India.
serpent_styled_glass = card_type("serpent_styled_glass",
    attributes(scale=1, thing=1, tool=1),
    consider_output = memory.sight,
)


# Shears of the Sisterhood
#
# Black iron shears marked with the Sisterhood's triple knot.
# ---
# Scrutiny
#
# Much older than much of the House, but still remarkably sharp.
shears_of_the_sisterhood = card_type("shears_of_the_sisterhood",
    attributes(moth=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Silent Typewriter
#
# An unusual custom device.
# ---
# Scrutiny
#
# The keys are bone, inlaid with ivory.
silent_typewriter = card_type("silent_typewriter",
    attributes(winter=1, thing=1, tool=1, ink=1),
    consider_output = memory.touch,
)


# Snootle Jar
#
# Useful for calcination, purification, alteration; invaluable for snootlery.
# ---
# Scrutiny
#
# In these dark days, true snootlery is rarely to be found, but I am now in a position to correct that.
snootle_jar = card_type("snootle_jar",
    attributes(lantern=1, moth=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Spanners
#
# When you need 'em, you need 'em.
# ---
# Scrutiny
#
# 'Every key has its lock,' Serena Blackwood once said, 'sounds much grander than when we say that every spanner has its nut. But both remain true.'
spanners = card_type("spanners",
    attributes(forge=1, thing=1, tool=1),
    consider_output = memory.sight,
)


# Spice Scales
#
# Redolent of decades of piquant pesage.
# ---
# Scrutiny
#
# An inspirer of sneezes…
spice_scales = card_type("spice_scales",
    attributes(grail=1, thing=1, kitchenware=1, tool=1, spicing=1),
    consider_output = memory.touch,
)


# Square
#
# The mason's pride.
# ---
# Scrutiny
#
# The architect's joy.
square = card_type("square",
    attributes(forge=1, thing=1, tool=1),
    consider_output = memory.touch,
)


# Typewriter
#
# Now they call it unromantic. In fifty years it'll be the most romantic thing in the room.
# ---
# Scrutiny
#
# Monogrammed 'D.G.'
typewriter = card_type("typewriter",
    attributes(forge=1, thing=1, tool=1, ink=1),
    consider_output = memory.sight,
)


# Watering Can
#
# Good for pottering.
# ---
# Scrutiny
#
# An unexpectedly elegant swoop to the handle suggests something more exotic. And it's heavy. An unusual alloy… taenite? Meteoric iron? Why?
watering_can = card_type("watering_can",
    attributes(nectar=1, thing=1, tool=1),
    consider_output = memory.sight,
)

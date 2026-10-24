from frozendict import frozendict

from ..model import attributes, card_type


# TODO (model) soul 'malady_name' does not need to repeat. Move 1-2 levels up.

# Chor
#
# Exuberance; instinct; rhythm. [One of the nine parts of the human soul.]
chor = card_type("chor",
    attributes(grail=1, heart=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Chor [fatigued]
            #
            # Exuberance; instinct; rhythm.
            fatigued = attributes(grail_fatigued=1, heart_fatigued=2, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # As my concentration lapses, I begin to hear a distant music, like the tapping of a drum. [Your Chor has a Malady.]
            # ---
            # Chor: Duendratic
            #
            # Duendracy is a kind of distraction or of inspiration, or of possession. In the wind, in the sea, in the crackle of flames, there's a music only I can hear, and when I give it too much attention, the world grows red as a rose...
            malady = attributes(heart=1, soul=1, malady=1, cured_with_moth=5),
            malady_name = "duendratic",
        ),
        frozendict( # +Chor
            fatigued = attributes(grail_fatigued=2, heart_fatigued=3, soul=1, fatigued=1),
            malady = attributes(heart=1, soul=1, malady=1, cured_with_moth=7),
            malady_name = "duendratic",
            normal = attributes(grail=2, heart=3, soul=1, occupant=1),
        ),
        frozendict( # ++Chor
            fatigued = attributes(grail_fatigued=3, heart_fatigued=4, soul=1, fatigued=1),
            malady = attributes(heart=1, soul=1, malady=1, cured_with_moth=9),
            malady_name = "duendratic",
            normal = attributes(grail=3, heart=4, soul=1, occupant=1),
        ),
    ),
)


# Ereb
#
# Pride, compassion; hatred and fear. [One of the nine parts of the human soul.]
ereb = card_type("ereb",
    attributes(edge=1, grail=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Ereb [fatigued]
            #
            # Pride, compassion; hatred and fear.
            fatigued = attributes(edge_fatigued=1, grail_fatigued=2, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # As my spirits sink lower, a creaking fear passes softly into me, like something crawling through a window left carelessly open. [Your Ereb has a Malady.]
            # ---
            # Ereb: Westengryred
            #
            # Westengryre is what the early monks of St Brandan's called it; that old green-sickness, the raptness of desolation, the terror of the wastes, and it is upon me now. The Wood. The Wood. The Wood...!
            malady = attributes(nectar=1, soul=1, malady=1, cured_with_forge=5),
            malady_name = "westengryred",
        ),
        frozendict( # +Ereb
            fatigued = attributes(edge_fatigued=2, grail_fatigued=3, soul=1, fatigued=1),
            malady = attributes(nectar=1, soul=1, malady=1, cured_with_forge=7),
            malady_name = "westengryred",
            normal = attributes(edge=2, grail=3, soul=1, occupant=1),
        ),
        frozendict( # ++Ereb
            fatigued = attributes(edge_fatigued=3, grail_fatigued=4, soul=1, fatigued=1),
            malady = attributes(nectar=1, soul=1, malady=1, cured_with_forge=9),
            malady_name = "westengryred",
            normal = attributes(edge=3, grail=4, soul=1, occupant=1),
        ),
    ),
)


# Fet
#
# That part of us which walks in dreams. [One of the nine parts of the human soul.]
fet = card_type("fet",
    attributes(moth=1, rose=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Fet [fatigued]
            #
            # That part of us which dreams.
            fatigued = attributes(moth_fatigued=1, rose_fatigued=2, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # As my concentration fails, a part of my soul flutters away, drawn by a distant half-imaginary light. [Your Fet has a Malady.]
            # ---
            # Fet: Gisting
            #
            # In dreams I have visited the House behind the world... and some part of me is trapped there now, even when I wake.
            malady = attributes(rose=1, soul=1, malady=1, cured_with_grail=5),
            malady_name = "gisting",
        ),
        frozendict( # +Fet
            fatigued = attributes(moth_fatigued=2, rose_fatigued=3, soul=1, fatigued=1),
            malady = attributes(rose=1, soul=1, malady=1, cured_with_grail=7),
            malady_name = "gisting",
            normal = attributes(moth=2, rose=3, soul=1, occupant=1),
        ),
        frozendict( # ++Fet
            fatigued = attributes(moth_fatigued=3, rose_fatigued=4, soul=1, fatigued=1),
            malady = attributes(rose=1, soul=1, malady=1, cured_with_grail=9),
            malady_name = "gisting",
            normal = attributes(moth=3, rose=4, soul=1, occupant=1),
        ),
    ),
)


# Health
#
# The dwelling-place of the soul. [The ninth of the nine parts of the soul; the only one that can be touched.]
health = card_type("health",
    attributes(heart=1, nectar=1, scale=1, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Health [fatigued]
            #
            # The dwelling-place of the soul.
            fatigued = attributes(heart_fatigued=1, nectar_fatigued=1, scale_fatigued=1, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # I've exhausted my strength. [Your Health has a Malady.]
            # ---
            # Health: Sick
            #
            # I've become unwell.
            malady = attributes(winter=1, soul=1, malady=1, cured_with_heart=5),
            malady_name = "sick",
        ),
        frozendict( # +Health
            fatigued = attributes(heart_fatigued=2, nectar_fatigued=2, scale_fatigued=1, soul=1, fatigued=1),
            malady = attributes(winter=1, soul=1, malady=1, cured_with_heart=7),
            malady_name = "sick",
            normal = attributes(heart=2, nectar=2, scale=1, soul=1, occupant=1),
        ),
        frozendict( # ++Health
            fatigued = attributes(heart_fatigued=3, nectar_fatigued=3, scale_fatigued=2, soul=1, fatigued=1),
            malady = attributes(winter=1, soul=1, malady=1, cured_with_heart=9),
            malady_name = "sick",
            normal = attributes(heart=3, nectar=3, scale=2, soul=1, occupant=1),
        ),
    ),
)


# Mettle
#
# Will; self-discipline; that part of us which makes the right choice. [One of the nine parts of the human soul.]
mettle = card_type("mettle",
    attributes(edge=1, forge=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Mettle [fatigued]
            #
            # The capacity for meaningful choice.
            fatigued = attributes(edge_fatigued=1, forge_fatigued=2, soul=1, fatigued=1),
        ),
        frozendict( # +Mettle
            fatigued = attributes(edge_fatigued=2, forge_fatigued=3, soul=1, fatigued=1),
            normal = attributes(edge=2, forge=3, soul=1, occupant=1),
        ),
        frozendict( # ++Mettle
            fatigued = attributes(edge_fatigued=3, forge_fatigued=4, soul=1, fatigued=1),
            normal = attributes(edge=3, forge=4, soul=1, occupant=1),
        ),
    ),
)


# Phost
#
# Sight, perception, inspiration, all the Glory's gifts. [One of the nine parts of the human soul.]
phost = card_type("phost",
    attributes(lantern=2, sky=1, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Phost [fatigued]
            #
            # Sight, perception, inspiration, all the Glory's gifts.
            fatigued = attributes(lantern_fatigued=2, sky_fatigued=1, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # My inner light gutters, then flares - I am snared in a dangerous fascination.  [Your Phost has a Malady.]
            # ---
            # Phost: Fascinated
            #
            # The HIGHER I RISE the MORE I SEE
            malady = attributes(lantern=1, soul=1, malady=1, cured_with_nectar=5),
            malady_name = "fascinated",
        ),
        frozendict( # +Phost
            fatigued = attributes(lantern_fatigued=3, sky_fatigued=2, soul=1, fatigued=1),
            malady = attributes(lantern=1, soul=1, malady=1, cured_with_nectar=7),
            malady_name = "fascinated",
            normal = attributes(lantern=3, sky=2, soul=1, occupant=1),
        ),
        frozendict( # ++Phost
            fatigued = attributes(lantern_fatigued=4, sky_fatigued=3, soul=1, fatigued=1),
            malady = attributes(lantern=1, soul=1, malady=1, cured_with_nectar=9),
            malady_name = "fascinated",
            normal = attributes(lantern=4, sky=3, soul=1, occupant=1),
        ),
    ),
)


# Shapt
#
# Eloquence and understanding. The door opens both ways. [One of the nine parts of the human soul.]
shapt = card_type("shapt",
    attributes(forge=1, knock=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Shapt [fatigued]
            #
            # Eloquence and understanding. The door opens both ways.
            fatigued = attributes(forge_fatigued=1, knock_fatigued=2, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # The doors of my soul have opened too wide. Every sound rings like a bell - every word scratches at my eyes or skin -
            # ---
            # Shapt: Acusis
            #
            # The doors of my soul have opened too wide. Every sound rings like a bell - every word scratches at my eyes or skin -
            malady = attributes(knock=1, soul=1, malady=1, cured_with_winter=5),
            malady_name = "acusis",
        ),
        frozendict( # +Shapt
            fatigued = attributes(forge_fatigued=2, knock_fatigued=3, soul=1, fatigued=1),
            malady = attributes(knock=1, soul=1, malady=1, cured_with_winter=7),
            malady_name = "acusis",
            normal = attributes(forge=2, knock=3, soul=1, occupant=1),
        ),
        frozendict( # ++Shapt
            fatigued = attributes(forge_fatigued=3, knock_fatigued=4, soul=1, fatigued=1),
            malady = attributes(knock=1, soul=1, malady=1, cured_with_winter=9),
            malady_name = "acusis",
            normal = attributes(forge=3, knock=4, soul=1, occupant=1),
        ),
    ),
)


# Trist
#
# The change and the longing. [One of the nine parts of the human soul.]
trist = card_type("trist",
    attributes(moon=1, moth=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Trist [fatigued]
            #
            # The change and the longing.
            fatigued = attributes(moon_fatigued=1, moth_fatigued=2, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # I've placed too heavy a strain on my soul. [Your Trist has a Malady.]
            # ---
            # Trist: Despairing
            #
            # Melancholy is the mist on the soul's waters. Despair is the wolf that prowls the water's edge.
            malady = attributes(edge=1, soul=1, malady=1, cured_with_sky=5),
            malady_name = "despairing",
        ),
        frozendict( # +Trist
            fatigued = attributes(moon_fatigued=2, moth_fatigued=3, soul=1, fatigued=1),
            malady = attributes(edge=1, soul=1, malady=1, cured_with_sky=7),
            malady_name = "despairing",
            normal = attributes(moon=2, moth=3, soul=1, occupant=1),
        ),
        frozendict( # ++Trist
            fatigued = attributes(moon_fatigued=3, moth_fatigued=4, soul=1, fatigued=1),
            malady = attributes(edge=1, soul=1, malady=1, cured_with_sky=9),
            malady_name = "despairing",
            normal = attributes(moon=3, moth=4, soul=1, occupant=1),
        ),
    ),
)


# Wist
#
# Name, memory, that part which remains. Most librarians know that books have souls; most librarians hope for books with simple souls of wist and nothing else. [One of the nine parts of the human soul.]
wist = card_type("wist",
    attributes(lantern=1, winter=2, soul=1, occupant=1),
    soul_states = (
        frozendict(
            # Wist [fatigued]
            #
            # Name, memory, that part which remains. (Most librarians know that books have souls; most librarians hope for books with simple souls of wist and nothing else.)
            fatigued = attributes(lantern_fatigued=1, winter_fatigued=1, soul=1, fatigued=1),

            # Malady: Inflicted!
            #
            # I've over-tired myself. My thoughts are crabbed and strange. [Your Wist has a Malady.]
            # ---
            # Wist: Shell-Crossed
            #
            # My thoughts are tangled and unfamiliar to me. Something of those who came before - the Carapace Cross - has always lingered in humankind. It's risen now in me.
            malady = attributes(scale=1, soul=1, malady=1, cured_with_lantern=5),
            malady_name = "shell_crossed",
        ),
        frozendict( # +Wist
            fatigued = attributes(lantern_fatigued=2, winter_fatigued=3, soul=1, fatigued=1),
            malady = attributes(scale=1, soul=1, malady=1, cured_with_lantern=7),
            malady_name = "shell_crossed",
            normal = attributes(lantern=2, winter=3, soul=1, occupant=1),
        ),
        frozendict( # ++Wist
            fatigued = attributes(lantern_fatigued=3, winter_fatigued=4, soul=1, fatigued=1),
            malady = attributes(scale=1, soul=1, malady=1, cured_with_lantern=9),
            malady_name = "shell_crossed",
            normal = attributes(lantern=3, winter=4, soul=1, occupant=1),
        ),
    ),
)

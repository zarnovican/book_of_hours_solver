from ..model import attributes, card_type


# Numen: a Final Understanding
#
# Eternity and History cannot be reconciled. Freedom cannot be perfection - not unless we understand the paradox of the eternal ending. And only in certain Histories is that paradox possible... [Any Librarian can use this to establish a History and complete the game - but the Magnate can use it to win a particular victory.]
a_final_understanding = card_type("a_final_understanding",
    attributes(rose=5, sky=5, winter=5, numen=1, memory=1, persistent=1),
)


# Memory: A Stolen Secret
#
# Something I overheard in dreams?
a_stolen_secret = card_type("a_stolen_secret",
    attributes(knock=1, moon=2, memory=1),
)


# Numen: an Irresistible Feast
#
# It was Hunger that made Worms of Dragons - when they consumed the corpses of Hours. Without the savour-secret of the Carapace, their hunger would not have been sufficient. In certain Histories, that savour-secret still has power... [Any Librarian can use this to establish a History and complete the game - but the Artist can use it to win a particular victory.]
an_irresistible_feast = card_type("an_irresistible_feast",
    attributes(edge=5, grail=5, nectar=5, numen=1, memory=1, persistent=1),
)


# Ascendant Harmony
#
# A bright and ringing music which evokes the blue sweep of the lower heavens.
ascendant_harmony = card_type("ascendant_harmony",
    attributes(lantern=2, sky=4, evolve_via_birdsong=1, memory=1, persistent=1, sound=1),
)


# Awen
#
# Divine inspiration? Or just the right breath of air at the right moment? [This mood increases certain aspects.]
awen = card_type("awen",
    attributes(knock=2, lantern=2, rose=2, sky=2, memory=1),
)


# Numen: Back Into Balance
#
# When the travelling Carapace-kinds passed beyond the wave and the sky, they made arrangements for their return. There are Histories where those arrangements might be invoked...  [Any Librarian can use this to establish a History and complete the game - but the Executioner and the Revolutionary can win a particular victory.]
back_into_balance = card_type("back_into_balance",
    attributes(heart=5, sky=5, winter=5, numen=1, memory=1, persistent=1),
)


# Beguiling Melody
#
# A sweet enchantment of a song.
beguiling_melody = card_type("beguiling_melody",
    attributes(grail=2, sky=2, memory=1, sound=1),
)


# Craft: Bittersweet Certainty
#
# Hold on to it.
bittersweet_certainty = card_type("bittersweet_certainty",
    attributes(lantern=1, winter=2, memory=1, sound=1),
)


# Cheerful Ditty
#
# A rousing little rhythm.
cheerful_ditty = card_type("cheerful_ditty",
    attributes(heart=2, sky=1, memory=1, sound=1),
)


# Confounding Parable
#
# 'The Moth, the Grail, and the Egg Unhatching all tell different stories of the world's beginning. One of those stories is the oldest, but it may not be the first.' - Abbess Nonna
confounding_parable = card_type("confounding_parable",
    attributes(moon=2, rose=2, sky=2, memory=1),
)


# Memory: Contradiction
#
# Something uncomfortable.
contradiction = card_type("contradiction",
    attributes(edge=2, moon=1, memory=1),
)


# Didumos
#
# No Star is permitted upon Earth, but we may cozen them to dream of us, and the Dream of a Star may take a kind of form, which we call <i>didumos</i>.' - Thomas Dewulf
didumos = card_type("didumos",
    attributes(knock=3, lantern=3, sky=6, winter=3, evolve_via_horomachistry=1, evolve_via_hushery=1, memory=1, persistent=1),
)


# Curious Hunch
#
# A sudden unlikely certainty.
curious_hunch = card_type("curious_hunch",
    attributes(heart=3, knock=4, lantern=3, moth=3, evolve_via_nyctodromy=1, memory=1, persistent=1, omen=1),
)


# Duende
#
# 'The duende is a force not a labour, a struggle not a thought.' - Lorca
#
# [This mood increases certain aspects.]
duende = card_type("duende",
    attributes(grail=2, heart=2, nectar=2, memory=1),
)


# Earth-Sign
#
# 'In the Tracks of Beasts, in the Convolutions of his own Carapace, in Egg-vein and Shell-shadow, the Many-Eyed One found the Signs which can be History.' An Earth-Sign is an auspice traced on the cloaked shape of the earth, perceptible to the sensitive, interpreted only by the wise.
earth_sign = card_type("earth_sign",
    attributes(nectar=2, scale=2, evolve_via_skolekosophy=1, memory=1, persistent=1, omen=1),
)


# Earthquake Name
#
# Everything comes when it is called - even the nightmares that trouble stone's deep sleep.
earthquake_name = card_type("earthquake_name",
    attributes(forge=3, scale=6, evolve_via_skolekosophy=1, evolve_via_ithastry=1, memory=1, persistent=1, omen=1),
)


# Enduring Reflection
#
# Refine what is; recall what remains.
enduring_reflection = card_type("enduring_reflection",
    attributes(heart=1, knock=1, rose=3, evolve_via_nyctodromy=1, memory=1, persistent=1),
)


# Epiphany
#
# 'It was for the man of letters to record these epiphanies with extreme care, seeing that they themselves are the most delicate and evanescent of moments.' - Joyce
#
# [This mood increases certain aspects.]
epiphany = card_type("epiphany",
    attributes(forge=2, moon=2, moth=2, memory=1),
)


# Memory: Fear
#
# 'The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown.' - Lovecraft
fear = card_type("fear",
    attributes(edge=1, scale=2, memory=1),
)


# Forbidden Epic
#
# 'The attention of the Hours is drawn to the bloodiest wars. Afterwards, the Histories are braided like hair.'
forbidden_epic = card_type("forbidden_epic",
    attributes(edge=6, moon=4, rose=4, evolve_via_horomachistry=1, evolve_via_birdsong=1, memory=1, persistent=1),
)


# Memory: Foresight
#
# 'Wit's forge and fire-blast, meaning's press and screw.' - Coleridge, 'On Donne's Poetry'
foresight = card_type("foresight",
    attributes(forge=2, lantern=1, memory=1),
)


# Memory: Gossip
#
# Frivolous, but tasty.
gossip = card_type("gossip",
    attributes(grail=1, rose=2, memory=1),
)


# Memory: Hindsight
#
# Some things we can only really understand when they're gone.
hindsight = card_type("hindsight",
    attributes(scale=1, winter=2, memory=1),
)


# Hive's Lament
#
# A song of pragmatic sorrow.
hives_lament = card_type("hives_lament",
    attributes(moth=2, nectar=4, winter=2, evolve_via_bosk=1, memory=1, persistent=1, sound=1),
)


# Horizon-Sight
#
# 'On a clear autumn day, the story goes, you can see Ys from the Watchman's Tower. I don't know whether that's true. But on a clear day in Numa… you would see the City Unbuilt.' - Dr Brian Levinsen
horizon_sight = card_type("horizon_sight",
    attributes(rose=4, evolve_via_hushery=1, memory=1, persistent=1),
)


# Memory: Impulse
#
# It doesn't exactly make sense - but I understand it anyway.
impulse = card_type("impulse",
    attributes(moth=2, nectar=1, memory=1),
)


# Numen: Inescapable Confinement
#
# Everything ultimately comes down to a choice between Eternity and History. There's only one place you're safe from both, and it's not a place anyone would want to be. It's a prison that can only exist in certain Histories...  [Any Librarian can use this to establish a History and complete the game - but the Prodigal and the Archaeologist can win a particular victory.]
inescapable_confinement = card_type("inescapable_confinement",
    attributes(knock=5, scale=5, winter=5, numen=1, memory=1, persistent=1),
)


# Memory: Intuition
#
# You just know, you know?
intuition = card_type("intuition",
    attributes(moon=2, rose=2, memory=1),
)


# Invincible Audacity
#
# 'A general says: when I make the right choice, I win. An Illuminate says: when I win, I determine which choice was the right one.' - Natalia Brulleau
invincible_audacity = card_type("invincible_audacity",
    attributes(edge=6, forge=3, lantern=3, evolve_via_illumination=1, evolve_via_ithastry=1, memory=1, persistent=1),
)


# Numen: Loopholes
#
# When Eternity came into the world, certain prudent powers arranged loopholes: the House of the Moon, the persistence of possibility, the right to vengeance. In the right Histories, those loopholes will open again... [Any Librarian can use this to establish a History and complete the game - but the Twice-Born can win a particular victory.]
loopholes = card_type("loopholes",
    attributes(knock=5, moon=5, moth=5, numen=1, memory=1, persistent=1),
)


# Memory: Loss
#
# Whatever it was, now it isn't.
loss = card_type("loss",
    attributes(edge=1, winter=1, memory=1),
)


# Numen: Merciless Alteration
#
# The fundamental flaw; the irresistible shortcut; the hate that heats; the change that mars; the scar that opens. These are the foulest Histories.  [Any Librarian can use this to establish a History and complete the game - but the Artist and the Archaeologist can win a particular victory.]
merciless_alteration = card_type("merciless_alteration",
    attributes(edge=5, forge=5, grail=5, numen=1, memory=1, persistent=1),
)


# Nameday Riddle
#
# A deceptively intricate riddle that might just teach us who we really are. Gervinus van Lauren was notoriously fond of these.
nameday_riddle = card_type("nameday_riddle",
    attributes(knock=2, moth=3, memory=1),
)


# Occult Scrap
#
# Secret histories are layered beneath the one we know, like the notes in rare wine. The Librarian knows this well.
occult_scrap = card_type("occult_scrap",
    attributes(knock=2, moth=2, rose=2, evolve_via_horomachistry=1, memory=1, persistent=1, omen=1),
)


# Old Moment
#
# You've had them too; those moments when we seem to look out at the world through another's eyes. What if those moments were real?
old_moment = card_type("old_moment",
    attributes(lantern=2, moth=2, scale=4, evolve_via_preservation=1, memory=1),
)


# Old Wound
#
# The wound is visible; the pain is not. 
old_wound = card_type("old_wound",
    attributes(edge=1, moon=2, winter=3, memory=1, persistent=1),
)


# Memory: Pattern
#
# Something fits just right.
pattern = card_type("pattern",
    attributes(forge=1, knock=2, memory=1),
)


# Memory: Regret
#
# Every choice has its shadow.
regret = card_type("regret",
    attributes(forge=1, winter=2, memory=1),
)


# Memory: Revelation
#
# Some truths come to us from outside, or above.
revelation = card_type("revelation",
    attributes(lantern=2, memory=1),
)


# Memory: Salt
#
# Sea-spray, depth-sorrow.
salt = card_type("salt",
    attributes(knock=1, moon=1, winter=1, memory=1),
)


# Memory: Satisfaction
#
# Some appetites are easier to satisfy than others.
satisfaction = card_type("satisfaction",
    attributes(grail=2, heart=1, memory=1),
)


# Savage Hymn
#
# A music that urges valour and violence.
savage_hymn = card_type("savage_hymn",
    attributes(scale=2, sky=2, memory=1, sound=1),
)


# Memory: Scent
#
# Green scents recall rain.
scent = card_type("scent",
    attributes(nectar=1, memory=1),
)


# Secret Threshold
#
# It's not easy to draw our own doors, but it's not impossible.
secret_threshold = card_type("secret_threshold",
    attributes(knock=2, rose=1, memory=1),
)


# Memory: Sight
#
# 'The eye sees more than the heart knows.' - Blake
sight = card_type("sight",
    attributes(lantern=1, memory=1),
)


# Memory: Solace
#
# Peace after trouble.
solace = card_type("solace",
    attributes(heart=2, sky=1, memory=1),
)


# Memory: Sound
#
# A memory lasts longer than an echo. Of course when Speech came into the world, and we could cast echoes into words, things got more complicated.
sound = card_type("sound",
    attributes(heart=1, memory=1),
)


# Memory: Storm
#
# There are storms great enough to shake the moon from the sky, and one's thoughts from one's skull.
storm = card_type("storm",
    attributes(heart=2, sky=2, memory=1),
)


# Memory: Taste
#
# 'Every sweet has its sour.' - Emerson
taste = card_type("taste",
    attributes(grail=1, memory=1),
)


# Numen: That Old Lost Music
#
# In the right Histories, every song ever sung still lingers in wind and echo, untouched by the demands of Eternity…  [Any Librarian can use this to establish a History and complete the game - but the Symurgist and the Magnate can win a particular victory.]
that_old_lost_music = card_type("that_old_lost_music",
    attributes(rose=5, scale=5, sky=5, numen=1, memory=1, persistent=1),
)


# Numen: the Bells of Ys
#
# Ys, by her arts, found the strike-tone that shakes the Hours. For this reason among many the Hours discourage traffic with Ys. But a bell cast with this secret could speak the Ys-note…  [Any Librarian can use this to establish a History and complete the game - but the Prodigal and the Revolutionary can win a particular victory.]
the_bells_of_ys = card_type("the_bells_of_ys",
    attributes(edge=5, forge=5, rose=5, numen=1, memory=1, persistent=1),
)


# Numen: the Great Counterfeit
#
# The Sun-in-Splendour and the Forge of the Days could not be joined. But Sunset Celia and the Swan King could. This secret is the trick of it. [Any Librarian can use this to establish a History and complete the game - but the Twice-Born can win a particular victory.]
the_great_counterfeit = card_type("the_great_counterfeit",
    attributes(lantern=5, moon=5, nectar=5, numen=1, memory=1, persistent=1),
)


# Numen: the Paths of the Sun
#
# The Sun has charted his Paths - paths beyond walls and woods and Bounds. When the Sun lights our way, when we are ready, all of us will enter Eternity - at least, in the right History... [Any Librarian can use this to establish a History and complete the game - but the Cartographer and the Twice-Born can win a particular victory.]
the_paths_of_the_sun = card_type("the_paths_of_the_sun",
    attributes(forge=5, knock=5, lantern=5, numen=1, memory=1, persistent=1),
)


# Numen: the Sun's Weakness
#
# The Sun's sins and the Sun's scars are our salvation. There are Histories where they will trap us - prevent us rising to Eternity - [Any Librarian can use this to establish a History and complete the game - but the Executioner can use it to win a particular victory.]
the_suns_weakness = card_type("the_suns_weakness",
    attributes(grail=5, lantern=5, moth=5, numen=1, memory=1, persistent=1),
)


# Numen: Three Rules
#
# The Hours are bound by their own edicts - even the Chancel and the Calyptra. That's why their deepest rules are secret. In certain Histories, if we know those deepest rules, we know what even the Chancel and the Calyptra may not do.  [Any Librarian can use this to establish a History and complete the game - but the Revolutionary can win a particular victory.]
three_rules = card_type("three_rules",
    attributes(heart=5, moth=5, scale=5, numen=1, memory=1, persistent=1),
)


# Thunderskin's Paean
#
# A song of joyous sacrifice.
thunderskins_paean = card_type("thunderskins_paean",
    attributes(grail=1, heart=4, scale=1, evolve_via_preservation=1, memory=1, sound=1),
)


# Torgue's Cleansing
#
# The librarian Natalia Brulleau learnt this powerful - if unpleasant - technique from the priest and Edge-long, Reverend Torgue.
torgues_cleansing = card_type("torgues_cleansing",
    attributes(edge=2, memory=1),
)


# Memory: Touch
#
# Craft is learnt through the tips of the fingers.
touch = card_type("touch",
    attributes(forge=1, memory=1),
)


# 'Ubi Sunt'?
#
# 'Where are my kindred? Where is the giver of treasure? Where are the benches to bear us? Joys of the hall to bring us together?'
#
# [This mood increases certain aspects.]
ubi_sunt = card_type("ubi_sunt",
    attributes(edge=2, scale=2, winter=2, memory=1),
)


# Numen: Weaving the World
#
# The Histories, they say, are braided like hair - or tangled like roots. What is the shape of that knot? Funny you should ask…  [Any Librarian can use this to establish a History and complete the game - but the Symurgist and the Cartographer can win a particular victory.]
weaving_the_world = card_type("weaving_the_world",
    attributes(heart=5, moon=5, nectar=5, numen=1, memory=1, persistent=1),
)


# Wild Surmise
#
# 'Eyes open, skies open!'
wild_surmise = card_type("wild_surmise",
    attributes(lantern=3, moth=3, sky=3, evolve_via_ithastry=1, memory=1),
)


# Wind-in-Waiting
#
# 'When the sun was redder, when the world was softer, and the Thirty ruled the sky… the winds were better neighbours.'
wind_in_waiting = card_type("wind_in_waiting",
    attributes(grail=3, moth=3, scale=3, sky=6, evolve_via_bosk=1, evolve_via_birdsong=1, memory=1, persistent=1),
)


# Wind-Rumour
#
# 'If the cloud were a canvas, who spread it? If the sky were a sheet, who knotted it?' A Wind-Rumour is an auspice found in the sky by those who look too long, interpretable only by the wise.
wind_rumour = card_type("wind_rumour",
    attributes(heart=1, sky=2, evolve_via_birdsong=1, memory=1, omen=1),
)


# Winning Move
#
# Those who've studied the Hours of the Edge often say the world is a war - the Corrivality. Every event that might happen differently is a battle in that war, a contention between alternate outcomes. The Wisdoms can sometimes show those battles might be won. 
winning_move = card_type("winning_move",
    attributes(edge=3, evolve_via_illumination=1, memory=1),
)


# Wistful Air
#
# A half-sorrowful music of half-pleasant longing.
wistful_air = card_type("wistful_air",
    attributes(rose=2, sky=2, memory=1, sound=1),
)


# Wormwood Dream
#
# If there are laws which apply only in dream - then it must also be that there are crimes which can only be committed there.
wormwood_dream = card_type("wormwood_dream",
    attributes(edge=3, moon=6, winter=6, evolve_via_nyctodromy=1, evolve_via_skolekosophy=1, memory=1, persistent=1, omen=1),
)

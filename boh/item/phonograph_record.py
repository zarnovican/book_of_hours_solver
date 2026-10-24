from ..item import memory
from ..model import attributes, card_type


# A Tower Falls
#
# The phonograph is packaged in glossy amethyst purple card with the words A TOWER FALLS in nine languages on both sides. There is no other identifying information at all.
# ---
# I'm Reading...
#
# A recording of uncertain origin: inexplicably compelling poetry recorded by a speaker with a rasping, rumbling, impossibly deep voice… in the language called Vak, which probably isn't spoken by more than a few dozen living scholars.
# ---
# I've Read...
#
# The poem speaks of a four-winged war, a four-mouthed king, a four-rayed sun, a four-cornered stone. It speaks of a tide-washed hunger of the heart; it speaks, lastly, of its own conclusion, when it might, might, might be spoken in dreams before the Deep Door, by a Messenger of Histories...
a_tower_falls = card_type("a_tower_falls",
    attributes(tally_price=1, mystery_knock=16, written_in_vak=1, readable=1, thing=1, subject_preliminal_meter=1, nocturnal_period=1, phonograph_record=1),
    lessons=3,
    provides=memory.confounding_parable,
)


# A Tower Rises
#
# The phonograph is packaged in glossy card the bright pink of a dog-rose, with the words A TOWER RISES in nine languages on both sides. There is no other identifying information at all.
# ---
# I'm Reading...
#
# A recording of uncertain origin: inexplicably compelling poetry recorded by a speaker with a high, sweet voice that scales up beyond human hearing… in the language called Vak, which probably isn't spoken by more than a few dozen living scholars.
# ---
# I've Read...
#
# The poem speaks of the Wheel that turns, the Coil that turns, the Tide that returns, Egg that returns; it speaks of a cloven sky, an opened heart, a dream of glittering eyes; speaks, lastly, of its own conclusion, when it might, might, might be spoken in dreams before the Deep Door, by a Messenger of Histories...
a_tower_rises = card_type("a_tower_rises",
    attributes(tally_price=1, mystery_rose=18, written_in_vak=1, readable=1, thing=1, subject_preliminal_meter=1, nocturnal_period=1, phonograph_record=1),
    lessons=3,
    provides=memory.confounding_parable,
)


# An Investigation of A Foundered Country
#
# Subtitled 'Recordings from the Atlantic Coast.'
# ---
# I'm Reading...
#
# The phonograph initially seems to consist entirely of wave sounds, and the cries of gulls - but attention to the cries suggests they are not gulls at all - perhaps not even birds.
# ---
# I've Read...
#
# The bird-cries resolve to possibly-human voices, half-lost in the sound of waves. They lament the absence of a 'city unborn'; they hymn the 'ice behind the wave,' the 'amber cobbles', or perhaps 'amber corals.' The tenor of their song is melancholy but also, increasingly, menacing, as they promise the 'city irresistible.' As the voices fade, distant bells are clearly to be heard among the surf-sounds.
an_investigation_of_a_foundered_country = card_type("an_investigation_of_a_foundered_country",
    attributes(tally_price=1, mystery_moon=4, readable=1, thing=1, subject_hill_and_hollow=1, nocturnal_period=1, phonograph_record=1),
    lessons=1,
    provides=memory.a_stolen_secret,
)


# Lake Fucino Recordings
#
# Recordings of the folk-dances of the Fucine Marshes.
# ---
# I'm Reading...
#
# The wailing of flutes, the roaring of drums, cries like birds lost in the marshes…
# ---
# I've Read...
#
# These are the songs the Sister sang to the Witch - that the Thunderskin roared to the Sky - the songs with which the duendrazones of the Mansus keep their vigil. Once heard, they are not forgotten.
lake_fucino_recordings = card_type("lake_fucino_recordings",
    attributes(tally_price=1, mystery_heart=12, readable=1, thing=1, nocturnal_period=1, subject_drums_and_dances=1, phonograph_record=1),
    lessons=2,
    provides=memory.beguiling_melody,
)


# Opening the Sky
#
# An unusual recording of Verro's 'Opening the Sky', composed for the coronation of the New King, Henry IX. The record bears the Suppression stamp EXPUNGE.
# ---
# I'm Reading...
#
# The first movement is soft, autumnal. The second unsettling, febrile. The third is bright, soaring, rapturous. The fourth movement is glassy, slithering, a tintinnabulous icicle rattle…
# ---
# I've Read...
#
# The fifth returns to the theme of the third, bright and rapturous once again, but this is a choral movement. It becomes apparent, though, that these are much, much too pure and high to be human voices. They recall birdsong - they recall the sweep of the windswept sky, blue turning black at the edge of the higher heaven - and they wrench the heart in a direction the Bureau does not permit.
opening_the_sky = card_type("opening_the_sky",
    attributes(tally_price=1, mystery_sky=10, readable=1, thing=1, nocturnal_period=1, subject_strings_and_songs=1, phonograph_record=1),
    lessons=2,
    provides=memory.cheerful_ditty,
)


# Recordings from the Althiban Abyss
#
# Recordings from a subterranean space in the mountains near Baghdad of 'conversations' between the entomologist Juliana Zawistowski and an unidentified presence.
# ---
# I'm Reading...
#
# Only Zawistowski's part in the 'conversations' is comprehensible to the listener. The other side consists of grating, buzzing and rumbling sounds, perhaps only rock movements or artifacts of the recording process, which Zawistowski nevertheless unhesitatingly translates.
# ---
# I've Read...
#
# Zawistowski seems to believe that the presence identifies itself as a Name or remnant of the lost Hour called Seven-Coils. It pleads with her to assist its rebirth; it begs her to find something for it in the city of Emesa. Towards the end of the interview, Zawistowski grows suspicious, and repeatedly accuses the presence of being not the Seven-Coils at all - only 'an inhabitant.' The recording ends in mid-sentence.
recordings_from_the_althiban_abyss = card_type("recordings_from_the_althiban_abyss",
    attributes(tally_price=1, written_in_deep_mandaic=1, mystery_scale=4, readable=1, thing=1, phonograph_record=1, nocturnal_period=1, subject_stone_stories=1),
    lessons=1,
    provides=memory.fear,
)


# The Invisible Opera (Unfinished Recording)
#
# A recording of a 1911 attempt at a performance of 'Wings within Wings', the so-called Invisible Opera.
# ---
# I'm Reading...
#
# The singers complete <i>the Skewbald Aria</i>, <i>Beneath Our Skin</i>, and <i>A Rose in Miah</i> without incident; but the Invisible Opera is dedicated to Ferezeref the Magpie, who delights in unexpected interruptions…
# ---
# I've Read...
#
# The recording ends with a clamour of horrified voices, a grating metallic screech, and a soft brass buzzing that fades into burring silence…
the_invisible_opera_unfinished_recording = card_type("the_invisible_opera_unfinished_recording",
    attributes(tally_price=1, mystery_sky=12, readable=1, thing=1, nocturnal_period=1, subject_strings_and_songs=1, phonograph_record=1),
    lessons=2,
    provides=memory.cheerful_ditty,
)


# Velletri Interviews
#
# Interrogation of a man named Lacombe, a former Nocturnal Branch inspector now identified as 'terminally robigoid'.
# ---
# I'm Reading...
#
# Lacombe is not especially lucid, and the state called 'robigoia' evidently includes a malady of the lungs which causes coughing fits: he weakens audibly over the course of the interrogation. He is questioned about the disposition of various unsanctioned items recovered from a Nocturnal Branch raid on a castle at Ortucchio, in the region of the Fucine Marshes. He is, however, defiant as well as incoherent.
# ---
# I've Read...
#
# Lacombe insists the items have been put to good use; he derides Nocturnal Branch as 'the lackeys of Calyptra'. Alarmingly, during the last few minutes of the interrogation, he begins to insist that his interrogator should 'burn the Library'. He waxes enthusiastic about the fire he wants to see, leading to a final coughing fit after which the interview abruptly ends.
velletri_interviews = card_type("velletri_interviews",
    attributes(tally_price=1, mystery_heart=6, readable=1, thing=1, subject_edicts_inviolable=1, nocturnal_period=1, phonograph_record=1),
    lessons=1,
    provides=memory.a_stolen_secret,
)

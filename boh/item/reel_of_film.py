from ..item import memory
from ..model import attributes, card_type


# COLOURS IN THE LIVER
#
# Ilse Bischoff's most controversial film, blamed for outbreaks of cannibalistic killings in Tiflis and Leipzig.
# ---
# I'm Reading...
#
# A gang of heretic priests agrees to strike the 'fear of the Change' into the infuriatingly atheist citizenry. At night they dress as four-winged angels and crawl down chimneys and through windows to savage members of their congregation.
# ---
# I've Read...
#
# The priests are caught by unidentified figures wearing heavily mandibled masks, like grotesque caricatures of ants. They are force-fed larvae: a final caption indicates that at dawn the larvae will hatch…
colours_in_the_liver = card_type("colours_in_the_liver",
    attributes(tally_price=1, mystery_grail=6, readable=1, thing=1, subject_resurgences_and_emergences=1, reel_of_film=1, nocturnal_period=1),
    lessons=1,
    provides=memory.revelation,
)


# EXPERIMENT BEYOND SIGHT
#
# Ilse Bischoff's bewildering, widely derided final film.
# ---
# I'm Reading...
#
# The film is an unrelenting fusillade of apparently unrelated images - birth, mirrors, grain-threshers, animal attacks, crowds at stations… but a single image appears again and again, dominating the rush of images until the film is only a single static shot.
# ---
# I've Read...
#
# The repeating image is a view through a grimy window-pane of a nearby tower. There is a vague impression of flickering light around the tower-top. Just as the film ends, smoke plumes from the tower. That's it. Nothing of note at all… unless one happens to recognise the view of the Crucible Tower from the window of the Librarian's Quarters, and unless one happens to know that Ilse Bischoff never visited Brancrug, or even Britain, before her untimely death.
experiment_beyond_sight = card_type("experiment_beyond_sight",
    attributes(tally_price=1, mystery_moon=8, readable=1, thing=1, subject_edicts_inviolable=1, reel_of_film=1, nocturnal_period=1),
    lessons=2,
    provides=memory.revelation,
)


# The Admonitory Automata Project
#
# Footage of experimental devices under development in the Cucurbit under Governor Collers' supervision.
# ---
# I'm Reading...
#
# The 'admonitory automata' are nasty little things of spring and wire, but they all have merry faces of painted tin…
# ---
# I've Read...
#
# The last item shown is a prototype towards something called a 'condignator', which, Collers says proudly, will allow a prisoner to 'elaborate their own punishment.' He hastens to add that he hopes that in the coming era, 'punishment' will be an entirely obsolete concept.
the_admonitory_automata_project = card_type("the_admonitory_automata_project",
    attributes(tally_price=1, mystery_forge=10, readable=1, thing=1, subject_lockworks_and_clockworks=1, reel_of_film=1, nocturnal_period=1),
    lessons=2,
    provides=memory.foresight,
)


# THE OPEN HEAD
#
# Ilse Bischoff's hallucinatory quasi-documentary, notionally about the Greco-Turkish War of the previous decade.
# ---
# I'm Reading...
#
# A hammer-armed Turk and a sword-armed Greek pursue each other through the Pindus, setting traps for each other, robbing peasants, chalking insulting graffiti on walls. The tone is notionally anti-war, but any scholar of the invisible arts would recognise the Edge-hour subtext... and the Hyksos messages in the graffiti.
# ---
# I've Read...
#
# The sword-wielder methodically fills a church with candles; lights each one; strips, again, to the waist to reveal his terrible scars; his chest somehow swings open like a cupboard door to reveal a blood-drenched book… and the film ends.
the_open_head = card_type("the_open_head",
    attributes(tally_price=1, mystery_edge=8, written_in_hyksos=1, readable=1, thing=1, reel_of_film=1, nocturnal_period=1, subject_disciplines_of_the_scar=1),
    lessons=2,
    provides=memory.revelation,
)

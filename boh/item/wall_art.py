from ..item import memory
from ..model import attributes, card_type


# 'A Bargain'
#
# A serpent laps at the blood that drips from a sewn-closed mouth.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
a_bargain = card_type("a_bargain",
    attributes(knock=1, wall_art=1),
    consider_output = memory.sight,
)


# 'A Sacrifice'
#
# A silent crowd watches a robed priest drown a struggling victim in a bowl of rainbowed oil.
# ---
# Scrutiny
#
# Signed 'CI'.
a_sacrifice = card_type("a_sacrifice",
    attributes(grail=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Again, at Night'
#
# One of Dr Levinsen's 'prefigures', a close (and impossible) copy of a painting made twenty years later by Kirchner, whose work Levinsen often anticipated in his mirror-dreams.
# ---
# Scrutiny
#
# Watchful? Hungry? Both?
again_at_night = card_type("again_at_night",
    attributes(grail=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# ALIIS LICET TIBI NON LICET
#
# 'To us it is permitted; to you it is not permitted.' The motto of the Suppression Bureau.
# ---
# Scrutiny
#
# The story goes that Governor Collers used to keep another sign in his office with the motto of the Nocturnal Branch, the Bureau's predecessor: RADIX MALORUM LIBERTAS EST. If someone complained about Bureau policies, he would point to the sign to remind them that things could be worse. Eventually it was pointed out to him that 'the root of evils is liberty' was an undiplomatic motto to display in a prison, and he grumpily retired the sign.
aliis_licet_tibi_non_licet = card_type("aliis_licet_tibi_non_licet",
    attributes(knock=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# 'As Above, So Below'
#
# A framed page of illustrated vellum. Up close, the colours dazzle and puzzle.
# ---
# Scrutiny
#
# A handwritten slip of paper reads ABBESS MELANCTHE, 1100? Melancthe's work was sometimes reckoned 'too radiant for the eye'…
as_above_so_below = card_type("as_above_so_below",
    attributes(sky=1, wall_art=1),
    consider_output = memory.sight,
)


# Azita's Practice Sword
#
# A varnished length of wood. The name AZITA is inlaid in silver.
# ---
# Scrutiny
#
# The wood is Cornish oak. This is one of the newer items in the practice room - no older than the current century.
azitas_practice_sword = card_type("azitas_practice_sword",
    attributes(edge=2, heart=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# Bokken: Captain Torgue and Mistress Dearday
#
# Souvenirs from the East, heavily padded.
# ---
# Scrutiny
#
# Treasured items left behind by the occupants of the cell during their inglorious career on the high seas. Procured by Governor Collers as a gift for the occupants of the cell, in the hope it would induce better behaviour.
bokken_captain_torgue_and_mistress_dearday = card_type("bokken_captain_torgue_and_mistress_dearday",
    attributes(edge=2, sky=1, wall_art=1),
    consider_output = memory.contradiction,
)


# Brazen Clock
#
# It's not immediately apparent that this clock lacks hands, although, when wound, it dutifully ticks.
# ---
# Scrutiny
#
# An inscription reads: 'For D.M. Time is; Time was; Time is past.'
brazen_clock = card_type("brazen_clock",
    attributes(forge=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# Caer Ys
#
# A spired city is dimly visible through a vast rolling wave.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
caer_ys = card_type("caer_ys",
    attributes(rose=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Chac'
#
# Valentine Dewulf's magnificent green cockatoo. The painting is signed by Valentine himself.
# ---
# Scrutiny
#
# Valentine, who had an interest in the religions of the new world, named his bird for the Mayan god of rain and thunder.
chac = card_type("chac",
    attributes(nectar=2, sky=2, wall_art=1),
    consider_output = memory.sight,
)


# Crossbow
#
# An antique crossbow from Hush House's early Baronial period.
# ---
# Scrutiny
#
# Still in excellent condition. In the unlikely event I ever need to fend off robber knights, I could do worse than this.
crossbow = card_type("crossbow",
    attributes(forge=1, sky=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# 'Crowcross Sands at High Tide'
#
# A gloomy study of the sea in gloomy weather.
# ---
# Scrutiny
#
# Barely visible at the painting's edge, there are floating timbers that suggest a wrecked fishing boat…
crowcross_sands_at_high_tide = card_type("crowcross_sands_at_high_tide",
    attributes(moon=1, wall_art=1),
    consider_output = memory.sight,
)


# Cudgels: Dyddgu and St Twrog
#
# Very old iron cudgels, recently and heavily padded.
# ---
# Scrutiny
#
# Retrieved from Gladwyn Lake and returned to the cell's occupants as a reward for good behaviour.
cudgels_dyddgu_and_st_twrog = card_type("cudgels_dyddgu_and_st_twrog",
    attributes(edge=2, forge=2, sky=1, wall_art=1),
    consider_output = memory.contradiction,
)


# Dappled Practice Sword
#
# A leaf-shaped wooden sword of considerable age.
# ---
# Scrutiny
#
# The wood is poplar; the hilt is marked with blackthorn and holly.
dappled_practice_sword = card_type("dappled_practice_sword",
    attributes(edge=1, moth=1, wall_art=1, made_of_wood=1),
    consider_output = memory.sound,
)


# Dappled Quarterstaff
#
# A long staff marked with bands of black and white.
# ---
# Scrutiny
#
# The wood is poplar; the bands are blackthorn and holly.
dappled_quarterstaff = card_type("dappled_quarterstaff",
    attributes(moth=1, nectar=1, wall_art=1, made_of_wood=1),
    consider_output = memory.sound,
)


# Dearday's Foil
#
# A pin-sharp length of flexible steel. The blade is inscribed DEARDAY.
# ---
# Scrutiny
#
# Dearday was one-half of the Edge dyad that Natalia Brulleau hoped to lure to Hush House - to learn from them or to imprison them?
deardays_foil = card_type("deardays_foil",
    attributes(edge=2, sky=1, wall_art=1),
    consider_output = memory.touch,
)


# 'Departure'
#
# Here Valentine has painted gulls migrating across a darkening sea.
# ---
# Scrutiny
#
# Each winter the black-backed gulls would leave Brancrug for warmer climes. Valentine would command a candle-lit dinner on the beach in their honour, with dancing and drumming, though he would never attend, only watch approvingly from the Gullscry Tower.
departure = card_type("departure",
    attributes(moth=2, winter=2, wall_art=1),
    consider_output = memory.sight,
)


# 'Dr Serena Blackwood'
#
# No-one is in the picture - only an empty garden.
# ---
# Scrutiny
#
# Blackwood abandoned Hush House for another library, the Invisible Serapeum in Alexandria. Is this a joke at her expense?
dr_serena_blackwood = card_type("dr_serena_blackwood",
    attributes(forge=1, rose=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Eva and Abraham, 1724'
#
# A magnificent depiction in oils of an elegantly dressed eighteenth century couple. The face of the gentleman, however, was long ago obliterated by a splash of some dark, corrosive substance.
# ---
# Scrutiny
#
# In her youth, Lady Eva is engaged to be married to an Abraham Wheelock of Monmouthshire, but in 1725 he leaves her at the altar. Furious and humiliated, she returns to Brancrug, and is not seen in London again.
# Three days after her departure, Abraham Wheelock's body is washed up near Gravesend. His face is so badly pecked by birds that he is only identified by his belongings. These include a waxed pouch containing a letter addressed to Wheelock, whose contents seem to show he is a spy in the pay of the Austrians. Subsequent investigations suggest that the letter is a forgery, but the matter remains obscure.
eva_and_abraham_1724 = card_type("eva_and_abraham_1724",
    attributes(grail=1, wall_art=1),
    consider_output = memory.sight,
)


# Finnian
#
# Ambrose Westcott liked to name his hunting trophies after former rivals or adversaries whom (he said) his trophies resembled.
# ---
# Scrutiny
#
# Finnian Boole was a tobacconist whose bills Westcott inexplicably refused to pay.
finnian = card_type("finnian",
    attributes(scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)


# Fractured Mirror
#
# Cracked and fly-specked.
# ---
# Scrutiny
#
# Your face in this glass looks scarred - older - harsher. A certain Door in dreams - it is said - opens only for a mirror which has just been cracked. But this mirror was cracked long ago.
fractured_mirror = card_type("fractured_mirror",
    attributes(knock=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# Fraser's Practice Sword
#
# A varnished length of wood. The name FRASER has been carved into the flat.
# ---
# Scrutiny
#
# The wood is dark ash. The practice weapon has seen considerable use, and is notched and battered - it must be more than fifty years old.
frasers_practice_sword = card_type("frasers_practice_sword",
    attributes(edge=1, scale=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# Genealogical Chart
#
# Six years ago, King George's heir Edward killed him in a quarrel over Edward's womanising. The kingdom was saved from constitutional collapse by  Henry Huddleston Abney-Hastings, 13th Count of Loudoun - who claimed descent through the Plantagenet line. Heaven lift the New King!
# ---
# Scrutiny
#
# Collers was keenly interested in the history of the houses Tudor, Plantagenet, Hanover, Windsor, et cetera, all the way back to the days of the Leashed Flame. He has also doodled the Suppression Bureau seal by the name of King Henry's mother Edith. Of course: Lady Edith serves as Nocturnal Secretary... the minister with final responsibility for the entire Bureau.
genealogical_chart = card_type("genealogical_chart",
    attributes(forge=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Glory's Gift'
#
# A human figure is silhouetted against a blazing sun.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
glorys_gift = card_type("glorys_gift",
    attributes(lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Gods Return'
#
# A green shoot splits a rock.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
gods_return = card_type("gods_return",
    attributes(nectar=1, wall_art=1),
    consider_output = memory.sight,
)


# Golden Lion Shield
#
# Painted leather, riveted to heavy iron.
# ---
# Scrutiny
#
# This is clearly a reproduction or facsimile, perhaps from the mid nineteenth century - but it is heavy and durable. The leather is stiff and coarse - it might be cowhide, or perhaps even lionhide.
golden_lion_shield = card_type("golden_lion_shield",
    attributes(edge=1, heart=1, wall_art=1),
    consider_output = memory.touch,
)


# Green Stag Shield
#
# Painted leather, riveted to heavy iron.
# ---
# Scrutiny
#
# This is clearly a reproduction or facsimile, perhaps from the mid nineteenth century - but it is heavy and durable. The leather is fine-grained and subtle, and may in fact be deerhide.
green_stag_shield = card_type("green_stag_shield",
    attributes(heart=1, nectar=1, wall_art=1),
    consider_output = memory.touch,
)


# Greene's Practice Sword
#
# A varnished length of wood.
# ---
# Scrutiny
#
# The hilt is charred, as if Greene had held it over a candle-flame.
greenes_practice_sword = card_type("greenes_practice_sword",
    attributes(edge=1, heart=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# Hokobald
#
# Ambrose Westcott liked to name his hunting trophies after former rivals whom (he said) his trophies resembled.
# ---
# Scrutiny
#
# The set of the mouth of the stag has, perhaps, a surly quality
hokobald = card_type("hokobald",
    attributes(scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)


# Hunter's Bow
#
# A very practical weapon.
# ---
# Scrutiny
#
# Stout English elm - or stout once. It hasn't been used in years. It'd probably snap in two.
hunters_bow = card_type("hunters_bow",
    attributes(sky=1, winter=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# 'Julian Coseley'
#
# Julian is known to be Winter-long: at a prescribed date, his Hour-patron will ensure him a beautiful ending, but until then, he is even harder than most Long to dispose of finally. That said, he is known to have been defeated by an ascendant Long in the 1920s, and his true current status - a diminished survivor? a determined memory? something else? - is the subject of esoteric debate.
# ---
# Scrutiny
#
# Coseley spent time at Hush House in the seventeenth century, but this painting, though undated, is clearly much more recent. It is also signed by Coseley himself. A gift to an imprisoned admirer?
julian_coseley = card_type("julian_coseley",
    attributes(moon=1, winter=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Lady Tryphon'
#
# A very old portrait in the Byzantine style.
# ---
# Scrutiny
#
# A handwritten card tucked into the frame reads 'Sequester on sight. - G.C'
lady_tryphon = card_type("lady_tryphon",
    attributes(grail=2, moth=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Leaves in the Wind'
#
# A soothing but undistinguished work in oils. Someone evidently was good at trees, and wanted you to know it.
# ---
# Scrutiny
#
# In the foreground, an odd curl of shadow might just be a hand reaching from a crevice in a yew-tree trunk.
leaves_in_the_wind = card_type("leaves_in_the_wind",
    attributes(nectar=1, wall_art=1),
    consider_output = memory.sight,
)


# Lepidoptery Display (Grail-centric)
#
# A collection of lepidopteran insects with unusual characteristics.
# ---
# Scrutiny
#
# On closer inspection, these are more like bees, but they seem to have adopted the wings and limbs of other insects, rather like hermit crabs. A typed card reads PROPINOMANIDAE.
lepidoptery_display_grail_centric = card_type("lepidoptery_display_grail_centric",
    attributes(grail=1, wall_art=1),
    consider_output = memory.sight,
)


# Lepidoptery Display (Heart-centric)
#
# A collection of lepidopteran insects with unusual characteristics.
# ---
# Scrutiny
#
# The bulbous heads of these insects are alarmingly well-endowed with a great many eyes. A typed card reads TRIGINTIDAE.
lepidoptery_display_heart_centric = card_type("lepidoptery_display_heart_centric",
    attributes(heart=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Lord Munday'
#
# A well-dressed, middle-aged gentleman with receding hair and a clear expression of astonished delight.
# ---
# Scrutiny
#
# A small plaque reads MUNDAY ENDOWMENT - WITH GRATITUDE
lord_munday = card_type("lord_munday",
    attributes(grail=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Love in a Quiet Place'
#
# One of Dr Levinsen's 'prefigures', a close (and impossible) copy of a painting made twenty years later by Kirchner, whose work Levinsen often anticipated in his mirror-dreams.
# ---
# Scrutiny
#
# Levinsen has signed the painting but added 'E.L.K.?'
love_in_a_quiet_place = card_type("love_in_a_quiet_place",
    attributes(grail=1, lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# Matched Flintlock Pistols
#
# A pair of pistols - the style and maker's mark suggest late seventeenth century.  The initials 'MD' are marked in silver, above the wolf-sejant of the Barons Brancrug.
# ---
# Scrutiny
#
# There is a story that Musgrave Dewulf died in a secret duel with a 'Welsh visitor'. There is nothing to suggest that this is true, or that these pistols were ever used in a duel… but the date might match, and one might speculate.
matched_flintlock_pistols = card_type("matched_flintlock_pistols",
    attributes(edge=1, heart=1, wall_art=1),
    consider_output = memory.touch,
)


# Mehrad's Practice Sword
#
# A varnished length of wood. The name MEHRAD is inlaid in gold.
# ---
# Scrutiny
#
# The wood is Cornish oak. This is one of the newer items in the practice room - no older than the current century.
mehrads_practice_sword = card_type("mehrads_practice_sword",
    attributes(edge=2, lantern=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# 'Mlle Matutine'
#
# An alluring young woman with deep blue eyes hard and dark as sapphires.
# ---
# Scrutiny
#
# Her teeth are very white; it is hard to be sure, but they seem also to be pointed…
mlle_matutine = card_type("mlle_matutine",
    attributes(grail=1, moon=1, wall_art=1),
    consider_output = memory.sight,
)


# Natalia's Practice Sword
#
# A varnished length of wood. The name NATALIA has been carved into the flat.
# ---
# Scrutiny
#
# The wood is dark ash. The practice weapon has seen considerable use, and is notched and battered - it must be more than fifty years old.
natalias_practice_sword = card_type("natalias_practice_sword",
    attributes(edge=1, lantern=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# Night Mirror
#
# An oddly dim mirror.
# ---
# Scrutiny
#
# The glass returns reflected light with some reluctance, so even in broad daylight the effect is that of dusk.
night_mirror = card_type("night_mirror",
    attributes(lantern=1, moon=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Our Benefactor'
#
# Evidently someone who donated to the Curia… but preferred to remain anonymous.
# ---
# Scrutiny
#
# He's wearing a little silver brooch fashioned in the shape of a fox's head.
our_benefactor = card_type("our_benefactor",
    attributes(forge=1, heart=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Our Benefactress'
#
# Evidently someone who donated to the Curia… but preferred to remain anonymous.
# ---
# Scrutiny
#
# She's wearing a little silver brooch fashioned in the shape of a cat's head.
our_benefactress = card_type("our_benefactress",
    attributes(forge=1, heart=1, wall_art=1),
    consider_output = memory.sight,
)


# Philemon
#
# Ambrose Westcott liked to name his hunting trophies after former rivals whom (he said) his trophies resembled.
# ---
# Scrutiny
#
# Philemon was the <i>nom de plume</i> of a poet who satirically christened Westcott 'the Magus of the Silver'd Smoke'. Whatever this meant exactly, it clearly enraged Westcott.
philemon = card_type("philemon",
    attributes(scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)


# Poacher's Bow
#
# A very practical weapon.
# ---
# Scrutiny
#
# Supple Cornish ash - or supple once. It hasn't been used in years. It'd probably snap in two.
poachers_bow = card_type("poachers_bow",
    attributes(rose=1, sky=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# 'Portrait of a Behatted Lady'
#
# 'The More Prominent the Headgear, the Closer to the Glory'
# ---
# Scrutiny
#
# The headgear is, without doubt, impressively prominent.
portrait_of_a_behatted_lady = card_type("portrait_of_a_behatted_lady",
    attributes(lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Raveline Summer'
#
# A dry spell in a still place.
# ---
# Scrutiny
#
# This is signed 'Brulleau' but dated 1902, long after the Librarian of that name left Hush House… she did come of a family of painters.
raveline_summer = card_type("raveline_summer",
    attributes(forge=1, nectar=1, wall_art=1),
    consider_output = memory.sight,
)


# 'Red, Blue'
#
# It's a decent copy of a Picasso… painted twenty years before Picasso painted the original. Brian Levinsen, up to his tricks again.
# ---
# Scrutiny
#
# Levinsen has signed it, but added a question mark after his signature.
red_blue = card_type("red_blue",
    attributes(grail=1, sky=1, wall_art=1),
    consider_output = memory.sight,
)


# Red Deer Antlers
#
# Not quite hair, not quite teeth, but proof that someone killed something.
# ---
# Scrutiny
#
# BD' is scratched on one antler. Bryan Dewulf was a prolific and successful hunter in his time…
red_deer_antlers = card_type("red_deer_antlers",
    attributes(scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)


# Red Drake Shield
#
# Painted leather, riveted to heavy iron.
# ---
# Scrutiny
#
# This is clearly a reproduction or facsimile, perhaps from the mid nineteenth century - but it is heavy and durable. The leather is strongly textured, with small scales arranged in a diamond pattern.
red_drake_shield = card_type("red_drake_shield",
    attributes(heart=1, scale=1, wall_art=1),
    consider_output = memory.touch,
)


# Red Practice Sword
#
# A leaf-shaped wooden sword of considerable age.
# ---
# Scrutiny
#
# The wood is birch; the hilt is marked with red ochre.
red_practice_sword = card_type("red_practice_sword",
    attributes(edge=1, grail=1, wall_art=1, made_of_wood=1),
    consider_output = memory.scent,
)


# Red Quarterstaff
#
# A long staff marked with bands of red.
# ---
# Scrutiny
#
# The wood is birch; the bands are marked with red ochre.
red_quarterstaff = card_type("red_quarterstaff",
    attributes(grail=1, nectar=1, wall_art=1, made_of_wood=1),
    consider_output = memory.scent,
)


# Sebastian's Swords
#
# Matching eighteenth-century cutlasses. The initials SD are engraved on the blade near the hilt.
# ---
# Scrutiny
#
# The hilt is bone; the guard is brass, decorated rather racily with nymphs pursued by satyrs. These were not regulation Royal Navy pattern, and must have been gifts or commissions by Captain Sebastian Dewulf, last of the Dewulf line, who died in action at Quiberon Bay.
sebastians_swords = card_type("sebastians_swords",
    attributes(edge=1, moon=1, sky=1, wall_art=1, knife=1),
    consider_output = memory.touch,
)


# 'Sedona, Not Yet'
#
# One of Dr Levinsen's 'prefigures', an impossible copy of a painting that the real artist hadn't yet executed. He's signed it with the Illumination mark, and dated it '1958'.
# ---
# Scrutiny
#
# At this very moment, perhaps, Max Ernst is dreaming of Arizona. But he hasn't painted this yet.
sedona_not_yet = card_type("sedona_not_yet",
    attributes(moth=2, wall_art=1),
    consider_output = memory.sight,
)


# 'Self-Born'
#
# A furry, cloven-looking foot reaches towards a mirror: its reflection is a bird's claw.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
self_born = card_type("self_born",
    attributes(sky=1, wall_art=1),
    consider_output = memory.sight,
)


# Sentry's Bow
#
# A fearsome weapon.
# ---
# Scrutiny
#
# Good Welsh yew once… now it's rotting from the inside out.
sentrys_bow = card_type("sentrys_bow",
    attributes(lantern=1, sky=1, wall_art=1, made_of_wood=1),
    consider_output = memory.touch,
)


# Shaving Mirror
#
# <i>Snip snip!</i>
# ---
# Scrutiny
#
# Faint rust-specks dot the mirror. Or, just possibly, blood.
shaving_mirror = card_type("shaving_mirror",
    attributes(lantern=1, moth=1, wall_art=1),
    consider_output = memory.sight,
)


# Sol Invictis Symbol
#
# The eternal symbol of the Unconquered Sun, all the way back to the Shadowless Empire, even through the wild heresies of the Intercalate.
# ---
# Scrutiny
#
# Since the Reformation, one quarter is assigned to each of the orthodox Hours - Madrugad, Watchman, Wolf, Meniscate - and the junction at the wheel's heart to the Sun in Rags or Splendour. A less orthodox tradition assigns the rim to the enigmatic St Januarius.
sol_invictis_symbol = card_type("sol_invictis_symbol",
    attributes(lantern=1, wall_art=1),
    consider_output = memory.sight,
)


# Storm-Tossed Mirror
#
# Solid workmanship, but not obviously remarkable.
# ---
# Scrutiny
#
# A plaque explains that in 1872 this mirror survived a shipwreck untouched, and was gifted to the House by a grateful survivor who was nursed back to health in the infirmary below.
storm_tossed_mirror = card_type("storm_tossed_mirror",
    attributes(lantern=1, sky=1, wall_art=1),
    consider_output = memory.sight,
)


# Tavish
#
# Ambrose Westcott liked to name his hunting trophies after former rivals whom (he said) his trophies resembled.
# ---
# Scrutiny
#
# Tavish is a gamekeeper who once derided Westcott's ability to shoot straight.
tavish = card_type("tavish",
    attributes(scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)


# 'The Boy Prays'
#
# There's no sign of a boy in this distorted, menacing image, and no-one seems to be praying.
# ---
# Scrutiny
#
# In the darkness gathering at the back, a crowd of eyes might suggest a pack of hounds…
the_boy_prays = card_type("the_boy_prays",
    attributes(grail=1, moon=1, scale=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The First Answer'
#
# A vast moth spirals towards a burning sun, alone in a star-speckled void.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_first_answer = card_type("the_first_answer",
    attributes(moth=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The First Birth'
#
# A single ripple disturbs the still surface of a well of blood.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_first_birth = card_type("the_first_birth",
    attributes(grail=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The First End'
#
# A single candle burns against darkness; its flame is the crescent moon.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_first_end = card_type("the_first_end",
    attributes(forge=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The First Threshold'
#
# A horned double axe stands alone in a sandy desert.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_first_threshold = card_type("the_first_threshold",
    attributes(heart=1, scale=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The Foundation of the Sun'
#
# 'Long ago in this country, one did not build a church without first sacrificing a white bull to the Sun-in-Rags…' Solomon Husher brought this tapestry with him from - well, wherever it was that Solomon came from.
# ---
# Scrutiny
#
# The tapestry ripples very slowly, even in still air. Candle-flames bend towards it.
the_foundation_of_the_sun = card_type("the_foundation_of_the_sun",
    attributes(winter=2, wall_art=1, woven=1),
    consider_output = memory.sight,
)


# 'The Foundlings'
#
# A pair of human eyes peer from darkness in a tangle of roots.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_foundlings = card_type("the_foundlings",
    attributes(heart=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The Hatching'
#
# Human figures crawl from a clamshell.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_hatching = card_type("the_hatching",
    attributes(scale=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The Mansus'
#
# There have been many attempts to depict the House of the Sun. This, by the visionary painter known only as the Magyar, is the best known. It's signed and dated - if it's really the original, it must count as one of the great treasures of the House.
# ---
# Scrutiny
#
# 'Beneath the skin of the world we find the Mansus, also called the World-Spine, also called the House of the Sun. The Mansus is the home of the Hours, on which the world depends, and a sojourning-place for certain departed souls. Above the House is the Glory, the origin of light, to which souls aspire. At the foot of the House, and around its walls - though it has no walls - is the Wood. Beneath the House is Nowhere…'
the_mansus = card_type("the_mansus",
    attributes(knock=2, lantern=2, moth=2, wall_art=1),
    consider_output = memory.sight,
)


# 'The Sister-and-Witch'
#
# 'The Sister-and-Witch brings together what cannot be apart. She is sought beneath the moon and at the water's edge. She is pearl, amber, coral; she cannot be touched; she cannot be separated.'
# ---
# Scrutiny
#
# Abbot Geffrey recorded a prophetic dream: two women, one in violet, one in white, gathering seashells. The white-clad one, he wrote, handed him a shell and reminded him that one cannot keep what one cannot hold…
the_sister_and_witch = card_type("the_sister_and_witch",
    attributes(grail=1, heart=2, moth=2, wall_art=1),
    consider_output = memory.sight,
)


# 'The Tattered Outlaw'
#
# Thirza Blake, Seventh Librarian of Hush House, liked painting donkeys. No-one else liked her donkey paintings, but Thirza never much cared what other people liked.
# ---
# Scrutiny
#
# For some reason, this donkey has human eyes. There is also a cigarette-holder  - with no cigarette - sticking coyly out of the corner of its mouth.
the_tattered_outlaw = card_type("the_tattered_outlaw",
    attributes(heart=1, scale=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The Thunderskin'
#
# 'He cannot be stilled; he demands the dance; he is beaten, like a drum. He is heard in the Wood below the world.'
# ---
# Scrutiny
#
# A story is told of Hendrik, 1st Baron Dewulf, and a local cunning man, one Red William, who placed a curse on the Dewulfs: 'There will be no seventh of their line.' There is another story that it was no curse but a prophecy, and that Hendrik did not execute William but kept him safe in the caves below the isle...
the_thunderskin = card_type("the_thunderskin",
    attributes(heart=2, sky=2, wall_art=1),
    consider_output = memory.sight,
)


# 'The Velvet'
#
# 'The Glory is a question, and the Moth always answers Yes. The Velvet's answer is No, and that is always her answer.'
# ---
# Scrutiny
#
# The Velvet is the Hour that keeps secrets, and this painting has no more secrets to share.
the_velvet = card_type("the_velvet",
    attributes(moon=2, wall_art=1),
    consider_output = memory.sight,
)


# 'The Watcher'
#
# Another of Valentine's paintings; a barn owl he nursed back to health.
# ---
# Scrutiny
#
# Owls, of course, are associated with the Horned-Axe; but only one with one of her blades.
the_watcher = card_type("the_watcher",
    attributes(knock=2, lantern=2, wall_art=1),
    consider_output = memory.sight,
)


# 'The Wheel Still Turns'
#
# A shining spoked Wheel with a vaguely organic look turns beneath a full moon that holds her finger to her lips.
# ---
# Scrutiny
#
# Signed 'Nina Lagasse'.
the_wheel_still_turns = card_type("the_wheel_still_turns",
    attributes(moon=1, wall_art=1),
    consider_output = memory.sight,
)


# 'The Witch-and-Sister'
#
# 'The Witch-and-Sister unites what is at rest. She is sought at the water's edge and beneath the moon. She cannot be separated; she cannot be touched; she is coral, amber, pearl'
# ---
# Scrutiny
#
# Abbot Geffrey recorded a prophetic dream: two women, one in violet, one in white, gathering seashells. Each gave him a shell, but each gave him different advice…
the_witch_and_sister = card_type("the_witch_and_sister",
    attributes(grail=2, heart=1, moth=2, wall_art=1),
    consider_output = memory.sight,
)


# 'To Be Fruitful'
#
# It's a decent copy of a Picasso… painted twenty years before Picasso painted the original. Brian Levinsen, up to his tricks again.
# ---
# Scrutiny
#
# Levinsen has signed it, but added a question mark after his signature.
to_be_fruitful = card_type("to_be_fruitful",
    attributes(grail=1, nectar=1, wall_art=1),
    consider_output = memory.sight,
)


# 'To Hear Those Voices'
#
# A Levinsen 'prefigure' - a copy of a painting that would not be committed to canvas by the <i>real</i> artist for twenty years.
# ---
# Scrutiny
#
# Kirchner, one of Levinsen's favourite pre-subjects. Kirchner and Levinsen fought in the Great War on opposite sides… but there is no reason to believe Kirchner had anything at all to do with Levinsen's death.
to_hear_those_voices = card_type("to_hear_those_voices",
    attributes(moon=2, nectar=1, wall_art=1),
    consider_output = memory.sight,
)


# Torgue's Foil
#
# A pin-sharp length of flexible steel. The blade is inscribed TORGUE.
# ---
# Scrutiny
#
# Torgue was one-half of the Edge dyad that Natalia Brulleau hoped to lure to Hush House - to learn from them or to imprison them?
torgues_foil = card_type("torgues_foil",
    attributes(edge=2, nectar=1, wall_art=1),
    consider_output = memory.touch,
)


# Wasters: Darling-Dear and Father Turk
#
# Wooden swords of recent manufacture, never used.
# ---
# Scrutiny
#
# Provided to the occupants of the cell, who clearly disdained and never used them.
wasters_darling_dear_and_father_turk = card_type("wasters_darling_dear_and_father_turk",
    attributes(edge=2, sky=1, wall_art=1),
    consider_output = memory.contradiction,
)


# Yeth-Hound Horns
#
# In times past the Yeth pursued the impious and impure across the moors of this country. Hendrik Dewulf never liked them.
# ---
# Scrutiny
#
# Someone has scratched derisively on one horn 'Pray Thou Upon This!'
yeth_hound_horns = card_type("yeth_hound_horns",
    attributes(grail=1, scale=2, wall_art=1, carcass=1),
    consider_output = memory.sight,
)

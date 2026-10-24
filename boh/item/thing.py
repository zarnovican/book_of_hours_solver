from ..item import memory
from ..model import attributes, card_type


# 'Abbot Geffrey'
#
# It was Abbot Geffrey who gave Natan of Regensburg sanctuary here, and decreed the building of the Barber's Tower where Natan and his family could dwell. In fifteenth-century England, only a determined and well-respected abbot could have persuaded the brothers to shelter a Jewish physician.
# ---
# Scrutiny
#
# The bust is carved from hazel wood. The night before Natan's arrival at the Isle, Abbot Geffrey recorded a certain prophetic dream… and there is an old tradition in this country concerning the prophetic virtues of hazel. Perhaps none of these things are related.
abbot_geffrey = card_type("abbot_geffrey",
    attributes(knock=1, thing=1),
    consider_output = memory.touch,
)


# 'Abbot Thomas'
#
# Thomas was one of the first abbots here, just before the beginning of the Solar Gothic period. This bust is much more recent - a nineteenth-century bronze. An inscription reads: SPEECH, THE FIRST SWORD.
# ---
# Scrutiny
#
# The Abbey chronicles record how Viking mercenaries were quartered at the Abbey. One of their number, Toke, attempted to loot the church, and his eyes are pecked out by 'thorn-beaked crows'. He repented, became a sworn brother of the abbey under the name Thomas, and rose in time to be Abbot. But that was not the end of his story...
abbot_thomas = card_type("abbot_thomas",
    attributes(moth=1, thing=1),
    consider_output = memory.sight,
)


# 'Abduction, Salvation'
#
# Either interpretation is plausible.
# ---
# Scrutiny
#
# The sculpture is signed 'SB'.
abduction_salvation = card_type("abduction_salvation",
    attributes(grail=1, knock=1, thing=1),
    consider_output = memory.touch,
)


# 'Ambrose Westcott'
#
# This bust is cast in brass.
# ---
# Scrutiny
#
# Ambrose Westcott, first Librarian of Hush House: metallurgist, alchemist, pyrographer.
ambrose_westcott = card_type("ambrose_westcott",
    attributes(forge=1, thing=1),
    consider_output = memory.sight,
)


# Basket of Clean Linen
#
# A night-time luxury.
# ---
# Scrutiny
#
# I can use this to ensure a good night's sleep. [If you have no Beverages available to cure Maladies, this will do - though it won't provide any additional Power Aspects.]
basket_of_clean_linen = card_type("basket_of_clean_linen",
    attributes(heart=1, thing=1, woven=1, restorative=1),
    consider_output = memory.touch,
)


# Basket of Damp Towels
#
# A bath-time luxury (but soggy from use, now.)
# ---
# Scrutiny
#
# They'll be dry the next day.
basket_of_damp_towels = card_type("basket_of_damp_towels",
    attributes(heart=2, thing=1, woven=1, soaked=1),
    consider_output = memory.touch,
)


# Basket of Dirty Laundry
#
# Once washed, it'll be suitable again.
# ---
# Scrutiny
#
# No Librarian washes their own laundry. Perhaps I can find help in the village.
basket_of_dirty_laundry = card_type("basket_of_dirty_laundry",
    attributes(scale=1, thing=1, woven=1, soiled=1),
    consider_output = memory.touch,
)


# Basket of Towels
#
# A suitable companion for bathing.
# ---
# Scrutiny
#
# If I go swimming, I should take these. They'll be dry the next day.
basket_of_towels = card_type("basket_of_towels",
    attributes(heart=2, thing=1, woven=1),
    consider_output = memory.touch,
)


# Bobos of Spring
#
# A votive vessel for harvest offerings.
# ---
# Scrutiny
#
# It might be construed as friendly.
bobos_of_spring = card_type("bobos_of_spring",
    attributes(nectar=1, thing=1),
    consider_output = memory.touch,
)


# Bolt of Buttercup Linen
#
# Suitable for a summer suit or an altar-veil.
# ---
# Scrutiny
#
# This is the colour that an Undivided Afternoon would choose to be.
bolt_of_buttercup_linen = card_type("bolt_of_buttercup_linen",
    attributes(lantern=2, moon=2, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# Bolt of Moss-Green Velvet
#
# Suitable for a ball gown or a jewel's cushion.
# ---
# Scrutiny
#
# This is the colour that a first forest might choose to be.
bolt_of_moss_green_velvet = card_type("bolt_of_moss_green_velvet",
    attributes(grail=2, winter=2, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# Bolt of Pale Silk
#
# Suitable for handkerchiefs or anbaric experiments.
# ---
# Scrutiny
#
# This is the colour that the snow before spring would choose to be.
bolt_of_pale_silk = card_type("bolt_of_pale_silk",
    attributes(moth=2, nectar=2, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# 'Brian Levinsen'
#
# This bust is cast from aluminium - oxidised to grey.
# ---
# Scrutiny
#
# Brian Levinsen, ninth Librarian, painter and doctor, who never returned from the Western Front.
brian_levinsen = card_type("brian_levinsen",
    attributes(moth=1, thing=1),
    consider_output = memory.sight,
)


# Cat of Depths
#
# A votive offering to the Horned-Axe.
# ---
# Scrutiny
#
# The Horned-Axe has been known to appreciate both owls and cats.
cat_of_depths = card_type("cat_of_depths",
    attributes(scale=1, thing=1),
    consider_output = memory.sight,
)


# Cranial Tchotchke
#
# We all of us come to this condition in the end, but not all of us are fortunate enough to be lovingly buffed and fixed carefully to a stylish wooden stand.
# ---
# Scrutiny
#
# There is no sign of any cranial trauma; rule that out as a cause of death.
cranial_tchotchke = card_type("cranial_tchotchke",
    attributes(winter=1, thing=1),
    consider_output = memory.sight,
)


# Cyprian's Lamp
#
# A curio brought back from one of Serena Blackwood's trips to Greece.
# ---
# Scrutiny
#
# On the base is scratched SERENA. FOR THE BAY AT SUNSET. XX
cyprians_lamp = card_type("cyprians_lamp",
    attributes(grail=1, thing=1, light=1),
    consider_output = memory.sight,
)


# Daybreak Clock
#
# A particularly unrepentant example of the roccoco style of the mid-eighteenth century.
# ---
# Scrutiny
#
# Ambrose Westcott loved this clock. Most of his successors thought it was hideous, so it's been quietly shuffled from room to room where they didn't have to look at it, until it ended up here.
daybreak_clock = card_type("daybreak_clock",
    attributes(forge=1, thing=1),
    consider_output = memory.touch,
)


# 'Eva Dewulf'
#
# This is the crystal called scolecite - the worm-stone - polished to chill smoothness.
# ---
# Scrutiny
#
# Baroness Eva - satirist, salonnière, herpetologist, and last of the Dewulfs.
eva_dewulf = card_type("eva_dewulf",
    attributes(winter=1, thing=1),
    consider_output = memory.sight,
)


# Flour
#
# Pulverised grains, bread's precursor. [Mix with Butter or Milk for Dough; mix with Water for Batter.]
# ---
# Scrutiny
#
# Oooops.
flour = card_type("flour",
    attributes(heart=1, nectar=1, thing=1, cooking_ingredient=1),
    consider_output = memory.touch,
)


# 'Fraser Strathcoyne'
#
# This bust is shaped from beeswax. Careful with it!
# ---
# Scrutiny
#
# Fraser Strathcoyne, 'the Collector', formerly Treasurer of the Curia and (briefly, in the absence of other candidates, and to his annoyance) fourth Librarian.
fraser_strathcoyne = card_type("fraser_strathcoyne",
    attributes(scale=1, thing=1),
    consider_output = memory.sight,
)


# Fringed Lamp
#
# A cosy little night light.
# ---
# Scrutiny
#
# The base is  unexpectedly heavy. Obsidian?
fringed_lamp = card_type("fringed_lamp",
    attributes(lantern=1, thing=1, light=1),
    consider_output = memory.sight,
)


# Frith-Weft
#
# The 'peace-weaving' for which the Abbey was famous, long before it was named for St Brandan, when it was the Abbey of the Black Dove or the Abbey of the White Crow
# ---
# Scrutiny
#
# Tease it apart, and hear the distant crackle of old, peace-bound hatreds, twitching to life in the forgotten Histories. [There are Scholar-level Heart recipes that can craft one of these with fabric.]
frith_weft = card_type("frith_weft",
    attributes(heart=3, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# 'Gervinus van Lauren'
#
# This bust is cast in highly polished bronze.
# ---
# Scrutiny
#
# Gervinus van Lauren, eleventh Librarian of Hush House: an enigmatic recluse and reluctant ally of the Suppression Bureau, as skilled at closing ways as his predecessor Harries was at opening them.
gervinus_van_lauren = card_type("gervinus_van_lauren",
    attributes(knock=1, thing=1),
    consider_output = memory.sight,
)


# 'Gideon Dewulf'
#
# The bust is terracotta, brightly painted.
# ---
# Scrutiny
#
# Gideon the physician, fifth of his line, nicknamed 'the Motley Baron' by those who disliked him and 'the Cutter' by those who feared him.
gideon_dewulf = card_type("gideon_dewulf",
    attributes(heart=1, thing=1),
    consider_output = memory.sight,
)


# Glinting Cranial Tchotchke
#
# We all of us come to this condition in the end, but not all of us are fortunate enough to be lovingly buffed and fixed carefully to a stylish wooden stand.
# ---
# Scrutiny
#
# Someone has tucked a glinting lens into one of its eye-sockets.
# ---
# Scrutiny
#
# There is no sign of any cranial trauma; rule that out as a cause of death.
glinting_cranial_tchotchke = card_type("glinting_cranial_tchotchke",
    attributes(rose=1, thing=1),
    #consider_output = xxx .. morph
)


# Goddess-who-changes-skin
#
# 'To every god her skin.'
# ---
# Scrutiny
#
# A forgotten Name of the Moth?
goddess_who_changes_skin = card_type("goddess_who_changes_skin",
    attributes(moth=1, thing=1),
    consider_output = memory.touch,
)


# Half-Faceless Face
#
# A mask to fit a face that at the very least began as human.
# ---
# Scrutiny
#
# A soft melancholy lingers in its single eye…
half_faceless_face = card_type("half_faceless_face",
    attributes(scale=1, thing=1),
    consider_output = memory.touch,
)


# Hallowed Anthropoderm
#
# Yes, it's human skin, but it's not <i>just</i> human skin.
# ---
# Scrutiny
#
# Blessed by the priests of the Thunderskin, in those hollows of time where the Thunderskin is honoured for his work of preservation…
hallowed_anthropoderm = card_type("hallowed_anthropoderm",
    attributes(heart=2, thing=1, blank=1),
    consider_output = memory.touch,
)


# 'Hendrik Dewulf'
#
# Hendrik Dewulf, 1st Baron Brancrug, known for his pious, merciless justice. Granted Brancrug Isle in 1536 after the dissolution of St Brandan's.
# ---
# Scrutiny
#
# Dewulf had been a mercenary captain on the Continent, under the notorious Maarten van Rossum. He was a hard man in a hard time, but not a simple one. He left van Rossum's service after the sack of the Hague, apparently after a spiritual crisis;  it is known that he was at one point in training as a priest.
hendrik_dewulf = card_type("hendrik_dewulf",
    attributes(edge=1, thing=1),
    consider_output = memory.sight,
)


# Hendrik's Blade
#
# A long hunting knife, or a short close-quarters sword. A plaque reads 'Hendrik Dewulf, 1525'
# ---
# Scrutiny
#
# If the blade is real and the date correct, Hendrik must have borne this weapon during his time on the Continent, long before he ever became first Baron Brancrug… perhaps even in the 1527 Sack of Rome, which apparently provoked his spiritual crisis and brought him, eventually, to Brancrug.
hendriks_blade = card_type("hendriks_blade",
    attributes(edge=2, lantern=1, thing=1, knife=1),
    consider_output = memory.touch,
)


# Hurricane Lamp
#
# Proof against storm-wind and moth-swoop alike.
# ---
# Scrutiny
#
# Unimpeachably sturdy.
hurricane_lamp = card_type("hurricane_lamp",
    attributes(lantern=1, sky=1, thing=1, light=1),
    consider_output = memory.sight,
)


# Hush House Key
#
# Heavy enough that it takes both hands to turn. Heavy enough to brain someone, though you'd need both hands for that too.
# ---
# Scrutiny
#
# Serena Blackwood herself forged this key. 'I'm tired of losing it,' she said.
hush_house_key = card_type("hush_house_key",
    attributes(knock=3, winter=3, thing=1, key=1),
    consider_output = memory.sound,
)


# Inscribed Clock
#
# A gift from Sir David Greene to a favoured retainer.
# ---
# Scrutiny
#
# 'A.M.F. SORRY ABOUT THE MIRRORS. - D.G.'
inscribed_clock = card_type("inscribed_clock",
    attributes(winter=1, thing=1),
    consider_output = memory.sight,
)


# Inscribed Stone
#
# A stone tablet with rows of badly worn scratches that once, probably, were writing.
# ---
# Scrutiny
#
# Successive Librarians all failed to decipher this tablet. It might as easily be a household inventory or an invocation to a god. Natalia Brulleau established a tradition that it always remain in the Librarian's quarters, to inspire her, and her successors, with humility and to illustrate the limits of knowledge.
inscribed_stone = card_type("inscribed_stone",
    attributes(lantern=3, thing=1),
    consider_output = memory.sight,
)


# 'Kitty Mazarine'
#
# This bust is carved from black limestone.
# ---
# Scrutiny
#
# Kitty Mazarine, second Librarian - musician, composer, one-time placée. 'Almost French, almost Spanish, or almost American.'
kitty_mazarine = card_type("kitty_mazarine",
    attributes(grail=1, thing=1),
    consider_output = memory.sight,
)


# Lacquered Bone Chess Set
#
# Born of battles?
# ---
# Scrutiny
#
# The white queen and black king are both scowling. But the black queen and white king are both grinning delightedly.
lacquered_bone_chess_set = card_type("lacquered_bone_chess_set",
    attributes(edge=2, winter=1, thing=1),
    consider_output = memory.sight,
)


# Librarian's Glasses
#
# They're not lenses; just plain glass! But a certain sort of visitor is disappointed by a librarian who doesn't wear glasses.
# ---
# Scrutiny
#
# Of much more recent manufacture than they might appear. Possibly one of Gervinus van Lauren's little jokes.
librarians_glasses = card_type("librarians_glasses",
    attributes(lantern=1, thing=1, glass=1, light=1),
    consider_output = memory.sight,
)


# Librarian's Timepiece
#
# One of Ambrose Westcott's appalling roccoco enthusiasms. This one, less ugly than some, was suffered to remain by his sentimental successors.
# ---
# Scrutiny
#
# Inscribed 'ALAS CARBONEK'.
librarians_timepiece = card_type("librarians_timepiece",
    attributes(lantern=1, thing=1),
    consider_output = memory.sight,
)


# Masquewatch Clock
#
# Reputedly crafted for the Masque of Masques during the Great Writhing.
# ---
# Scrutiny
#
# A handle that looks like a pull-repeat - to strike the hour again - produces only a discouraging rustling sound…
masquewatch_clock = card_type("masquewatch_clock",
    attributes(lantern=1, thing=1),
    consider_output = memory.touch,
)


# 'Musgrave Dewulf'
#
# The bust is carved from wood - cherry?
# ---
# Scrutiny
#
# Musgrave Dewulf, who was mocked as 'the Bleating Baron' even while Brancrug prospered quietly, who was renowned for his piety but who won praise from the magus Julian Coseley. A quiet contradiction of a man.
musgrave_dewulf = card_type("musgrave_dewulf",
    attributes(rose=1, thing=1),
    consider_output = memory.sight,
)


# 'Natalia Brulleau'
#
# This bust is cast in iron.
# ---
# Scrutiny
#
# Natalia Brulleau, fifth Librarian - duellist, mystic, traveller.
natalia_brulleau = card_type("natalia_brulleau",
    attributes(edge=1, thing=1),
    consider_output = memory.sight,
)


# Ninewink Clock
#
# The most effective and irrefutable alarm clock ever to grace the House.
# ---
# Scrutiny
#
# The alarm can only be switched off with a particular rotation of the key. Lazier Librarians have found it easier just to let the thing run down.
ninewink_clock = card_type("ninewink_clock",
    attributes(moon=1, thing=1),
    consider_output = memory.touch,
)


# Nivine Parchment
#
# Pale as the first wisp of mountain-cloud.
# ---
# Scrutiny
#
# What animal gave its skin to make this parchment? Something colourless as glass and snow; something bleached and wrung and purer than silence.
nivine_parchment = card_type("nivine_parchment",
    attributes(winter=1, thing=1, blank=1),
    consider_output = memory.touch,
)


# Owl of Spirals
#
# An ancient bird for an ancient place.
# ---
# Scrutiny
#
# 'To every cry its beginning.'
owl_of_spirals = card_type("owl_of_spirals",
    attributes(knock=1, moth=1, rose=1, thing=1),
    consider_output = memory.touch,
)


# Pale Bust
#
# A delicate-featured young (?) woman. An inscription reads ABRA SOUTHEY.
# ---
# Scrutiny
#
# The bust bears a slight but definite resemblance to the many depictions of the notorious Eva Dewulf. But surely Eva bore only a son, and her grand-daughters died young.
pale_bust = card_type("pale_bust",
    attributes(moon=1, thing=1),
    consider_output = memory.touch,
)


# Pigeon Statuette
#
# A beautifully enamelled little image. The maker's mark is 'AW'.
# ---
# Scrutiny
#
# Was Ambrose Westcott really asked to provide a 'watcher of the skies?'
pigeon_statuette = card_type("pigeon_statuette",
    attributes(sky=1, thing=1),
    consider_output = memory.sight,
)


# Potatoes
#
# [Slice 'em with a Knife and add dripping to make Game Chips; or roast 'em with or without dripping.]
# ---
# Scrutiny
#
# Appetite satisfied.
potatoes = card_type("potatoes",
    attributes(heart=1, winter=1, thing=1, cooking_ingredient=1),
    consider_output = memory.touch,
)


# Quire of Paper
#
# Creamy-smooth, eagerly awaiting ink.
# ---
# Scrutiny
#
# How much exactly is a quire? Enough, that's how much.
quire_of_paper = card_type("quire_of_paper",
    attributes(nectar=1, thing=1, blank=1, fuel=1),
    consider_output = memory.sight,
)


# Red Lotus Vase
#
# A red-glazed chinoiserie vase.
# ---
# Scrutiny
#
# A local reproduction; but a good one.
red_lotus_vase = card_type("red_lotus_vase",
    attributes(grail=1, heart=1, thing=1),
    consider_output = memory.sight,
)


# Reference Image
#
# This is no kind of reference for conventional medicine…
# ---
# Scrutiny
#
# The junction-points of the soul are clearly marked.
reference_image = card_type("reference_image",
    attributes(heart=2, thing=1),
    consider_output = memory.touch,
)


# Regensburg Menorah
#
# A relic of the physician Natan of Regensburg.
# ---
# Scrutiny
#
# The monks of St Brandan's were recorded to have expressed concerns about Natan's 'many-headed device'.
regensburg_menorah = card_type("regensburg_menorah",
    attributes(heart=1, lantern=2, thing=1, light=1),
    consider_output = memory.sight,
)


# 'Serena Blackwood'
#
# This bust is carved from alabaster.
# ---
# Scrutiny
#
# Serena Blackwood, tenth Librarian, a redoubtable scholar and administrator who quarrelled with the prison governor and never completed her term.
serena_blackwood = card_type("serena_blackwood",
    attributes(lantern=1, thing=1),
    consider_output = memory.sight,
)


# 'Sir David Greene'
#
# This bust is carved from reddish granite.
# ---
# Scrutiny
#
# Sir David Greene, eighth Librarian - a former Nocturnal Branch superintendent, better known for rooting out mysteries than illuminating them.
sir_david_greene = card_type("sir_david_greene",
    attributes(lantern=1, thing=1),
    consider_output = memory.sight,
)


# 'SISTER'
#
# Priestess? Oracle? Queen? A very old image from the Dawn Period with a simple inscription.
# ---
# Scrutiny
#
# Before the Suppression Bureau, before the Curia of the Isle, before the Dewulfs, before the Church… the Sisters of the Knot were here. Almost a hundred generations have lived and died since this thing was shaped.
sister = card_type("sister",
    attributes(grail=1, thing=1),
    consider_output = memory.sight,
)


# 'Solomon Husher'
#
# This bust is the palest white marble.
# ---
# Scrutiny
#
# The Very Reverend Solomon Husher, third Librarian of Hush House. 'Nothing is a place. Everything ends.'
solomon_husher = card_type("solomon_husher",
    attributes(winter=1, thing=1),
    consider_output = memory.sight,
)


# 'St Melancthe'
#
# Visionary, philosopher, alchemist. Most revered, and most heterodox, of the isle's abbesses. An inscription in Latin reads: THE CROSS DIED NOT BUT PASSED WITHIN.
# ---
# Scrutiny
#
# On closer inspection, this is a reliquary bust; which is to say, if I cracked it open, I could retrieve St Melancthe's actual skull. That would be uncouth.
st_melancthe = card_type("st_melancthe",
    attributes(lantern=2, thing=1),
    consider_output = memory.sight,
)


# Strategist's Lamp
#
# Purchased by Governor Collers from a complicated general after the Great War.
# ---
# Scrutiny
#
# In certain obscure contexts, the Great War is referred to as the 'Second Worm War'. But the Suppression Bureau discourages - suppresses, in fact - use of that term.
strategists_lamp = card_type("strategists_lamp",
    attributes(edge=1, thing=1, light=1),
    consider_output = memory.sight,
)


# 'The Velvet'
#
# An Hour of secrecy? Ignorance? Privacy? Shame? The Velvet has never encouraged insight, investigation, or worship. Even an image of her is unusual.
# ---
# Scrutiny
#
# The material is painted iron. The craftsmanship is commendable, but the artist's name has been obliterated by furious scratching and scoring.
the_velvet = card_type("the_velvet",
    attributes(moon=2, thing=1),
    consider_output = memory.touch,
)


# The Writing on the Wall
#
# The most delicious traditions of the Carapace Cross, as recorded on the walls of the Mansus and transcribed into a book of ninety-nine pages by one known only as 'cc'. Although this book does not exist, it is read to a sleeper under certain very specific circumstances - and certain fragments jotted down on waking. [This 'book' houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# 'It was Hunger that made Worms of Dragons - when they consumed the corpses of Hours. Without the savour-secret of the Carapace, their hunger would not have been sufficient…'
# ---
# I've Read...
#
# Here is outlined the savour-secret of the Carapace, which harnesses hunger to permit impossible hybridisations. With this secret, even the most potent and fundamental entities have devoured and been devoured. And this, no doubt, is why it's secret.
the_writing_on_the_wall = card_type("the_writing_on_the_wall",
    attributes(tally_price=8, mystery_nectar=10, written_in_vak=1, readable=1, thing=1, dawn_period=1, subject_spices_and_savours=1),
    lessons=2,
    provides=memory.an_irresistible_feast,
)


# 'Thirza Blake'
#
# This bust is carved from malachite.
# ---
# Scrutiny
#
# Thirza Blake, seventh Librarian, mistress of Wood-lore, squanderer of fortunes, giver of no damns whatsoever.
thirza_blake = card_type("thirza_blake",
    attributes(nectar=1, thing=1),
    consider_output = memory.sight,
)


# 'Thomas Dewulf'
#
# The bust is carved from limestone.
# ---
# Scrutiny
#
# Thomas Dewulf, called 'Baron Silence', second of his line - astronomer, ouranoscoper, who followed in the footsteps of his long-deceased namesake.
thomas_dewulf = card_type("thomas_dewulf",
    attributes(lantern=1, thing=1),
    consider_output = memory.sight,
)


# Twilight Pot
#
# A stylised bat grimaces gleefully on its surface.
# ---
# Scrutiny
#
# It might have been intended to be menacing. It is in no way menacing.
twilight_pot = card_type("twilight_pot",
    attributes(moon=1, sky=1, thing=1),
    consider_output = memory.sight,
)


# Twinned-Fish Stone
#
# This stone disc is lighter than it should be; and the surface is soapy-smooth.
# ---
# Scrutiny
#
# A memorial stone preserved from Ys, the city behind the sea…
twinned_fish_stone = card_type("twinned_fish_stone",
    attributes(moon=1, thing=1),
    consider_output = memory.touch,
)


# 'Valentine Dewulf'
#
# Valentine Dewulf, 6th Baron Brancrug, known for his eccentricities. 'IN THE SKY HE SOUGHT HIS FRIENDS', an inscription reads.
# ---
# Scrutiny
#
# In 1721, poor Valentine fell from the top of the Gullscry Tower. Perhaps it was his melancholia that killed him - there were no witnesses, and his body was not found for three days. His son, Eales, was in no fit shape to inherit; and so his daughter Eva became Baroness at the age of only nineteen.
valentine_dewulf = card_type("valentine_dewulf",
    attributes(sky=1, thing=1),
    consider_output = memory.sight,
)


# 'Walter Dewulf'
#
# The bust is carved from serpentinite - a striking local stone.
# ---
# Scrutiny
#
# Walter Dewulf, who found Hush House a draughty castle and left it a stately home, but who will always be remembered for his cowardice, his sorrow, and his son Bryan's treachery.
walter_dewulf = card_type("walter_dewulf",
    attributes(scale=1, thing=1),
    consider_output = memory.sight,
)


# Warmly Coloured Yarns
#
# A blushing nest of possibilities.
# ---
# Scrutiny
#
# Each thread departs the next…
warmly_coloured_yarns = card_type("warmly_coloured_yarns",
    attributes(grail=1, heart=1, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# White Matilda
#
# In 1093, twin infant girls were admitted to the care of the sisters here. Both were named Matilda. In 1127, the elder of the two became Abbess.
# ---
# Scrutiny
#
# According to gossip and circumstantial evidence, the Matildas were illegitimate daughters of Gunnhild, daughter of King Harold, and a brother of the Earl of Cornwall - though which brother is a particularly murky question.
white_matilda = card_type("white_matilda",
    attributes(winter=2, thing=1),
    consider_output = memory.touch,
)


# 'Willem Harries'
#
# This bust is cast in highly polished bronze.
# ---
# Scrutiny
#
# Willem Harries, sixth Librarian, priest and nyctodromist, whose end has always remained obscure.
willem_harries = card_type("willem_harries",
    attributes(knock=1, thing=1),
    consider_output = memory.sight,
)


# Wyrd-Weft
#
# A weave that either entrains, or follows, Fate. It's hard to be sure which.
# ---
# Scrutiny
#
# Tease it apart, and find what might have been. [There are Keeper-level Winter recipes which can craft one of these with fabric.]
wyrd_weft = card_type("wyrd_weft",
    attributes(heart=3, winter=6, thing=1, fabric_and_fibre=1),
    consider_output = memory.touch,
)


# Yellowing Newspaper
#
# It's dated the year that Hush House was abandoned.
# ---
# Scrutiny
#
# Nothing's history when first it happens…
yellowing_newspaper = card_type("yellowing_newspaper",
    attributes(rose=1, thing=1),
    consider_output = memory.occult_scrap,
)

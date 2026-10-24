from ..item import memory
from ..model import attributes, card_type


# Ambrose's Favourite Chair
#
# Somewhat pocked with cigar-burns.
# ---
# Scrutiny
#
# Ambrose Westcott was a capacious gentleman, and he ensured the springs in this his fortress were calibrated to bear any conceivable weight. Two hundred years on, the springs still do their duty.
ambroses_favourite_chair = card_type("ambroses_favourite_chair",
    attributes(grail=1, comfort=1),
    consider_output = memory.touch,
)


# Atrium Chair
#
# Reserved for latecomers, non-believers, and the pensive.
# ---
# Scrutiny
#
# Is there any accusatory element to its creaks? Was that intentional?
atrium_chair = card_type("atrium_chair",
    attributes(lantern=1, comfort=1),
    consider_output = memory.touch,
)


# 'Authority'
#
# Once this shepherd's crook represented the authority of the Church. Perhaps the Suppression Bureau kept it here because they liked the idea of authority, in general.
# ---
# Scrutiny
#
# The Suppression Bureau, of course, is of a more ecclesiastical character than its progenitory Nocturnal Branch, though it has never had any <i>official</i> links to the Church Solar…
authority = card_type("authority",
    attributes(lantern=1, comfort=1),
    consider_output = memory.sight,
)


# Bell-Tower Chair
#
# Sturdy, undistinguished, and, like so much else in the House, the last of its kind.
# ---
# Scrutiny
#
# Serena Blackwood brought this chair up the church tower stairs to sit and read by candle-light. The stairs were tough on her knees, but she learnt that Governor Collers was unlikely to bother her here.
bell_tower_chair = card_type("bell_tower_chair",
    attributes(forge=1, sky=2, comfort=1),
    consider_output = memory.touch,
)


# Carpenter's Stool
#
# Irreparably wobbly. Perhaps it's haunted.
# ---
# Scrutiny
#
# Someone has deliberately sanded down the end of each leg to a different angle.
carpenters_stool = card_type("carpenters_stool",
    attributes(edge=1, moth=2, comfort=1),
    consider_output = memory.touch,
)


# Chair of Challenges
#
# Here the Librarian Harries sat, to formulate the paradoxes he would bequeath to van Lauren.
# ---
# Scrutiny
#
# Perhaps the faintest, driest voice murmured: 'Who will see the Second Dawn?' Or perhaps that was only something that once I read.
chair_of_challenges = card_type("chair_of_challenges",
    attributes(knock=1, comfort=1),
    consider_output = memory.sound,
)


# Chaise-Longue of Conclusions
#
# Here the Librarian van Lauren lay, to ponder the paradoxes he had inherited from Harries.
# ---
# Scrutiny
#
# 'Perhaps the faintest, driest voice murmured: 'The Librarian that comes after is not the Librarian.' Or perhaps that was only something that once we read.
chaise_longue_of_conclusions = card_type("chaise_longue_of_conclusions",
    attributes(grail=1, knock=1, comfort=1),
    consider_output = memory.sound,
)


# Comfortable Garden Chair
#
# Amateurishly varnished, characterfully stained.
# ---
# Scrutiny
#
# Shadows shift, sun-bars follow.
comfortable_garden_chair = card_type("comfortable_garden_chair",
    attributes(nectar=1, comfort=1),
    consider_output = memory.touch,
)


# Contemplative Seat
#
# Perch here to meditate on the mysteries of dawn.
# ---
# Scrutiny
#
# 'Light like the ever-burning Wheel rolls all our sins away / they fly forgotten as a dream dies at the opening day.'
contemplative_seat = card_type("contemplative_seat",
    attributes(lantern=1, comfort=1),
    consider_output = memory.touch,
)


# Delightful Repose
#
# Placed by the Curia of the Isle to allow a rest before an ascent. Or after a descent.
# ---
# Scrutiny
#
# What's this down the back of the cushions? A small and unexpected treasure.
# ---
# Scrutiny
#
# House folklore claims that Ambrose Westcott suffered his final apoplexy on this sofa, after a particularly hasty trample up and down the stairs to argue with visiting priests.
delightful_repose = card_type("delightful_repose",
    attributes(grail=1, comfort=1),
    consider_output = memory.touch,
)


# Elegant Sunburst Lamp
#
# A bright tree of brass.
# ---
# Scrutiny
#
# An inscription on the pediment reads 'The Gods-from-steel did not exist.'
elegant_sunburst_lamp = card_type("elegant_sunburst_lamp",
    attributes(lantern=3, comfort=1, light=1),
    consider_output = memory.sight,
)


# Expansive Chair
#
# Upholstered in a velvet of peculiar richness that invites the hand. Sit down a while. You've earned it.
# ---
# Scrutiny
#
# A printed card reads: NOW SAFE TO SLEEP IN THIS CHAIR. G.C.
expansive_chair = card_type("expansive_chair",
    attributes(grail=1, moon=1, comfort=1),
    consider_output = memory.touch,
)


# Grand Reading Armchair
#
# Nestle grandly.
# ---
# Scrutiny
#
# Once a favoured chair of the Treasurer of the Curia - an office that Fraser Strathcoyne often held, and much preferred to the post of Librarian.
grand_reading_armchair = card_type("grand_reading_armchair",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Greene's Red Chair
#
# A little wobbly. Greene used to lean forward.
# ---
# Scrutiny
#
# Someone has absent-mindedly carved symbols down one leg. From top to bottom: a cup; a winged insect; an axe; a candle.
greenes_red_chair = card_type("greenes_red_chair",
    attributes(grail=1, comfort=1),
    consider_output = memory.touch,
)


# Imposing Reading Armchair
#
# Nestle imposingly.
# ---
# Scrutiny
#
# A printed card reads: NOW PROBABLY SAFE TO SLEEP IN THIS CHAIR. G.C.
imposing_reading_armchair = card_type("imposing_reading_armchair",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Inviting Footstool
#
# How many home from the storm propped their feet here and gazed into the fire?
# ---
# Scrutiny
#
# Ambrose Westcott was once lost on the moors. He would not suffer it to be spoken of. Thirza Blake was often lost on the moors. She would not suffer it not to be spoken of.
inviting_footstool = card_type("inviting_footstool",
    attributes(grail=1, comfort=1),
    consider_output = memory.touch,
)


# Kitty's Armchair
#
# This <i>looks</i> very like the armchair in which Kitty Mazarine, second Librarian, sat for El Bretón's famous group portrait.
# ---
# Scrutiny
#
# Kitty Mazarine (the story goes) napped in an armchair and dreamt of mirrors. She woke to find herself humming an unknown melody. That melody became her fuging-tune 'Thirty Birds'. If this is really that armchair, it's a little bit of history.
kittys_armchair = card_type("kittys_armchair",
    attributes(sky=1, comfort=1),
    consider_output = memory.touch,
)


# 'Lady de Braose'
#
# Sometimes known affectionately as 'the first Eva'. Lady de Braose never visited the Isle, but it was her generous endowment that allowed the Abbey to thrive and grow in the thirteenth century.
# ---
# Scrutiny
#
# Why did Eva de Braose, the widow of a Marcher Lord from much further north, take such an interest in St Brandan's? There are stories…
lady_de_braose = card_type("lady_de_braose",
    attributes(heart=1, comfort=1),
    consider_output = memory.sight,
)


# 'Lady Rowena'
#
# For as long as there has been a Hush House, there have been stories of its enigmatic protectress.
# ---
# Scrutiny
#
# A Henry Moore piece - perhaps a genuine one. Moore did speak, very cautiously, of an 'encounter with a pale commission.'
lady_rowena = card_type("lady_rowena",
    attributes(winter=1, comfort=1),
    consider_output = memory.sight,
)


# Librarian's Armchair
#
# A sea-coloured, star-ornamented armchair.
# ---
# Scrutiny
#
# According to consistent tradition, this is the most comfortable chair in the entire House.
librarians_armchair = card_type("librarians_armchair",
    attributes(lantern=1, comfort=1),
    consider_output = memory.sight,
)


# Librarian's Footstool
#
# A sea-coloured, star-ornamented footstool.
# ---
# Scrutiny
#
# Put your feet up. The House is yours. Your work might not be done, but you've earned a rest.
librarians_footstool = card_type("librarians_footstool",
    attributes(lantern=1, comfort=1),
    consider_output = memory.touch,
)


# Librarian's Stool
#
# A sea-coloured, star-ornamented stool.
# ---
# Scrutiny
#
# A stout little soldier, on whose worn surface have rested the slippers of a dozen generations of Librarians.
librarians_stool = card_type("librarians_stool",
    attributes(lantern=1, comfort=1),
    consider_output = memory.touch,
)


# Lingering Repose
#
# Upholstered in a velvet of peculiar richness that invites the hand.
# ---
# Scrutiny
#
# Carved on the back by the maker: BE WITH ME, A LITTLE WHILE. Hearts and flowers have also been carved, by an unauthorised but skilful hand.
lingering_repose = card_type("lingering_repose",
    attributes(grail=1, lantern=1, comfort=1),
    consider_output = memory.touch,
)


# Lumpy Melodic Chair
#
# Someone appears to have tuned the squeaks.
# ---
# Scrutiny
#
# Relax on it just <i>so</i>, and you can almost make out the first notes of Kitty Mazarine's fuging-tune, 'Thirty Birds'.
# ---
# Scrutiny
#
# Someone has tucked a sad little treasure beneath the seat cushion…
lumpy_melodic_chair = card_type("lumpy_melodic_chair",
    attributes(sky=1, comfort=1),
    #consider_output = xxx ..morph
)


# Melodic Chair
#
# Someone appears to have tuned the squeaks.
# ---
# Scrutiny
#
# Relax on it just <i>so</i>, and you can almost make out the first notes of Kitty Mazarine's fuging-tune, 'Thirty Birds'.
melodic_chair = card_type("melodic_chair",
    attributes(sky=1, comfort=1),
    consider_output = memory.touch,
)


# Moon Footstool
#
# A soft gold glimmer in the half-light.
# ---
# Scrutiny
#
# There is a stain half way down the side where, some time in the mid 1830s, Solomon Husher spilt his tea when he heard that Julian Coseley had apologised.
moon_footstool = card_type("moon_footstool",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Moon Stool
#
# Polished to pallor by the posteriors of past Librarians.
# ---
# Scrutiny
#
# A dark fruitwood - cherry? with very nicely executed joinery at the top.
moon_stool = card_type("moon_stool",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Morgue Boots
#
# Reliable rubber.
# ---
# Scrutiny
#
# Purchased the second time that the morgue was ever used.
morgue_boots = card_type("morgue_boots",
    attributes(winter=1, comfort=1),
    consider_output = memory.sight,
)


# Nighted Chair
#
# Solid, comfortable, oddly unobtrusive.
# ---
# Scrutiny
#
# 'Someone died in this chair,' I find myself thinking. There are no stains or remains; there is nothing at all to suggest that this might be true.
nighted_chair = card_type("nighted_chair",
    attributes(moon=1, comfort=1),
    consider_output = memory.fear,
)


# Nightsky Chair
#
# Velvet smooth as midnight.
# ---
# Scrutiny
#
# A sometime seat of the Secretary Enigmatic of the Curia, whose responsibilities and even identity were not widely discussed, but might conceivably have been one called 'cc'.
nightsky_chair = card_type("nightsky_chair",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Painter's Stool
#
# A comfortable enough perch.
# ---
# Scrutiny
#
# Someone has doggedly cleaned bird droppings and paint from this, not once but many times. The fabric is splotched and discoloured - the varnish of the wood is streaked like rain.
painters_stool = card_type("painters_stool",
    attributes(sky=1, comfort=1),
    consider_output = memory.touch,
)


# Pale Stool
#
# Bleached beech.
# ---
# Scrutiny
#
# Subtle, elegant fluting along each leg. Initialled L.T.P.
pale_stool = card_type("pale_stool",
    attributes(winter=1, comfort=1),
    consider_output = memory.sight,
)


# Paradise Palm
#
# An unquenchable vitality.
# ---
# Scrutiny
#
# Once, these grew only on one tiny island on the other side of the world. That's empire for you.
paradise_palm = card_type("paradise_palm",
    attributes(nectar=2, comfort=1),
    consider_output = memory.scent,
)


# Plain Stool
#
# The most reliable object imaginable. How old <i>is</i> it?
# ---
# Scrutiny
#
# It's older than one might expect. Very faintly, the triple knot can be made out on the underside of the seat…
plain_stool = card_type("plain_stool",
    attributes(winter=1, comfort=1),
    consider_output = memory.touch,
)


# Prison Stool
#
# A cheerful lavender colour, possibly to encourage rehabilitative enthusiasm.
# ---
# Scrutiny
#
# Someone has scratched a series of tally marks down one leg. Seventy-seven days.
prison_stool = card_type("prison_stool",
    attributes(heart=2, knock=1, comfort=1),
    consider_output = memory.touch,
)


# Reading Lamp
#
# To ensure clarity of vision even in utmost dark. It does flicker occasionally.
# ---
# Scrutiny
#
# A gift from Governor Collers - apparently, for once, without any ulterior motive.
reading_lamp = card_type("reading_lamp",
    attributes(lantern=1, comfort=1, light=1),
    consider_output = memory.sight,
)


# Restful Garden Chair
#
# Sit here and listen to the trees grow. Or the leaves fall. Preferences differ.
# ---
# Scrutiny
#
# Inlaid with green-stained bone.
restful_garden_chair = card_type("restful_garden_chair",
    attributes(nectar=1, comfort=1),
    consider_output = memory.touch,
)


# Restful Seat
#
# A dawn-coloured seat for a solar congregation.
# ---
# Scrutiny
#
# Sit in serenity.
restful_seat = card_type("restful_seat",
    attributes(heart=1, comfort=1),
    consider_output = memory.touch,
)


# Russet Couch
#
# A utilitarian item, arms varnished, upholstery shiny with hard use.
# ---
# Scrutiny
#
# Did Christopher Illopoly really have this stolen from a first-class waiting-room? And did he really bribe a bishop to keep the matter quiet?
russet_couch = card_type("russet_couch",
    attributes(moth=1, comfort=1),
    consider_output = memory.sight,
)


# Sea-Green Sofa
#
# Here, Lady Eva Dewulf would weave her intrigues, and satisfy her secret craving for sentimental novels.
# ---
# Scrutiny
#
# Lord Franklin Bancroft, magus and rake, was a frequent visitor to Hush House and his name was often linked with Lady Eva's. He provoked scandal with a lubricious encomium, <i>Thy Throne Malachite</i>, dedicated to this very item of furniture. Lady Eva took this badly, withdrawing Bancroft's invitation to Christmas dinner, but relented in time for her spring ball, on condition he attended dressed entirely in green.
sea_green_sofa = card_type("sea_green_sofa",
    attributes(winter=1, comfort=1),
    consider_output = memory.touch,
)


# Severe Chair
#
# Unfussy marsh-green upholstery.
# ---
# Scrutiny
#
# This chair is innocent of chairly secrets.
severe_chair = card_type("severe_chair",
    attributes(edge=1, comfort=1),
    consider_output = memory.touch,
)


# Snug Chair
#
# A wicker chair with a soft white lap blanket for chilly evenings.
# ---
# Scrutiny
#
# Is the blanket bear-skin? Polar bear? It might be, but it's softer than one would expect.
snug_chair = card_type("snug_chair",
    attributes(heart=2, scale=2, comfort=1),
    consider_output = memory.touch,
)


# Soft Blue Sofa
#
# Gently complements the seas and skies around Brancrug.
# ---
# Scrutiny
#
# Ambrose Westcott ordered the destruction of Valentine's bed, for reasons he did not choose to articulate. Much later, Brian Levinsen had this sofa installed so he could nap here.
soft_blue_sofa = card_type("soft_blue_sofa",
    attributes(moon=2, sky=2, comfort=1),
    consider_output = memory.touch,
)


# Spartan Chair
#
# The cushion has been removed, perhaps as an act of petty revenge.
# ---
# Scrutiny
#
# Hard Librarians value hard chairs.
spartan_chair = card_type("spartan_chair",
    attributes(edge=1, comfort=1),
    consider_output = memory.touch,
)


# Staff Armchair
#
# Polished by the posteriors of dozens of loafing prison guards.
# ---
# Scrutiny
#
# For a great many years this chair sat below a dartboard. The leather is pocked with the marks of occasional misses (or, just possibly, assassination attempts.)
staff_armchair = card_type("staff_armchair",
    attributes(knock=2, comfort=1),
    consider_output = memory.touch,
)


# Starstrewn Chair
#
# Velvet soft as starlight.
# ---
# Scrutiny
#
# The pattern was reputedly preferred by Baron Thomas.
starstrewn_chair = card_type("starstrewn_chair",
    attributes(moon=1, comfort=1),
    consider_output = memory.touch,
)


# Straw-Cushioned Chair
#
# Upholstered without any particular skill.
# ---
# Scrutiny
#
# A little scratchy, but an optimistic sort would point out that makes it easier to stay awake when one's eyelids waver.
straw_cushioned_chair = card_type("straw_cushioned_chair",
    attributes(lantern=1, comfort=1),
    consider_output = memory.touch,
)


# Treasury of Shelters
#
# It's like an armoury for not getting pneumonia.
# ---
# Scrutiny
#
# A thick deposit has accrued to the bottom of the stand. A hundred years of rain applied to a hundred winters of mud.
treasury_of_shelters = card_type("treasury_of_shelters",
    attributes(heart=1, sky=1, comfort=1),
    consider_output = memory.touch,
)


# Uncomfortable Seat
#
# Shaped to assure the attention of the faithful.
# ---
# Scrutiny
#
# Ornamented with the circled sun-cross of the Church.
uncomfortable_seat = card_type("uncomfortable_seat",
    attributes(knock=1, comfort=1),
    consider_output = memory.touch,
)


# Valentine's Memorial
#
# Valentine died two centuries ago. This stone is much newer - more like two decades old.
# ---
# Scrutiny
#
# Brian Levinsen, ninth Librarian of the House, often spoke of his sympathy for Valentine Dewulf. He commissioned this memorial stone in 1914, but by the time it arrived, he had volunteered as a medical officer in the Great War. He never returned; he never saw this memorial; and it became his own.
valentines_memorial = card_type("valentines_memorial",
    attributes(winter=3, comfort=1),
    consider_output = memory.touch,
)


# Violet Stool
#
# Damson cushion, holly-wood marquetry.
# ---
# Scrutiny
#
# The cushion is embroidered with the serpents of St Agnes.
violet_stool = card_type("violet_stool",
    attributes(knock=1, comfort=1),
    consider_output = memory.touch,
)


# Wicker Chair
#
# Elderly, but robust.
# ---
# Scrutiny
#
# A creaking cane back generates the occasional spiteful splinter.
wicker_chair = card_type("wicker_chair",
    attributes(heart=1, comfort=1),
    consider_output = memory.sight,
)


# Wine-Dark Chair
#
# An elegant eighteenth-century piece imported from France.
# ---
# Scrutiny
#
# There were twelve of these, but Gervinus van Lauren had most of them broken up and burnt the week after his arrival. 'Bad memories,' was all he would say.
wine_dark_chair = card_type("wine_dark_chair",
    attributes(grail=1, comfort=1),
    consider_output = memory.touch,
)


# Watchful Potted Plant
#
# Not everything needs eyes.
# ---
# Scrutiny
#
# The sense of awareness persists; but the plant remains immobile. Unsettling, but harmless. It doesn't even have thorns.
watchful_potted_plant = card_type("watchful_potted_plant",
    attributes(lantern=1, nectar=1, comfort=1),
    consider_output = memory.scent,
)

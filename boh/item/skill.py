from frozendict import frozendict

from ..item import lesson, soul
from ..model import attributes, card_type


# Anbary & Lapidary
#
# 'Lightning is a little life, and jewels are its eyes.' - Eva Dewulf
anbary_and_lapidary = card_type("anbary_and_lapidary",
    attributes(forge=1, sky=2, skill=1, horomachistry=1, ithastry=1),
    commit_output = frozendict(
        # Black Sapphire
        #
        # The Bright Arts speak of a shining City Unbuilt. One day, we might build it in the Mansus, the great house of dreams… with a foundation-stone of black sapphire. This would be a great matter of Horomachistry.
        horomachistry = soul.fet,

        # Amber
        #
        # The Bright Arts speak of a shining City Unbuilt. One day, we might build it like a jewel in the sea… with a foundation-stone of amber.  This would be a great work of Ithastry.
        ithastry = soul.phost,
    ),
)


# Applebright Euphonies
#
# 'Breath is the temptation of the soul.' Pleasures and insights that the Church would call 'the Secrets', the Sisterhood 'the Mysteries', and the Bureau 'unsanctioned.'
applebright_euphonies = card_type("applebright_euphonies",
    attributes(grail=1, sky=2, skill=1, the_bosk=1, illumination=1),
    commit_output = frozendict(
        # What May Be True
        #
        # Calyptra is the law that requires secret knowledge to be forgotten - except in the libraries of the Watchman's Tree. The number of the Hours of the Calyptra is three, and we do not trust the third Hour, though we heed her. This paradox is a matter of Illumination.
        illumination = soul.mettle,

        # What May Be Known
        #
        # Calyptra is the law that requires secret knowledge to be concealed - except in the libraries of the Watchman's Tree. The number of the Hours of the Calyptra is three, and we do not speak of the oldest Hour. This observance is a matter of Bosk. 
        the_bosk = soul.ereb,
    ),
)


# Auroral Contemplations
#
#'To know what will pass in what has passed.' The practitioners of this discipline see endings and beginnings, passages and transitions, in the same mode as dawn and sunset.
auroral_contemplations = card_type("auroral_contemplations",
    attributes(edge=1, lantern=2, skill=1, illumination=1, nyctodromy=1),
    commit_output = frozendict(
        # The First Sunrise
        #
        # Yesterday's light determines the colours of tomorrow... and through Illumination, we learn that we all began in light.
        illumination = soul.phost,

        # The Sunset Road
        #
        # Each journey is a day, and we are tested as travellers and as pilgrims. That is the part these Contemplations play in the Nyctodromy Wisdom.
        nyctodromy = soul.fet,
    ),
)


# Bells & Brazieries
#
# That resonance which lingers from the hammer's touch.
bells_and_brazieries = card_type("bells_and_brazieries",
    attributes(forge=2, sky=1, skill=1, horomachistry=1, ithastry=1),
    commit_output = frozendict(
        # The Toll
        #
        # In the right mortal's hand, the right tool can become the weapon that begins a war. This is a high consequence of Horomachistry.
        horomachistry = soul.mettle,

        # The Chime
        #
        # In the right mortal's hand, the right tool can become the weapon that ends a war. This is a high purpose of Ithastry.
        ithastry = soul.wist,
    )
)


# Coil & Chasm
#
# Worms, Seven-Coils, dangerous places; how earthquakes are bound and why they are released.
coil_and_chasm = card_type("coil_and_chasm",
    attributes(nectar=1, scale=2, skill=1, nyctodromy=1, skolekosophy=1),
    commit_output = frozendict(
        # Peacock
        #
        # The Night Arts teach that the Peacock Gate is the highest door in dreams to which mortals may aspire; but that before she rose to this estate, the Gate was a Name of the Horned-Axe. All nyctodromists seek to understand what this might mean.
        nyctodromy = soul.shapt,

        # Serpent
        #
        # The Night Arts speak of the Savage Door, to which Echidna, mother of monsters, keeps her Savage Key. It was the means by which the gods-who-were-stone entered the Mansus; for Echidna was once counted among their Names. All skolekosophists seek to understand what this might mean.
        skolekosophy = soul.ereb,
    ),
)


# Cracktrack
#
# In the Tracks of Beasts, in the Convolutions of his own Carapace, in Egg-vein and Shell-shadow, the Many-Eyed One found the Signs which can be History.
cracktrack =  card_type("cracktrack",
    attributes(nectar=2, scale=1, skill=1, language=1, illumination=1, preservation=1),
    commit_output = frozendict(
        # A Tongue of Sky
        #
        # Cracktrack was a gift from the light above the world. When Glory touched the first life-motes with this language, they entered the waking world. They were Illuminated.
        illumination = soul.phost,

        # A Tongue of Earth
        #
        # Cracktrack is the native tongue of the living world. As long as Cracktrack is spoken, in cloud-shape and hill-form, life persists. This is a matter of Preservation.
        preservation = soul.chor,
    ),
)


# Deep Mandaic
#
# The most secret script of the innermost rites of the deep sects of the deep desert. The birth-tongue, it is claimed, of the Mother of Ants herself.
deep_mandaic = card_type("deep_mandaic",
    attributes(forge=2, lantern=1, skill=1, language=1, horomachistry=1, ithastry=1),
    commit_output = frozendict(
        # The Jeweller's Tale
        #
        # There is a story known to jewellers: of a guild-master who made a wager with a keeper of butterflies. The master-jeweller claimed his jewelled egg would hatch something greater than any of the butterfly-keeper's chrysalids. Of course, after a month, the butterfly-keeper's gardens were bright with wings and the egg had hatched nothing at all. The jeweller, unable to pay his debts, fled into the desert with his egg. Horomachistry teaches us: know your limits.
        horomachistry = soul.mettle,

        # The Chandler's Tale
        #
        # There is a story known to candle-makers: of a guild-master who made a wager with a master of the potter's guild. The potter's oldest cup (she said) was older far than the chandler's oldest candle. However often one drinks from a cup, it can always be refilled. So they brought their witnesses to the judging on the appointed day, and the potter's witness brought a cup he had used for seventy years until its shattering. But the chandler's witness brought a candle seventy-<i>seven</i> years old: every month, the chandler had bought the old stumps, returned their matter to the vat, and used them in his wares, so that each newest candle was also the oldest. Ithastry teaches us: there's always a way.
        ithastry = soul.phost,
    ),
)


# Desires & Dissolutions
#
# The boundaries between flesh, pearl, and pleasure are equally contingent.
desires_and_dissolutions = card_type("desires_and_dissolutions",
    attributes(grail=2, moon=1, skill=1, the_bosk=1, horomachistry=1),
    commit_output = frozendict(
        # Above
        #
        # What begins in light may end in flesh. Without distinction and perception, pleasure cannot be distinguished from pain. These traditions are Horomachistry.
        horomachistry = soul.mettle,

        # Underneath
        #
        # RED THE DAWN AND BLACK THE NIGHT AND WHITE WHAT'S LEFT. ABOVE WE SEE, BENEATH WE KNOW.
        #
        # Bosk.
        the_bosk = soul.ereb,
    ),
)


# Disciplines of the Hammer
#
# To purify and to combine the selves and the essences. The Hammer shapes gates and shatters doors, within us and without.
disciplines_of_the_hammer = card_type("disciplines_of_the_hammer",
    attributes(edge=2, forge=1, skill=1, illumination=1, nyctodromy=1),
    commit_output = frozendict(
        # Steel and Glass
        #
        # A certain parable of the Bright Arts tells of a priest who raised an altar of steel and glass to an old god; but then found a new god within the altar.
        illumination = soul.mettle,

        # Amber, Orichalcum
        #
        # A certain parable of the Night Arts tells of a pilgrim who raised a gate of amber and orichalcum that they might pass to reach their destination; but then found their destination lay on this side of the gate.
        nyctodromy = soul.shapt,
    ),
)


# Disciplines of the Scar
#
# To master boundaries through their determination. The Scar marks wisdom and regrets; one is often born from the other.
disciplines_of_the_scar = card_type("disciplines_of_the_scar",
    attributes(edge=2, lantern=1, skill=1, hushery=1, illumination=1),
    commit_output = frozendict(
        # The Crime
        #
        # The Mansus is the fortress in dream raised by the gods-who-were-stone. Nowhere is the inevitable scar beneath it. Monstrous, the gods-from-Nowhere; but cruel, the gods-who-were-stone.
        hushery = soul.trist,

        # The Scar
        #
        # The Mansus is the fortress of dream where the true Hours rule, and Nowhere is the scar beneath it where the Nowhere Hours lair. Without the Hours above, that scar would be an open wound. So the Bright Arts teach us.
        illumination = soul.phost,
    ),
)


# Door & Wall
#
# 'The lock seeks its key, the wall seeks its door, and we who would pass learn at last that they are not our servants.' - Willem Harries
door_and_wall = card_type("door_and_wall",
    attributes(forge=1, knock=2, skill=1, horomachistry=1, nyctodromy=1),
    commit_output = frozendict(
        # What Should Not Be
        #
        # There is a prophecy, of a shining City that mortals might build. There is a paradox, that a City Unbuilt can always be greater than one that exists. The Bright Arts teach this resolution: that the Hours will always forbid the raising of that City, so that it will remain a great hope and a great travelling.
        horomachistry = soul.fet,

        # What May Not Be
        #
        # There is a prophecy, of a shining City that mortals might build. There is a paradox, that a City Unbuilt can always be greater than one that exists. The Night Arts teach this resolution: that the gate to that City must be fashioned from black sapphire, and raised in dreams.
        nyctodromy = soul.shapt,
    ),
)


# Drums & Dances
#
# The first musics were not made by mortals, but taken; from sand-coil and sea-thorn, from flint-heart and dragon-womb.
drums_and_dances = card_type("drums_and_dances",
    attributes(heart=2, nectar=1, skill=1, the_bosk=1, horomachistry=1),
    commit_output = frozendict(
        # The Heart
        #
        # The Thunderskin, the eternal drum that beats to preserve the skin of the world, is a god-from-flesh, which is to say he was once mortal. But the Horned-Axe, last of the gods-from-stone, required his death, and so the Grail gave him up, though he loved her. Love is always subject to the will of the Hours, as all horomachists know.
        horomachistry = soul.mettle,

        # The Root
        #
        # The Thunderskin, the eternal drum that beats to preserve the skin of the world, is a god-from-flesh, which is to say he was once mortal. He died to preserve the last god-from-stone; he died for love; he died for necessity. In matters of Bosk, these three are often intertwined.
        the_bosk = soul.health,
    ),
)


# Edicts Inviolable
#
# The precepts of occlusion and dissolution; their jealous enforcement is the nature of the Calyptra.
edicts_inviolable = card_type("edicts_inviolable",
    attributes(heart=2, moon=1, skill=1, horomachistry=1, preservation=1),
    commit_output = frozendict(
        # Fire
        #
        # The Mare-in-the-Tree is not the youngest Hour; but she is the youngest Hour of Calyptra, for she has been born many times in many places. The Red Flower on the Watchman's Tree is the fire fuelled by truth, and without it the Tree would fall, as all horomachists know.
        horomachistry = soul.mettle,

        # Night
        #
        # The Velvet is not the oldest Hour; but she is the oldest Hour of Calyptra. The Black Flower on the Watchman's Tree is the preservation of secrets, and without it the Tree would fall. This is a matter of Preservation.
        preservation = soul.chor,
    ),
)


# Edicts Liminal
#
# The precepts of limitation and division; established by the enigmatic conclave of Hours sometimes called the Chancel.
edicts_liminal = card_type("edicts_liminal",
    attributes(knock=1, moth=2, skill=1, nyctodromy=1, skolekosophy=1),
    commit_output = frozendict(
        # Sapphire
        #
        # There is a prophecy of a glorious City that mortals could raise, but the Hours of the Chancel have decreed that it will not exist. The decrees of the Chancel are not defied, but now and then they have been circumvented… and we might conceive that a City with walls of shining flint could be raised in dreams; in the Mansus. This would be Nyctodromy.
        nyctodromy = soul.fet,

        # Scolecite
        #
        # There is a prophecy of a glorious City that mortals could raise, but the Hours of the Chancel have decreed that it will not exist. The decrees of the Chancel are not defied, but now and then they have been circumvented… and we might conceive that City with walls of shining scolecite could be raised Nowhere; in the darkness below dreams. This would be Skolekosophy.
        skolekosophy = soul.ereb,
    ),
)


# Edicts Martial
#
# The precepts of struggle and conflict which drive the cosmic engine of change sometimes called the Corrivality.
edicts_martial = card_type("edicts_martial",
    attributes(edge=1, moon=2, skill=1, horomachistry=1, illumination=1),
    commit_output = frozendict(
        # Conflict Creates Gods
        #
        # All the Hours are defined by their opposition to other Hours... just as we are defined by the battles we choose. This is a matter of the Horomachistry Wisdom.
        horomachistry = soul.mettle,

        # Understanding Creates Conflict
        #
        # When we name our differences, we learn our enemies. Where there are no names, there are no enemies. This is a matter of the Illumination Wisdom.
        illumination = soul.phost,
    ),
)


# Ericapaean
#
# A language of surpassing beauty and allusiveness, revealed through the ecstatic apprehensions of the Orphics, the Eleusinians, and the Sibyls of the Rhine. Ericapaean, these mystics claimed, allows the elaboration of hues, sensations and states of mind too subtle for grosser tongues.
ericapaean = card_type("ericapaean",
    attributes(lantern=2, winter=1, skill=1, language=1, hushery=1, illumination=1),
    commit_output = frozendict(
        # The King in the Mirror
        #
        # There is a story told by students of silence: that a great and golden King held the only key to his deepest prison cell. One day he gave the key to his minister, and offered him a choice: to submit to execution, or to visit the cell and tell him what he found there. The minister made the wiser choice, and returned to show the King what he had found in the cell: a mirror.
        #
        # 'Then I release you,' the King declared. The minister left the palace that same day. His reflection, of course, said nothing at all.
        hushery = soul.trist,

        # TODO skill 'Ericapaean' tree description
        illumination = soul.phost,
    )
)


# Fucine
#
# A people lived east of the lost lake Fucino. Horace warned that theirs was the land of witches. This was their language, called by some 'the dry tongue' and by others 'the tongue of witches'.
fucine = card_type("fucine",
    attributes(heart=2, knock=1, skill=1, language=1, hushery=1, ithastry=1),
    commit_output = frozendict(
        # The Queen's Wound
        #
        # There is a story known to painters: of a Queen who could love no other, neither woman nor man, but only her own image. She sought nine colours to grace the image, and the last was the turquoise of her eyes, a gift from the Shadowless King. Her court poet hymned his Queen and her image, and in his poem she heard the truth: that the image was greater. So she fled into the Wood, and the image ruled her domain with the poet as its consort, but it always remembered her kindly.
        hushery = soul.trist,

        # The Queen's Weapon
        #
        # There is a story known to smiths: of a Queen whose realm was invaded by a great army. When she learnt that there were nine invaders for every defender, she ordered her army to surrender its swords. Night and day her smiths laboured to melt down the swords to bronze, while her generals threatened mutiny and the enemy advanced unhindered. They used the bronze to cast a Bell, but each time the Bell was rung, it cracked and had to be recast. At last on the night before the invaders reached the city, the Queen surrendered her crown to the casting. When at dawn the smiths rang the Bell, it cracked the moon like an egg and drove the sun from the sky. The invaders fled. But the Queen without a crown was no longer any queen at all.
        ithastry = soul.wist,
    ),
)


# Furs & Feathers
#
# Beasts, birds, husbandry, harvest.
furs_and_feathers = card_type("furs_and_feathers",
    attributes(scale=1, sky=2, skill=1, the_bosk=1, nyctodromy=1),
    commit_output = frozendict(
        # The Wings in the Wood
        #
        # When the first hunters were lost in the Wood, in the days before its darkening, they found a chrysalis of black and white. To it they sacrificed the birds of the air, so that it would show them the way home. So the Moth came to be, and so the Moth was the first to navigate the ways of the Wood. This is the foundation of Nyctodromy.
        nyctodromy = soul.fet,

        # The Well in the Wood
        #
        # When the first hunters were starving in the Wood, in the days before its darkening, they found a deep and crimson well. In it they drowned the beasts of the earth, so that the beasts would be reborn threefold, and the hunters could feast. So the Red Grail came to be, and so ever since she feeds us and she feeds upon us. This, the Matriarchs of the Knot have taught us.
        the_bosk = soul.health,
    ),
)


# Glassblowing & Vesselcrafting
#
# 'We are all vessels. Let us contain only what will grace us when the light shines through.' - Thirza Blake
glassblowing_and_vesselcrafting = card_type("glassblowing_and_vesselcrafting",
    attributes(knock=2, sky=1, skill=1, hushery=1, ithastry=1),
    commit_output = frozendict(
        # Glass, the Keeper
        #
        # The highest purpose of a glass vessel: to separate what is without from what is within. Perhaps, Hushery suggests, this was the first purpose of the first Hour, and only in that first moment could there be perfect understanding.
        hushery = soul.wist,

        # Glass, the Egg
        #
        # The highest purpose of a glass vessel: to show clearly perfectly what would otherwise be hidden within. Perhaps, Ithastry suggests, this was the first purpose of the first Hour, and only in that first moment could there be perfect clarity.
        ithastry = soul.phost,
    ),
)


# Glaziery & Lightsmithing
#
# 'Break a window. What have you made? A way? A new light? A weapon?' - Natalia Brulleau
glaziery_and_lightsmithing = card_type("glaziery_and_lightsmithing",
    attributes(lantern=2, sky=1, skill=1, chandlery=1, illumination=1, ithastry=1),
    commit_output = frozendict(
        # The White Flower's Paradox
        #
        # A paradox of Illumination: light reveals, light blinds. This is the lesson of the White Flower of the Watchman's Tree: even the most dangerous of knowledge is no danger at all when it is forgotten.
        illumination = soul.mettle,

        # The Red Flower's Lesson
        #
        # A lesson from Ithastry: fire reveals, smoke conceals. This is the lesson of the Red Flower of the Watchman's Tree: even the most dangerous of knowledge is no danger at all when it is given to the fire.
        ithastry = soul.phost,
    ),
)


# Herbs & Infusions
#
# Pluck it, powder it, mix it, warm it, drink it. But not that one.
herbs_and_infusions = card_type("herbs_and_infusions",
    attributes(heart=2, nectar=1, skill=1, the_bosk=1, preservation=1, effective_against_corruption=1),
    commit_output = frozendict(
        # The Source and the Root
        #
        # In the inmost walled garden of the palace of the Shadowless Kings in Persia, there was preserved a yew-tree older than any other. The Kings set a bee-hive in its branches, in memory of their forefathers, and they brewed from its flowers a sovereign cure against all poisons. This is the root of all our science, and this is Preservation.
        preservation = soul.health,

        # The Root and the Source
        #
        # In the inmost walled garden of the palace of the Shadowless Kings in Persia, there grew a yew-tree older than any other. Its root was red, its flowers were black, its berries were white. The Kings would leave their girl-children overnight in the nest of its roots, in memory of the great Mother of their line, and so their daughters were assured health, longevity and wisdom. This is the source of all our science, and this is Bosk.
        the_bosk = soul.ereb,
    ),
)


# Hill & Hollow
#
# The ways of the hill-children and the gods-from-stone. Old paths, old secrets, the songs that still echo beneath the earth.
hill_and_hollow = card_type("hill_and_hollow",
    attributes(moon=2, scale=1, skill=1, birdsong=1, preservation=1, effective_against_infestations=1),
    commit_output = frozendict(
        # How They Began
        #
        # In the beginning, the Carapace Cross served the first Hours, the gods born from stone. And the first of the Carapace Cross were the Thritige-kind, who sought the Monarch-at-the-Crossroads to rule them wisely and found him in themselves, who began as many and ended as one. This is a riddle, and the riddlemakers know its importance.
        birdsong = soul.chor,

        # How They Endured
        #
        # In the beginning, the Carapace Cross served the first Hours, the gods born from stone. When the gods-from-stone were defeated, where could the Cross go? Into the hills; into the Bounds; and into us. This is how humankind came to be, and in our most secret hollows, the Cross endures. This is a matter of Preservation.
        preservation = soul.health,
    ),
)


# Horns & Ivories
#
# The Hunter, the Way, and their memories.
horns_and_ivories = card_type("horns_and_ivories",
    attributes(knock=1, scale=2, skill=1, the_bosk=1, skolekosophy=1),
    commit_output = frozendict(
        # The Chandler's Path
        #
        # When the Chandler goes a-hunting in the dark of the Wood, he shields his candle so his prey is not forewarned, but he leaves a trail of ivory wax so we may follow him and purchase his prizes. After all, the goal of every hunt is to bring home a trophy, and when we understand Skolekosophy, we know how to bargain.
        skolekosophy = soul.shapt,

        # The Moth's Way
        #
        # When the Moth goes a-hunting in the dark of the Wood, he remembers a time when the Wood was bright, but he uses his horns to find the way, and we may follow him if we choose. After all, a trophy is nothing without a hunt: that's the lesson of the Wood.
        the_bosk = soul.ereb,
    ),
)


# Hyksos
#
# The Shepherd-Kings brought this speech west from Canaan to use in their wards and snares. Had they never come to Egypt, they might never found a way to write it; given its addictive qualities, that might have been for the best.
hyksos = card_type("hyksos",
    attributes(edge=1, grail=2, skill=1, language=1, nyctodromy=1, skolekosophy=1),
    commit_output = frozendict(
        # The Watchmen
        #
        # The veterans of the Légion du Seuil, who guard the boundaries of the waking world, tell stories of the labyrinths under the Mansus, above the Wood, and inside the Moon, where the first fallen Hours sleep, or hide, or rot: the gods-from-stone. Why the labyrinths? Because, the legionnaires say, there are Hours ruling now who would fight to consume the last scraps of their old enemies; and those who feast would eclipse those who abstain. The legionnaires have been known to boast that if they were only offered a great enough prize, they could guide the hungry Hours to their feast.
        nyctodromy = soul.shapt,

        # The Dartsmen
        #
        # The assassins of the Tragulari, who end the long lives of Long, tell stories of the wars between the Hours in the dawn of the world, when the sun was red and low - wars where the savage sound of savage bells unravelled the light of moon and sun - wars where dreams burned on pyres where Long were the fuel. All this ended, the Tragulari say, once the Worms came, and the Hours had a common enemy. And so the Tragulari fear Worms; hate Worms; and make offerings to Worms.
        skolekosophy = soul.ereb,
    ),
)


# Inks of Containment
#
# The inks in which the Histories are preserved.
inks_of_containment = card_type("inks_of_containment",
    attributes(moon=1, winter=2, skill=1, horomachistry=1, preservation=1, effective_against_theoplasmic_contamination=1),
    commit_output = frozendict(
        # When It Is Permitted
        #
        # Certain knowledge is forbidden to mortals… unless it's wisely contained. This law is named Calyptra; the enforcement of this law is named Calyptra also; the three Hours who enforce it share that name. They permit that knowledge to persist only in certain sanctioned places, and the most dangerous secrets must only be recorded in the inks called <i>encaustum terminale</i>. Horomachistry teaches us Calyptra's importance.
        horomachistry = soul.mettle,

        # When It Is Safe
        #
        # Certain knowledge is forbidden to mortals… except in nine great libraries protected by the covenant-stones they hold, where this knowledge can be safely recorded in the inks called <i>encaustum terminale</i>. These libraries are together called the Watchman's Tree, and the covenant marked by these stones shares that name. All this, then, is a matter of Preservation.
        preservation = soul.health,
    ),
)


# Inks of Power
#
# The inks in which the Histories are written.
inks_of_power = card_type("inks_of_power",
    attributes(rose=2, scale=1, skill=1, horomachistry=1, hushery=1),
    commit_output = frozendict(
        # The Weapon
        #
        # The greatest and most secret truths can only be recorded by the Librarians of the Watchman's Tree - even then, only beneath the shelter of the Tree's branches, and only in the sanctioned inks called <i>encaustum</i>. There are still certain languages in which these truths might be spoken aloud, but the Hours no longer permit that power in the mouths of mortals, as the wisdom of Horomachistry teaches us.
        horomachistry = soul.mettle,

        # The Wound
        #
        # The greatest and most secret truths can only be recorded by the Librarians of the Watchman's Tree - even then, only beneath the shelter of the Tree's branches, and only in the sanctioned inks called <i>encaustum terminale</i>. There are still certain languages in which these secrets can be spoken aloud, but that has never been safe. These secrets are the world's blood, and to speak them aloud is to shed that blood. We who are silent have always known this.
        hushery = soul.trist,
    ),
)


# Inks of Revelation
#
# The inks in which the Histories are revealed.
inks_of_revelation = card_type("inks_of_revelation",
    attributes(lantern=2, moth=1, skill=1, hushery=1, ithastry=1),
    commit_output = frozendict(
        # Truths that Were
        #
        # The inks called <i>encaustum terminale</i> are permitted only to the Librarians of the Watchman's Tree. Those inks can be used to reveal truths - even truths that are no longer so, not since the dawn times when the sun hung red and low and we felt its warmth like autumn. If that first and gentlest sun returned, the truths might return with it. Hushery remembers.
        hushery = soul.wist,

        # Truths that Will Be
        #
        # The inks called <i>encaustum terminale</i> are permitted only to the Librarians of the Watchman's Tree. Those inks can be used to reveal truths - even truths too great for daylight. Perhaps, then, daylight is not bright enough; perhaps we must find a way to kindle a light bright enough to reveal those greater truths. This would be a matter for Ithastry.
        ithastry = soul.phost,
    ),
)


# Insects & Nectars
#
# The Hive, the Nest, and the Chrysalis are the three secret principalities of the lesser world. Two of those three know the temptations of sweetness.
insects_and_nectars = card_type("insects_and_nectars",
    attributes(moon=1, nectar=2, skill=1, chandlery=1, the_bosk=1, nyctodromy=1),
    commit_output = frozendict(
        # The Moth's Spawn
        #
        # The bright-winged, dark-winged Glaeterfleoge-kind called themselves the Moth's spawn. They are gone now, like all the Carapace-kinds, but we can still use the arts of the Nest to follow the old roads of the night; the legacy of the Carapace Cross; Nyctodromy.
        nyctodromy = soul.fet,

        # The Grail's Favourlings
        #
        # The bright-winged, dark-winged Glaeterfleoge-kind called themselves the Grail's favourlings. They are gone now, like all the Carapace-kinds, but we can still use the arts of the Hive to glean the sweetness in the hidden places of the Wood; the legacy of the Carapace Cross; Bosk.
        the_bosk = soul.ereb,
    ),
)


# TODO (future) 'Henavek' skill name does not match attribute 'written_in_kernewek_henavek'
# Henavek
#
# Kernewek Henavek; the oldest form of the language now called Cornish; or something even older.
kernewek_henavek = card_type("kernewek_henavek",
    attributes(forge=1, scale=2, skill=1, language=1, the_bosk=1, ithastry=1),
    commit_output = frozendict(
        # The Stars
        #
        # A smiths' proverb in Brancrug: 'What starts in the sky, ends in the earth.' A story goes with it, that the village smith's anvil in the time of the Dewulfs was hatched from a meteor stone, and so every plough in the village knows something of the stars. Not many remember the story, but everyone remembers the proverb. It would probably count as Ithastry.
        ithastry = soul.wist,

        # The Roots
        #
        # A farmers' proverb in Brancrug: 'What starts in the roots, ends in the sky.'  A superstition goes with it, that before a child's first birthday you should leave her for a summer night sleeping in the roots of an apple-tree, to make sure she grows tall and straight-backed. Not many pay heed to the superstition now, but everyone remembers the proverb. It would probably count as Bosk.
        the_bosk = soul.health,
    )
)


# Killasimi
#
# If there is speech in Nowhere; if there is a language used by the Dead; if the House of the Moon has a native tongue; then it must be Killasimi. If none of this is true, it is still not a language to be spoken in daylight. Each word breathes woe. Read it, as they say, and weep.
killasimi = card_type("killasimi",
    attributes(moon=1, winter=2, skill=1, language=1, the_bosk=1, skolekosophy=1),
    commit_output = frozendict(
        # The Carpenter's Tale
        #
        # There is a prophecy among carpenters: a master of their kind will resolve, unwisely, that the coffins he shapes are too beautiful to sully with corpses. He will steal trinkets from the dead, he will ask the help of smiths and jewellers, and day and night he will labour to shape something worthy of his work. At last he will tire of his task and offer his breath to the shape in the casket. When it accepts, it will rise from the coffin and pronounce itself King. It will rule by fear, or fear will destroy it. In either case, its maker will have no coffin and no grave, and his name will be lost.
        skolekosophy = soul.ereb,

        # The Weaver's Tale
        #
        # There is a prophecy among weavers: of one who will unwisely seek to find the future in a tapestry of her own hair. Her house will grow dark, shrouded in the labyrinths of her tresses. Pilgrims will seek her in the cellar of her house, where she will plead with them to cut her free. They will always fail, and she will always devour them. At last one will come who will ask instead to stay with her. Others will join them, until the house becomes a palace and the palace a city, below the world, where all are welcome and in the tapestry all truths are revealed.
        the_bosk = soul.health,
    )
)


# Leaves & Thorns
#
# There is no scent without sorrow.
leaves_and_thorns = card_type("leaves_and_thorns",
    attributes(grail=1, nectar=2, skill=1, birdsong=1, the_bosk=1),
    commit_output = frozendict(
        # Looking Up
        #
        # The gardener's first lesson is this: look up. What starts as weather ends in the world, what starts as sky ends in the soil. This is what the birds know, and the birds know most things first.
        birdsong = soul.chor,

        # Looking Down
        #
        # The gardener's first lesson is this: know your thorns, know your poisons. There's no point thinking about tomorrow when we aren't expecting to live through today. This is the lesson our ancestors learnt the hard way in the Wood: this is Bosk.
        the_bosk = soul.health,
    ),
)


# Lockworks & Clockworks
#
# The little ways of little machines.
lockworks_and_clockworks = card_type("lockworks_and_clockworks",
    attributes(knock=2, sky=1, skill=1, ithastry=1, skolekosophy=1),
    commit_output = frozendict(
        # Of Clocks
        #
        # The clocksmith's first duty: when the time comes, the device should speak its purpose. Since the Sun was sundered, Noon is not as it was. Perhaps, if we found the true hour of Noon, we'd know how the Sun might return. Ithastry might give us that answer.
        ithastry = soul.wist,

        # Of Locks
        #
        # The locksmith's first duty: a key for every lock, and a lock for every key. If a key were an Hour, what lock would it open? Skolekosophy might hold the answer.
        skolekosophy = soul.shapt,
    ),
)


# Maggephene Mysteries
#
# 'The greater plagues may not be cured, only bound. The very greatest of all may only be entreated… and it is death to do so improperly.'
maggephene_mysteries = card_type("maggephene_mysteries",
    attributes(heart=1, moon=2, skill=1, hushery=1, preservation=1, effective_against_corruption=1),
    commit_output = frozendict(
        # Revenge
        #
        # The gods-who-are, which we call the Hours, warred against the gods-from-stone and cast them down. What remains of the gods-from-stone we call plague, scourge, catastrophe. If the Hours were cast down in their turn, would the gods-from-stone be satisfied? Would revenge bring peace? The Night Arts hint that it might be so.
        hushery = soul.trist,

        # Rebirth
        #
        # The gods-who-are, which we call the Hours, warred against the gods-from-stone and cast them down. What remains of the gods-from-stone we call plague, scourge, catastrophe. But if the gods-from-stone were reborn, would they still be plagues? Would renewal bring peace? The Arts Unregarded hint that it might be so. 
        preservation = soul.health,
    ),
)


# Meniscate Reflections
#
# 'Without is purified, within is erased.'
meniscate_reflections = card_type("meniscate_reflections",
    attributes(edge=1, forge=2, skill=1, illumination=1, preservation=1, effective_against_theoplasmic_contamination=1),
    commit_output = frozendict(
        # What Could Be
        #
        # Dream of a city of perfect balance. There can be no perfect balance outside dream. Meditate on the Hour named Meniscate, whose light is cast in dreams but we see even in the Wake. Build the City in the heart of her domain, in the House of the Moon. Be Illuminated.
        illumination = soul.phost,

        # What Might Be
        #
        # Dream of a city of perfect balance. There can be no perfect balance outside dream. Meditate on the Hour named Meniscate, whose light distinguishes the possible from the real. Let the City remain unbuilt; let the perfection of eternity be Preserved.
        preservation = soul.health,
    ),
)


# Orchids & Narcotics
#
# There is no greed without beauty.
orchids_and_narcotics = card_type("orchids_and_narcotics",
    attributes(grail=2, nectar=1, skill=1, the_bosk=1, skolekosophy=1),
    commit_output = frozendict(
        # The Chandler's Kindling
        #
        # If flowers are flame, the earth is their fuel. The Hour named Flowermaker cannot harm us, and he cannot find us, but he always has what we desire, and the Hour named Chandler can bring the spark to light the flame. These are the temptations of Skolekosophy.
        skolekosophy = soul.shapt,

        # The Grail's Births
        #
        # Learn from blood and drink from the earth. The Red Grail brought forth the Hours called Flowermaker and Beachcrow, who know where in the wood we can find delight. These are the temptations of Bosk.
        the_bosk = soul.ereb,
    ),
)


# Ouranoscopy
#
# 'Consider the Star. Hath each Star, its Seven Names. Observe that these Names are Never Shared.' - Thomas Dewulf
ouranoscopy = card_type("ouranoscopy",
    attributes(moon=1, sky=2, skill=1, horomachistry=1, hushery=1),
    commit_output = frozendict(
        # Peace
        #
        # If night is peace, then dawn is battle, when the Sun drives the stars from the sky. A day might come when the Sun's victory is not assured. The battles of heaven are a matter of Horomachistry.
        horomachistry = soul.fet,

        # Wisdom
        #
        # If the stars are wisdom, then dawn is ignorance. A day might come when there is no dawn. Ouranoscopy should be numbered among the Night Arts.
        hushery = soul.trist,
    ),
)


# Path & Pilgrim
#
# 'The traveller is always returning. One who does not is no traveller.' - Arun Peel
path_and_pilgrim = card_type("path_and_pilgrim",
    attributes(rose=2, scale=1, skill=1, birdsong=1, nyctodromy=1),
    commit_output = frozendict(
        # The Threshold
        #
        # Every traveller crosses a threshold twice. The Horned-Axe is the Hour who faces both ways at every threshold. Find the answer to her riddles in Birdsong.
        birdsong = soul.chor,

        # The Path
        #
        # Speech is the key to dream, and because we are speaking apes, every night is a journey. Nyctodromy is the wisdom of the paths of night.
        nyctodromy = soul.fet,
    ),
)


# Pearl & Tide
#
# The depths of the sea, the waves upon the shore, and the memories of their withdrawal.
pearl_and_tide = card_type("pearl_and_tide",
    attributes(moon=1, rose=2, skill=1, the_bosk=1, nyctodromy=1),
    commit_output = frozendict(
        # What Remains
        #
        # The Sea: whale-road, salt-realm, moon-way. Anything given to the waves may find another home - unless its home is the Sea. Nyctodromy shows us the way across the sea, and the way home.
        nyctodromy = soul.fet,

        # What Returns
        #
        # The Sea accepts every gift it is given, and sometimes, now and then, those gifts are returned. The Red Grail slew the Hour named Tide, and what remained was given to the Sea; so, perhaps, one day, that Hour might return. This is life, and so this is Bosk.
        the_bosk = soul.health,
    ),
)


# Pentiments & Precursors
#
# Feats and feits of forgotten things: the Carapace Cross, the line of Antaios, the world of a low red sun. 'Though much is taken, much abides.'
pentiments_and_precursors = card_type("pentiments_and_precursors",
    attributes(grail=1, scale=2, skill=1, birdsong=1, skolekosophy=1),
    commit_output = frozendict(
        # Coral
        #
        # Of the Ligeian Medusa, it has been said: 'She might be the oldest of her kind still living; and she is dead.' Symurgists might interpret this thus: she is the oldest of the shared Names of the Twins - the Hours we call Sister-and-Witch, Witch-and-Sister.
        birdsong = soul.chor,

        # Carapace
        #
        # Of the Ligeian Medusa, it has been said: 'She might be the oldest of her kind still living; and she is dead.' Skolekosophists might interpret this thus: she is the oldest of the Seglaz-kind, which is to say of a Carapace-lineage famed for the breadth of their wisdom and the complexity of their teeth.
        skolekosophy = soul.ereb,
    ),
)


# Preliminal Meter
#
# 'Nine modes, nine horizons': the subtle rhythms of words which open ways.
preliminal_meter = card_type("preliminal_meter",
    attributes(knock=2, rose=1, skill=1, illumination=1, ithastry=1),
    commit_output = frozendict(
        # Of Keys
        #
        # One of us passed the Summit. One may not.
        # Two of us sought the Lantern. Two chose flight.
        # The seventh rarely named, but not forgot.
        #
        #  This is Illumination.
        illumination = soul.phost,

        # Of Swords
        #
        # Birds of a scale, wings and talons bright
        # Worms of a feather, kissed again by stones
        # Kissed by fire, kissed by snow, by blight.
        #
        #  This is Ithastry.
        ithastry = soul.wist,
    ),
)


# Purifications & Exaltations
#
# 'No-one ever truly wants to be truly changed. Azoth and refulgin are justly feared. But no-one who has been changed would choose to go back.' - George Collers
purifications_and_exaltations = card_type("purifications_and_exaltations",
    attributes(lantern=1, sky=2, skill=1, illumination=1, ithastry=1, effective_against_corruption=1),
    commit_output = frozendict(
        # The Hours
        #
        # Never underestimate the Hour named Meniscate. Foolish adepts deride her as an Hour of vanity. What do they think defines the Hours? Light purifies; light exalts.
        illumination = soul.mettle,

        # The Tree
        #
        # Never underestimate the Hour named Madrugad. Foolish adepts deride her as an Hour of ashes. What do they think the Watchman's Tree sprang from? Fire purifies; light exalts.
        ithastry = soul.phost,
    ),
)


# Putrefactions & Calcinations
#
# 'Death alters; Snow endures.' - Solomon Husher
putrefactions_and_calcinations = card_type("putrefactions_and_calcinations",
    attributes(moon=1, winter=2, skill=1, ithastry=1, skolekosophy=1),
    commit_output = frozendict(
        # In Flames
        #
        # All days are death, all lives are sunset. No fire will last without fuel; there can be no Second Dawn without a war to burn the bones of earth. This is Ithastry at its most merciless.
        ithastry = soul.wist,

        # In Ashes
        #
        # All days are death, all lives are sunset. For a time, light persists, but we should not fear the scorch of a Second Dawn. This is Skolekosophy at its most merciful.
        skolekosophy = soul.ereb,
    ),
)


# Pyroglyphics
#
# 'One script that all the world must read, even the blind, and it is written in flames.' Matters of fireworks and their kin - lights, colours, infernal detonations.
pyroglyphics = card_type("pyroglyphics",
    attributes(forge=2, lantern=1, skill=1, chandlery=1, illumination=1, ithastry=1),
    commit_output = frozendict(
        # Birth in Fire
        #
        # Fire was the first understanding. The Hour named Moth learnt that even before the Watchman brought light. This is Illumination.
        illumination = soul.mettle,

        # A Red Blossom
        #
        # Stories written in fire end all the sooner... but are remembered all the longer. The Ithastry wisdom teaches us the certainty of change.
        ithastry = soul.wist,
    ),
)


# Quenchings & Quellings
#
# Arts which quench fires and bring solace to the troubled mind. 'A true adept is never troubled by fire, nor by fever, nor by restless spirit.' - Ambrose Westcott
quenchings_and_quellings = card_type("quenchings_and_quellings",
    attributes(heart=1, winter=2, skill=1, hushery=1, preservation=1, effective_against_theoplasmic_contamination=1),
    commit_output = frozendict(
        # Safety in Silence
        #
        # Unwise words are dangerous. Mourn them, remember them, speak them not. This is Hushery.
        hushery = soul.trist,

        # Safety in Oblivion
        #
        # Let the flesh forget disease, let the smoke forget the flame, let the troubled mind forget its pain: Preservation.
        preservation = soul.health,
    ),
)


# Ragged Crossroads
#
# 'To understand why four paths were not taken.'
ragged_crossroads = card_type("ragged_crossroads",
    attributes(edge=2, winter=1, skill=1, illumination=1, skolekosophy=1),
    commit_output = frozendict(
        # Tomorrow's Light
        #
        # Every regret is a lesson. We cannot change what is past, but neither should we wish to. Regret is Illumination.
        illumination = soul.phost,

        # At the Threshold
        #
        # Every regret is a threshold; and every threshold can be crossed in both directions. A skolekosophist knows that no threshold need remain inviolate.
        skolekosophy = soul.shapt,
    ),
)


# Ramsund
#
# This language has been called <i>'mantiq al-tair'</i> and <i>'lenga aucel'</i> and <i>'the speech of birds'</i> and <i>'Ramsund'</i> and <i>'the hazelnut tongue'</i>, but it's a language of secrets, and its true name may never be used. The aviform Hours use it at their Roost, or so the story goes.
ramsund = card_type("ramsund",
    attributes(moth=2, sky=1, skill=1, language=1, birdsong=1, preservation=1),
    commit_output = frozendict(
        # The Falconer's Tale
        #
        # There's a very old story told by falconers about the aviform Hours - the secret gods who take the shape of birds. Once there were only five - the dove, the crow, the laughingthrush, the twin kites. The sixth had fallen to the talons of an owl, and they sought another to join their company. But the crow rejected half of all those they found,  for the dowdiness of their plumage, and the dove rejected the others, for being too gaudy. At last they found a night-bird whose feathers were both the perfect white and the perfect black of the crow and of the dove. But once they had accepted him they learnt he was no bird at all - only a night-flitting moth. Fortunately for the moth, their pride kept them from admitting their mistake; but since that day, the aviform Hours will only meet at night, when the sixth of their kind won't be unmasked.
        birdsong = soul.trist,

        # The Thief's Tale
        #
        # There's a very old story told by thieves about a competition among the aviform Hours - the secret gods who take the shape of birds. The dove boasted of the bones he'd stolen from flesh, and the crow of the flesh he'd picked from bones. One of the kite-twins bragged that that she'd stolen the borders from kingdoms, and the other that she'd taken the roads from crossroads. The magpie told all the colours he'd taken that are no longer found in the world, and the laughingthrush topped that with the tales of the sights she'd stolen. But when the glitter-winged seventh of their number told them what he'd stolen, they all were shocked into silence. They fell upon him and stripped him of his wings and drove him from the sky. So he, and what he stole, are gone from the world, and now we cannot even name them, but still we feel their lack.
        preservation = soul.chor,
    ),
)


# Resurgences & Emergences
#
# Birth and death are only directions. Between the two we find a crossroads.
resurgences_and_emergences = card_type("resurgences_and_emergences",
    attributes(grail=1, moth=2, skill=1, the_bosk=1, preservation=1, effective_against_infestations=1),
    commit_output = frozendict(
        # Moth and Grail
        #
        # The gods-from-Stone made a law that the keys of dream cannot be held or owned. The time of Stone is past, but the keys remain. So the holders of these keys can only be the seven Ligeians, whose crime has set them outside the law. And the Ligeians serve an Hour of Moth and Grail: when the last remnants of the gods-from-Stone are renewed, the law will be renewed with them. Preservation is the wisdom of renewal.
        preservation = soul.chor,

        # Grail and Moth
        #
        # The gods-from-Stone made a law that the keys of dream cannot be held or owned. The time of Stone is past, but the keys remain. So the holders of these keys can only be the seven Ligeians, whose crime has set them outside the law. But the Ligeians serve an Hour of Grail and Moth: when the last remnants of the gods-from-Stone are consumed, the law will be consumed with them. Bosk is the wisdom of change.
        the_bosk = soul.health,
    ),
)


# Rhyme & Remembrance
#
# To speak with the dead; to torment the living; to celebrate both.
rhyme_and_remembrance = card_type("rhyme_and_remembrance",
    attributes(moon=1, winter=2, skill=1,  birdsong=1, skolekosophy=1),
    commit_output = frozendict(
        # What We Were?
        #
        # The shapes that loped beside you in the frost,
        # The scraps you gleaned of caul and periost
        # Once these were answers to 'What May Be Lost?'.
        #
        # All part of the matter we call Birdsong.
        birdsong = soul.trist,

        # Secrecy; Knowledge; Power
        #
        # The sights we name are rarely named by day
        # The shapes we seek are rarely sought in clay
        # The names we claim are often claimed as pay.'
        #
        # This is Skolekosophy.
        skolekosophy = soul.ereb,
    ),
)


# Rites of the Roots
#
# The oldest Hours are the gods-from-blood, who rose from sacrifice. That blood was always spilt on the roots, and the rites of its spilling are still remembered.
rites_of_the_roots = card_type("rites_of_the_roots",
    attributes(moth=1, nectar=2, skill=1, the_bosk=1, preservation=1),
    commit_output = frozendict(
        # What is Given
        #
        # The oldest <i>living</i> Hours are the gods-who-were-blood. The gods-from-Stone were older still, but they're buried in the earth, scattered in the sea, lost to the moon. This is why we're always careful where we make the sacrifice: without it, the gods-from-Stone would pass from memory. This is Preservation.
        preservation = soul.health,

        # What is Taken
        #
        # The oldest <i>living</i> Hours are the gods-who-were-blood. The gods-from-Stone were older still, but they're buried in the earth, scattered in the sea, lost to the moon. This is why we're always careful where we make the sacrifice, because if we spilt enough blood on their graves, they'd return for their revenge. Bosk knows.
        the_bosk = soul.ereb,
    ),
)


# Sabazine
#
# There is a History where Alexander defeated first the Great Knot of Sabazos, and then the King of Kings. There is another History where, instead, he learnt from them. How many more? If we curl our hands into the correct shapes, we may yet understand.
sabazine = card_type("sabazine",
    attributes(lantern=1, moth=2, skill=1, language=1, birdsong=1, horomachistry=1),
    commit_output = frozendict(
        # The Fisher's Tale
        #
        # There's a story told by fisherfolk, about a city of amber and orichalcum that lies behind the waves. Those who eat of its fruits can breathe water and drink light, but they can never drink anything else afterwards. Only in another History, they say; but if you tie your nets right, you might just catch one of its citizens in this History, and they might just tell you the way.
        birdsong = soul.trist,

        # The Sailor's Tale
        #
        # There's a story told by sailors, about a city of ivory and iron across the sea. Those who come there never die, but those who leave again have never lived. Only in another History, they say; but if you rig your sails right, you might just catch the wind that takes you there in this one.
        horomachistry = soul.fet,
    ),
)


# Sacra Limiae
#
# The rites of an order of immortals who have tried to remain apart. These rites touch on secrets of Hours of the Mansus - chiefly gods-who-were-flesh and gods-from-Light.
sacra_limiae = card_type("sacra_limiae",
    attributes(moth=2, sky=1, skill=1, horomachistry=1, hushery=1, effective_against_curses=1),
    commit_output = frozendict(
        # Of Limits
        #
        # The Hours are not all-powerful. There is a place beyond their reach, where mortals and immortals might build a shining City of iron and ivory. Horomachists understand the Hours' limits.
        horomachistry = soul.mettle,

        # Of Endings
        #
        # The Hours are not eternal. The Sun-in-Splendour was riven and cast down. If we mortals so desire, we might prevent his return. Understand Hushery, and you understand endings.
        hushery = soul.trist,
    ),
)


# Sacra Solis Invicti
#
# The rites of the Church of the Unconquered Sun, and certain secrets of the gods-from-Light.
sacra_solis_invicti = card_type("sacra_solis_invicti",
    attributes(lantern=2, sky=1, skill=1, horomachistry=1, illumination=1, effective_against_curses=1),
    commit_output = frozendict(
        # A Light Above
        #
        # The New King's light shines brightly. The Sanctioned Version of the Book of Suns tells us that he may herald the unification of the gods-who-were-Light, into a new Sun-in-Splendour.  We should seek answers in Horomachistry.
        horomachistry = soul.fet,

        # A Light Within
        #
        # The New King's light is uncertain. The Received Version of the Book of Suns tells that the Sun-in-Splendour will never return. If the King claims otherwise, he leads us astray. We should seek answers in Illumination.
        illumination = soul.phost,
    ),
)


# Sand Stories
#
# Of wandering tribes, watchful vagabonds, and winged devourers.
sand_stories = card_type("sand_stories",
    attributes(moon=1, rose=2, skill=1, birdsong=1, skolekosophy=1),
    commit_output = frozendict(
        # A City
        #
        # The seven tainted immortals we call Ligeians are relentless in their appetite, and outcast under the laws of heaven. But they have their uses to the Hours. The Ligeian Kleidouchos has known all the great keys, and even now she holds the Key of Days; so every year she meets the Vagabond in Vienna, to exchange the names of lesser keys for the stories of the Vagabond's travels. We call their gossip Birdsong.
        birdsong = soul.trist,

        # A Temple
        #
        # The seven tainted immortals we call Ligeians are relentless in their appetite, and outcast under the laws of heaven. But they have their uses to the Hours. The Ligeian Echidna learnt her shaping arts in the world's dawn, and even now the Lionsmith values her skill; so every year they meet in the desert, among the furnace shadows of the Seven-Coiled temple, to share their knowledge of how monsters were made. We call their stories Skolekosophy.
        skolekosophy = soul.shapt,
    ),
)


# Sea Stories
#
# The sea has always been the widest road.
sea_stories = card_type("sea_stories",
    attributes(grail=1, moon=2, skill=1, birdsong=1, nyctodromy=1),
    commit_output = frozendict(
        # The Sea-Born
        #
        # The Ligeian Morgen, holder of the key of black sapphire, called sea-born, tide-drawn. Did she come from Ys behind the wave? If we speak her name at the rising of the moon, can we summon that old song of flutes and bells? These are Birdsong-riddles.
        birdsong = soul.chor,

        # The Wolf-Wife
        #
        # The Ligeian Rowena, holder of the Mare's Key, called sea-opener, wolf-wife. Whom did she invite from Ys behind the wave? When the moon sets across the sea, will they follow its road again? This matter of roads and keys is Nyctodromy.
        nyctodromy = soul.shapt,
    ),
)


# Serpents & Venoms
#
# These are the Mother's neglected children, and we prefer that they pass not through any door.
serpents_and_venoms = card_type("serpents_and_venoms",
    attributes(moon=1, scale=2, skill=1, hushery=1, skolekosophy=1),
    commit_output = frozendict(
        # The Last Sun
        #
        # In the dawn times the sun was lower, so we gave it our blood. From our blood it knew us, and so it was kinder. Its serpents brought us its poisons to drink, and so we died. But we only died a little, and so we dreamed, and returned the next day to give it our blood again. Those times of peace persist in the lessons of Hushery.
        hushery = soul.trist,

        # The First Sun
        #
        # In the dawn times the sun was lower, so we gave it our blood. From our blood it knew us, and so it was kinder. But those days are long gone. If we were foolish enough to find the first Sun and give it our blood again, it would devour us. If we fed it the blood of our enemies, of course, it might devour them. This is the kind of thing you hear from skolekosophists.
        skolekosophy = soul.shapt,
    ),
)


# Sharps
#
# Knives, dangers, and things out of place.
sharps = card_type("sharps",
    attributes(edge=2, moon=1, skill=1, hushery=1, skolekosophy=1),
    commit_output = frozendict(
        # A Wound in Dreams
        #
        # Before speech, we could not dream, which is to say that before speech tore open the Peacock Gate to dreams, the Mansus was unwounded and at peace. It's not obligatory for Long to pass that gate, but they generally choose to. Perhaps that's why the Hours charge their Names to hunt down Long - even the Long who claim to serve them. Hushery recognises this truth.
        hushery = soul.wist,

        # A War in Dreams
        #
        # Before speech, we could not dream, which is to say that before we could wield words, we were weaponless, and even Long dared not enter the Mansus for fear of being devoured. It's not obligatory for Long to wield the weapons of speech, but they generally choose to. Perhaps that's why the Hours charge their Names to hunt down Long - even the Long who claim to serve them. Skolekosophy recognises this truth.
        skolekosophy = soul.shapt,
    ),
)


# Sickle & Eclipse
#
# Salt and silver; balance, necessity and rebuke.
sickle_and_eclipse = card_type("sickle_and_eclipse",
    attributes(edge=2, moon=1, skill=1, nyctodromy=1, preservation=1, effective_against_corruption=1),
    commit_output = frozendict(
        # Words to Walk By
        #
        # Unwise words unlocked unwise doors; we can use wise words to lock them. This is a matter of Nyctodromy.
        nyctodromy = soul.shapt,

        # Secret, Safe
        #
        # Let's keep night-things in the night so that day-things can walk in the day. That's Preservation.
        preservation = soul.chor,
    ),
)


# Sights & Sensations
#
# To mix the rarest colours, a merciless detachment is required.
sights_and_sensations = card_type("sights_and_sensations",
    attributes(sky=2, winter=1, skill=1, hushery=1, nyctodromy=1),
    commit_output = frozendict(
        # The End
        #
        # The artist knows: their every work could be improved. The artist understands: perfect work can never be completed. Perfection exists only as absence: Hushery understands this.
        hushery = soul.wist,

        # An End
        #
        # The artist knows: their every work could be improved. The artist understands: perfect work exists Nowhere. To go Nowhere - to go below the world - is not an easy journey. But there the artist could achieve their utmost. Nyctodromy is the way to perfection.
        nyctodromy = soul.fet,
    ),
)


# Sky Stories
#
# The nine winds gossip, and sometimes we can listen.
sky_stories = card_type("sky_stories",
    attributes(rose=1, sky=2, skill=1, birdsong=1, horomachistry=1),
    commit_output = frozendict(
        # The Roost
        #
        # A thief of sights, a scavenger of thrones,
        # A border-reaver and a thief of knots
        # A thief of colours and a thief of bones.
        #
        # This is Birdsong.
        birdsong = soul.trist,

        # The Tryst
        #
        # The Pilgrim's intrigue and the Grail's scheme
        # The Sun in shadow and the Forge unseen
        # The Swan King and the Elagabaline.
        #
        # This is Horomachistry.
        horomachistry = soul.fet,
    ),
)


# Snow Stories
#
# Of wind, woe, and winter.
snow_stories = card_type("snow_stories",
    attributes(moon=1, winter=2, skill=1, birdsong=1, hushery=1),
    commit_output = frozendict(
        # Much Remains
        #
        # Medusa's Riddle, first: What Is Not Seen?
        # The Night, the Heart, the Moon, the Day. Between.
        # The palest key. The birth-scarred Coil Queen.
        #
        # This is Birdsong.
        birdsong = soul.trist,

        # Much is Lost
        #
        # Still all the winds, still every beating tongue
        # Now still the mirrored moon, the sea's cauldron
        # When nothing's left then nothing is undone.
        #
        # Hushery.
        hushery = soul.wist,
    ),
)


# Solutions & Separations
#
# The surgeon plies the knife and the mason plies the chisel. There are subtler tools than either.
solutions_and_separations = card_type("solutions_and_separations",
    attributes(knock=1, moth=2, skill=1, ithastry=1, skolekosophy=1),
    commit_output = frozendict(
        # The Straight
        #
        # The world is all imbalance. With time, with care, with ingenuity, we can restore the balance, through the shaping of stone, the equilibrium of ichors, the unhatching of the egg. Ithastry teaches ingenuity.
        ithastry = soul.wist,

        # The Crooked
        #
        # The world is all imbalance, and imbalance is opportunity. Moth knows that; Worms prove it. This is Skolekosophy.
        skolekosophy = soul.shapt,
    ),
)


# Spices & Savours
#
# There is no sacrifice without sustenance.
spices_and_savours = card_type("spices_and_savours",
    attributes(forge=1, nectar=2, skill=1, the_bosk=1, ithastry=1, spicing=1),
    commit_output = frozendict(
        # Served Hot
        #
        # Copper, coal, fire, cinnamon, sunlight, obsidian. Add salt to taste. Serve. That's Ithastry.
        ithastry = soul.wist,

        # Served Cold
        #
        # Oak, earth, ice, ash, stars, blood. Drown to quenching. Serve. That's Bosk.
        the_bosk = soul.health,
    ),
)


# Stitching & Binding
#
# Nothing is entirely broken nor entirely whole - not so long as we have our needles.
stitching_and_binding = card_type("stitching_and_binding",
    attributes(heart=1, sky=2, skill=1, ithastry=1, preservation=1, effective_against_infestations=1),
    commit_output = frozendict(
        # To Hold
        #
        # A deft enough binding might contain anything: flesh; spirit; gods; light. That would be Ithastry.
        ithastry = soul.wist,

        # To Heal
        #
        # A deft enough binding might heal anything: flesh; spirit; song; stone. That would be Preservation.
        preservation = soul.chor,
    ),
)


# Stone Stories
#
# Of the earth, of its forms, of dwellers living and dead.
stone_stories = card_type("stone_stories",
    attributes(nectar=1, scale=2, skill=1, birdsong=1, preservation=1, effective_against_infestations=1),
    commit_output = frozendict(
        # A Vengeance
        #
        # The Hours once called Flint and the Wheel are gone, but the blood of their Name-emanations was mingled with the blood of mortals, and from it sprang the line of Antaios. Be careful: if enough Antaian blood is spilled, the Flint and the Wheel might wake. This is remembered in the songs of warning.
        birdsong = soul.trist,

        # A Vigilance
        #
        # The Hours once called Flint and the Wheel are gone, but the blood of their Name-emanations was mingled with the blood of mortals, and from it sprang the line of Antaios. As long as the Antaian line continues, the legacy of Flint and Wheel may endure. This then is Preservation.
        preservation = soul.chor,
    ),
)


# Strings & Songs
#
# The harmonies of the lower skies are here reproduced.
strings_and_songs = card_type("strings_and_songs",
    attributes(heart=1, sky=2, skill=1, birdsong=1, nyctodromy=1),
    commit_output = frozendict(
        # The Round
        #
        # There are no words in the song of birds; so birdsong had no beginning and will have no end.
        birdsong = soul.chor,

        # The Passage
        #
        # Words are the way through the sky, and a song without words is no song at all. Nyctodromy is the wisdom of ways.
        nyctodromy = soul.shapt,
    ),
)


# Surgeries & Exsanguinations
#
# Surgery entails the flow of blood, and the flow of blood entails purification, but the door also opens the other way.
surgeries_and_exsanguinations = card_type("surgeries_and_exsanguinations",
    attributes(heart=2, knock=1, skill=1, hushery=1, preservation=1, effective_against_infestations=1),
    commit_output = frozendict(
        # The White
        #
        # The Watchman's Tree has flowers three: Black, Red, and White. Red is the life that flows in the body's courses, and white is the writing at the body's core. Hushery teaches what ends.
        hushery = soul.wist,

        # The Golden
        #
        # In the times when nothing was forgotten, three flowers bloomed on the Watchman's Tree: Black, Red, and Gold. Red is the life that flows in the body's courses, but the blood of the Carapace Cross was golden. Preservation teaches what endures.
        preservation = soul.chor,
    ),
)


# The Great Signs and the Great Scars
#
# Some glyphs are too obscure to reside in any language, but too potent to remain unwritten.
the_great_signs_and_the_great_scars = card_type("the_great_signs_and_the_great_scars",
    attributes(grail=2, knock=1, skill=1, horomachistry=1, hushery=1),
    commit_output = frozendict(
        # The First Enemy
        #
        # Vak is a Great Scar; the first enemy of Calyptra. When the black flower blossoms on the Watchman's tree, she retreats, and Calyptra protects perilous knowledge behind secrecy's veil. The nature of their enmity is a Horomachistry matter.
        horomachistry = soul.fet,

        # The First Error
        #
        # Vak is a Great Scar; Calyptra's first mistake. If she could only be healed of her pain, Calyptra might reign inviolate, and the perilous knowledge it protects might be truly safe. The nature of her healing is a Hushery matter.
        hushery = soul.trist,
    ),
)


# Transformations & Liberations
#
# Forge and Moth are less different than we think. Every change is in some way a release.
transformations_and_liberations = card_type("transformations_and_liberations",
    attributes(forge=2, moth=1, skill=1, chandlery=1, illumination=1, ithastry=1),
    commit_output = frozendict(
        # From Light
        #
        # If even the Sun's division was a plan... then once we complete that plan, we'll bring the Second Dawn, and unite the sun. It won't be easy, but what great work ever is? Illumination might show the way.
        illumination = soul.mettle,

        # From Steel
        #
        # If the Sun has failed… then we must manufacture our own Second Dawn, with eye, with hand, with the light beneath the heart. It won't be easy, but what great work ever is? Ithastry might shape the way.
        ithastry = soul.phost,
    ),
)


# Tridesma Hiera
#
# The rites of the Sisterhood of the Triple Knot, which include certain mysteries of the dwellers in the Wood behind the World.
tridesma_hiera = card_type("tridesma_hiera",
    attributes(grail=1, moon=2, skill=1, the_bosk=1, preservation=1, effective_against_curses=1),
    commit_output = frozendict(
        # The Light, the Night, the Wood
        #
        # What lit the Wood in the days before its darkening? There was a light upon the earth long before Glory came to the sky. Preserve the night, and the light might return.
        preservation = soul.health,

        # The First among the Feasts
        #
        # The Moth consumed the Wheel; the Grail consumed the Tide; in the days of the Forge, the Stars fled from every facet of Flint. What feast was the first? Those who walk the Wood know that whichever was first, the Grail's was greatest.
        the_bosk = soul.ereb,
    ),
)


# Vak
#
# Before gods arose from blood, before ever ape stood upright, this was the language heard in the House of the Sun.... 'I am Vak,' the Peacock Door boasted, 'both the tongue and the Goddess. I am the only entrance into secret light. I was worshipped before you upright apes, and I will be still when all of you are ugly ash. Listen, and I will prove it.'
vak = card_type("vak",
    attributes(knock=2, rose=1, skill=1, language=1, birdsong=1, nyctodromy=1),
    commit_output = frozendict(
        # An Opportunity
        #
        # Something not commonly understood: were there no Calyptra to conceal perilous knowledge, there could be no Vak. A door opens both ways. This is understood by scholars of the Arts Unregarded.
        birdsong = soul.chor,

        # An Arrangement
        #
        # Something not commonly understood: without Vak, the exception, there could be no Calyptra, the law. Vak is in this sense, and perhaps in every sense, Calyptra's servant. This is known to scholars of the Night Arts.
        nyctodromy = soul.fet,
    ),
)


# Watchman's Paradoxes
#
# 'That amber preserves and is preserved by light; that to hatch is not to die; that the Sun.' There is a place behind the world called the Mansus. Deeds that would be impossible in the world are inevitable there. The Watchman, who knows all the ways of the Mansus, also knows how to make these deeds possible in the waking world.
watchmans_paradoxes = card_type("watchmans_paradoxes",
    attributes(lantern=2, sky=1, skill=1, illumination=1, nyctodromy=1),
    commit_output = frozendict(
        # From Light
        #
        # Our dreams are shadows cast by the Watchman's light. So we perceive him even in our shadow. This is Illumination.
        illumination = soul.phost,

        # From Change
        #
        # We recognise the dream-places that the Watchman shows us, though we have never seen them before. Perhaps we were something else when we saw them. This paradox is fundamental to Nyctodromy.
        nyctodromy = soul.fet,
    ),
)


# Weaving & Knotworking
#
# 'Hee hee hee hee hee hee hee hee hee. Hee.' - Valentine Dewulf
weaving_and_knotworking = card_type("weaving_and_knotworking",
    attributes(heart=2, moth=1, skill=1, birdsong=1, the_bosk=1),
    commit_output = frozendict(
        # What Remains
        #
        # Cut a thread, and the tapestry remains. Birdsong follows the thread.
        birdsong = soul.chor,

        # What Endures
        #
        # Cut a thread, and the tapestry must be healed. Bosk renews the weave.
        the_bosk = soul.health,
    ),
)


# Wolf Stories
#
# Sometimes we eat the wolf, and sometimes the wolf eats us.
wolf_stories = card_type("wolf_stories",
    attributes(moon=2, scale=1, skill=1, birdsong=1, skolekosophy=1),
    commit_output = frozendict(
        # The Wolf's Return
        #
        # The Sanctioned Version of the Book of Suns says that the Wolf-Divided was awoken by the Sun's division. We know from this that the Wolf was its own Hour even when the Sun was whole. So we glean and we guess that the Sun might be healed, and the Wolf return to its slumbers. So we glean and guess that a Second Dawn would bring peace, but the Wolf will fight to prevent it. This is Birdsong.
        birdsong = soul.trist,

        # The Wolf's Beginning
        #
        # The Received Version of the Book of Suns tells us that the Wolf-Divided was born from the Sun-in-Splendour's division. We know from this that the Sun can be reborn only if the Wolf joins the Sun's other selves. Only if the Wolf's hunger is assuaged will it join its other selves. And only the flesh of its other selves can assuage the hunger of the Wolf. A Second Dawn would herald the Last Day. This is the grim lesson of Skolekosophy.
        skolekosophy = soul.ereb,
    ),
)

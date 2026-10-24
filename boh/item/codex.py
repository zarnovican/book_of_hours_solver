from ..item import memory
from ..model import attributes, card_type


# A Catalogue of Uncharted Pleasures
#
# 'The Dark Gentleman' is the only, and rather grandiosely, identified author of this often-copied work.
# ---
# I'm Reading...
#
# Some pleasures,' the Formulae Voluptuous attest, 'are so intense they can corrupt the laws of the physical world'. This text catalogues some of those instances.
# ---
# I've Read...
#
# Birth occurs at the conjunction of pleasure and torment. So the first Forbidden Acts of the Forge birthed sparks of delight which took root in the Glory or in Nowhere: who can say? So the seeds of the Flowermaker were planted, though for long years he was nothing but an unfulfilled ache.
a_catalogue_of_uncharted_pleasures = card_type("a_catalogue_of_uncharted_pleasures",
    attributes(tally_price=5, mystery_grail=12, written_in_phrygian=1, readable=1, thing=1, dawn_period=1, subject_orchids_and_narcotics=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# A Child's Treasury of Golden Afternoons
#
# Once upon a time, a very bad man encoded very bad secrets into the charming illustrations of a book of charming stories. Wake the pictures, and you will see. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# Lord Jacob Gristwood: surgeon, ethnologist, philanthropist. There is no proof that he ever kept children in hutches beneath his bed. There is no proof he vivisected cats at dinner with his pen-knife. The Suppression Bureau keeps its secrets.
# ---
# I've Read...
#
# 'Here is your paint,' whispered the Wolf to the Pale Girl. 'Here is your knife-for-scraping. And here is your face.'
a_childs_treasury_of_golden_afternoons = card_type("a_childs_treasury_of_golden_afternoons",
    attributes(tally_price=8, mystery_edge=10, written_in_hyksos=1, readable=1, thing=1, subject_sharps=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.merciless_alteration,
)


# A Descent of the Shell
#
# A treatise on eggs, light, and optics by Abbess Melancthe, dazzlingly illuminated with renderings of the Abbess' visions.
# ---
# I'm Reading...
#
# The book is unexpectedly challenging to read. The bright glitter of the gold-leaf illuminations acquires a migrainous quality; the eye aches and tires…
# ---
# I've Read...
#
# This is, most likely, the 'certain vivid book' that Melancthe once sent to Gunnhild, daughter of King Harold, which provoked in her 'a dream of eyes' but also caused her to begin to lose her sight (until she was healed by the saint-bishop Wulfstan). To complete it is a kind of test. Its double thesis, at last, seems to be that the Sun is either an eye or an egg; and so the Second Dawn will be either its opening, or its hatching.
a_descent_of_the_shell = card_type("a_descent_of_the_shell",
    attributes(tally_price=4, mystery_forge=14, readable=1, thing=1, solar_gothic_period=1, subject_purifications_and_exaltations=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# A Journey to the Grove
#
# Black Elie, who much later became Damascene Matriarch of the Sisterhood of the Knot, recounts her journey to the Grove of Green Immortals.
# ---
# I'm Reading...
#
# In the Grove, Elie meets with an entity identified as 'Three Faces, Nine Colours' - who may have become her lover.
# ---
# I've Read...
#
# Three Faces is a Name of the Applebright, the Nowhere Hour of youth, healing and mutation. It offers Elie a form of eternal youth to take back West with her, which she rejects for certain reasons. She does promise, however, to renew their acquaintance 'in the season when the Applebright is the Witch' - not from sentiment, but rather grandly, to ensure the continuity of the Histories.
a_journey_to_the_grove = card_type("a_journey_to_the_grove",
    attributes(tally_price=4, mystery_grail=10, readable=1, thing=1, solar_gothic_period=1, subject_orchids_and_narcotics=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# A Light in the Inkwell
#
# Musgrave, fourth of the Dewulf line, writes tentatively about the 'Covenant of Brancrug' and the legacy of the sacred inks he calls 'encausta revelationia'.
# ---
# I'm Reading...
#
# 'Words are of the First Importance. So the Book of Suns teaches. But do not Words require Ink? And is the Inkwell not then the Womb of Words?'
# ---
# I've Read...
#
# Musgrave identifies 'the Ichor Auroral' as the mother of the encaustum Porphyrine. He adds that it would be blasphemous to describe the origins of the Ichor itself, although a scrawled marginal note suggests a later reader thought Musgrave was only hiding his ignorance beneath a cloak of piety.
a_light_in_the_inkwell = card_type("a_light_in_the_inkwell",
    attributes(tally_price=3, mystery_lantern=8, readable=1, thing=1, subject_inks_of_revelation=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.revelation,
)


# A Manual for Departure
#
# The author, who identifies itself as the Jekadu, claims to be one of the Great Hooded Princes of the Land of the River. The style is informal, even chatty.
# ---
# I'm Reading...
#
# 'No, these doors shouldn't be recorded, but if we had only recorded things before we'd had to leave the Fifth History, we would be in a much better state. So here I am writing it down, and if you don't like it you can sanction me.'
# ---
# I've Read...
#
# The 'Manual for Departure' lists a number of strategies - occult, martial and political - for quick escapes. Many are irrelevant, obsolete or enigmatic, but the Manual does include a number of powerful techniques for opening portals.
a_manual_for_departure = card_type("a_manual_for_departure",
    attributes(tally_price=5, mystery_knock=14, written_in_vak=1, readable=1, thing=1, subject_door_and_wall=1, dawn_period=1, codex=1),
    lessons=2,
    provides=memory.secret_threshold,
)


# A Novel Method for Invocation & Contrition
#
# Ingenious and rather beautiful techniques for entreating the Names of the Hours, developed by Rory Morrow, who styled himself 'the Sage-Knight'.
# ---
# I'm Reading...
#
# The techniques rely on the unique qualities of the Ericapaean tongue. Morrow professes himself surprised that they serve better to entreat the Names of the Vagabond than the Names of Lantern or Winter Hours…
# ---
# I've Read...
#
# Morrow demonstrates that Preliminal Meter techniques can be used with sufficient Rose to invoke the Vagabond's Names, transforming an Enduring Reflection into 'something wider of sky.'
a_novel_method_for_invocation_and_contrition = card_type("a_novel_method_for_invocation_and_contrition",
    attributes(tally_price=2, written_in_ericapaean=1, mystery_rose=14, readable=1, thing=1, curia_period=1, subject_preliminal_meter=1, codex=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# A Pale Lady and a Prince of Wines
#
# An anonymous biography of Eva Dewulf, last of the Dewulfs, focused rather salaciously on her personal troubles and intrigues.
# ---
# I'm Reading...
#
# Eva Dewulf is engaged to one Abraham Wheelock, but he leaves her at the altar. Furious and humiliated, she returns to Brancrug, and is not seen in London again. Three days after her departure, Abraham Wheelock's body is washed up near Gravesend. His face is so badly pecked by birds that he is only identified by his belongings. These include a waxed pouch containing a letter addressed to Wheelock, whose contents seem to show he is a spy in the pay of the Austrians. Subsequent investigations suggest that the letter is a forgery, but the matter remains obscure...
# ---
# I've Read...
#
# Lord Franklin Bancroft, sometimes called the Prince of Wines, begins a series of visits to Brancrug House. His relationship with Eva becomes a source of scandal. Eva is by now forty-nine, but rumours persist for years of a Dewulf-Bancroft heir. Eva's biographer claims that before her 'drowning death', her child by Bancroft was adopted by her friends the Southeys - that the child became the sister of the later Poet Laureate, Robert Southey. (No real evidence is provided in support of this claim.)
a_pale_lady_and_a_prince_of_wines = card_type("a_pale_lady_and_a_prince_of_wines",
    attributes(tally_price=2, mystery_moon=4, readable=1, thing=1, subject_sea_stories=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.salt,
)


# A Second Glory
#
# The priest Juceh celebrates the extirpation of the Gods-who-were-stone, those Hours who preceded humanity.
# ---
# I'm Reading...
#
# Juceh engages in an apologia for the destruction of the Hours: they were old, they were cowardly, they were vile, their time had passed, and it was the shining destiny of humankind to seize the House through glorious battle.
# ---
# I've Read...
#
# Juceh recounts how the Hour called Seven-Coils was slain in battle by the Colonel, how the Grail devoured the Hour called Tide, and how the Egg Unhatching 'fled like a coward'. He's quite vituperative about the Egg Unhatching. He warns darkly against its return.
a_second_glory = card_type("a_second_glory",
    attributes(tally_price=4, written_in_deep_mandaic=1, mystery_winter=12, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_snow_stories=1),
    lessons=2,
    provides=memory.hindsight,
)


# A Seventh Voice
#
# Samuel Savage's cycle of comic poems about a band of players who double as footpads seeking a seventh member.
# ---
# I'm Reading...
#
# Sir Snatch-Sea is distracted by Mistress Twitch-Shell kissing Mistress Nether-Pearls, and fails to see Master Magglepie making off with the players' funds…
# ---
# I've Read...
#
# The whole enterprise almost ends in disaster when Mistress Wander-Eye's family insults her costume, and she burns down their house in a fit of pique, but the day is finally saved by the Seventh Voice, a wandering book-monger who returns the band's lost music.
a_seventh_voice = card_type("a_seventh_voice",
    attributes(tally_price=3, mystery_sky=8, readable=1, thing=1, subject_preliminal_meter=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# A Shape in Smoke
#
# Ambrose Westcott's exposition on tobacco-blending and 'the Oracles of the Pipe.'
# ---
# I'm Reading...
#
# The text is spotted with spark-holes throughout…
# ---
# I've Read...
#
# Westcott observes gnomically that a pipe might be said to manifest the Red Flower of the Watchman's Tree: 'for when Lies are burnt, Wisdom arises, and <i>vice versa</i>.'
a_shape_in_smoke = card_type("a_shape_in_smoke",
    attributes(tally_price=3, mystery_forge=8, readable=1, thing=1, subject_pyroglyphics=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.revelation,
)


# A True and Complete Accounting of the Asclepian Mysteries of the Roots of the House
#
# Descriptions of the 'Asclepian Mysteries', reproduced by one 'Rylee Grese' from - supposedly - a much older text. It's unlikely to be genuine, but it makes a reference to 'The House without Walls and its Wood' right there in the prologue.
# ---
# I'm Reading...
#
# This is very obviously not an antique text. At the very least, it has been badly mutilated. But it contains substantial intriguing material: especially, a persuasive comparison of the House without Walls, without doors to the human body, with its many portals.
# ---
# I've Read...
#
# 'The direction of Death is down,' the book explains. 'The Peacock Door has been considered a rent, or an abrasion, but in some respects is more like a mouth - if not a more treasured point of entry.' Discussions of the Doors include a rite which may conjure creatures through those doors, although key incantations are missing.
a_true_and_complete_accounting_of_the_asclepian_mysteries_of_the_roots_of_the_house = card_type("a_true_and_complete_accounting_of_the_asclepian_mysteries_of_the_roots_of_the_house",
    attributes(tally_price=2, written_in_greek=1, mystery_heart=4, readable=1, thing=1, subject_weaving_and_knotworking=1, codex=1, curia_period=1),
    lessons=1,
    provides=memory.impulse,
)


# A True History of Valentine Dewulf
#
# Written in the third person by Valentine Dewulf. Rarely coherent, though it includes some useful footnotes on falconry and on exotic veterinary medicine.
# ---
# I'm Reading...
#
# Valentine is obsessed with the meaning of the Dewulf coat-of-arms: 'On a field or, a chevron enarched gules between two corby heads erased sable in chief and a wolf sejant sable in base.'
# ---
# I've Read...
#
# 'Long have the two birds pursued my blood, yet one is no Crow, yet it is darker. Long has the Wolf rolled itself in gold like a clovered cow, until its slobberings stain our thoughts…'
a_true_history_of_valentine_dewulf = card_type("a_true_history_of_valentine_dewulf",
    attributes(tally_price=3, mystery_sky=6, readable=1, thing=1, subject_furs_and_feathers=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.fear,
)


# Advice on Containment
#
# Thirza Blake discusses ways 'to keep Wood-things out of trouble, and Mansus-things in it.'
# ---
# I'm Reading...
#
# Thirza is irritatingly light on specifics, insisting above all that the duties of an adept are the duties of a host, and that a conjured spirit should be kept in as luxurious a vessel as possible.
# ---
# I've Read...
#
# Thirza notes the similarities between the Lantern-long habit of 'scrining' - returning to the physical world, despite their absence of a body, by entering a mirror or light - and Poemander's techniques of confining Mansus-long to mirrors. She wonders whether Poemander himself might be lured to visit Hush House if provided with a sufficiently alluring scrine.
advice_on_containment = card_type("advice_on_containment",
    attributes(tally_price=2, mystery_knock=4, readable=1, thing=1, curia_period=1, subject_glassblowing_and_vesselcrafting=1, codex=1),
    lessons=1,
    provides=memory.pattern,
)


# Against the Sisterhood of the Knot and the Foulness of their Depraved Customs
#
# Hieronymus Pseudo-Hypnerotomachus wrote this furious screed about the sinister influence of the Sisterhood of the Knot on his own Church of the Unconquered Sun.
# ---
# I'm Reading...
#
# Hieronymus claims that the powers served by the Sisterhood of the Knot made an arrangement: the Thunderskin loved the Yew, and the Grail destroyed him, as restitution for the destruction of the Axe's loved ones. Hieronymus' writing becomes incoherent with rage at this point.
# ---
# I've Read...
#
# Hieronymus recovers his composure, eventually, to describe how the Thunderskin entered the Mansus through the Peacock Door. This, Hieronymus insists, is 'abomination upon abomination: but then that most abominable of Doors has always been an abomination.'
against_the_sisterhood_of_the_knot_and_the_foulness_of_their_depraved_customs = card_type("against_the_sisterhood_of_the_knot_and_the_foulness_of_their_depraved_customs",
    attributes(tally_price=2, written_in_greek=1, mystery_sky=6, readable=1, thing=1, subject_sky_stories=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.intuition,
)


# Against Vitruvius
#
# A fourteenth-century treatise on esoteric mechanics and parahydraulics by Abbot Ranulph, best known now as a mason-architect.
# ---
# I'm Reading...
#
# Ranulph describes how he tested some of these techniques in the construction of the Winter Tower (now called the Long Tower). He admits to unexpected consequences…
# ---
# I've Read...
#
# Ranulph mentions that the tower of Ely Cathedral collapsed around the time the Winter Tower was completed… although he stops short of suggesting that one was the cause of another. 'A tower falls, a tower rises,' is all he'll commit to.
against_vitruvius = card_type("against_vitruvius",
    attributes(tally_price=4, mystery_sky=6, readable=1, thing=1, solar_gothic_period=1, subject_lockworks_and_clockworks=1, codex=1),
    lessons=1,
    provides=memory.pattern,
)


# Ambrosial!
#
# Ambrose Westcott's inventive - one might say pioneering, or indeed buccaneering - essays into kitchencraft.
# ---
# I'm Reading...
#
# Westcott proudly announces his intention to transform cuisine to become 'an Engine of Alchemy, a Fount of War.'
# ---
# I've Read...
#
# Westcott compares the ferocity of fire with the intensity of appetite as 'in essence, one essence'. A fire's ability to transform and destroy grows when it is offered the correct fuel; so too, he implies, can a sufficiently inspired appetite allow its possessor to consume 'greatly, strangely, unwisely.'
ambrosial = card_type("ambrosial",
    attributes(tally_price=2, mystery_forge=8, readable=1, thing=1, subject_spices_and_savours=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# An Almanac of Entrances
#
# A handbook of sealed and unsealed byways and shortcuts through the Bounds, compiled by Willem Harries in the 1860s - during his term as Librarian of Hush House.
# ---
# I'm Reading...
#
# Harries discusses the role played by the 'Légion du Seuil' and the 'Company of the Wolf-in-Gold' in warding the Bounds against outside influences. He warns that Bounds-travellers may themselves be considered 'outside influences…'
# ---
# I've Read...
#
# 'The Mansus, as Ys, lacks walls; Ys and the Mansus have both their gates, and there may be no gate without a wall. Thus the paradox resolves, as all those who walk in dream will learn. But the Wood has neither gate nor wall, and so it is the Wood whose roots may creep after us into the hours of our waking.'
an_almanac_of_entrances = card_type("an_almanac_of_entrances",
    attributes(tally_price=2, mystery_knock=10, readable=1, thing=1, curia_period=1, subject_edicts_liminal=1, codex=1),
    lessons=2,
    provides=memory.secret_threshold,
)


# An Echo of Silence
#
# A very heterodox history of the House of Lethe as recorded by 'the Serenity' - a Lethean adept who declares that the House of Lethe was created explicitly to prevent the ascension of any more mortals to Name or Hour status.
# ---
# I'm Reading...
#
# 'Eternity cannot be escaped; but in History, it may be delayed,' the Serenity explains. 'The gods-who-were-flesh, by their nature, are a surrender to Eternity.'
# ---
# I've Read...
#
# The 'roots of the House' are said to pass into the Wood of dreams through three forests in the Bounds, identified as the Bei Ilai, the Black Cedar Forest, and the Brecheliant. 'While one tree of these may yet stand, one single tree, the Histories continue.'
an_echo_of_silence = card_type("an_echo_of_silence",
    attributes(tally_price=4, mystery_moth=10, written_in_sabazine=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_sacra_limiae=1),
    lessons=2,
    provides=memory.impulse,
)


# An Exorcist's Field Manual
#
# A practical guide to 'troublesome Dead', grounded in theory but with a clear focus on their disposal, by the redoubtable Detective-Ostiary Wheelock of the Suppression Bureau.
# ---
# I'm Reading...
#
# 'The Dead usually avoid Light - as the most immediate manifestation of Eternity, which has no place for death. However those Dead 'uplifted by gold', that is to say touched by an actinic theoplasma, happily bod about in daylight and are perhaps strongest at noon...'
# ---
# I've Read...
#
# 'If you are dead but 'uplifted by green', that's the Ring-Yew's blessing. (The Crowned Growth offers a similar but nastier benefit.) This is how Burgeoning Risen come about, but there are different degrees of sentience and freedom depending on which growths are involved. The consciousness of one 'uplifted by green' is always greatly altered, though - they never really seem like the same person. They may have dregs of their original souls, but these are often replaced by something else. The upshot, invariably, is that they need to be set firmly on fire.'
an_exorcists_field_manual = card_type("an_exorcists_field_manual",
    attributes(tally_price=1, mystery_moon=6, readable=1, thing=1, subject_edicts_martial=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.contradiction,
)


# An Impertinent Vitulation
#
# A book of kitchen-garden techniques and aphrodisiac recipes recorded by Ernestine Peterhans, the 'Iron Seneschale' of Hush House for three generations of Dewulfs.
# ---
# I'm Reading...
#
# Peterhans asserts casually that the rousing liquor called 'Rubywise Ruin', which Leaves & Thorns techniques can brew from flowers, was a favourite of the notoriously severe Baron Thomas. If true, this would have raised eyebrows had it been known in his lifetime...
# ---
# I've Read...
#
# Peterhans mentions that one of these Leaves & Thorns techniques, with sufficient Nectar aspect, can supposedly cause 'a marvellous copper fruit' to burst from wood, although she has never managed it herself - but in a 'certain season' the pear-trees in the Practic Garden will deliver something similar.
an_impertinent_vitulation = card_type("an_impertinent_vitulation",
    attributes(tally_price=3, mystery_grail=6, readable=1, thing=1, subject_leaves_and_thorns=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.satisfaction,
)


# An Introduction to Histories
#
# The seventeenth-century mystic and antiquarian Claude Hersault describes divergent incidents in five major Histories.
# ---
# I'm Reading...
#
# The prologue warns at length of the iniquities of one Julian Coseley, a former colleague who Hersault now describes darkly as 'a Worm of Worms'. It seems Coseley advised Hersault early in the writing of the book, but Hersault later became suspicious.
# ---
# I've Read...
#
# Hersault identifies Blood, Silver, Design and the Worms as the central axes of each of the Histories, and claims that the so-called Second History is the true one. 
an_introduction_to_histories = card_type("an_introduction_to_histories",
    attributes(tally_price=3, mystery_winter=4, readable=1, thing=1, baronial_period=1, codex=1, subject_snow_stories=1),
    lessons=1,
    provides=memory.hindsight,
)


# Annals of St Brandan's
#
# Over a hundred years of the abbey's annals, from 1230 to 1350.
# ---
# I'm Reading...
#
# Three events of particular interest are recorded: an endowment by Eva de Braose, widow of the Marcher Lord Gwilym Ddu ('Black William), which enables an expansion of the Abbey; the construction of the Winter Tower, which is dedicated to the Madrugad; and the death 'by poisoning and Arts unsanctioned' of Abbess Nonna...
# ---
# I've Read...
#
# After Abbess Nonna's death, the 'double foundation' is dissolved and the monastery is reformed to accept only male novices. At this point the ink changes. The helpful scribe explains that for the new foundation, the Abbot has mandated stargall, not yewgall, ink. He outlines the differences (use of Inks of Containment techniques with a Sky, not Nectar, context) but doesn't trouble to explain why.
annals_of_st_brandans = card_type("annals_of_st_brandans",
    attributes(tally_price=4, written_in_latin=1, mystery_winter=4, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_inks_of_containment=1),
    lessons=1,
    provides=memory.regret,
)


# Apollo and Marsyas
#
# The libretto of a lost opera concerning the contest between Apollo and Marsyas, and its tragic outcome. The librettist is identified only by their initials.
# ---
# I'm Reading...
#
# In the original myth, Marsyas lost the musical contest and was flayed by Apollo, who later regretted it. In this version, Marsyas' skin has a further history...
# ---
# I've Read...
#
# The Skin of Marsyas gives oracles, and is later smuggled to Phrygia, where the priestesses of Cybele use it for a drum. At the climax, the striking of the drum drives would-be violators of the priestess to suicidal madness. The opera ends with a wistful hymn from the youngest priestess on the beauty of mountain pines.
apollo_and_marsyas = card_type("apollo_and_marsyas",
    attributes(tally_price=2, mystery_heart=4, readable=1, thing=1, curia_period=1, subject_surgeries_and_exsanguinations=1, codex=1),
    lessons=1,
    provides=memory.storm,
)


# As The Sun His Course
#
# Joel of the Bridge, a retired soldier and sometime tollkeeper, wrote this epic poem about Alexander's famously inexplicable decision at Issus to withdraw from the war with the Achaemenids, and his subsequent return to Macedonia.
# ---
# I'm Reading...
#
# Alexander meets at Issus with Darius, King of Kings, for three days and three nights. On the first day, the two men trade threats; on the second, promises; on the third, secrets. Darius tells Alexander something so shattering that he retires to his tent to consider 'matters of strength and matters of mastery'.
# ---
# I've Read...
#
# At dawn on the fourth day, Alexander announces: 'the Sun has his course, upon which he returns; and so do I'. He returns to Macedonia, executing two of his captains when they dispute his decision. He brings with him the 'names of a blind God', and a 'rite of sacred betrayal': for, Joel opines, without betrayal there would be an end to war.
as_the_sun_his_course = card_type("as_the_sun_his_course",
    attributes(tally_price=5, written_in_aramaic=1, mystery_edge=8, readable=1, thing=1, dawn_period=1, subject_sickle_and_eclipse=1, codex=1),
    lessons=2,
    provides=memory.contradiction,
)


# Ascite Supplications
#
# Prayers addressed to the Horned-Axe by the Sisterhood of the Triple Knot.
# ---
# I'm Reading...
#
# 'If we should pass not, let our enemies pass, unto their deserved end…'
# ---
# I've Read...
#
# One prayer describes how sufficient Moon-aspect can be used with Tridesma Hiera with almost any egg to hatch 'the Stone's children, the Sky's daughters, the Sea's sons.'
ascite_supplications = card_type("ascite_supplications",
    attributes(tally_price=4, written_in_greek=1, mystery_scale=8, readable=1, thing=1, solar_gothic_period=1, subject_stone_stories=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# Bancroft Diaries
#
# Lord Franklin Bancroft was initiated into the arts of the Flowermaker by the 'rose-witch' Fionna Ayrshire. He rose to become a Society provider of occult services and secret pleasures, before his abrupt disappearance in 1790.
# ---
# I'm Reading...
#
# Bancroft seems to have been a talented adept, but devoted his energies to frustratingly whimsical projects: arranging 'grape-fetching races' between Mansus-spirits, teaching Percussigants to juggle, and conjuring storms of imaginary blossoms for the rose-witch Ayrshire, who resolutely refused ever to couple with him. Bancroft spends twenty pages bemoaning this last.
# ---
# I've Read...
#
# The Mantra here recorded is a high and exacting magic which can be used to pledge one's spirit to the Watchman, beginning an ascent to the House. Bancroft boasts of his ability to recite it when in his cups. He also had it set to music for a performance with fireworks at Vauxhall Gardens.
bancroft_diaries = card_type("bancroft_diaries",
    attributes(tally_price=2, mystery_lantern=4, written_in_latin=1, readable=1, thing=1, subject_pyroglyphics=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.foresight,
)


# Black Nephrite
#
# One of Valentine Dewulf's dream-journals, in which he records his visions of 'a place that is no place, beneath the house that is no house.'
# ---
# I'm Reading...
#
# The dark, inchoate, feral space described by Valentine seems to be the 'Nowhere' of the Invisible Arts - the infra-oneiric lair of the alien Hours sometimes called gods-from-Nowhere.
# ---
# I've Read...
#
# Valentine's attitude to the Nowhere-Hours is unexpectedly relaxed. He speaks darkly of their appetites, but he insists they are too alien to penetrate the House of the Sun, let alone the waking world. He even seems to suggest that the Mansus-Hours have exaggerated the threat of the Nowhere-Hours for their own reasons. 'Not all Birds are trustworthy in their Feathers', he warns.
black_nephrite = card_type("black_nephrite",
    attributes(tally_price=3, mystery_moon=6, readable=1, thing=1, codex=1, subject_wolf_stories=1, baronial_period=1),
    lessons=1,
    provides=memory.fear,
)


# Book of Miah
#
# An account of the 'five visits of the Desert Wanderer' - probably the Hour called the Vagabond - to the city Miah. She begins as a delighted child - perhaps even a mortal - but things then go badly…
# ---
# I'm Reading...
#
# 'In her second visit, she came as Laughingthrush. Her heart was bright within, her beak was ripe with song, but in the first moment her feathers touched the city stones, the laughter began….'
# ---
# I've Read...
#
# The Wanderer's penultimate visit is as Centipede, whose 'venom cracks stone'. Miah is abandoned to the desert. But she returns one last time, again as Laughingthrush, with four other Hours who take the shape of birds, 'to celebrate the First Roost above the bones of her hated kin.'
book_of_miah = card_type("book_of_miah",
    attributes(tally_price=5, written_in_hyksos=1, mystery_rose=10, readable=1, thing=1, subject_sand_stories=1, dawn_period=1, codex=1),
    lessons=2,
    provides=memory.intuition,
)


# Book of True Blood
#
# Cassius the Thoman reveals the deeds of the Unnumbered Legion, the secret army that protected Rome against the Shadowless Empire.
# ---
# I'm Reading...
#
# The Legion's Legate answered directly to the Hour called the Tribune of Scars, and was promised immortality if he died in battle....
# ---
# I've Read...
#
# In the final part, Cassius confesses to being a former Legate. He recounts his terror of the Tribune, and divulges the secret lore of the Golden General, the champion of the Shadowless Empire, the enemy of the Tribune, in the hope that the Tribune will some day be undone.
book_of_true_blood = card_type("book_of_true_blood",
    attributes(tally_price=4, mystery_edge=14, written_in_latin=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_meniscate_reflections=1),
    lessons=2,
    provides=memory.fear,
)


# By Their Marks Shall Ye Know them
#
# A monster-hunting initiate of the Hour named the Colonel, who identifies herself as 'Little Sophia', provides advice on finding the weak spots of Long.
# ---
# I'm Reading...
#
# Little Sophia observes drily: 'Should one desire to slay an immortal, it is most practical to do so before they become immortal entirely.' She details the 'Marks', the changes that Long undergo as they abandon their mortal condition.
# ---
# I've Read...
#
# As the Lantern-long begins to abandon its flesh, its skin becomes loose, its bones soften. The Sixth Mark is to be observed thus: when the flesh between finger and thumb can be pulled to the final finger-joint…'
by_their_marks_shall_ye_know_them = card_type("by_their_marks_shall_ye_know_them",
    attributes(tally_price=2, mystery_knock=6, readable=1, thing=1, curia_period=1, subject_surgeries_and_exsanguinations=1, codex=1),
    lessons=1,
    provides=memory.pattern,
)


# Calicite Supplications
#
# Prayers addressed to the Red Grail by the Sisterhood of the Triple Knot.
# ---
# I'm Reading...
#
# 'If we should remember not, let our children remember, in their redmost dreams…'
# ---
# I've Read...
#
# One prayer describes how sufficient Grail-aspect can be used with Tridesma Hiera rites to give 'a life, a little life, a little little life' to a doll twisted from fabric…
calicite_supplications = card_type("calicite_supplications",
    attributes(tally_price=4, mystery_grail=8, written_in_greek=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_tridesma_hiera=1),
    lessons=2,
    provides=memory.satisfaction,
)


# Cardea's Delights
#
# The third volume of Abbot Geffrey's hypothetical theological dialogues in the Socratic mode.
# ---
# I'm Reading...
#
# 'If Janus were an Hour, Cardea might be counted among his Names, but the world has never turned in such a manner, and so she is not…'
# ---
# I've Read...
#
# Geffrey discusses the 'living Signs' - signs which change their shape, and whose flexibility is part of what makes it identifiable. He gives as one example 'the Paradox of the Hinge', and draws comparisons with the 'Names' called Twins (who would be considered Hours beyond the Church). He hints at the 'Amethyst Vessel' which can be sanctified by the Great Signs in the presence of Knock...
cardeas_delights = card_type("cardeas_delights",
    attributes(tally_price=4, mystery_knock=8, written_in_latin=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=2,
    provides=memory.pattern,
)


# Chione at Abydos
#
# A play dealing with the nine-year sojourn of a snow-goddess in the Thracian city of Abydos, by 'Apollo Fireweaver'. In English, published in 1892; purportedly from an older Greek text.
# ---
# I'm Reading...
#
# The entity called 'Chione' arrives in a blizzard and demands the city gates are barred. As Abydos falls under her spell, the dead return, but do not speak...
# ---
# I've Read...
#
# For eight years the city is a place of slow death, frosty ecstasy and silent beauty, but in the ninth year a Conspiracy of Shouts is mounted against the quiet that Chione demands. The conspirators open the city gates, and a scarred man comes to drag Chione out by the hair. Summer returns, but the conspirators die of remorse.
chione_at_abydos = card_type("chione_at_abydos",
    attributes(tally_price=3, mystery_winter=6, readable=1, thing=1, baronial_period=1, codex=1, subject_snow_stories=1),
    lessons=1,
    provides=memory.regret,
)


# Codex Acephali
#
# Sometimes called 'The Book of the Clean Skull'. The book contains accounts of enlightenments available through the gradual, surgical removal of the lobes of the brain.
# ---
# I'm Reading...
#
# It becomes clear that the processes described are mostly allegorical or metaphorical descriptions of Winter techniques for less revolting occult work. Even the metaphors are pretty horrible, though.
# ---
# I've Read...
#
# The author explains adaptations of these techniques, with sufficient Winter aspect, to harvest a mysterious substance described as the 'rags of the final bone' from the remains of almost any animal…
codex_acephali = card_type("codex_acephali",
    attributes(tally_price=2, written_in_latin=1, mystery_moon=10, readable=1, thing=1, curia_period=1, subject_snow_stories=1, codex=1),
    lessons=2,
    provides=memory.regret,
)


# Collected Hush House Lectures
#
# In the 1800s, Dr Arun Peel was invited to give a series of lectures to the Curia. They combine his pithy view of the Histories with his particular brand of unhelpfully ironical insight.
# ---
# I'm Reading...
#
# '1776, the Third History: Louis declares the Masque of Masques, and forbids mention of the Great Writhing within the walls of the Palace of Versailles, although by this point the Worms are observed to move openly along the boulevards of Paris, sometimes even in daylight. The Army is redeployed to defend the Court. The Masque lasts one lunar month, and attracts several of the Long abroad in Western Europe at the time - fleeing the Worms, or hoping to take advantage of the desperate Louis, or seeking access to the sealed mirrors of the Palace - or just eager to attend the most inventive and desperate debauch of the century…'
# ---
# I've Read...
#
# 'Many Know espouse Wormish sympathies. Let a hundred Histories flourish! Tear down the tyranny of eternity! To grow Long is, usually, to cast off these sympathies. There would be no immortality without Eternity, and Eternity, we often seem to decide, is only tyranny as long as <i>we</i> are not eternal.'
collected_hush_house_lectures = card_type("collected_hush_house_lectures",
    attributes(tally_price=2, mystery_moon=4, readable=1, thing=1, subject_sickle_and_eclipse=1, codex=1, curia_period=1),
    lessons=1,
    provides=memory.intuition,
)


# Commandments For the Preservation of All That Exists
#
# Black Elie, Damascene Matriarch of the Sisterhood of the Knot, was imprisoned by the emperor Didius Julianus. She reportedly instructed that these secret doctrines be recorded in writing to preserve against their loss. Regrettably, the story goes, Didius Julianus ordered that the work be entombed with her in an unmarked sepulcher.
# ---
# I'm Reading...
#
# Elie describes powerful protective incantations to be used in a variety of circumstances.
# ---
# I've Read...
#
# 'It is essential that these Protections be completed every fourth year, to defend against the entry of the Worms and against the avidity of the Wave and the Wound.' In the current History at least, there is no indication that these Protections have been performed regularly for at least the last thousand years.
commandments_for_the_preservation_of_all_that_exists = card_type("commandments_for_the_preservation_of_all_that_exists",
    attributes(tally_price=4, mystery_heart=14, written_in_deep_mandaic=1, readable=1, thing=1, solar_gothic_period=1, subject_stitching_and_binding=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# Cucurbit Prisoner Records 1927
#
# Accounts by Governor Collers' private secretary of interventions and experiments in the last years of the Cucurbit prison, focusing particularly on prisoners he believes might have Carapace Cross lineage.
# ---
# I'm Reading...
#
# Two prisoners suspected of oneiric crimes are encouraged to access their inner Carapace Cross tendencies, and develop the attributes of the Seglaz-kind ('sickle-formed pseudocrustacea'). Regrettably they lose the ability to breathe air; one dies and Collers releases the other into the sea.
# ---
# I've Read...
#
# Collers describes how he's successfully induced an unstable Carapace-larva to develop into a greater form, using Insects and Nectars techniques in the context of considerable Moon-aspect to 'awaken what would rather remain hidden'. He hopes that similar techniques might be used to expedite the moral development of prisoners...
cucurbit_prisoner_records_1927 = card_type("cucurbit_prisoner_records_1927",
    attributes(tally_price=1, mystery_nectar=12, readable=1, thing=1, subject_insects_and_nectars=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# Cucurbit Prisoner Records 1928
#
# Accounts by Governor Collers' private secretary of interventions and experiments in the last years of the Cucurbit prison, focusing particularly on the 'hill-children', wild Wood-things that have found a shape in the physical world.
# ---
# I'm Reading...
#
# Something called a 'Singlefoot', a horned mountain-dweller, is brought back from some kind of embassy to the Grove of Green Immortals. Collers expresses his irritation that Gervinus van Lauren refuses to assist in its containment.
# ---
# I've Read...
#
# The Singlefoot somehow conjures an earthquake that cracks the tower and enables its escape. Collers determines that it should not have been permitted to dream while kept beneath the earth: it had access to sufficient Scale aspect to use its 'arts of Hill and Hollow' to develop an Old Moment into an Earthquake Name. He mandates above-ground confinement for all hill-children prisoners in the future.
cucurbit_prisoner_records_1928 = card_type("cucurbit_prisoner_records_1928",
    attributes(tally_price=1, mystery_scale=12, readable=1, thing=1, subject_hill_and_hollow=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.salt,
)


# Damascene Traditions of the House of Lethe
#
# The House of Lethe was an order of immortals who sought obscurity, rejecting their past and future. If the author of this short text is to be believed, the initiates of the Damascene branch were much more radical than their fellows elsewhere.
# ---
# I'm Reading...
#
# The House generally forbade any potentially procreative activities, for fear of the terrible consequences of two Long bearing a child. The Damascene order took this much further…
# ---
# I've Read...
#
# At one point, male initiates were required to undergo castration, and female initiates to strangle any children they had previously borne. These measures were so horrific that the Order was shaken by repeated schisms, and eventually absorbed into the local Sisterhood of the Knot as a society of healers and exorcists.
damascene_traditions_of_the_house_of_lethe = card_type("damascene_traditions_of_the_house_of_lethe",
    attributes(tally_price=4, mystery_sky=8, readable=1, thing=1, solar_gothic_period=1, subject_sacra_limiae=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# De Bellis Murorum
#
# An eighteenth-century epic poem by the pseudonymous 'Solipsistos'.
# ---
# I'm Reading...
#
# The poem elliptically describes a war between beasts, weather phenomena, and arcane concepts. It's quite specific about their tactics.
# ---
# I've Read...
#
# 'The Two-One joined, and the Horned distinguished. Consequently, blood.'
de_bellis_murorum = card_type("de_bellis_murorum",
    attributes(tally_price=2, mystery_edge=6, written_in_latin=1, readable=1, thing=1, curia_period=1, subject_disciplines_of_the_scar=1, codex=1),
    lessons=1,
    provides=memory.contradiction,
)


# De Horis book 1
#
# An occasionally coherent catalogue of the secret gods, organised by hour. This is a reprint, but in the original Latin.
# ---
# I'm Reading...
#
# This volume deals mostly with the Hours of the Wood: the Moth, the Black-Flax, the Ring-Yew, among others.
# ---
# I've Read...
#
# 'The Glory is a question, and the Moth always answers 'Yes'.'
de_horis_book_1 = card_type("de_horis_book_1",
    attributes(tally_price=3, written_in_latin=1, mystery_nectar=4, readable=1, thing=1, codex=1, subject_rites_of_the_roots=1, baronial_period=1),
    lessons=1,
    provides=memory.impulse,
)


# De Horis book 2
#
# In Latin. A nineteenth-century reprint (by the indefatigable Nathaniel Darcy-Evers) of a fourteenth-century Latin translation of a fourth-century work.
# ---
# I'm Reading...
#
# This volume deals mostly with the Hour called Lionsmith, the Hour called the Tribune of Scars, and with their enmity.
# ---
# I've Read...
#
# 'The Lionsmith makes monsters to defeat the Tribune; but the scars of the Tribune are each a weapon.'
de_horis_book_2 = card_type("de_horis_book_2",
    attributes(tally_price=3, mystery_edge=4, written_in_latin=1, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.foresight,
)


# De Horis book 3
#
# In Latin. A nineteenth-century reprint (by the indefatigable Nathaniel Darcy-Evers) of a fourteenth-century Latin translation of a fourth-century work.
# ---
# I'm Reading...
#
# This is usually described as the third volume of 'De Horis', but Darcy-Evers' foreword argues persuasively that it's a substantial reworking by the original author…
# ---
# I've Read...
#
# The Lionsmith makes monsters, the Colonel has his scars, but the <i>De Horis</i> now insists that neither can truly defeat the other; that they must at some level understand these limits in their strategies; and that their enmity is an 'eternal engine of the world.'
de_horis_book_3 = card_type("de_horis_book_3",
    attributes(tally_price=3, mystery_edge=4, written_in_latin=1, readable=1, thing=1, codex=1, subject_disciplines_of_the_scar=1, baronial_period=1),
    lessons=1,
    provides=memory.contradiction,
)


# De motu corporum vetitorum
#
# The author rejoices in the name of 'Abelard Hubris', and the title might be translated as 'On the Forbidden Motions of Bodies' - evidently a reference to Newton's 'De Motu Corporem', published some twenty years previously.
# ---
# I'm Reading...
#
# Hubris's thesis: that stars, planets and other bodies are the proxies or even essences of the Hours, and that conjunctions and occlusions reveal the outcome of Hour-intrigues in the Mansus.
# ---
# I've Read...
#
# Hubris declares that the Great Comet of 1577 was the physical embodiment of the Hour named Madrugad; that It disintegrated but its fragments gravitate to bone-marrow, where they can be located even now. He insists that Ouranoscopic techniques can be used with Essential Periost and sufficient Sky to create a 'talisman gerifugic'.
de_motu_corporum_vetitorum = card_type("de_motu_corporum_vetitorum",
    attributes(tally_price=2, mystery_sky=10, readable=1, thing=1, curia_period=1, subject_ouranoscopy=1, codex=1),
    lessons=2,
    provides=memory.storm,
)


# De Ratio Quercuum
#
# In English the title translates roughly as 'the Account of the Oaks'; but this is Nathaniel Darcy-Evers' fascinating, if haphazard, survey of the occult properties of every tree he can find, not just oaks.
# ---
# I'm Reading...
#
# 'In Persia <i>taxus baccata</i>, the yew, is called <i>sorkhdar</i>, which is 'the red tree'. There they had long understood the Grail-Root. In later times, the Great King of Pontus had bee-hives set in the branches of the oldest of the female trees….'
# ---
# I've Read...
#
# 'The berries of the Pontine Yew open the door to death but the honey of their flowers opens a different door entirely. This was not the Great King's <i>mithridate</i> but one who has suckled at the Great Yew fears poison no longer. Perhaps they should…' Nathaniel is here distracted, however, by the toxic properties of certain inks. He does mention more usefully that the minor Ink of Power, Yewgall, can be brewed through the Rites of the Roots with the assistance of the aspect Nectar.
de_ratio_quercuum = card_type("de_ratio_quercuum",
    attributes(tally_price=2, written_in_latin=1, mystery_nectar=8, readable=1, thing=1, curia_period=1, subject_rites_of_the_roots=1, codex=1),
    lessons=2,
    provides=memory.earth_sign,
)


# Deaths and their Evasions
#
# Father Stanislav John Schaller writes of the means and limitation of passage between the orders of the Mansus - Know, Long, Names, Hours. Unusually, Father John has written this book in Fucine - for, he says, especial secrecy.
# ---
# I'm Reading...
#
# He speaks <i>very</i> cautiously of the exceptions that can sometimes be made to the edicts of Chancel and Calyptra, and hints at the means by which he successfully returned a Lantern-long to flesh...
# ---
# I've Read...
#
# Schaller mentions most cautiously of all that he has been permitted to see a book that speaks more deeply on the matter, but that it was surrendered 'into the shadow of a covenant-stone of the Watchman's Tree.' It can be retrieved if 'the ninety-ninth wink is reserved under the Edicts Liminal.'
deaths_and_their_evasions = card_type("deaths_and_their_evasions",
    attributes(tally_price=3, written_in_fucine=1, mystery_knock=14, readable=1, thing=1, subject_edicts_liminal=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.a_stolen_secret,
)


# Each Flame His Fuel
#
# A work by Omar, the Blaze, an initiate or craftsmaster at the Labyrinth of Lions.
# ---
# I'm Reading...
#
# Omar describes his work in the construction of mirrors for the enclosure of a sacred flame, and his slow realisation of 'a Flaw in the Glass'.
# ---
# I've Read...
#
# Omar explains how his lightsmithing techniques can be used, in the presence of sufficient Lantern, to enrich Xanthotic Essence into 'the Great Ink of the First History'. But he pleads caution in its use… 'lest the Chandler be Realised.'
each_flame_his_fuel = card_type("each_flame_his_fuel",
    attributes(tally_price=5, written_in_deep_mandaic=1, mystery_sky=14, readable=1, thing=1, dawn_period=1, subject_glaziery_and_lightsmithing=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# Echidnalia
#
# Part genealogy, part taxonomy, part family gossip - a closely detailed, highly specialised account of one branch of the complex brood of children associated with the Ligeian Echidna.
# ---
# I'm Reading...
#
# The gods-who-were-Stone knew the uses of the Biting Key, and now Echidna claims it. She has birthed so many children, and some yet survive.
# ---
# I've Read...
#
# Echidna's children are of two kinds: 'born' and 'won'. She seems to have had some success in winning over the creations of other powers to her service. In particular she has a habit of giving sustenance to the labhites, who consume what is found in the sky, and seducing them away from the Lionsmith...
echidnalia = card_type("echidnalia",
    attributes(tally_price=2, written_in_cracktrack=1, mystery_scale=21, readable=1, thing=1, multitudinuous=1, curia_period=1, subject_stone_stories=1, codex=1),
    lessons=3,
    provides=memory.impulse,
)


# Enchiridion Tragularis
#
# The poison-manual of the order of assassins called the Tragulari.
# ---
# I'm Reading...
#
# The Tragulari - 'dartsmen' - were employed by the Duties in their various incarnations to hunt down inhuman troublemakers. They developed poisons that even the immortals called Long could not withstand…
# ---
# I've Read...
#
# Immunity to their own poisons was a constant concern for the Tragulari, and they constantly dosed themselves with substances that might built up immunity. Perinculate, the notoriously toxic Unsanctioned Ink, can be used as a base for one of these - Serpent-Milk - with sufficient Scale and with arts of Serpents and Venoms.
enchiridion_tragularis = card_type("enchiridion_tragularis",
    attributes(tally_price=5, written_in_latin=1, mystery_moon=14, readable=1, thing=1, dawn_period=1, codex=1, subject_serpents_and_venoms=1),
    lessons=2,
    provides=memory.intuition,
)


# Ettery After
#
# An anonymous erotic novel occasionally claimed to have been written by Eva Dewulf, although at least two duels were fought in her honour to avenge this slander.
# ---
# I'm Reading...
#
# The novel graphically details Madame Ettery's various imprisonments, ravishments and escapes in the debauched Commonwealth of Tinctures and its neighbour, the pious Atrament.
# ---
# I've Read...
#
# It becomes apparent that many of Ettery's lovers and pursuers - Catwink, Houndsgall, Nilique - are transparent allegories for inks, and that Ettery is an embodiment of knowledge pinned to paper - to her mingled delight and dismay. The author only half-commits to the metaphor, though, and is clearly at least as interested in titillation as revelation.
ettery_after = card_type("ettery_after",
    attributes(tally_price=3, mystery_winter=8, readable=1, thing=1, baronial_period=1, codex=1, subject_inks_of_containment=1),
    lessons=2,
    provides=memory.hindsight,
)


# Eva's Treasury
#
# Eva Dewulf, last of the Brancrugs, discusses the occult and aesthetic properties of jewels and other precious minerals.
# ---
# I'm Reading...
#
# Black nephrite and scolecite, for Nowhere; orichalc and amber, for Ys; amethyst for the Night Key of the Spider Door...
# ---
# I've Read...
#
# Eva points out - bitterly? - that there is no shortage of uplifting parables and proverbs about the saving graces of a flaw in a jewel; but that no-one, 'not jeweller, not priest, not Hour' has ever found a way to repair such a flaw.
evas_treasury = card_type("evas_treasury",
    attributes(tally_price=3, mystery_sky=6, readable=1, thing=1, subject_anbary_and_lapidary=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.foresight,
)


# Exercises in the Continuity of Self
#
# Techniques proposed by the Haustorium - the most inaccessible and upsetting of the libraries of the Watchman's Tree - for 'the persistence of memory after the body is discarded'.
# ---
# I'm Reading...
#
# The soul-element wist is regarded as 'the fundamental value of the individual'. All other soul-elements, it is implied, may potentially be discarded, as can the individual itself.
# ---
# I've Read...
#
# The Haustorium expresses grudging respect for the Hour called Elegiast, 'who calls each of the Dead by name', but also concern over the Elegiast's subtlety when it chooses to inspire particular interpretations of Histories. The Haustorium proposes the use of Nowhere-energies in distracting or discouraging the Elegiast, in order to assure that 'the persistence of History remains unalloyed'.
exercises_in_the_continuity_of_self = card_type("exercises_in_the_continuity_of_self",
    attributes(tally_price=2, mystery_winter=8, readable=1, thing=1, curia_period=1, codex=1, subject_rhyme_and_remembrance=1),
    lessons=2,
    provides=memory.hindsight,
)


# Exorcism for Girls
#
# Simple but forceful techniques for 'rousting unbefitting spirits', written in straightforward and colourful language.
# ---
# I'm Reading...
#
# Blake seems uncertain at points whether the techniques are intended for use <i>by</i> or <i>on</i> girls. She clearly regards children as a nuisance.
# ---
# I've Read...
#
# Thirza's advice on the shapeless Wood-things known as Raw Prophets is typically practical: (1) discourage them with buckets of water as close as possible to freezing, and with the smoke of dried lemongrass (2) under no circumstances kiss them or receive kisses from them. (3) an effective formula is provided for laundering clothes stained with Prophet-slime.
exorcism_for_girls = card_type("exorcism_for_girls",
    attributes(tally_price=2, mystery_edge=6, readable=1, thing=1, subject_sickle_and_eclipse=1, codex=1, curia_period=1),
    lessons=1,
    provides=memory.fear,
)


# Fekri's Herbary
#
# The early wisdom of Ehsan Fekri, at that point a travelling healer, much later the Secretary Salvant of the Curia of the Isle.
# ---
# I'm Reading...
#
# As a skaptodon, Ehsan may consume only that which is found in the earth, so he's best with root-lore...
# ---
# I've Read...
#
# Ehsan identifies a pale sea-weed found on the beaches of Cornwall as a useful source of Rose and Winter aspect. His tone here is a little guilty - perhaps because he's showing an interest in sea-produce, which might be thought unwise for a skaptodon, and perhaps because his proposal to name it 'Eva's Locks' suggests a tiny crush on the Pale Lady of Brancrug...
fekris_herbary = card_type("fekris_herbary",
    attributes(tally_price=3, written_in_aramaic=1, mystery_nectar=6, readable=1, thing=1, codex=1, subject_herbs_and_infusions=1, baronial_period=1),
    lessons=1,
    provides=memory.satisfaction,
)


# Five Creations
#
# The itinerant scholar Shohei debated five possible origins for humanity with a hooded figure since claimed to be the Beach-Crow. Shohei later claimed that all these accounts had proven false, but the debate was, nevertheless, recorded.
# ---
# I'm Reading...
#
# THE CARAPACE ORIGIN: we were born from shell, like the children of the wasp from the spider. THE GLORIOUS ORIGIN: our life-motes descended from Light. THE ORIGIN BEFOULED: we were found naked and smeared with muck in the roots of the Wood...'
# ---
# I've Read...
#
# Shohei's preferred theories are that we are the children of apes who walked upright, although his tone here is satirical; or that we consumed not only our parents, 'which is not the Crime of the Sky', but also our origin, so that we came from Nowhere.
five_creations = card_type("five_creations",
    attributes(tally_price=5, mystery_moth=14, written_in_vak=1, readable=1, thing=1, codex=1, subject_resurgences_and_emergences=1, dawn_period=1),
    lessons=2,
    provides=memory.gossip,
)


# From History to Eternity
#
# A contraband manual of the Inks of Revelation. The author explains in a brief foreword that she is a high-ranking officer of 'an agency of the Duties' and that, though she supports its mission, she has concerns about the long-term consequences of its work.
# ---
# I'm Reading...
#
# 'All Histories braided into a golden loop; a shining ascent to Eternity. I had never imagined I could be afraid that there might be too few Truths. I could be wrong. But I'd like to leave at least one door ajar.'
# ---
# I've Read...
#
# 'Ichor Auroral' can be brewed into an <i>encaustum terminale</i> associated with the Second History, using Inks of Revelation techniques with Rose aspect. The author warns that this is exceptionally difficult, since these techniques aren't aligned with Rose. 'But that's why I'm hoping the door will stay ajar, even once all the others are closed. I wish you luck.'
from_history_to_eternity = card_type("from_history_to_eternity",
    attributes(tally_price=1, mystery_moth=10, readable=1, thing=1, subject_inks_of_revelation=1, codex=1, nocturnal_period=1),
    lessons=2,
    provides=memory.intuition,
)


# Glimmerings
#
# An anonymous prison diary written by a dreamer convicted of 'oneiric irresponsibility' and confined to the Cucurbit.
# ---
# I'm Reading...
#
# The prisoner is plainly terrified and bewildered by their situation, and has been unable to wrangle a coherent explanation out of anyone. But the dreams keep coming, and they keep writing them down…
# ---
# I've Read...
#
# Snow; broken mirrors; half-heard sky music; flowers of white, red and black; a blood-streaked winter dawn... the most notorious signifiers of oneiric risk, fantastically vivid and detailed. No wonder they were locked up. Their final recorded dream is of a 'worm-jewel' beneath Brancrug Isle, which they open with a key carved from their finger-bone.
glimmerings = card_type("glimmerings",
    attributes(tally_price=1, mystery_forge=10, readable=1, thing=1, subject_sights_and_sensations=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.bittersweet_certainty,
)


# Gospel of Nicodemus
#
# An apocryphal account of the works and experiences of the Shepherd Illuminate by one of his supposed companions.
# ---
# I'm Reading...
#
# 'Inventori Lucis Soli Invicto Nuntio' reads the dedication - loosely translatable as 'I am the herald of the Sun Unconquerable, Light's Contriver'. This is a variation on the more usual 'invicto augusto', the declaration which united the eastern and western traditions of the Church Solar.
# ---
# I've Read...
#
# The Shepherd Illuminate, the Virgin-Born, warns of the Sun's Division but promises its ultimate reunification in the Second Dawn 'through the ministry of St Uzult'. <i>Uzult</i> is of course the ink of power used by Librarians of the Tree, but also venerated as a saint in some borderline heterodox solar traditions.
gospel_of_nicodemus = card_type("gospel_of_nicodemus",
    attributes(tally_price=4, mystery_lantern=6, readable=1, thing=1, solar_gothic_period=1, subject_sacra_solis_invicti=1, codex=1),
    lessons=1,
    provides=memory.revelation,
)


# Green Jasper Tablet
#
# Supposedly copied from a tablet of green jasper which serves as the Covenant-stone of the Monastery of the Fifth Cup - the token which gives that Library shelter beneath the Watchman's Tree.
# ---
# I'm Reading...
#
# 'Humankind hid itself from the Glory's light in the Roots of the Watchman's Tree. But for every chink we stuffed with cloth and hair, we opened another, and the light crept in. Until we looked below, into Nowhere, and the Eye of the Mare-in-the-Tree winked Red...'
# ---
# I've Read...
#
# The Tablet expounds the dangers of inviting in the Nowhere-Hour called the Mare-in-the-Tree, and also of forbidding her entry, since she can never entirely be denied. Along the way, it reveals the secret of the Sacrament Malachite ('in which the merry Mare merrily spits') - brewed with the Rites of the Roots from the numa-pear, in the presence of sufficient Nectar-aspect.
green_jasper_tablet = card_type("green_jasper_tablet",
    attributes(tally_price=5, written_in_cracktrack=1, mystery_nectar=10, readable=1, thing=1, dawn_period=1, subject_rites_of_the_roots=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# Honey: the Comprehensive Guide
#
# Harvey Hattington - pilot, polymath, confectioner - writes with great enthusiasm about the 'marvellous work of the Bee'.
# ---
# I'm Reading...
#
# Hattington insists that all the primary aspects - Nectar, Scale, Heart, Lantern, Moth, Grail - are possessed by bees and expressed in honey. (Clearly, he points out, there are only six primary aspects, as a honeycomb has only six angles.)
# ---
# I've Read...
#
# 'Yewgall Ink is prepared with these techniques - but so is Skinshuck Mead, and only Skinshuck requires honey. Just as any beverage or foodstuff can be improved with the addition of honey, so any garden is improved with the presence of bees. Even those bloody Blomberende.'
honey_the_comprehensive_guide = card_type("honey_the_comprehensive_guide",
    attributes(tally_price=1, mystery_nectar=6, readable=1, thing=1, subject_insects_and_nectars=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.contradiction,
)


# How the End will Begin
#
# A prophecy of the Wars of the Roads, recorded in the Subcontinent in the days before the Great Hooded Princes.
# ---
# I'm Reading...
#
# In the foretold war, the Children of the Leashed Flame march on the cities of the Continent, but the 'Enactors of Solar Law' and the 'Triple Sisterhood' join forces to hold them back... at tremendous cost.
# ---
# I've Read...
#
# 'In that battle between the Imperishable Legions and the Leashed Flame, the Legions will perish and the Flame will be unleashed.'
how_the_end_will_begin = card_type("how_the_end_will_begin",
    attributes(tally_price=5, mystery_edge=14, written_in_vak=1, readable=1, thing=1, codex=1, dawn_period=1, subject_ragged_crossroads=1),
    lessons=2,
    provides=memory.fear,
)


# Hunting Journals of Bryan Dewulf
#
# Bryan Dewulf, the son of the 3rd Baron Brancrug, gives advice on hunting in the Bounds.
# ---
# I'm Reading...
#
# It is clear from Bryan's journals that he sought unorthodox trophies and put them to unorthodox uses. He was in fact hanged as a witch at the age of twenty-four, and never inherited the estate…
# ---
# I've Read...
#
# Bryan describes how a 'Sky-inspired fife' can be prepared using these Fur and Feathers techniques, in the presence of greater Sky-aspect, to 'make of the winds good neighbours.' It's a powerful technique to be described so casually: Bryan's main interest seems to be in ensuring good weather for his hunts.
hunting_journals_of_bryan_dewulf = card_type("hunting_journals_of_bryan_dewulf",
    attributes(tally_price=3, mystery_scale=8, readable=1, thing=1, subject_furs_and_feathers=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.fear,
)


# Inaam, Kapigiginlupir, Garkie, Cryppys
#
# In which four enigmatic figures tell the stories they've heard over the years at the Roost, the secret location where the aviform Hours congregate.
# ---
# I'm Reading...
#
# INAAM: Has not the Beach-Crow shared his treasures? GARKIE: Not the rarest. He takes those things most precious, which he claims found, not stolen.
# ---
# I've Read...
#
# The Beach-Crow, Kapigiginlupir suggests, is not only a thief, but also a spy and even a voyeur. He has hidden the memory of secret couplings among the Hours and their Names in the corners of the House, as treasures to gloat over. There is particularly fevered speculation on a liaison between the Ring-Yew, that fervent hour of the Wood, and the Mare-in-the-Tree, who sometimes has been the Witch's Sister.
inaam_kapigiginlupir_garkie_cryppys = card_type("inaam_kapigiginlupir_garkie_cryppys",
    attributes(tally_price=2, mystery_moth=14, written_in_phrygian=1, readable=1, thing=1, subject_transformations_and_liberations=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# In Memory of Gods
#
# The 'Barrowchild', a nameless Gaulish adept who joined an organisation identified as the Ordo Limiae, writes regretfully of the destruction of the gods-who-were-stone - the Hours who preceded humanity.
# ---
# I'm Reading...
#
# The Barrowchild singles out the Scarred Tribune, the Red Grail, the Forge and the Moth for especial condemnation as murderers of the first gods. 'We live in the shadow of their crime', she writes, 'and we must evade it or repeat it.'
# ---
# I've Read...
#
# The Barrowchild describes how the Grail drained the Hour called Tide, how the Moth 'usurped the Wheel from within', stealing its skin, and how the Forge first eclipsed then shattered Flint. 'Perhaps these are glories,' she observes, 'but then it cannot be that Glory is merciful.'
in_memory_of_gods = card_type("in_memory_of_gods",
    attributes(tally_price=5, written_in_fucine=1, mystery_winter=12, readable=1, thing=1, dawn_period=1, codex=1, subject_ragged_crossroads=1),
    lessons=2,
    provides=memory.hindsight,
)


# In the Malleary
#
# A lively account of the creation of each jewel at the world's beginning.
# ---
# I'm Reading...
#
# Lively, yes; but also almost entirely nonsense. 'Pearl, the tears of the forgotten moon, caught by the Lionsmith in his net. Ruby, the blood of the first bird, stung by the Lionsmith's hammer.'
# ---
# I've Read...
#
# The author is either terribly misinformed of the nature of the Hours, or - one begins to suspect - intentionally throwing up a smoke-screen to confuse seekers of the Invisible Arts. But there are some useful crumbs of fact to be picked out of the daft and gaping cracks. 
in_the_malleary = card_type("in_the_malleary",
    attributes(tally_price=3, mystery_lantern=4, readable=1, thing=1, subject_anbary_and_lapidary=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.foresight,
)


# In The Mountains As Upon The Plain There May Not Be A Path Where None Has Passed
#
# Ninegala of Lagash describes the secrets to be found in mountains.
# ---
# I'm Reading...
#
# Ninegala tells a number of lively stories about riddling ogres and wars between mountain tribes, but turns sombre in the tale of the Empty-Handed Hunter: a lover of the Grail who sought to match her appetites and join her as an Hour, but in the end rent and devoured himself, giving his name to the mountains he had once roamed.
# ---
# I've Read...
#
# Ninegala claims that the Hours who sometimes manifest as birds - the Laughingthrush, the Ivory Dove, the Beachcrow and the Witch-and-Sister - meet at a secret location on a mountaintop to exchange gossip unheard by their peers. Now and then a mortal overhears them. The mortal is always obliterated, and the meeting-place always changed.
in_the_mountains_as_upon_the_plain_there_may_not_be_a_path_where_none_has_passed = card_type("in_the_mountains_as_upon_the_plain_there_may_not_be_a_path_where_none_has_passed",
    attributes(tally_price=5, mystery_sky=18, written_in_vak=1, readable=1, thing=1, dawn_period=1, subject_sky_stories=1, codex=1),
    lessons=3,
    provides=memory.gossip,
)


# Isaac of Karth's History of the Shadowless Kings
#
# 'A True and Accurate History of the Shadowless Kings, by Isaac of Karth.' Isaac describes the thousand-year ascendancy of the Shadowless Empire.
# ---
# I'm Reading...
#
# 'The first and greatest history' is described herein. The Persian Empire - 'the sons of Achaemenes', 'the Shadowless Kings', 'the most Glorious Empire' - survives the assaults of Alexander the Great and flourishes as late as the fifth century.
# ---
# I've Read...
#
# After the fall of Rome, the Shadowless Empire takes Byzantium under its wing, and moves East against the Land of the Great River. Isaac begins to recount the invasion struggling against 'the unskinned armies of the hooded serpents', but ends abruptly with a series of incantations that he claims allowed the Shadowless Empire to persist.
isaac_of_karths_history_of_the_shadowless_kings = card_type("isaac_of_karths_history_of_the_shadowless_kings",
    attributes(tally_price=5, written_in_aramaic=1, mystery_rose=14, readable=1, thing=1, subject_sand_stories=1, dawn_period=1, codex=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# It Is Written
#
# Musgrave, fourth of the Dewulf line, writes tentatively about the 'Covenant of Brancrug' and the legacy of the sacred inks he calls 'encausta potentialia'.
# ---
# I'm Reading...
#
# 'As the Light passeth through a Prism into many Colours, so the Great Inks separateth into the Lesser Inks, and the Lesser Inks into Inks Minor…'
# ---
# I've Read...
#
# Musgrave coyly refuses to talk of the Great Inks (or else refuses to admit he doesn't know much about them). He insists that yewgall and stargall, which can be mixed with sufficient Nectar or Sky aspect, are sufficient for 'most befitting Purposes'.
it_is_written = card_type("it_is_written",
    attributes(tally_price=3, mystery_scale=8, readable=1, thing=1, codex=1, subject_inks_of_power=1, baronial_period=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# Journal of Sir David Greene, 1903
#
# A confidential journal kept by Greene, former Nocturnal Branch Superindent but, by 1903, Librarian of the House. Greene has kept his journal in Hyksos, presumably as an extra measure of privacy.
# ---
# I'm Reading...
#
# In 1903, the House co-operated closely with the Branch, and Greene was the public face of that co-operation. In private, however, Greene is clearly disillusioned with the Branch, which he increasingly regards as irresponsible. He is especially concerned about the construction of a 'suppressive mechanism' beneath Brancrug Gaol, and its likely occupant.
#
# 'Hours and Names are dangerous,' he writes, 'but at least our dealings have the benefit of long experience. An Hour who acts before she is born - who leaves those places she has never entered - if her Names walk the world already, how can we understand their courses and their capabilities?'
# ---
# I've Read...
#
# The last entries alternate between calculations (tides, dates, financial calculations) and expressions of fevered longing for 'A.F'. It seems that Greene intends to run away with A.F., and some of the calculations imply that he has been embezzling funds to that end, under cover of the chaos caused by the Ortucchio Incident and the subsequent reorganisation of Nocturnal Branch into the Suppression Bureau...
#
# The entries, however, stop abruptly before the year's end. It's not clear whether Greene did in fact abscond with funds and fond friend, or whether he abandoned this journal for other reasons.
journal_of_sir_david_greene = card_type("journal_of_sir_david_greene",
    attributes(tally_price=4, mystery_edge=14, written_in_hyksos=1, readable=1, thing=1, subject_sharps=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.fear,
)


# Journal of Thomas Dewulf
#
# Thomas Dewulf, 2nd Baron Brancrug, was nicknamed 'Baron Silence of Castle Silence' for his taciturn severity - most likely the origin, eventually, of the name 'Hush House'.
# ---
# I'm Reading...
#
# There are very few personal details here. Thomas, a talented astronomer and ouranoscopist, dispassionately details his observations and the building of the observatory atop the Watchman's Tower.
# ---
# I've Read...
#
# As he records the passing of the Great Comet in 1577, the tone finally becomes more animated but also more obscure. Thomas cites his Dawn Period namesake, Abbot Thomas, as an authority on 'Wind, Moon, and Shell in the Heavens Inferior'. He observes: 'My predecessor knew this Truth - three Blossoms hath the Watchman's Tree: Paper; Ink; and Flame. The Great Comet, I now aver, is that Flame.'
journal_of_thomas_dewulf = card_type("journal_of_thomas_dewulf",
    attributes(tally_price=3, mystery_sky=4, readable=1, thing=1, subject_ouranoscopy=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.salt,
)


# Journal of Walter Dewulf
#
# Walter Dewulf, 3rd Baron Brancrug, was grandson of Thomas, son of the disgraced Giles, who eloped with 'Pale Hafren'. The Dewulf line might have ended here if the Seneschale Ernestine - by then over eighty - had not managed to reconcile Thomas with a dying Giles.
# ---
# I'm Reading...
#
# Walter, though nominally siding with the Parliamentarians, manages to stay out of the war... but in 1642, his son Bryan runs away on the night of his sixteenth birthday and joins the Royalist army. He is captured and returned to his father, who pleads for mercy and gives his parole for his son's good behaviour.
# ---
# I've Read...
#
# In 1648, Bryan runs away again to join a Royalist uprising. Walter writes of news that Bryan has been seen on the field of battle at Gear Camp, but that his fate is yet unknown. Walter writes one last entry about his fear for his son and the future of his family.
#
# There the journal ends; but the extensive account of Walter's collaboration with the architect Gregory Wheelock includes usefully esoteric information.
journal_of_walter_dewulf = card_type("journal_of_walter_dewulf",
    attributes(tally_price=3, mystery_forge=6, readable=1, thing=1, subject_door_and_wall=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.foresight,
)


# Just Verse
#
# A rare surviving copy of Christopher Illopoly's notoriously unsuccessful volume of experimental poetry, published in 1912.
# ---
# I'm Reading...
#
# Illopoly is clearly more interested in the occult than the aesthetic aspects of the work. By most measures, the rhymes are contrived; the meter inconsistent; the imagery banal. Still, even the worst verses have a compelling quality, and I find myself drumming my fingers on the desk to accompany their rhythms.
# ---
# I've Read...
#
# In an afterword, Illopoly discusses 'mnemonic holometaboly', by which he seems to mean a sort of crafting process where memories, when fed into a Preliminal Meter technique in the presence of enough Knock or Rose, can 'blossom and fissure' into more potent versions of themselves...
just_verse = card_type("just_verse",
    attributes(tally_price=1, mystery_rose=6, readable=1, thing=1, subject_preliminal_meter=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.pattern,
)


# Key of Night
#
# The deliberations leading to a manifesto of the 'Worms of a Scale', as recorded around 1900 in the Bar Vienna, in the cellar of the Hotel Ciervo in Noon.
# ---
# I'm Reading...
#
# The Worms, all of whom use grandiose <i>noms de guerre</i> like Citizen Knife and the Midnight Pilgrim, agree that all previous iterations of their movement have been feckless and treacherous, and agree that the return of the prehuman Hours - the gods-from-stone - is the true way to end 'the tyranny of Eternity.'
# ---
# I've Read...
#
# The Worms identify the Wheel, the Tide, the Flint, Sulochana, the Spider Door, the Excellency Gnathobasis and Wickel Inextinguishable as the Seven Necessary Pentiments that must be 'returned to every History through the Propaganda of the Deed'. This is an eccentric list and clearly a compromise; the process of thrashing it out clearly exhausts all the participants, who don't specify the necessary Deed beyond a vague reference to 'the Loopholes'.
key_of_night = card_type("key_of_night",
    attributes(tally_price=1, mystery_scale=6, readable=1, thing=1, subject_pentiments_and_precursors=1, nocturnal_period=1, codex=1),
    lessons=1,
    period="curia", # game bug?
    provides=memory.fear,
)
# note: this book "falls out" of uncatalogued curia but it has a nocturnal_period tag


# Kitling Ripe and the Moldywarp's Grave (and Other Stories)
#
# A lusciously illustrated tome of loosely connected children's stories. Few of them are remotely suitable for children.
# ---
# I'm Reading...
#
# The protagonist, a speechless cat-thing called Kitling Ripe, performs a series of elaborate rites to rescue members of her extended family, culminating in the resurrection of her 'other grandmother', Moldywarp.
# ---
# I've Read...
#
# 'When the Snake-Witch killed the horse, Kitling snatched one of its eyes. When the Dry-Witch killed the pig, Kitling stole a cup of its blood. Then she took them to the place Moldywarp lay buried, and she shook out her hair, and she began to dance…'
kitling_ripe_and_the_moldywarps_grave = card_type("kitling_ripe_and_the_moldywarps_grave",
    attributes(tally_price=2, mystery_moth=6, readable=1, thing=1, subject_resurgences_and_emergences=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.impulse,
)


# Kitling Ripe's Tasty Treats
#
# The Velvet is the Hour of secrets; and so very little is known of the - Moth-long? Nectar-long? - who ascend to immortality under her auspices. But this book (by 'Kitling's Friend') purports to be part cook-book, and part manual for immortality.
# ---
# I'm Reading...
#
# Kitling Ripe is the name usually given to the speechless 'but never silent' cat-thing that serves as a Name of the Velvet. Kitling Ripe, it seems, enjoys hunting immortals; and the Velvet is very fond of Kitling Ripe.
# ---
# I've Read...
#
# The secret, it appears, is to arouse the Kitling's appetite enough to become her quarry, but not <i>quite</i> enough to be caught. The Velvet permits the game, since it culls immortals careless enough to attract attention, and keeps her Name happy. The author bemoans the loss of the Carapace Cross' savour-secrets, which apparently were particularly tempting - but suggests decent spice-substitutes, which also happen to make for excellent pigeon-pie.
kitling_ripes_tasty_treats = card_type("kitling_ripes_tasty_treats",
    attributes(tally_price=3, mystery_nectar=4, readable=1, thing=1, subject_spices_and_savours=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.satisfaction,
)


# Lady Eva's Repose
#
# A 'meditation' on the drowning of Lady Eva Dewulf and her two grandchildren, written in the years when the estate was abandoned by Father Theo, once the Dewulf family chaplain, one of the few to remain on the Isle in those desolate years.
# ---
# I'm Reading...
#
# 'There are so many stories of her heritage, so many rumours of her persistence. We might easily choose to believe that the grand-twins escaped - even that they live yet beyond the sea - '
# ---
# I've Read...
#
# Father Theo has come to believe that Eva sought an escape from a family curse - the 'pale heritage' of Hafren her forebear, or the curse placed upon the line by the cunning-man Red William in the time of Hendrik Dewulf. He had begun by believing neither curse was real; but as the book concludes, he decides that he has determined to believe in them, rather than accept the three deaths as a futile tragedy. 'One does not so easily escape the long necessity of faith,' he concludes.
lady_evas_repose = card_type("lady_evas_repose",
    attributes(tally_price=3, mystery_winter=4, readable=1, thing=1, baronial_period=1, codex=1, subject_rhyme_and_remembrance=1),
    lessons=1,
    provides=memory.regret,
)


# Letters from a Fugitive
#
# Lars Westergren, explorer and murderer, spent seven years escaping justice through his knowledge of byways and shortcuts in the Bounds. Throughout that time he wrote regularly to his daughter, possibly in part to taunt his pursuers.
# ---
# I'm Reading...
#
# A year with the Légion du Seuil, patrolling the Bounds, until he deserts; a month in the Priory of Captains in Morbihan; seven days, or so he claims, in Ys behind the wave…
# ---
# I've Read...
#
# Cornered at last by his pursuers, Westergren writes that he will 'attempt the Paths of the Sun'. He doesn't seem sanguine about his chances, and indeed, this is his last letter. An editor's note adds that Westergren's whereabouts or end remain unknown, although he was supposedly sighted at the 'Christmas Market' in Vienna - the negotiations between invisible underworld figures that happen each year there - in 1929.
letters_from_a_fugitive = card_type("letters_from_a_fugitive",
    attributes(tally_price=3, written_in_phrygian=1, mystery_rose=6, readable=1, thing=1, codex=1, subject_path_and_pilgrim=1, baronial_period=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# Letters To My Successor
#
# Advice from Gervinus van Lauren, eleventh Librarian of Hush House, to the one who will come after him.
# ---
# I'm Reading...
#
# Some of the advice is practical - don't worry about losing the House Key; always close the seaward windows; make sure you feed the cockatoo. Much more of it is rarefied, specifically about the 'Inks of Revelation'. And some of it relates to van Lauren's own doom...
# ---
# I've Read...
#
# 'When I was another, I made a foolish wager with the Hooded Princes, to solve seven riddles. I had not realised the riddles would be set by me for the one I would become. Six are resolved. The seventh will be the end of me. It waits now in the cellar of the Gaol, where Collers still believes I can keep it confined. But the first riddle told me I would not see the Second Dawn...'
letters_to_my_successor = card_type("letters_to_my_successor",
    attributes(tally_price=1, mystery_lantern=8, readable=1, thing=1, subject_inks_of_revelation=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# Malachite Supplications
#
# Prayers addressed to the Malachite by the Sisterhood of the Triple Knot.
# ---
# I'm Reading...
#
# 'If we should flourish not, let our enemies flourish, in that time when we are no more…'
# ---
# I've Read...
#
# One prayer describes how a strong degree of Nectar-aspect can be used with Leathy and Tridesma Hiera rites to bring forth 'the Last Nectar of the Last History, the Living Ink, the Ink-in-Secret…'
malachite_supplications = card_type("malachite_supplications",
    attributes(tally_price=4, written_in_greek=1, mystery_moon=8, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_tridesma_hiera=1),
    lessons=2,
    provides=memory.impulse,
)


# Medusan Commentaries
#
# Haustorial discussions of Medusa's histories.
# ---
# I'm Reading...
#
# 'Medusa's Riddle: 'What Is Not Seen?' She might be the oldest of her kind still living; and she is dead. Once she held the key to the door in the Wood; and though perhaps she lost it, she holds it still…
# ---
# I've Read...
#
# The scholars of the Haustorium seem to suggest that just as there are always seven Ligeians but they are not always the same, there is always one Medusa but she is not always the same. There does seem to be more of a common thread of identity than simply a series of titled successors, and here the Haustorium's argument becomes harder to follow - especially because the Haustorium and its members themselves have an unusual concept of individual identity...
medusan_commentaries = card_type("medusan_commentaries",
    attributes(tally_price=3, mystery_grail=21, written_in_killasimi=1, readable=1, thing=1, multitudinuous=1, codex=1, baronial_period=1, subject_pentiments_and_precursors=1),
    lessons=3,
    provides=memory.fear,
)


# Medusa's Lament
#
# On the death of the Hour called Seven-Coils, 'the Father of the Mother'.
# ---
# I'm Reading...
#
# The first part of the poem describes the ambush of the Seven-Coils by a warrior 'scarred all over by the traitor gods, scarred even unto his eyes, so that the sight of the great coils would not destroy him'.
# ---
# I've Read...
#
# The battle rages on until the Seven-Coils drowns in its own blood, at which point the narrative turns mystical and allusive. A seven-titled goddess arises from the foam of its blood: she is an armoured queen, a serpent-daughter, a key, a healer, a murderess, an oracle, but her seventh title is not to be revealed.
medusas_lament = card_type("medusas_lament",
    attributes(tally_price=4, written_in_greek=1, mystery_scale=14, readable=1, thing=1, solar_gothic_period=1, subject_horns_and_ivories=1, codex=1),
    lessons=2,
    provides=memory.fear,
)


# Musgrave's Sketches
#
# Musgrave, 4th Baron Brancrug, was widely mocked as 'the Bleating Baron' and 'the Lamb Dewulf', but these sketches reveal a complex, sombre inner life.
# ---
# I'm Reading...
#
# 'Art begins in Colours; grows Dappled; finally is either mostly Darkness, or mostly Light.'
# ---
# I've Read...
#
# Musgrave discusses the temptation of the perfectly minimal 'palest painting'. He has so far managed to resist this temptation, but does guiltily describe success in using Sights and Sensations with Winter-aspect to create first a 'chilly elixir' from flowers, which he believes he can refine further into a 'final pigment'...
musgraves_sketches = card_type("musgraves_sketches",
    attributes(tally_price=2, mystery_winter=8, readable=1, thing=1, curia_period=1, codex=1, subject_sights_and_sensations=1),
    lessons=2,
    provides=memory.bittersweet_certainty,
)


# My Deeds, My Powers, My Achievements and the Injustices Perpetrated Against Me
#
# A diatribe by Hokobald of Pocsind, formerly of the order of immortals called the House of Lethe (later the Ordo Limiae; much latter the Obliviates). He has scores to settle.
# ---
# I'm Reading...
#
# Hokobald boasts of his royal descent, and insists that the magics of the Forge are more effective when practised by those of noble blood.
# ---
# I've Read...
#
# Pocsind complains of his condemnation by the Ordo Limiae. He acknowledges that he has 'undergone alterations' after the 'consummation of that particular delight', but insists that these changes are both elegant and inevitable. 'Who is the fire, and who the fuel?' he asks rhetorically.
my_deeds_my_powers_my_achievements_and_the_injustices_perpetrated_against_me = card_type("my_deeds_my_powers_my_achievements_and_the_injustices_perpetrated_against_me",
    attributes(tally_price=4, mystery_forge=16, written_in_deep_mandaic=1, readable=1, thing=1, solar_gothic_period=1, subject_transformations_and_liberations=1, codex=1),
    lessons=3,
    provides=memory.foresight,
)


# Naenian Sketches
#
# Travelogues and studies exchanged by raggies and ghouls - that is, the Long who've ascended under the patronage of the Sun-in-Rags and those who won the attention of the Elegiast.
# ---
# I'm Reading...
#
# 'Naenia is the Elegiast's Name, but she has always stood high in the Sun-in-Rags' favour; and she offers her consolations also to those Long who have taken him as a patron...'
# ---
# I've Read...
#
# Both kinds of Winter-long know that their death is only deferred, so both tend to seek and treasure beauty. Here they detail their purest experiences - the mountain after the avalanche, the peace after the storm-wreck, the gusted silence of the sun-shadowed hill...
naenian_sketches = card_type("naenian_sketches",
    attributes(tally_price=1, written_in_sabazine=1, mystery_winter=21, readable=1, thing=1, multitudinuous=1, subject_sights_and_sensations=1, codex=1, nocturnal_period=1),
    lessons=3,
    provides=memory.hindsight,
)


# Nix Abolix
#
# A grim treatise on 'those feasts that occur, those feasts that are not to be witnessed.'
# ---
# I'm Reading...
#
# The alukites, who feasted on their children and became monsters. The dragon-kinds among the Carapace Cross, who feasted on Hour-flesh and became monsters. The khalvites, who drank of Echidna's bounty, and became monsters…
# ---
# I've Read...
#
# 'Marinette, the Ligeian: so young, so hungry. All her children cannot slake her thirst. When Moth rose, another held the Flaying Key, but at the Grail's bidding did Marinette consume that she.'
nix_abolix = card_type("nix_abolix",
    attributes(tally_price=5, written_in_fucine=1, mystery_moon=16, readable=1, thing=1, dawn_period=1, subject_wolf_stories=1, codex=1),
    lessons=3,
    provides=memory.fear,
)


# Notes on Bindings
#
# Gideon Dewulf, 5th Baron Brancrug, discusses techniques shared between medical suturing, tailoring, and - carefully, allusively - the binding of restless spirits.
# ---
# I'm Reading...
#
# Gideon's favourite motif is 'the history of the flesh'. He insists obscurely that histories should be woven, not written.
# ---
# I've Read...
#
# Gideon speaks reverently of the 'wyrd-weft', which he has achieved by applying Stitching and Binding arts to a fabric in the presence of sufficient Winter. He laments however that its complexities only approach those understood by the Sisterhood of the Knot, which in turn are only a shadow of 'the true Braid of Histories'.
notes_on_bindings = card_type("notes_on_bindings",
    attributes(tally_price=3, mystery_heart=10, readable=1, thing=1, codex=1, subject_stitching_and_binding=1, baronial_period=1),
    lessons=2,
    provides=memory.solace,
)


# Nyn's Cages (Avignon Text)
#
# The 'merciful measures' of the witch Nyn.
# ---
# I'm Reading...
#
# Nyn's stated aim was to 'keep beyond the Walls of Sleep that business which should not trouble the world'. This includes fever, madness and delirium, as well as spirits identified as 'Devourers' and 'Deceivers'.
# ---
# I've Read...
#
# Nyn warns against cutting hair, cracking mirrors, spilling blood, or invoking the Edicts Liminal or Inviolable before sleep - 'for no matter how secure a lock may be, its key will surely open it.'
nyns_cages_avignon_text = card_type("nyns_cages_avignon_text",
    attributes(tally_price=4, written_in_ericapaean=1, mystery_heart=16, readable=1, thing=1, solar_gothic_period=1, subject_quenchings_and_quellings=1, codex=1),
    lessons=3,
    provides=memory.hindsight,
)


# Nyn's Cages (Bruges Text, Illuminated)
#
# The 'merciful measures' of the witch Nyn. This is only a partial version of the original, but it contains illustrations by Nyn's pupil, Mabelie of Bruges, which supplement the original.
# ---
# I'm Reading...
#
# Nyn's stated aim was to 'keep beyond the Walls of Sleep that business which should not trouble the world'. This includes fever, madness and delirium as well as spirits identified as 'Devourers' and 'Deceivers'. (Mabelie clearly enjoyed drawing both Devourers and Deceivers, but was less interested in illustrating disease symptoms.)
# ---
# I've Read...
#
# Nyn warns against invoking the Edicts Liminal or Inviolable before sleep - 'for no matter how secure a lock may be, its key will surely open it.' Mabelie has helpfully illustrated this by drawing a sleepwalker clambering through an open window, about to leap into the jaws of a sea-monster. The sea-monster is goggle-eyed with happy anticipation.
nyns_cages_bruges_text = card_type("nyns_cages_bruges_text",
    attributes(tally_price=4, written_in_ericapaean=1, mystery_winter=10, readable=1, thing=1, solar_gothic_period=1, subject_quenchings_and_quellings=1, codex=1),
    lessons=2,
    provides=memory.hindsight,
)


# Oblations in Iron
#
# A Monster-hunting initiate of the Hour named the Colonel, who identifies herself as 'Little Sophia', records the exhibits she has rendered to the Worm Museum in the Mansus.
# ---
# I'm Reading...
#
# Little Sophia has never visited the Worm Museum, or even the Mansus, in person, and evidently has no desire to do so. She mixes ink which incorporates the remains of her prey, writes her records in that ink, then burns them before the Colonel's altar…
# ---
# I've Read...
#
# 'It is essential however to permit no drop of the ink thereby obtained to enter any portal of the body, even a break in the barrier of the skin. Should any fragment of the Worm remain viable, it might enter thereby, and the Hunt's ultimate conclusion be melancholy indeed...'
oblations_in_iron = card_type("oblations_in_iron",
    attributes(tally_price=2, mystery_winter=6, readable=1, thing=1, curia_period=1, codex=1, subject_inks_of_containment=1),
    lessons=1,
    provides=memory.hindsight,
)


# Observations on the Peacock Door
#
# Ninegala of Lagash discusses the Peacock Door, the highest door available to mortals in the Mansus: 'a rent, an imperfection, an abrasion.'
# ---
# I'm Reading...
#
# Notably, the book is written in Vak, which by some accounts is another aspect of the Peacock Door itself. Ninegala addresses this by apologising courteously to the Door, and the language, at the end of every section.
# ---
# I've Read...
#
# The Peacock Door did not exist - Ninegala says - in the days when the gods-from-stone entered the Mansus. They used the 'Fanged Key' to open the Savage Door, a door not usually available to mortals. 'Speech, as the initiates of Chione would have it, is a wound. I fear that through that wound, the blood of the Mansus flows even now, and that one day Speech will be an end to Dream. I fear that; but I fear the alternative far more.'
observations_on_the_peacock_door = card_type("observations_on_the_peacock_door",
    attributes(tally_price=4, mystery_moon=10, written_in_vak=1, readable=1, thing=1, solar_gothic_period=1, subject_sickle_and_eclipse=1, codex=1),
    lessons=2,
    provides=memory.contradiction,
)


# OGHKOR OGHKOR TISSILAK OGHKOR
#
# A surprisingly chatty text by an entity that identifies itself as 'the Excellency Gnathobasis'.
# ---
# I'm Reading...
#
# The Excellency Gnathobasis explains the 'limbs and extensions' of potent and dangerous 'glyphic achievements'. The sentences are nonsense on first reading, but quickly acquire an insistent meaning on each repetition.
# ---
# I've Read...
#
# 'With adequate Grail,' the Excellency Gnathobasis explains, 'the Pale Mommet wakes to life. With generous Grail, the Flushed Mommet accepts our beneficence. It may be necessary to overcome scruple! The Excellency Gnathobasis will assure you as to how, and to whom, and with which most perfect instrument.'
oghkor_oghkor_tissilak_oghkor = card_type("oghkor_oghkor_tissilak_oghkor",
    attributes(tally_price=3, mystery_knock=12, readable=1, thing=1, codex=1, baronial_period=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=2,
    provides=memory.pattern,
)


# Old Coppernose and the Softer Metal
#
# A disgraceful compendium of ribald poetry about the habits and corruptions of Henry VIII.
# ---
# I'm Reading...
#
# Henry's 'Great Misfortune' - his crushing injury at a jousting bout - has left him unable to stand 'any straighter than a splintered withy'…
# ---
# I've Read...
#
# The most savage mockery is reserved for Henry's 'Great Debasement', where the corruption of his softer metal is supposed to have crept into the coin of the realm. The last and most serious lampoon makes seditious references to 'the Crucible Revolution'.
old_coppernose_and_the_softer_metal = card_type("old_coppernose_and_the_softer_metal",
    attributes(tally_price=2, mystery_forge=8, readable=1, thing=1, curia_period=1, codex=1, subject_bells_and_brazieries=1),
    lessons=2,
    provides=memory.foresight,
)


# On Imperfections
#
# Poemander, light-smith and Lantern-long, describes the process of 'transinhabitation', which he calls 'a manifestation of imperfection.'
# ---
# I'm Reading...
#
# Lantern-long lack bodies, and so cannot normally leave the Mansus - but they can 'steady-glint' in the physical world by establishing a 'road of glass'. Poemander notes with disgust that the order of Long called the Obliviates refer to it as 'scrining', which he considers a 'debased term'.
# ---
# I've Read...
#
# Poemander explains the benefits of transinhabitation - that a Lantern-long can affect the senses and thoughts of those nearby, that they can even enter their spirits, and that they can 'employ the senses of those inhabited to experience again the scent of blossom and season'. This seems to be what interests him most. He insists that a Lantern-long should only ever inhabit a mirror of silver, not silvered glass, but he declines to explain why.
on_imperfections = card_type("on_imperfections",
    attributes(tally_price=3, mystery_knock=10, readable=1, thing=1, codex=1, subject_glassblowing_and_vesselcrafting=1, baronial_period=1),
    lessons=2,
    provides=memory.pattern,
)


# On Matthias and the Amethyst Imago: Loss
#
# An account of an occult romance. A certain Para, son of Aaron, claims to have written this in a single night as part of his initiation into the Damascene branch of the House of Lethe - that order of immortals who rejected their past and future.
# ---
# I'm Reading...
#
# 'The laws of the House forbade Matthias to love. The customs of the Wood forbade the Imago to remain. So he conjured her a final time, when she had uncovered the Shears of Alakapura; and she suffered him to cut the wings from her back, so that she might remain; and he suffered her to cut the parts which hold man's seed, to keep them from the Detestable Act. This was love in all its blood and joy. We have cast out Matthias from the House.'
# ---
# I've Read...
#
# 'In the cradle of the roots, Matthias and the Imago left their names, and though their names were lost, they found their Nameday Riddles. This we recall in Solution and Separation, so that in the presence of the Moth our memories may become our futures. Do this wisely, in memory of the Name and the Long who gave up their past that they might be together forgotten.'
on_matthias_and_the_amethyst_imago_loss = card_type("on_matthias_and_the_amethyst_imago_loss",
    attributes(tally_price=5, written_in_aramaic=1, mystery_moth=6, readable=1, thing=1, dawn_period=1, codex=1, subject_solutions_and_separations=1),
    lessons=1,
    provides=memory.a_stolen_secret,
)


# On Matthias and the Amethyst Imago: Pursuit
#
# An account of an occult romance. A certain Mek claims to have written this in a single night as part of his initiation into the Theban branch of the House of Lethe - that order of immortals who used the arts of water to conceal themselves.
# ---
# I'm Reading...
#
# 'Matthias defied us to hunt the Names of the Moth in the Wood, to populate his pinned collection. The Amethyst Imago had dallied with the Witch-and-Sister, but she'd returned to the Wood to plead the Moth's pardon. The Moth, as a whim or a penance, sent her out to lure the Long to a slough of nightmares.'
# ---
# I've Read...
#
# 'Matthias loved the Imago. (Did he? Can Long love, or has that organ of their soul desiccated beyond repair?) The Imago loved Matthias. (Did she? or did she only enact a whim?) He pursued her through the Wood, but at the last she turned aside from the nightmare-slough, and they lay together where the Bounds grow bright. So they learnt the Grail's pleasures, and this is the lore they won.'
on_matthias_and_the_amethyst_imago_pursuit = card_type("on_matthias_and_the_amethyst_imago_pursuit",
    attributes(tally_price=5, written_in_aramaic=1, mystery_grail=6, readable=1, thing=1, dawn_period=1, subject_desires_and_dissolutions=1, codex=1),
    lessons=1,
    provides=memory.gossip,
)


# On Matthias and the Amethyst Imago: Transformation
#
# An account of an occult romance. A certain Iyavogos claims to have written this in a single night as part of his initiation into the Aleppine branch of the House of Lethe - that order of immortals who would not pledge themselves to any Hour.
# ---
# I'm Reading...
#
# 'We cast Matthias out, and we pronounced a curse upon the Amethyst Imago, but we watched them in dreams. We saw them pledge themselves to the Forge, to change themselves and ascend anew. Into the fire they fly.'
# ---
# I've Read...
#
# ''This is the first of the practices that the Imago and Matthias used, to begin their ascent to power. They have risen beyond our sight, but their flames may yet burn in the Malleary.'
on_matthias_and_the_amethyst_imago_transformation = card_type("on_matthias_and_the_amethyst_imago_transformation",
    attributes(tally_price=5, written_in_aramaic=1, mystery_forge=6, readable=1, thing=1, subject_spices_and_savours=1, codex=1, dawn_period=1),
    lessons=1,
    provides=memory.impulse,
)


# On Resonance
#
# Experiments in ithastry by the 'sky-smith' Everett Vinzant.
# ---
# I'm Reading...
#
# Vinzant suggests percussion instruments that might be 'sympathetic' to a number of Hours and Names. Some are more likely than others…
# ---
# I've Read...
#
# Vinzant uncontroversially suggests drums of various materials as the sympathetic instrument for the Thunderskin and its 'ascendant duendrazones'. He proposes bells of bronze and iron for the Lionsmith and Colonel. He spends some time on the design of a 'bee-rattle' for the Malachite, but doesn't seem entirely confident of his findings...
on_resonance = card_type("on_resonance",
    attributes(tally_price=3, mystery_sky=6, readable=1, thing=1, codex=1, baronial_period=1, subject_bells_and_brazieries=1),
    lessons=1,
    provides=memory.foresight,
)


# On the Matter and the Deeds of Serpents
#
# This was probably the 'prophecies of the naga' rendered into English, and illustrated, by 'William Midnight' in Paris in the 1880s; but it shows a number of divergences from that text. It's certainly quite recent by the standards of Vak texts.
# ---
# I'm Reading...
#
# The serpent-folk called the Great Hooded Princes came to know the order called the House of Lethe, and warred across the miles with them. They made an alliance with the Mother of Ants, 'whose children they had been'...
# ---
# I've Read...
#
# The text describes how the Great Hooded Princes escaped (or will escape) from the Fifth History, where they had died (or were doomed to die). They engaged in a secret conquest of 'the land of the Great River', called India in some histories, and have ensured that all other conquests of that land are false conquests.
on_the_matter_and_the_deeds_of_serpents = card_type("on_the_matter_and_the_deeds_of_serpents",
    attributes(tally_price=2, mystery_knock=12, written_in_vak=1, readable=1, thing=1, curia_period=1, subject_edicts_liminal=1, codex=1),
    lessons=2,
    provides=memory.secret_threshold,
)


# On the White
#
# Solomon Husher writes, perhaps allegorically, of Winter, and its long slow doomed romance with the Sun. The epigraph is 'Sunset at Noon'.
# ---
# I'm Reading...
#
# On closer investigation, the work seems to be a theory of aesthetics, or perhaps a set of warnings about the dangers of painting.
# ---
# I've Read...
#
# Husher writes distractedly about his suspicion of colours and his yearning for death. He hints at a Great Work he has envisaged, or begun, where the 'palest of paintings' will enthral the world. He returns again and again to certain compelling phrases which he claims are the 'secret words of Winter'.
on_the_white = card_type("on_the_white",
    attributes(tally_price=2, mystery_winter=6, readable=1, thing=1, subject_quenchings_and_quellings=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.regret,
)


# On the Winding Stair
#
# Gregory Wheelock, the master mason and architect employed by Walter Dewulf to construct the Winding Stair and the guest chambers in Hush House, describes a more ambitious and dangerous project.
# ---
# I'm Reading...
#
# Gregory marks the bricks of his Roost-touched family home, Treowen, with Ramsund, hoping to open forbidden doors…
# ---
# I've Read...
#
# Gregory evidently succeeds in opening a way to something he calls the 'Moon-Hall', but here his account becomes erratic. He insists that in the Moon-Hall the Horned-Axe is still an Edge-power; he hopes for an 'eternal rival', but cannot find the one he needs. The narrative is increasingly interspersed with chess notations, and ends abruptly.
on_the_winding_stair = card_type("on_the_winding_stair",
    attributes(tally_price=2, mystery_knock=8, written_in_ramsund=1, readable=1, thing=1, subject_door_and_wall=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# On Thirstlies, Ivories and Lovelies
#
# Fionna Ayrshire recounts her visits in dreams to the 'Red Church' in the Mansus, and her conversations with the Names of the Grail.
# ---
# I'm Reading...
#
# An Hour, Ayrshire explains, may usually only have seven Names - but since the Thirstlies, Ivories and Lovelies who usually comprise the Red Grail's Names are constantly attempting to devour one another, and the Names of other Hours, that number fluctuates.
# ---
# I've Read...
#
# Lovelies, the 'freshest' of the Grail's Names, usually adopt the characteristics of whatever they devour - be it an Ivory, a Thirstly, or, occasionally, an entirely different kind of Name. A practical application of the principle is described. The arts of Resurgences and Emergences, in the presence of sufficiently potent Grail-aspect, can be used to feed a Pale Mommet to its successor-doll, creating something 'notably more avid'.
on_thirstlies_ivories_and_lovelies = card_type("on_thirstlies_ivories_and_lovelies",
    attributes(tally_price=2, mystery_grail=10, readable=1, thing=1, subject_resurgences_and_emergences=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# On What is Contained By Silver
#
# A dire bestiary of the horrors to be found in mirrors. This is a recent edition of a third century text by 'Poemander'.
# ---
# I'm Reading...
#
# Poemander engages in a considerable and pedantic discussion about the particular mirror-alloys that attract particular danger from particular entities. This is less useful, of course, in an era where most mirrors are silvered glass.
# ---
# I've Read...
#
# 'The virgins/maidens of the mirror favour orchids. The [behindlings?] favour the rhododendron. Cut flowers of either nature should not be placed before polished bronze.'
on_what_is_contained_by_silver = card_type("on_what_is_contained_by_silver",
    attributes(tally_price=3, written_in_greek=1, mystery_sky=6, readable=1, thing=1, subject_glassblowing_and_vesselcrafting=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.pattern,
)


# One Hundred And Eight
#
# Eva Dewulf discurses on the Fifth History, and particularly on those who are said to have 'passed over' from it - the Great Hooded Princes, the Knock-long who ascended under the Mother of Ants but now (so Eva claims) honour the Horned-Axe.
# ---
# I'm Reading...
#
# 'The Great Hooded Princes call their library the Tomb of Lies, and this has given rise to a foolish tradition that the Princes are habitual liars. Of course, in fact, Truth flourishes when Lies are slain. On the other hand, the Princes do not say 'Knowledge is Power', but rather, 'Power is Knowledge.'
# ---
# I've Read...
#
# Eva has, to her regret, never visited the Library. She notes that it is said to be 'west of the Lion, and north of Victory' - and suggests that, although the Princes are generally associated with India, their library might be farther East…
one_hundred_and_eight = card_type("one_hundred_and_eight",
    attributes(tally_price=3, mystery_scale=4, readable=1, thing=1, subject_pentiments_and_precursors=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# One Thousand Threads
#
# The fate-supplications of the Matriarch of the Well, recorded in darkness by her weavers and her daughters…
# ---
# I'm Reading...
#
# The Well is long choked with rubble and ashes; the Matriarch long gone. She predicted her own end even as these supplications were recorded, but their power remains.
# ---
# I've Read...
#
# Speak these supplications before an altar whose roots have drawn from a sacred spring; perhaps another root will rise towards daylight.
one_thousand_threads = card_type("one_thousand_threads",
    attributes(tally_price=5, mystery_grail=12, written_in_killasimi=1, readable=1, thing=1, dawn_period=1, codex=1, subject_tridesma_hiera=1),
    lessons=2,
    provides=memory.fear,
)


# Operations of a Certain Finality
#
# Subtitled 'The Hammer's Sundering'. The work of an anonymous adept who violently despised the Invisible Serapeum, the library of the Watchman's Tree in Alexandria.
# ---
# I'm Reading...
#
# The author outlines the means they had taken to sabotage the place and its collection, which increasingly seem more poetic than effective, to the point where the whole business may in fact be some kind of allegory.
# ---
# I've Read...
#
# The author gloats that with the techniques of Putrefaction and Calcination, they have transformed the Library's stocks of asimel to 'a seduction of black sapphire' which will ensure the texts therein contain only 'Moon-truths'.
operations_of_a_certain_finality = card_type("operations_of_a_certain_finality",
    attributes(tally_price=2, mystery_winter=8, readable=1, thing=1, curia_period=1, codex=1, subject_putrefactions_and_calcinations=1),
    lessons=2,
    provides=memory.hindsight,
)


# Opus Magnum Caeruleum
#
# Ambrose Westcott used to render the title of this venerable and anonymous work mockingly as 'the Big Blue Business'. A kinder translation would be 'the Great Work in Azure'.
# ---
# I'm Reading...
#
# The reasons for Westcott's enmity to this work are clear to any pyroglyphicist: it was written at least two centuries before he was born, but anticipates or undermines many of his preferred conclusions.
# ---
# I've Read...
#
# The 'Work' in question is the creation of the 'blue gold' allegedly necessary for the terrible Rite which allows a Forge-long to become a Name. The book mentions that Pyroglyphics techniques can be used with Forge to create Iotic Essence as a necessary component; but withholds the final step, insisting that the consequences are too dire, and that any interest should remain only a matter of theory.
opus_magnum_caeruleum = card_type("opus_magnum_caeruleum",
    attributes(tally_price=3, mystery_lantern=14, readable=1, thing=1, subject_pyroglyphics=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.foresight,
)


# Perugian Diaries
#
# In 1907, at the age of eighteen, Christopher Illopoly left Strathcoyne's household to study theology at the University of Perugia in Italy, enrolling under the name 'Christopher Strathcoyne'.
# ---
# I'm Reading...
#
# For four years, since his adoption from a Bristol orphanage, Illopoly served as Strathcoyne's pupil and protégé, but his relationship with this austere and secretive man was always complicated. His journal confides: 'I still think Fraser's intentions are good. Certainly he agrees. But I never understood the final goal of his investigations. He was never prepared to enlighten me. And good intentions or not, I can no longer bear this dream of eyes. We have agreed to part, almost amicably.'
# ---
# I've Read...
#
# Illopoly left Perugia in 1909 without completing his degree. He had long lost interest in his studies, and the latter half of the journal is concerned with his studies of Umbrian folk-songs, and notes towards his own compositions (which are of widely varying quality). One of the better ones, 'In the Marshes of Night', suggests he visited the site of the old Lake Fucinus near Ortucchio…
perugian_diaries = card_type("perugian_diaries",
    attributes(tally_price=1, mystery_sky=4, readable=1, thing=1, nocturnal_period=1, subject_strings_and_songs=1, codex=1),
    lessons=1,
    provides=memory.cheerful_ditty,
)


# Plantagenet Mysteries
#
# Exhaustive attempts to analyse and renew the Blood of the Sun by one of the numerous occult societies, after the manner of the Endeavour Club, for whatever squalid political motive.
# ---
# I'm Reading...
#
# '…until the King fell beneath his great Steed in its Utmost Configuration. By the time he could be cut free, his Alloy had already begun to tarnish, and that Day was ever afterwards known as his Great Misfortune…'
# ---
# I've Read...
#
# 'Since the Sun and the Forge had both bestowed their Favour, one could not remove it without the other - or would not. But neither could the Alloy be renewed by any Power in the Mansus. So the King looked beyond the Mansus - beyond the Bounds…'
plantagenet_mysteries = card_type("plantagenet_mysteries",
    attributes(tally_price=2, written_in_deep_mandaic=1, mystery_moth=21, readable=1, thing=1, multitudinuous=1, subject_transformations_and_liberations=1, codex=1, baronial_period=1),
    lessons=3,
    provides=memory.foresight,
)


# Prophecies of Glory
#
# Religious and patriotic fables collected, or composed, by William Gore.
# ---
# I'm Reading...
#
# This is much more sober in tone than Gore's previous 'Wainscot Histories'; evidently he became religious in his later years.
# ---
# I've Read...
#
# Each fable describes the coming of the Second Dawn, when the Hours of the Sun will be united - but in 'Eternity Denied', 'The Vampire Light', and 'The Feast of Rays,' Gore depicts a tainted Dawn which can only be purified by a second Division of the Sun. He insists repeatedly on the dangers and temptations of a false Dawn...
prophecies_of_glory = card_type("prophecies_of_glory",
    attributes(tally_price=3, mystery_lantern=8, readable=1, thing=1, subject_watchmans_paradoxes=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.revelation,
)


# Quirinic Meditations
#
# Battle-apothegms of the Name Quirinus.
# ---
# I'm Reading...
#
# Quirinus of the Two-Headed Spear is one of the more approachable Names of the Colonel - still grave and inflexible, but more inclined to divulge occasionally useful advice…
# ---
# I've Read...
#
# When Quirinus was honoured in Rome, he was sometimes associated with the enigmatic god Janus - especially in the rites of the Unnumbered Legion. The advice in these pages doesn't confirm any such connection, but does suggest a more philosophical side to this warrior-Name.
quirinic_meditations = card_type("quirinic_meditations",
    attributes(tally_price=4, written_in_ericapaean=1, mystery_lantern=21, readable=1, thing=1, subject_auroral_contemplations=1, multitudinuous=1, solar_gothic_period=1, codex=1),
    lessons=3,
    provides=memory.contradiction,
)


# Rapt in the King
#
# Detailed accounts of secret bacchanals and ecstatic dances observed in necropolises and graveyards in Southern Europe, in Egypt and in Anatolia. The author is a self-confessed ghoul, an eater of buried flesh: he claims to have witnessed the dances while at his feasting.
# ---
# I'm Reading...
#
# The dances draw from the traditions of the Mysteries, of the cults of Isis and of Cybele, but include both symbolic and literal flayings, and the human heart is always central in the rites. The author punctuates his accounts with queasily sensuous descriptions of his own interrupted feasts.
# ---
# I've Read...
#
# 'At these greater Feasts a Black Pig is always crowned as King before its Slaying. On this Occasion, its Heart was weighed in the Balance against a Knot of Feathers, and its Skin became a Cape for the Officiant. Its Flesh was left for the Crows, but I must confess my Interest was not in its Carcass but in the Perfumed Flesh of the Milliner laid fresh in the Earth.'
rapt_in_the_king = card_type("rapt_in_the_king",
    attributes(tally_price=3, mystery_heart=8, readable=1, thing=1, subject_drums_and_dances=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.earth_sign,
)


# Seven Faces of Icarus
#
# In the early 1530s, the last Abbot of St Brandan's, called 'Roaring Richard', set down his conversations with the illiterate local cunning-man, Red William.
# ---
# I'm Reading...
#
# Red William describes the seven forms in which he 'goes about and under the world' - viper, cat, fox, eagle, dove, boar and crow. Abbot Richard ingeniously fits these all into a framework of Solar belief…
# ---
# I've Read...
#
# According to Abbot Richard, each of Red William's forms is closer to the Sun, and is increasingly 'winged with virtue'. Richard draws an analogy with the waxen wings of Icarus: hypocrisy and false virtue will melt before the Sun's heat, and so sincerity and untrammelled expression of the Self are the utmost piety. It's worth noting that only a year or two after Richard wrote this book, John Tregonwell was so appalled by the debaucheries of the monks of St Brandan's that he recommended the monastery's immediate dissolution.
seven_faces_of_icarus = card_type("seven_faces_of_icarus",
    attributes(tally_price=3, mystery_sky=4, readable=1, thing=1, subject_furs_and_feathers=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.fear,
)


# Seven Shards
#
# The Lionsmith, one of the two great Hours of struggle, broke his sword into seven shards. Natalia Brulleau, fifth Librarian of Hush House, describes the nature of each of those shards, allegorically and otherwise.
# ---
# I'm Reading...
#
# 'The Third Shard then has been identified with 'the cry of pain'. The Lionsmith is a stoic Hour, but we must assume that in the Sundering Moment even he might have been unable to restrain his distress. Now the sound of tin under pressure we call the 'tin cry' - a reason, perhaps, for the further identification of the Third Shard as the 'Shard Royal'...
# ---
# I've Read...
#
# 'The Seventh Shard we call, informally, the Invincible Audacity, which is struck from the Winning Move as the Winning Move is struck from a memory - with the application of sufficient Edge.'
seven_shards = card_type("seven_shards",
    attributes(tally_price=2, mystery_edge=10, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, curia_period=1),
    lessons=2,
    provides=memory.hindsight,
)


# Singlefoot Songs
#
# Father Stanislav John Schaller, priest and diplomat, writes of his time on the slopes of Huashan - 'near to the Grove of the Green Immortals, but never too near.'
# ---
# I'm Reading...
#
# Schaller's relations with the Grove are cautious - it's a Library of the Tree, but under the hand of the Hour named Applebright. In time, however, Schaller comes to be more sympathetic to the Applebright, which he suggests 'causes harm only when so invited.'
# ---
# I've Read...
#
# The 'Singlefoots' of the title are one-horned, one-footed hill-things with sweet but powerful voices - powerful enough to 'open the mountain.' The Singlefoots sometimes trample pilgrims; sometimes heal them; sometimes coerce them to 'enter the mountain' and become Singlefoots. Schaller explains that when he found this last becoming too tempting, he decided to return to his homeland.
singlefoot_songs = card_type("singlefoot_songs",
    attributes(tally_price=1, mystery_scale=6, readable=1, thing=1, subject_hill_and_hollow=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.savage_hymn,
)


# Skin of Silver
#
# The epic of the final battle of the Lionsmith with the remnant-giant Antaios.
# ---
# I'm Reading...
#
# As always, the Lionsmith drew his strength from metal, and Antaios from stone… but the Lionsmith began to suspect also that this time, Antaios was drawing power from the Moon.
# ---
# I've Read...
#
# The Lionsmith beseeches the Three for their assistance, and the Meniscate favours him with a skin of silver, like water, like mercury, so he too can drink power from the Moon; for, she whispers, he too will one day be drawn into a perfect balance.
skin_of_silver = card_type("skin_of_silver",
    attributes(tally_price=5, mystery_edge=10, written_in_deep_mandaic=1, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, dawn_period=1),
    lessons=2,
    provides=memory.fear,
)


# Snare of the Tree: Collected Proverbs of Aunt Mopsy
#
# 'Once in the Wood, we call a visit. Twice in the Wood, we call a journey. Thrice, we call coming home.'
# ---
# I'm Reading...
#
# 'Every timber has its knots, the straight and the crooked both. Every weave is more absence than thread. You can't keep Nowhere out any more than you can keep Somewhere in…'
# ---
# I've Read...
#
# 'When the cuckoo learns the nightingale's song, our sleep is sweeter than honey.'
snare_of_the_tree_collected_proverbs_of_aunt_mopsy = card_type("snare_of_the_tree_collected_proverbs_of_aunt_mopsy",
    attributes(tally_price=1, mystery_grail=8, readable=1, thing=1, subject_applebright_euphonies=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# Stolen Histories
#
# The agitator and pamphleteer Alexander Sparrow inveighs against the 'monstrous Serpents, Thieves of History.'
# ---
# I'm Reading...
#
# Sparrow acknowledges five Histories, insists the Third History may be 'overrun by Coils', warns the Fifth History is already lost.
# ---
# I've Read...
#
# Sparrow, with his usual paranoia, appears to be conflating the horror of the Worm Wars and the Great Writhing with the activities of the Great Hooded Princes. Still, he draws thought-provoking comparisons between the Princes - normally conceived as exotic Knock-long - and the widely feared Worms.
stolen_histories = card_type("stolen_histories",
    attributes(tally_price=3, mystery_scale=4, readable=1, thing=1, codex=1, subject_coil_and_chasm=1, baronial_period=1),
    lessons=1,
    provides=memory.fear,
)


# Sunrise Awakenings
#
# An uncharacteristically poignant meditation by the Edge-long Twrog of Meirionnydd, who later came to Hush House under a variety of other names, often in search of some sort of fight.
# ---
# I'm Reading...
#
# 'If Light were not silent, it would be Music. If Music were visible, it would be Light…'
# ---
# I've Read...
#
# Each day's light, Twrog suggests, is faintly touched by the light of every past day; so in the light of every present day, we may begin to understand something of days to come. At least, this appears to be his conclusion, but he stops in mid-sentence, apparently having lost patience with the act of writing, or possibly been ambushed.
sunrise_awakenings = card_type("sunrise_awakenings",
    attributes(tally_price=3, mystery_lantern=4, readable=1, thing=1, subject_auroral_contemplations=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.revelation,
)


# Sunset Celia and the End of Days
#
# An Obliviate adept identified only as 'the Emiliano' rants desperately about the part Sunset Celia played in the Intercalate, as 'the proxy of the Sun'. 
# ---
# I'm Reading...
#
# 'Now she walks behind the Watchman, but did she always? She has many of the characteristics of a Maid-in-the-Mirror, after all. In older texts she has been called Caelia the Elagabaline. Perhaps she was his daughter? Perhaps Tryphon's sister? Perhaps, like the Watchman himself, she is like a shadow cast by two candles.'
# ---
# I've Read...
#
# 'What must be revealed, will be revealed. Our Order's root is tainted, but its branches flourish beneath the shelter of the Watchman's greater Tree. I shall invoke its rites before the Chancel, the Cruciate, and the Rode. I shall write a final History. Or another shall write it for me.'
sunset_celia_and_the_end_of_days = card_type("sunset_celia_and_the_end_of_days",
    attributes(tally_price=2, mystery_sky=10, readable=1, thing=1, subject_sacra_limiae=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# Sunset Passages
#
# A miscellany of the funerary prayers, ceremonies and hymns of the Church of the Unconquered Sun, which was ascendant in the Third and Fourth Histories. It schismed during the Intercalate, when the Sun was divided, and has not survived as a significant force.
# ---
# I'm Reading...
#
# The Church revered the Sun-in-Splendour before it was divided - but even while it was still whole, its later selves were recognised as its Names. The Madrugad, of course, presided over death and the passage into the House.
# ---
# I've Read...
#
# The White Ceremony was spoken to honour the Madrugad, at funerals held in the chilly space before dawn. The text cautions that all blades should remain sheathed while the Ceremony is spoken, 'lest the corpse be not quiet.'
sunset_passages = card_type("sunset_passages",
    attributes(tally_price=5, mystery_forge=4, written_in_latin=1, readable=1, thing=1, subject_sacra_solis_invicti=1, codex=1, dawn_period=1),
    lessons=1,
    provides=memory.revelation,
)


# The Account of Kanishk at the Spider's Door
#
# Lok Kahuli, Kanishk's victim and lover, wrote this account, perhaps posthumously.
# ---
# I'm Reading...
#
# Kanishk sought to become a Name. In pursuit of that end, he made Lok Kahuli the vessel of his appetites, promising Lok that they would ascend together. At the Spider's Door, he betrayed his lover...
# ---
# I've Read...
#
# The Chiliarch listened to it happen and then forced Kanishk into his service. The Chiliarch cannot be denied. Lok Kahuli remained to write this work, and to describe the outer magics of struggle and contest.
the_account_of_kanishk_at_the_spiders_door = card_type("the_account_of_kanishk_at_the_spiders_door",
    attributes(tally_price=5, written_in_aramaic=1, mystery_moon=6, readable=1, thing=1, dawn_period=1, subject_sharps=1, codex=1),
    lessons=1,
    provides=memory.a_stolen_secret,
)


# The Alloy of the White Rose
#
# An account by 'Mistress White-Flower' of the alchemical techniques favoured by the House of York, also identified with the 'Dawn Road'. These techniques failed to bring them victory in the War of the Roads, but are 'not to be discounted'.
# ---
# I'm Reading...
#
# The author asserts proudly that the Dawn Road ends in the Second Dawn; and hints darkly that the downfall of the House of York was 'Grail-sabotage'.
# ---
# I've Read...
#
# 'Mistress White-Flower' urges a 'History of Uzult', where the Second Dawn may come to pass. She identifies Xanthotic Essence as Uzult's predecessor; she explains that with sufficient Lantern, Bitterblack Salts can be Purified to Xanthotic Essence, and Iotic Essence can be Exalted to Xanthotic Essence.
the_alloy_of_the_white_rose = card_type("the_alloy_of_the_white_rose",
    attributes(tally_price=4, mystery_lantern=10, readable=1, thing=1, solar_gothic_period=1, subject_purifications_and_exaltations=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# The Amalgam of the Red Rose
#
# An account by 'Mistress Red-Flower' of the alchemical operations favoured by the House of Lancaster, also identified with the 'Sunset Road'. These operations ultimately led to their victory in the War of the Roads, but are described as 'now debased'.
# ---
# I'm Reading...
#
# The generals of the Houses of Lancaster and York are described as 'brother-enemies' - a term more usually associated with the dyadic, invariably twinned Edge-long…
# ---
# I've Read...
#
# The author's conclusion is that in the absence of the operations of the Dawn Road, the operations of Sunset inevitably became unbalanced, debased, and ultimately enfeebled. The combination of the two is described, tantalisingly, as 'the Forge's True Alloy'.
the_amalgam_of_the_red_rose = card_type("the_amalgam_of_the_red_rose",
    attributes(tally_price=2, mystery_forge=8, readable=1, thing=1, curia_period=1, codex=1, subject_meniscate_reflections=1),
    lessons=2,
    provides=memory.foresight,
)


# The Ascendant
#
# The Edge-long Dardesh boasts of her victories over her brother-enemy Tareg in the days of the Shadowless Empire.
# ---
# I'm Reading...
#
# 'Sweeter than wine, than nectar is the blood of my brother. We have raised up armies one against another, we have sated the Blackbone with the sinking of our ships…'
# ---
# I've Read...
#
# Dardesh's boasting at length turns melancholy. An Edge-long is half a dyad; she may not defeat her hated brother-enemy without ending herself. She doesn't even want to; but she is aware, to her frustration, that she is 'a piece on the board, an axle on the ox-cart' - an essential part of the eternal engine of contention which the Lionsmith and Colonel use to sustain the world.
the_ascendant = card_type("the_ascendant",
    attributes(tally_price=4, mystery_edge=10, written_in_hyksos=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_edicts_martial=1),
    lessons=2,
    provides=memory.contradiction,
)


# The Barrowchild's Elegies
#
# The Barrowchild, a Gaulish adept who won a place in the ranks of the Ordo Limiae, enumerates the 'great shadows' laid to rest in tombs of power, and discusses their various conditions.
# ---
# I'm Reading...
#
# The Barrowchild identifies numerous modes that are neither true death nor true life: the 'vitrification of the heart'; 'the corrupt light of the Wood'; 'chor-stasis'; 'the wandering of the fet'…
# ---
# I've Read...
#
# The Barrowchild warns particularly of the 'avidity of trist', where a remnant-shadow's longing for change survives its sense of self and even devours its wist. That longing may draw the curious into the tomb, where the remnant-shadow changes so that it cannot be distinguished from its visitor - or that the reverse becomes true - and that it is never again possible to say whether it is the shadow or the visitor that exits the tomb.
the_barrowchilds_elegies = card_type("the_barrowchilds_elegies",
    attributes(tally_price=3, written_in_latin=1, mystery_winter=10, readable=1, thing=1, baronial_period=1, codex=1, subject_rhyme_and_remembrance=1),
    lessons=2,
    provides=memory.regret,
)


# The Bee-Keeper's Ends
#
# Dialogues with bees and uses for honey, as erratically recorded by Ricardo Milagro, gardener of Hush House in Musgrave's time.
# ---
# I'm Reading...
#
# Milagro spends an entire chapter on his hatred of wasps, which he describes as 'the Vile Pretenders'.
# ---
# I've Read...
#
# Milagro claims that bees retain many traditions passed down from earlier and greater branches of their species, but that they are fiercely jealous of these traditions being passed to lesser insects, and insist above all on an oath of secrecy. Tragically, therefore, he is unable to describe these more substantial and powerful traditions.
the_bee_keepers_ends = card_type("the_bee_keepers_ends",
    attributes(tally_price=3, mystery_nectar=8, readable=1, thing=1, subject_insects_and_nectars=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.impulse,
)


# The Berrybook
#
# Thirza Blake, seventh librarian of Hush House, talks about fruit. For no other apparent reason but that it was the kind of thing she did, she talks about fruit in the woven language Killasimi.
# ---
# I'm Reading...
#
# 'Who was it once said, fruit is the womb of a plant? It was me. Take a few moments to think on that enripened wisdom. I shall leave a blank space for your moments, here in this page.'
# ---
# I've Read...
#
# 'Nectar, children mine - cast my words into a sufficiency of Nectar and watch the pyrus pyrissimus burst from wood. Gather more Nectar! Wring it from the trees and earth! And our pyrissimus gushes forth the Sacrament! You will thank me.'
the_berrybook = card_type("the_berrybook",
    attributes(tally_price=2, written_in_killasimi=1, mystery_nectar=8, readable=1, thing=1, subject_leaves_and_thorns=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Black Book of Brittany
#
# A volume of ink-lore gifted to St Brandan's by Brian of Brittany, who was made Earl of Cornwall after the Norman Conquest.
# ---
# I'm Reading...
#
# ''The Black Flower lies heavy, but the roots of the Watchman's Tree run deep, and they may not be hidden forever…'
# ---
# I've Read...
#
# The Black Flower, spoken of as a doom or geas, can be held at bay with the Last Ink of Power - brewed from 'the Pale Mixture' in the presence of sufficient Winter with the arts of Containment.
the_black_book_of_brittany = card_type("the_black_book_of_brittany",
    attributes(tally_price=4, mystery_moon=12, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_inks_of_containment=1),
    lessons=2,
    provides=memory.bittersweet_certainty,
)


# The Book of Cinders
#
# Ostensibly an eighteenth-century fireworks manual, but with some exotic ingredient choices and a substantial section on 'teframancy', divination from ashes.
# ---
# I'm Reading...
#
# The text takes as its theme the motto of the Society of the Noble Endeavour, ALITUR PROPRIIS IGNIS CINERIBUS - 'a fire by its own ashes is nourished', and uses this as a way into discussions of alchemical techniques…
# ---
# I've Read...
#
# A surprisingly casual final section mentions that iotic essence, 'the root of the Great and Exultant Ink Orpimental', can be refined with enough Forge from a variety of liquids.
the_book_of_cinders = card_type("the_book_of_cinders",
    attributes(tally_price=2, mystery_forge=6, readable=1, thing=1, subject_pyroglyphics=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.foresight,
)


# The Book of Dissolution
#
# Alexander Probst recovered a copy of this work from a mountain-temple in Persia. Other copies surface now and then, usually seared on rock.
# ---
# I'm Reading...
#
# The Book consists mostly of prayers to the Unburnt God, the Forge of Days which consumes and transforms. It suggests the Forge's power arises partly from its nature, and partly from its tools.
# ---
# I've Read...
#
# The Book describes an earlier House of the Sun, whose doors and ways were different. It praises the Forge of Days for opening the ways into the house, and for transforming that which was to that which is, despite the screams of stone...
the_book_of_dissolution = card_type("the_book_of_dissolution",
    attributes(tally_price=5, mystery_forge=12, written_in_deep_mandaic=1, readable=1, thing=1, subject_transformations_and_liberations=1, codex=1, dawn_period=1),
    lessons=2,
    provides=memory.foresight,
)


# The Book of Masks
#
# Athena Vana's work on the rogue Hour called the Vagabond, who is also known as the Laughingthrush, the Centipede, the Pilgrim, and by many other names - or as Vana has it, 'masks'.
# ---
# I'm Reading...
#
# The Mask of the Laughingthrush, says Athena Vana, had a great friendship with the Sun-in-Splendour, the highmost Hour of the Mansus (now divided and departed). The Mask of the Sight-Thief painted the river in the Mansus. The Mask of the Vagabond was forbidden the Mansus, not for what she had done, but for what would occur...
# ---
# I've Read...
#
# The Mask of the Centipede recalled her birth-place, Miah, which had punished her for creeping into the temple precinct. This Mask cursed Miah to drink only dust and to be remembered only by the wind - 'for not beneath any Mask does she forgive, and the Centipede's hunger is not to be forgotten.'
the_book_of_masks = card_type("the_book_of_masks",
    attributes(tally_price=5, mystery_moth=14, written_in_phrygian=1, readable=1, thing=1, dawn_period=1, subject_weaving_and_knotworking=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# The Book of the Centipede
#
# In the mid 1860s one 'Madam Yi' presented an entertainment based, she claimed, on this book.
# ---
# I'm Reading...
#
# 'The Centipede always found her way into the dark places. When she was punished for it, she reacted badly, in the Mansus as in Miah.'
# ---
# I've Read...
#
# 'The River runs through the sands out of myth and into legend. The Painted River runs the other way. One is barred to the Centipede now, but she finds ways back in, sometimes.'
the_book_of_the_centipede = card_type("the_book_of_the_centipede",
    attributes(tally_price=2, written_in_greek=1, mystery_rose=6, readable=1, thing=1, subject_sand_stories=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.intuition,
)


# The Book of the Extinguished Heart
#
# In the days of the Shadowless Kings, Ennis Lazali was executed for prophesying the Division of the Sun. If any of his captors grew Long, they probably feel rather abashed now.
# ---
# I'm Reading...
#
# Lazali indicates that the Sun will be divided in the Malleary, by the Forge of Days, armed with the love in her heart.
# ---
# I've Read...
#
# 'Love will not be the cause of the Sun's death, but rather envy. Envy will not be the cause of the Sun's death, but rather thirst. Thirst shall not be the cause of his death, but curiosity. Curiosity shall not be his end; rather will it be love.'
the_book_of_the_extinguished_heart = card_type("the_book_of_the_extinguished_heart",
    attributes(tally_price=5, mystery_heart=16, written_in_deep_mandaic=1, readable=1, thing=1, dawn_period=1, subject_quenchings_and_quellings=1, codex=1),
    lessons=3,
    provides=memory.bittersweet_certainty,
)


# The Book of the White Cat
#
# Stories brought by a blind white cat to Penelope of Gordion.
# ---
# I'm Reading...
#
# The aviform Hours - the Crow, the Laughingthrush, the Dove, and the twin Kites - have been known to meet in the mountains north of Gordion, at a place called the Roost, to exchange gossip. Penelope indicates that mortals who hear their words directly are obliterated, but claims that her cat goes unnoticed and returns to her with rumours from the Hours' meetings.
# ---
# I've Read...
#
# The stories that Penelope claims as Hour-gossip are fragmentary and confusing: accounts of contests where Hope and Dread and the Shadowless Empire are used as game-pieces, agendas of ruin and remembrance from no known history. The most interesting element is the protective incantation she records at the end of the book, after she worries that the Hours might in fact learn of her spying.
the_book_of_the_white_cat = card_type("the_book_of_the_white_cat",
    attributes(tally_price=5, written_in_phrygian=1, mystery_sky=16, readable=1, thing=1, subject_watchmans_paradoxes=1, dawn_period=1, codex=1),
    lessons=3,
    provides=memory.revelation,
)


# The Book of Thrones
#
# A legend of the Shadowless Empire, transcribed by Alexander Peterhans from annals at a secret shrine in Anatolia.
# ---
# I'm Reading...
#
# In 'the first and greatest history', a subject of the Shadowless Empire of Persia travels to the West, to the kingdom of the Perseids. There he becomes a protégé of the tutelary Perseid deity, the Scarred Man who lives in the dark. He returns after seven years to put his skills at the service of the Shadowless Empire, becoming their Golden General...
# ---
# I've Read...
#
# After many years of peace, the heirs of the Perseids move against the King of Kings and the Shadowless Empire. The Golden General will not take arms against the blood of his mentor, until the King of Kings whispers 'a great secret of betrayal' in his ear. He breaks his sword, forswears his oath to both the Empire and the Scarred Man, and enters 'the Temple behind the World', leaving his life behind.
the_book_of_thrones = card_type("the_book_of_thrones",
    attributes(tally_price=2, mystery_edge=12, written_in_phrygian=1, readable=1, thing=1, subject_auroral_contemplations=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.contradiction,
)


# The Burning Woman
#
# A transcription of the play by Menander the Victor, possibly the dramatist of that name, into Phrygian, with commentaries.
# ---
# I'm Reading...
#
# The play describes a pilgrimage of smiths and adepts following the trail of the Burning Woman, who has appeared in all their dreams and given each a Wound and a Word.
# ---
# I've Read...
#
# The smiths and adepts give up on finding the Burning Woman, and resolve to build their own kingdom, 'where our strength will be sufficient to shatter the world.'
the_burning_woman = card_type("the_burning_woman",
    attributes(tally_price=5, mystery_forge=14, written_in_phrygian=1, readable=1, thing=1, subject_transformations_and_liberations=1, codex=1, dawn_period=1),
    lessons=2,
    provides=memory.foresight,
)


# The Carbonek Schism
#
# The order of Obliviates, on the brink of schism, assembles in a Bounds-house identified only as 'Carbonek', after the Fisher-King's castle of legend. There the Know and the Long of the order debate their long policy of non-involvement in 'matters of Feather and Scale'.
# ---
# I'm Reading...
#
# One of their number - the one recording their debates - describes how in desperation he has found some kind of solution in a 'volume of transcendent heresy', but dares not pursue it alone. He convinces a handful of other Obliviates to depart Carbonek with him, while the others cross the sea to Port Noon.
# ---
# I've Read...
#
# In the last few pages, the author reveals himself as the Know-adept Ambrose Westcott, writing in an uncharacteristically serious mode. He informs any who should find this work that he has returned the book he spoke of to 'Abbot Geffrey's Secret', where it can be retrieved with certain invocations of the Sacra Limiae. He hopes that one who has read this far, and understood this much, will find a History to determine.
the_carbonek_schism = card_type("the_carbonek_schism",
    attributes(tally_price=3, mystery_moth=6, written_in_sabazine=1, readable=1, thing=1, subject_sacra_limiae=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.hindsight,
)


# The Carmine Petal: Revised
#
# An apparently theoretical project proposed by 'Lionel' of the Society of the Noble Endeavour which might permit the imprisonment of a renegade Forge-Name. A very heavily revised edition of an earlier and even more controversial work.
# ---
# I'm Reading...
#
# The book was evidently revised some time after the Wars of the Roads had ended, but even then this kind of discussion would have been politically difficult.
# ---
# I've Read...
#
# 'Lionel' suggests that the Disciplines of Scar and Hammer together would be necessary to create such a prison - but that either on its own would serve to release its occupant.
the_carmine_petal_revised = card_type("the_carmine_petal_revised",
    attributes(tally_price=3, mystery_forge=12, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.foresight,
)


# The Carmine Petal: Unexpurgated
#
# A project proposed by 'Lionel' of the Society of the Noble Endeavour by which, he claims, he succeeded in creating a sanctuary for a fugitive Forge-Name. The unexpurgated version.
# ---
# I'm Reading...
#
# At the time this book was written, a 'fugitive' Forge-Name would have been guilty of heresy, treason, or both.
# ---
# I've Read...
#
# 'Lionel' suggests that the 'house of iron and fire' so created would include 'hollows of air and night', which would serve as a final hiding-place if the larger sanctuary were uncovered - though, he says, they could be easily revealed with invocations of the Disciplines either of Scar or of Hammer.
the_carmine_petal_unexpurgated = card_type("the_carmine_petal_unexpurgated",
    attributes(tally_price=3, mystery_forge=18, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, baronial_period=1),
    lessons=3,
    provides=memory.foresight,
)


# The Ceaseless Tantra
#
# The avant-garde choreographer Nicholas Keirle supposedly incorporated this Tantra into his menacing ballets.
# ---
# I'm Reading...
#
# The Ceaseless Tantra is devoted mostly to warnings about the lively creatures called Percussigants, but concludes with a chant which can be used to summon them. It observes that Percussigants can be taught any dance, but they prefer only one.
# ---
# I've Read...
#
# 'That which does not cease, is not ceased.'
the_ceaseless_tantra = card_type("the_ceaseless_tantra",
    attributes(tally_price=2, mystery_heart=6, written_in_sanskrit=1, readable=1, thing=1, subject_weaving_and_knotworking=1, codex=1, curia_period=1),
    lessons=1,
    provides=memory.impulse,
)


# The Chandler's Wish
#
# Formulae and instructions invoking Moth, Lantern and - exceptionally, paradoxically - the liminal and theoretical Hour called the Chandler. The author is anonymous, admitting only that they are 'one who is not yet nameless.'
# ---
# I'm Reading...
#
# The author makes a passionate argument that the Hour named Chandler is in fact the oldest, even though he does not exist, because he is - supposedly - the culminating event of a plan that precedes even Grail and Moth.
# ---
# I've Read...
#
# 'Where the Chandler has passed, the understandings of the Colonel and the Lionsmith will wrench open truth. Where the Chandler will pass, Moth will pass before him.'
the_chandlers_wish = card_type("the_chandlers_wish",
    attributes(tally_price=2, mystery_lantern=12, readable=1, thing=1, curia_period=1, subject_inks_of_revelation=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# The Concursum Diaries
#
# The diaries of the explorer and murderer Lars Westergren. He's unhelpfully translated them into Phrygian, for privacy.
# ---
# I'm Reading...
#
# 'There are map-legends, there are maps of legends, and there are legends of maps. Aspects of the Mansus subsist in all of these, in much the same way that you find water in a swamp and in a cup and in the sky.'
# ---
# I've Read...
#
# Westergren describes a series of expeditions into the Mansus. He focuses on the details of the experience - the colours, the vistas, the textures - rather than the practicalities. He does warn that the Mansus changes each year, although he assures the reader that the Doors have been the same. 'Doors may close, but they never disappear. At least not while there have been mortals in the Mansus. We're like mice.'
the_concursum_diaries = card_type("the_concursum_diaries",
    attributes(tally_price=5, written_in_phrygian=1, mystery_rose=8, readable=1, thing=1, dawn_period=1, subject_path_and_pilgrim=1, codex=1),
    lessons=2,
    provides=memory.intuition,
)


# The Crossing to Noon
#
# The mystic Garcia Sauri gives a picaresque account of the adventures of Franklin Bancroft, 'Prince of Wines', and Eva Dewulf, 'the Pale Lady', on their way to the hidden island of Noon.
# ---
# I'm Reading...
#
# 'For a long long time the Blackbone pondered her next move, until the Moon dared to peep from behind a cloud, and the Prince completed the composition of his third sestina. But the Lady met the blind gaze of its open pores, waiting for the tide…'
# ---
# I've Read...
#
# Garcia Sauri acknowledges in an epilogue that it is widely known that Eva in fact tragically drowned herself - and her twin infant grand-daughters - without ever making such a journey. But he adds contemptuously: 'it is also widely known that the City Unbuilt will so remain, that only one History is ever written, and that Janus is a Mansus-prank.'
the_crossing_to_noon = card_type("the_crossing_to_noon",
    attributes(tally_price=2, written_in_latin=1, mystery_moon=8, readable=1, thing=1, subject_sea_stories=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.salt,
)


# The Deaths of the Moon
#
# A Haustorial tract on various forms of survival after death.
# ---
# I'm Reading...
#
# When the heart no longer beats, the Grail may keep the spirit in the body, and an appetite is indicated to sustain. (Alukites are the best-known, but not the only, of this nature). This is the waning-moon mode…
# ---
# I've Read...
#
# The full-moon mode is the intensification of one element of the soul to the point where ordinary sustension is unstable. Our Protector, the Generous of Hosts, began of this nature, and its generosity remains ungentle. It is possible for the body's health or the heart's chor to outpace the other elements, so that a static mode becomes impossible and growth proceeds in dramatic stages until balance remanifests...
the_deaths_of_the_moon = card_type("the_deaths_of_the_moon",
    attributes(tally_price=3, written_in_killasimi=1, mystery_moon=8, readable=1, thing=1, codex=1, subject_snow_stories=1, baronial_period=1),
    lessons=2,
    provides=memory.salt,
)


# The Debate of Seven Cups
#
# 'Distillations of Spirit' recorded by an alchemist who identifies himself in the foreword as 'But Sir Thomas Browne's Reflexion.'
# ---
# I'm Reading...
#
# 'Time is a pure Flame, and we live by an invisible Sun within us.'
# ---
# I've Read...
#
# 'Darkness and Light divide the Course of Time, and until that Course is Run, Eternity remains History's Bed-Fellow. Sorrow then is Sense's final Solvent, and even a Tear, should it fall enow, might destroy a Stone…'
the_debate_of_seven_cups = card_type("the_debate_of_seven_cups",
    attributes(tally_price=2, mystery_moth=10, readable=1, thing=1, curia_period=1, codex=1, subject_solutions_and_separations=1),
    lessons=2,
    provides=memory.impulse,
)


# The Deeds of the Scarred Captain
#
# Painstakingly assembled by the soldier of fortune and sometime remittance man, Pavel Shulga, during his years in Greece.
# ---
# I'm Reading...
#
# An account of the founding of Mycenae by a 'Scarred Captain' who first slew seven monsters to make the land safe.
# ---
# I've Read...
#
# As the Captain destroys each monster, a flood of blood rises higher, until at last a priestess drowns and is reborn as a serpent-goddess. She blesses the Captain, and he departs for the 'House above the Forest', leaving Mycenae to reign supreme after the flood of blood subsides.
the_deeds_of_the_scarred_captain = card_type("the_deeds_of_the_scarred_captain",
    attributes(tally_price=4, mystery_edge=12, written_in_greek=1, readable=1, thing=1, solar_gothic_period=1, subject_sharps=1, codex=1),
    lessons=2,
    provides=memory.fear,
)


# The Devoured Tantra
#
# The diplomat-priest Stanislav John Schaller transcribed this from the library of a Red Long, but his manuscript remains in a private collection in Kerisham.
# ---
# I'm Reading...
#
# The Devoured Tantra warns of the uses and dangers of appetite, but devotes an entire passage to the 'star-limbed hunger-bringers', who it describes with obvious affection.
# ---
# I've Read...
#
# 'A million blazing fires in the belly engulf what has been swallowed by the multiform mouths.'
the_devoured_tantra = card_type("the_devoured_tantra",
    attributes(tally_price=2, mystery_grail=6, written_in_sanskrit=1, readable=1, thing=1, subject_applebright_euphonies=1, codex=1, curia_period=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# The Dream of the Conspiracy of the Lower Skies
#
# The disgraced oracle Damaon Azenaten sifts through the tall tales of Penelope of Gordion, the work of the court poet Kalle and the forbidden fragments of the work of the adept Arrettrez, identifying common themes.
# ---
# I'm Reading...
#
# Damaon insists that the Hours, far more than mortals, are subject to their passions - to hatred, and even to love. 'The seasons of famine and plenty, the turn of the Earth, the transformations of the furnace - all these are only the results of the enactment of the lesser passions of the Hours.'
# ---
# I've Read...
#
# Damaon suggests that the Hours have constrained their rivalry to avoid a war within the House of the Sun. He identifies the 'Fear of the Crime of the Sky' as the reason that Hours do not satisfy other passions. He speculates on the horrifying possibilty of Hours turned alukite. 'What then would they devour?'
the_dream_of_the_conspiracy_of_the_lower_skies = card_type("the_dream_of_the_conspiracy_of_the_lower_skies",
    attributes(tally_price=5, mystery_grail=16, written_in_phrygian=1, readable=1, thing=1, dawn_period=1, codex=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=3,
    provides=memory.gossip,
)


# The Elations of Limentinus
#
# The second volume of Abbot Geffrey's hypothetical theological debates in the Socratic mode.
# ---
# I'm Reading...
#
# 'If Janus were an Hour, Limentinus might be counted among his Names, but Janus has never passed that threshold, and so Limentinus is not…'
# ---
# I've Read...
#
# Geffrey discusses 'the signs upon the Threshold', drawing comparisons between the duties of guest and host, and the status accorded to Hours and other powers who dwell in, are permitted in, or are forbidden access to the House of the Sun. (It was of course Geffrey who later invited censure by giving sanctuary to Natan of Regensburg, in an age when the Jews were by royal order unwelcome anywhere in the kingdom.)
the_elations_of_limentinus = card_type("the_elations_of_limentinus",
    attributes(tally_price=4, mystery_knock=6, written_in_latin=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=1,
    provides=memory.pattern,
)


# The Encircling Tantra
#
# The explorer and entrepreneur T. Everett Duplantis once attempted to plunder the temple where this text was held. His fate is recorded in an appendix.
# ---
# I'm Reading...
#
# The Encircling Tantra speaks of the Serpent Gate, that hungry portal sometimes known as the Spider's Door, which is sacred to the Mother of Ants, through which the Great Hooded Princes pass.
# ---
# I've Read...
#
# The tantra includes an invocation but cautions, helpfully, that the invocation is of insufficient power to reach the Serpent Gate from the Hunter's Gate. 'A road which has no destination is itself a destination,' it adds helpfully.
the_encircling_tantra = card_type("the_encircling_tantra",
    attributes(tally_price=2, written_in_sanskrit=1, mystery_scale=6, readable=1, thing=1, subject_horns_and_ivories=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.fear,
)


# The Fallen Cross
#
# In which Julian Coseley, magus, immortal, occasional anarchist, argues that through language the Carapace Cross decayed to seed the lives of our ancestors.
# ---
# I'm Reading...
#
# 'Speech is a Wound; Silence is Silver. There is no Silver Door, nor can there be, even in the Moon's House…'
# ---
# I've Read...
#
# 'Without Language there can be no Wordes. Without Wordes there can be no Message. But only in Silence can there be no Error; and Lo, even in that beginning, in that First of Messages, an Error. Thus did we enter the House.'
the_fallen_cross = card_type("the_fallen_cross",
    attributes(tally_price=3, mystery_sky=6, readable=1, thing=1, subject_ouranoscopy=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.regret,
)


# The Five Letters On Memory
#
# Julian Coseley's epistolary treatise on 'matters memorial and mnemonic', addressed to his then-friend Claude Hersault, the mystic and antiquarian.
# ---
# I'm Reading...
#
# The book is partly a practical manual, expounding memory-palace-like techniques, and partly an exploration of 'Memory Rarefied' - modes in which sense or experience persist outside a mortal mind.
# ---
# I've Read...
#
# This is an early work, and by Coseley's standards it brims with optimism, even enthusiasm. If books, he suggests, are the memory that does not die, then 'perhaps with sufficient Endeavours, Memory's Murderer might be Contain'd'.
the_five_letters_on_memory = card_type("the_five_letters_on_memory",
    attributes(tally_price=2, mystery_winter=6, readable=1, thing=1, curia_period=1, codex=1, subject_rhyme_and_remembrance=1),
    lessons=1,
    provides=memory.regret,
)


# The Focus of Amber
#
# Omar, the Blaze, spent seven years manning a lighthouse in Tyre, in atonement for the extinguishing of a sacred flame. By the end of his stint, he was so terrified of fire that he could not stand to share a room with a candle. This work was written in partial penance.
# ---
# I'm Reading...
#
# Omar claims that the Hour called Watchman is both a god-who-was-flesh - an Hour who was mortal - and also a god-from-Light - an Hour who descended from the Glory - but adds, finally, that the Watchman's origin is triple, and that 'in essence, he is Amber.'
# ---
# I've Read...
#
# The Watchman, according to Omar, was once another Hour entirely, who ascended into the Glory to escape efforts by other Hours to send him to Nowhere. It may be that Omar's sense of persecution creeps into the narrative at this point: certainly it grows less coherent, and the last part is devoted to attempts to prove that eyes, eggs and the Sun are all in some sense conjunct.
the_focus_of_amber = card_type("the_focus_of_amber",
    attributes(tally_price=5, written_in_deep_mandaic=1, mystery_sky=16, readable=1, thing=1, dawn_period=1, subject_glaziery_and_lightsmithing=1, codex=1),
    lessons=3,
    provides=memory.revelation,
)


# The Geminiad i
#
# A fragile manuscript, illuminated with twinned shapes of sad and luminous beauty, and with all the phases of the moon. It might be as old as the seventh century, but the language - Fucine - is much older. The cover is tooled goatskin decorated with garnet.
# ---
# I'm Reading...
#
# These pages outline the nature, and the doctrines, of an Hour that weaves together the willing, an Hour that is sought beneath the moon and at the water's edge: the Sister-and-Witch. The language is wilful, knotty, poetic. It'll take some untangling.
# ---
# I've Read...
#
# The first volume of the Geminiad reminds us that the Sister-and-Witch has been known to manifest as the Witch-and-Sister - and that this face is always hungry, while the other face may heal. It implies connections between the Sister-and-Witch and the Hours of the upper Mansus - especially the lunar Hour called the Meniscate - but it is ambiguous on whether the Sister-and-Witch is a Mansus-Hour proper. And it speaks at length about the sadness of the two-who-are-one, the sadness that remains from their time as flesh.
the_geminiad_i = card_type("the_geminiad_i",
    attributes(tally_price=2, written_in_fucine=1, mystery_heart=10, readable=1, thing=1, subject_weaving_and_knotworking=1, codex=1, curia_period=1),
    lessons=2,
    provides=memory.solace,
)


# The Geminiad ii
#
# A fragile manuscript, illuminated with twinned shapes of sad and luminous beauty, and with all the phases of the moon. It might be as old as the seventh century, but the language - Fucine - is much older. The cover is a dark and exotic leather with a smooth, almost chitinous surface, decorated with jasper.
# ---
# I'm Reading...
#
# These pages outline the seven bloody natures of the 'Daughters of Lagiah' - those corrupted immortals who gave birth to children, in defiance of the Laws of the Upper Heaven; who devoured them, in obedience to the Hours' punishment; and who have been left outside the law...
# ---
# I've Read...
#
# The second volume of the Geminiad suggests that these seven corrupted immortals have been accorded the privileges of Names of the Witch-and-Sister - or perhaps the Sister-and-Witch. It reminds us that the Twins unite what is apart, and that the 'Crime of the Sky' is in some sense a supreme joining. And it speaks at length about the sadness of the seven, the sadness of mothers whose children are forever lost, and far worse than lost.
the_geminiad_ii = card_type("the_geminiad_ii",
    attributes(tally_price=2, written_in_fucine=1, mystery_grail=10, readable=1, thing=1, curia_period=1, codex=1, subject_pentiments_and_precursors=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Geminiad iii
#
# A fragile manuscript, illuminated with twinned shapes of sad and luminous beauty, and with all the phases of the moon. It might be as old as the seventh century, but the language - Fucine - is much older. Coral decorates its cover, and its page-edges are sharp enough to slash a throat.
# ---
# I'm Reading...
#
# These pages outline the nature, and the doctrines, of an Hour that demands the union of what has been separated, an Hour that is sought at the water's edge and beneath the moon: the Witch-and-Sister. The language is allusive, enigmatic, intricate. It'll take some untangling.
# ---
# I've Read...
#
# The third volume of the Geminiad reminds us that the Witch-and-Sister has been known to manifest as the Sister-and-Witch - and that this face may heal, while the other face is always hungry. It implies connections between the Witch-and-Sister and the Hours of the Wood - especially the secret-keeper called the Velvet - but it is ambiguous on whether the Witch-and-Sister is a Wood-hour proper. And it speaks at length about the sadness of the two-who-are-one, the sadness that remains from their time as flesh.
the_geminiad_iii = card_type("the_geminiad_iii",
    attributes(tally_price=2, written_in_fucine=1, mystery_moth=12, readable=1, thing=1, subject_resurgences_and_emergences=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.beguiling_melody,
)


# The Gospel of Zacchaeus
#
# An extremely heterodox account of the Nazarene Messiah and his works, describing his ascension to the Mansus through the opening of his body.
# ---
# I'm Reading...
#
# 'Seven were the wounds of His body, seven the doors of the House. Seven the lesser aspects of the Hours, and Knock the aspect above all, for the Mother of Ants is the Mother of Salvation.'
# ---
# I've Read...
#
# The book includes a description of a rite which can be used to raise a corpse to half-life, 'in memory of He who bled for the Wood'; but the marginalia claim that the Mother of Ants no longer permits use of this rite.
the_gospel_of_zacchaeus = card_type("the_gospel_of_zacchaeus",
    attributes(tally_price=4, written_in_greek=1, mystery_knock=8, readable=1, thing=1, solar_gothic_period=1, subject_horns_and_ivories=1, codex=1),
    lessons=2,
    provides=memory.a_stolen_secret,
)


# The Grand Passage of the Hours
#
# The Limian Burzghash's gazetteer of the patterns and rhythms of the Hours' progress through the Mansus, from Concursum to Malleary, Malleary to Wood…
# ---
# I'm Reading...
#
# 'Each century in the Mansus is a great feasting-hall. In each ninety-ninth year, the hall falls silent; the Elegiast sits alone at the feast.'
# ---
# I've Read...
#
# 'There are paths in the Mansus that only the Sun has walked. In the time of the Sun's Division, who will know them? When the Second Dawn comes, who will walk them?'
the_grand_passage_of_the_hours = card_type("the_grand_passage_of_the_hours",
    attributes(tally_price=5, mystery_knock=12, written_in_vak=1, readable=1, thing=1, subject_door_and_wall=1, dawn_period=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# The High Mysteries of the Innermost Chamber of our Church Solar
#
# The secret rites of the Church of the Unconquered Sun, which held power in at least two Histories.
# ---
# I'm Reading...
#
# The Church chiefly worshipped the Sun-in-Splendour, the original undivided sun; but this text also includes the devotions of its aspects as the chilly winter dawn and the departing sunset, as well as the Meniscate, the Sun's 'night-self'. Priests of the Church were all male, but rites are also included which allowed women to cross ceremonially to manhood.
# ---
# I've Read...
#
# The Church's highest rites were performed in the Concursum, the chamber at the Mansus' heart where the Hours were known to pass. These rites include salutations to non-solar Hours: the Grail, the Ring-Yew, the Horned Axe and the Thunderskin.
the_high_mysteries_of_the_innermost_chamber_of_our_church_solar = card_type("the_high_mysteries_of_the_innermost_chamber_of_our_church_solar",
    attributes(tally_price=4, written_in_fucine=1, mystery_lantern=14, readable=1, thing=1, solar_gothic_period=1, subject_sacra_solis_invicti=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# The High Traditions of the Noble Endeavour
#
# A blandly positive work on the Endeavour Club, published by the Endeavour Club. The Club was founded in 1862 but claims to draw from much older traditions.
# ---
# I'm Reading...
#
# Club members are assigned names out of noble myth - 'Jaufre', 'Roland', and, unexpectedly, 'Breadbeddel'. They claim to be heirs to the Leashed Flame, which gave the island of Britain such appalling power in some histories.
# ---
# I've Read...
#
# Their 'Endeavour' itself is a purifying fire which makes its fuel something more than human. This transformation, however, is no longer encouraged by the Club, and perhaps - the work is coy on this - no longer permitted.
the_high_traditions_of_the_noble_endeavour = card_type("the_high_traditions_of_the_noble_endeavour",
    attributes(tally_price=3, mystery_edge=6, written_in_latin=1, readable=1, thing=1, subject_disciplines_of_the_hammer=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.foresight,
)


# The Hissing Key
#
# An account of the ascent of the Hour called the Mother of Ants, by the Bosk-scholar Mek, of the Theban branch of the House of Lethe.
# ---
# I'm Reading...
#
# Mek is not sympathetic to the Mother of Ants, who he calls 'the Milk-Thief'. He reviles her for her part in the death of the Seven-Coils, which he presents as a treacherous conspiracy.
# ---
# I've Read...
#
# The Milk-Thief conspires with the Ligeian Echidna and the Hour-to-be called Chiliarch (now more generally rendered as 'Colonel') to unseam the Seven-Coils with feathers and drown her in salt. The Colonel thus ascends to Hour status; the jealous Milk-Thief, once the Colonel's priestess, seduces Echidna into lending her the Hissing Key to enter the Mansus through the Savage Door, beginning her own ascent to Name and ultimately Hour.
the_hissing_key = card_type("the_hissing_key",
    attributes(tally_price=5, written_in_greek=1, mystery_scale=8, readable=1, thing=1, dawn_period=1, codex=1, subject_serpents_and_venoms=1),
    lessons=2,
    provides=memory.hindsight,
)


# The History of Inks
#
# A legendary grimoire of exotic ink-making lore. The cover and some of the pages, unfortunately are stained and crusted with something more like mucus than ink.
# ---
# I'm Reading...
#
# 'The encaustum Marakat is refined from the liquor named <i>leathy</i> in the presence of Nectar aspect. The Priestesses of the Knot have also learnt to brew Marakat in this wise - yet for the nature of their arts, their task may be easier…'
# ---
# I've Read...
#
# The History concludes with the admission that the encaustum named 'Orpiment Exultant' was once drawn from the veins of Forge-long. Thankfully, it seems, it can also be refined from Iotic Essence using the techniques in this book - or with 'transformations' and 'the jewel-science'.
the_history_of_inks = card_type("the_history_of_inks",
    attributes(tally_price=4, mystery_rose=14, readable=1, thing=1, solar_gothic_period=1, subject_inks_of_power=1, codex=1),
    lessons=2,
    provides=memory.intuition,
)


# The Humours of a Gentleman
#
# Samuel Savage's satirical comedy, on the intrigues of the ailing, but cunning John Sonne, his mistress Maevelin, her lover Leo, and the upstart Corvino.
# ---
# I'm Reading...
#
# By the end of the first act, Maevelin has revealed a secret door in the walls of the House to Leo, and Corvino has taken to consuming Worms.
# ---
# I've Read...
#
# The play is scabrous and occasionally hilarious. The characters are contrary and capricious. Many of the more resonant lines might well be formulae of power, disguised in plain sight.
the_humours_of_a_gentleman = card_type("the_humours_of_a_gentleman",
    attributes(tally_price=3, mystery_sky=4, readable=1, thing=1, subject_sky_stories=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.gossip,
)


# The Instruments of the Heart
#
# Sister Isabel, then Precentress of the Abbey-Church of St Brandan's, engages in dialogues with a Heart-long of a kind called 'duendrazon' that has taken partial possession of her body.
# ---
# I'm Reading...
#
# The duendrazon, like all its kind, usually dwells in the Mansus but can enter the physical world by manifesting as music, and take possession of a willing - or semi-willing - mortal who hears and loves that music… like Isabella.
# ---
# I've Read...
#
# Isabella records her dreams of the high Mansus, where she is accorded the duendrazon's status and titles. In return, the duendrazon enjoys what it calls 'caesura' - a welcome oblivion. 'Our mostly-blessing is that we may never cease - except <i>in caesurae</i>'. There is something more that Isabella refers to as the 'caesura magna', but she laments that her duendrazon will not tell her exactly what that might be.
the_instruments_of_the_heart = card_type("the_instruments_of_the_heart",
    attributes(tally_price=4, mystery_heart=10, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_drums_and_dances=1),
    lessons=2,
    provides=memory.cheerful_ditty,
)


# The Intimations of Skin
#
# Fiendishly complex, weirdly distorted illustrations of 'congress and anatomy' by the haunted visionary painter Niels Frederik Malskær.
# ---
# I'm Reading...
#
# Malskær illuminates the evolutions of the Names of the Grail with unfortunate clarity. It seems that a Lovely who consumes an Ivory becomes an Ivory. A Lovely who consumes a Thirstly becomes a Thirstly. A Lovely who consumes a Name of another Hour might take its place...
# ---
# I've Read...
#
# In the penultimate illustration, a Lovely grapples with a fungoid knot that can only be a Name of the Crowned Growth. The Lovely's mouth and other portals gape wide, and the Growth-Name is already partially engulfed - but it seems that Malskær couldn't bring himself to illustrate the result, and the final illustration is only a scrawled, bloated obscurity.
the_intimations_of_skin = card_type("the_intimations_of_skin",
    attributes(tally_price=1, mystery_grail=8, readable=1, thing=1, nocturnal_period=1, codex=1, subject_desires_and_dissolutions=1),
    lessons=2,
    provides=memory.beguiling_melody,
)


# The Iron Book
#
# A manual of the Ordo Limiae, an order of quasi-immortals who maintained a secret enclave at the source of the river Limia, in the Roman province of Hispania Gallaecia. This manual was compiled by one Melerai Yivni, who claims to have travelled to join the Ordo from 'the Crossroads of the Waters'.
# ---
# I'm Reading...
#
# Members of the Ordo took an oath, the Iron Chain, that required them to remain hidden from the world. This manual includes presumably long-obsolete addresses and pass-phrases that could have been used to find the Ordo's contact in the town of Iria.
# ---
# I've Read...
#
# The final part of the manual describes the punishments for Ordo members who break their oath of secrecy. This includes an invocation used to summon the spirit called King Crucible as an agent of vengeance. Yivni cautions that this must be a last resort when the oathbreaker would otherwise go unpunished: summoning King Crucible might draw the personal attention of the Forge of Days. (A marginal note suggests, in any case, that King Crucible, 'in a most transcendent Sulk of Sulks', no longer leaves the Mansus.)
the_iron_book = card_type("the_iron_book",
    attributes(tally_price=5, mystery_edge=8, written_in_fucine=1, readable=1, thing=1, dawn_period=1, subject_disciplines_of_the_hammer=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# The Ivory Book
#
# A manual of the Ordo Limiae, an order of quasi-immortals who maintained a secret enclave at the source of the river Limia, in the Roman province of Hispania Gallaecia. This manual was compiled by one Kurenai, who claims to have fled 'the tyranny of the Chrysanthemum Throne' to cross the world and join the Ordo.
# ---
# I'm Reading...
#
# Members of the Ordo took an oath, the Ivory Chain, not to have commerce with the Hours. Followed literally, this would be almost impossible for an adept, so the manual contains numerous clarifications, exceptions and processes of indulgence.
# ---
# I've Read...
#
# Kurenai describes the Order's burial rites, which include spells to ensure - in theory - that the souls of dead Long are not given to the Hours. The Hour called the Ivory Dove, who memorialises and commemorates, is to be invoked, in secret, in these rites, 'for with that Hour we have made an understanding'.
the_ivory_book = card_type("the_ivory_book",
    attributes(tally_price=5, written_in_fucine=1, mystery_winter=8, readable=1, thing=1, dawn_period=1, subject_quenchings_and_quellings=1, codex=1),
    lessons=2,
    provides=memory.regret,
)


# The Kerisham Portolan
#
# A beautifully illustrated and heavily annotated 'portolan' - a nautical atlas of ports and destinations.
# ---
# I'm Reading...
#
# It quickly becomes clear that many of its destinations no longer exist, or never existed in the traditional sense, but the annotations remain fascinating. The routes to Noon, the Long-sanctuary across the Western Sea, may remain viable…
# ---
# I've Read...
#
# Two pages have been gummed together. When teased apart they reveal a route to 'Ys Behind the Wave' - marked in red and gold inks with heavily underlined warnings. 'HERE THE FINAL CITY'. 'STRIKE THE HOURS.' 'LEST EARTH AND SKY BREAK OPEN…'
the_kerisham_portolan = card_type("the_kerisham_portolan",
    attributes(tally_price=2, mystery_moon=6, readable=1, thing=1, subject_sea_stories=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.gossip,
)


# The Known-Unknown Tantra
#
# Carlos Garcia Sauri, the ecstatic mystic of the Pyrenees, was known to recite this in three languages, though he had never visited the Subcontinent.
# ---
# I'm Reading...
#
# The Known-Unknown Tantra describes a journey to the White Door of the Mansus, beyond which speech ceases. It describes a mantra which can be used, at the right place and time, to achieve that door.
# ---
# I've Read...
#
# 'The light of a lantern can only ever reveal the space between the forest shadows.'
the_known_unknown_tantra = card_type("the_known_unknown_tantra",
    attributes(tally_price=2, mystery_lantern=6, written_in_sanskrit=1, readable=1, thing=1, subject_watchmans_paradoxes=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.revelation,
)


# The Larquebine Codex
#
# Christoph Larquebus claimed to have purchased two hand-written copies of the Codex from a family of witches on the shores of the Sea of Marmara. A third was 'given to the Sea'.
# ---
# I'm Reading...
#
# The Sister-and-Witch came from the West, where they were born in two wombs, one a princess, one a monster. Nevertheless they loved each other from birth, and met in secret 'to seek union'.
# ---
# I've Read...
#
# When the great drought came, the kings of that land tried to sacrifice the princess and the witch, so they sailed across the Sea. When despair took them, they flung themselves into the drowning waters... and so found the Painted River, where they entered the Mansus through the offices of the Red Grail. Nevertheless, the Codex ends with a condemnation of the Grail.
the_larquebine_codex = card_type("the_larquebine_codex",
    attributes(tally_price=5, mystery_moon=6, written_in_phrygian=1, readable=1, thing=1, subject_sea_stories=1, dawn_period=1, codex=1),
    lessons=1,
    provides=memory.salt,
)


# The Lion and the Glass
#
# An early work by Omar the Blaze, a novice or apprentice at the Labyrinth of Lions.
# ---
# I'm Reading...
#
# Omar describes his progress in mastering the Illumination techniques that rely on the 'Truths of Glass'.
# ---
# I've Read...
#
# Omar divulges a glassmaker's secret: that 'the Ichor Vitreous' can be filtered and enriched (with enough Lantern Aspect) to become the ink ashartine, which resists untruths…
the_lion_and_the_glass = card_type("the_lion_and_the_glass",
    attributes(tally_price=5, written_in_deep_mandaic=1, mystery_sky=12, readable=1, thing=1, dawn_period=1, subject_glaziery_and_lightsmithing=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# The Locksmith's Dream: a Light through the Keyhole
#
# The first volume of Teresa Galmier's examination of parallels in the mystic dreams of artisans.
# ---
# I'm Reading...
#
# The parallels in mystic dreams experienced by carpenters, masons and other artisans, and what they purport to reveal about the architecture of the world. Surprisingly mordant and even funny. No-one has ever explained why Galmier devoted herself to this quixotic exploration of artisan's dreams.
# ---
# I've Read...
#
# 'Time and again we hear of the Wood, which rises from the world's foundation. All trees reach for light. What does the Wood reach for? Is there a difference between light and Light? I think the key to dreams of the Wood might be one of these - the one that isn't exactly real.'
the_locksmiths_dream_a_light_through_the_keyhole = card_type("the_locksmiths_dream_a_light_through_the_keyhole",
    attributes(tally_price=1, mystery_lantern=4, readable=1, thing=1, nocturnal_period=1, subject_purifications_and_exaltations=1, codex=1),
    lessons=1,
    provides=memory.revelation,
)


# The Locksmith's Dream: Incursus
#
# The fifth (and final?) volume of Teresa Galmier's notorious work, which began as an examination of parallels in the mystic dreams of artisans but became an account of her own occult journey. This volume was apparently never published nor, allegedly, even written. Yet here it is.
# ---
# I'm Reading...
#
# 'The Law goes back all the way to Stone: the Keys cannot be held or owned. This had, I believe, the unexpected consequence that those outside the law may hold and own them. But even they cannot keep them. And of course a Key is no more physical than a spirit. But a spirit may be housed in a body, and I have touched a Key with my own hands.'
# ---
# I've Read...
#
# 'So the Ligeians hold the keys. I had thought the Ligeians only - 'only' - old and powerful transgressors of the Crime of the Sky. But I begin to understand that the Crime of the Sky is more even than it seems. And why a Twin, who unites what is not to be divided, might accept a Ligeian as her Name...'
the_locksmiths_dream_incursus = card_type("the_locksmiths_dream_incursus",
    attributes(tally_price=1, mystery_lantern=6, readable=1, thing=1, subject_glaziery_and_lightsmithing=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# The Locksmith's Dream: Portions and Proportions
#
# The second volume of Teresa Galmier's examination of parallels in the mystic dreams of artisans. The frontispiece has been slashed with a razor.
# ---
# I'm Reading...
#
# In this volume, Galmier records fewer dreams, and explicates more of her own elaborate theories. 'We see this again and again: what is below can't escape what is above.'
# ---
# I've Read...
#
# 'The finest artisans all dream of the White Door in the end. I'm no artisan, only a scholar. I think there's a Secret that all these artisans know, but I think that Secret is only half the story.'
the_locksmiths_dream_portions_and_proportions = card_type("the_locksmiths_dream_portions_and_proportions",
    attributes(tally_price=1, mystery_sky=4, readable=1, thing=1, subject_lockworks_and_clockworks=1, codex=1, nocturnal_period=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# The Locksmith's Dream: Stolen Reflections
#
# The fourth volume of Teresa Galmier's expansive work - no longer a discussion of the dreams of artisans, but a valuable survey of other works. The tone is calmer than that of 'Trespasses', but occasionally fearful, even paranoid. This volume was published in 1926 but almost immediately recalled and pulped by the publisher - at the request of the author or possibly the authorities, depending which story you believe. A few copies survive.
# ---
# I'm Reading...
#
# 'Janus is the Gatekeeper, the twin-god, the god that wounds, the presager of changes, the sun, the moon. So we identify him with the Watchman, the Twins, with the Mother, with the Forge, with the Meniscate and the Madrugad. He cannot be all these. Can he? The flamines knew the Church, knew the Dry Land, knew Elagabalus. Is he then synthesis? Or is he something else? In Gallaecia they called him Ianus Lamius, but the Obliviates are notorious for their slanders.'
# ---
# I've Read...
#
# 'Janus has, they say, not one face but two. To which I reply: why only one? Why only two? Hersault and Coseley - according to Thomas Love Denman - once agreed that Janus was 'all the gods and none'. But later, Hersault described him as 'all the gods', and Coseley favoured 'none'. Denman was a sinister dilettante, but this rings true of them both.'
the_locksmiths_dream_stolen_reflections = card_type("the_locksmiths_dream_stolen_reflections",
    attributes(tally_price=1, mystery_sky=4, readable=1, thing=1, subject_watchmans_paradoxes=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.revelation,
)


# The Locksmith's Dream: Trespasses
#
# The third volume of Teresa Galmier's examination of parallels in the mystic dreams of artisans.
# ---
# I'm Reading...
#
# In this volume, notoriously, Galmier's prose begins to disintegrate, and it is not clear which dreams are in fact her own.
# ---
# I've Read...
#
# 'The woman in the sand-coloured robe has told me: the stairways of the Mansus go ever up. Death is down. The Mother of Ants guards both directions with each of her heads, and so the passage must always be through a wound. I think the White Door might be a wound. That's one reason the Dead sometimes pass it. I think I have the other half of the Secret now, and I hope my reader can put both halves together.'
the_locksmiths_dream_trespasses = card_type("the_locksmiths_dream_trespasses",
    attributes(tally_price=1, mystery_knock=6, readable=1, thing=1, subject_edicts_liminal=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.impulse,
)


# The Manner in which the Alchemist was Spared
#
# In 1782, Anaël Verdier used this text as the basis for a presentation to the Academy of Sciences in Paris. He was executed in secret the following morning without trial.
# ---
# I'm Reading...
#
# In the days of the Carapace Cross, when humanity lived in the dark and ate on its knees, humans could enter the Mansus like vermin. One learnt the arts of Flint, the arts of shaping and remaking...
# ---
# I've Read...
#
# Through the Black, the Yellow, the Red, the Unwise Mortal ascended to the shadow of the Egg Unhatching, and remained in his service. He may be there to this day.'
the_manner_in_which_the_alchemist_was_spared = card_type("the_manner_in_which_the_alchemist_was_spared",
    attributes(tally_price=2, mystery_forge=14, written_in_vak=1, readable=1, thing=1, curia_period=1, subject_anbary_and_lapidary=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# The Messenger Awaiting Her Destination
#
# The Limian Burzghash records his prophecies of a City Unbuilt, and entreaties to its Herald.
# ---
# I'm Reading...
#
# 'The Herald may never arrive at the City Unbuilt. The City may never be built without the Herald's Message…'
# ---
# I've Read...
#
# The Herald is finally identified as the 'Twelfth Initiate of the House of Silence'. The foundation-stone will be taken from the House of Silence, Burzghash suggests, to become the foundation-stone of the City Unbuilt…
the_messenger_awaiting_her_destination = card_type("the_messenger_awaiting_her_destination",
    attributes(tally_price=5, mystery_forge=16, written_in_vak=1, readable=1, thing=1, subject_door_and_wall=1, codex=1, dawn_period=1),
    lessons=3,
    provides=memory.pattern,
)


# The Mirror of Melancthe
#
# The day-book and dream-journal of Abbess Melancthe, venerated as a saint and respected as an alchemist.
# ---
# I'm Reading...
#
# Melancthe speaks longingly of 'those we would call from behind the sky…'
# ---
# I've Read...
#
# Melancthe claims that the Sights and Sensations arts that she describes can be used to invoke 'the Dream of a Star', when sufficient Sky-aspect is invoked to uplift an Ascendant Harmony.
the_mirror_of_melancthe = card_type("the_mirror_of_melancthe",
    attributes(tally_price=4, mystery_sky=12, readable=1, thing=1, solar_gothic_period=1, subject_sights_and_sensations=1, codex=1),
    lessons=2,
    provides=memory.solace,
)


# The Moon's Egg
#
# The third and last volume of the meditations of Abbot Thomas of the Abbey of the Black Dove.
# ---
# I'm Reading...
#
# Abbot Thomas speaks of the coming death he hears in the sound of the waves, but rejoices that his blood will water the 'Egg of the Moon' - by which he seems to mean the future.
# ---
# I've Read...
#
# The last chapter was dictated, not written, by Abbot Thomas. When Thomas' old sword-brother Trygve returned to raid the Abbey, Thomas had broken his monastic oaths and taken up arms to defend the abbey. The two had both been mortally wounded. Thomas' last words are 'The Wheel turns; the Moon sleeps.'
the_moons_egg = card_type("the_moons_egg",
    attributes(tally_price=4, mystery_moon=4, readable=1, thing=1, solar_gothic_period=1, subject_pearl_and_tide=1, codex=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# The Morphy Codex
#
# A priestess of the Sisterhood of the Knot claims to have discerned the true meaning of the Thunderskin's birth.
# ---
# I'm Reading...
#
# The writer credits the Red Grail, the Ring-Yew and the Horned-Axe - the powers the Sisterhood reveres - with agreeing a final treaty between the Hours of the House and the Hours they'd displaced: the Thunderskin loved the Yew, and the Grail destroyed him, as restitution for the slaying of the Horned-Axe's sisters and brothers.
# ---
# I've Read...
#
# The Thunderskin entered the Mansus through the Peacock Door, 'a privilege never given to the Witch-and-Sister: but then their merit was much less'. The writer admits that entry through the Peacock Door is unseemly, but insists that under the circumstances, there was no other way.
the_morphy_codex = card_type("the_morphy_codex",
    attributes(tally_price=5, written_in_aramaic=1, mystery_moon=6, readable=1, thing=1, dawn_period=1, subject_tridesma_hiera=1, codex=1),
    lessons=1,
    provides=memory.beguiling_melody,
)


# The Most Sorrowful End of the Lady Nonna
#
# An unauthorised account of the death of Abbess Nonna, written by Eusebia, one of the two sisters accused of having murdered Nonna through 'poisoning and Arts unsanctioned.' Eusebia, awaiting execution, intends to hide this account in her cell...
# ---
# I'm Reading...
#
# Nonna has introduced Eusebia to an unsanctioned Thunderskin-cult which meets in the caves below the Abbey; there she and others perform sacred dances for 'the Preservation of the Kingdom.'
# ---
# I've Read...
#
# Eusebia claims that Nonna asked her and another sister to prepare her a leathy-draught (which can be brewed from another beverage with Herbs and Infusions techniques, and a sufficient quantity of Nectar) for a rite all three of them would perform below the Abbey. Something goes awry, Nonna is 'possessed of a tenebrous spirit', and the Abbey-brethren are forced to 'quell her with star-iron'. The other two are implicated: as scapegoats, Eusebia implies, although she acknowledges her fault also...
the_most_sorrowful_end_of_the_lady_nonna = card_type("the_most_sorrowful_end_of_the_lady_nonna",
    attributes(tally_price=4, written_in_kernewek_henavek=1, mystery_nectar=4, readable=1, thing=1, solar_gothic_period=1, subject_herbs_and_infusions=1, codex=1),
    lessons=1,
    provides=memory.impulse,
)


# The Orchid Transfigurations: a Birth
#
# The second volume of a compilation of quasi-Rosicrucian allegories, supposedly by Robert Fludd. This is in the original Latin.
# ---
# I'm Reading...
#
# Fludd, or pseudo-Fludd, suggests alignments between the alchemical tradition of rubedo and the older Grail traditions, through the Pine-Knight's quest for the Cinnabar Cup.
# ---
# I've Read...
#
# Seek the Cup in the birthing-bed,' the Pine-Knight is told. The Midwife at the birthing-bed, to his amazement, is the Mountain-Mother. In a fit of awe, he both gelds and flays himself. The Vigilant Storm bursts joyfully from the remains.
the_orchid_transfigurations_a_birth = card_type("the_orchid_transfigurations_a_birth",
    attributes(tally_price=3, mystery_grail=8, written_in_latin=1, readable=1, thing=1, subject_resurgences_and_emergences=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Orchid Transfigurations: a Feast
#
# A compilation of quasi-Rosicrucian allegories, supposedly by Robert Fludd. This is in the original Latin.
# ---
# I'm Reading...
#
# The illustrations are certainly striking. They flush the skin and glow beneath the eyelids after the book is closed.
# ---
# I've Read...
#
# 'We must devour to be devoured. We cannot be undevoured, as we cannot be unborn.'
the_orchid_transfigurations_a_feast = card_type("the_orchid_transfigurations_a_feast",
    attributes(tally_price=3, mystery_grail=4, written_in_latin=1, readable=1, thing=1, codex=1, baronial_period=1, subject_desires_and_dissolutions=1),
    lessons=1,
    provides=memory.intuition,
)


# The Orchid Transfigurations: Noon
#
# The third volume of a compilation of quasi-Rosicrucian allegories, supposedly by Robert Fludd. This is in the original Latin.
# ---
# I'm Reading...
#
# A long dialogue between the Mountain-Mother and the Vigilant Storm describes the ways in which both mountains and storms end, and the protections they use against those ends.
# ---
# I've Read...
#
# 'But we must use the knife,' said the Lion-Throned One, 'the noose, the flame, the Waking Word, against those who have passed the Three-Valved Door. And so none may pass: that is our Law, and the Law of the Sun.'
the_orchid_transfigurations_noon = card_type("the_orchid_transfigurations_noon",
    attributes(tally_price=2, mystery_heart=4, written_in_latin=1, readable=1, thing=1, subject_maggephene_mysteries=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.solace,
)


# The Origins of Hours
#
# The sage and ecstatic Soham, a frequent visitor to the Mansus, claimed to have discoursed with the Beachcrow in person. Soham later insisted on a sky-burial.
# ---
# I'm Reading...
#
# Soham's writings veer from poetry to confession. He identifies from flesh (those who were mortal), from blood (those who arose from sacrifice), from Light (entry from the Glory) and from stone (those who arose before his knowledge.) He insists that the Moth was the first god-who-was-blood, but later contradicts himself and claims it was the Red Grail.
# ---
# I've Read...
#
# 'The Mansus was different before the first god came from Light, but never doubt it existed, even then.'
the_origins_of_hours = card_type("the_origins_of_hours",
    attributes(tally_price=5, mystery_sky=16, written_in_vak=1, readable=1, thing=1, subject_sacra_limiae=1, dawn_period=1, codex=1),
    lessons=3,
    provides=memory.confounding_parable,
)


# The Other Eye of the Serpent
#
# In which the heresiarch Cygnifer attempts to resolve certain mysteries of Lightning.
# ---
# I'm Reading...
#
# Cygnifer considers Lightning to be 'the division, the connection, the joined serpent.' The Serpent's Eye is said to be the Sun - but as the division and connection, it must have a second Eye.
# ---
# I've Read...
#
# Cygnifer considers and rejects, three times, the hypothesis that the Moon is the Serpent's other eye, insisting that it and the Sun do not share a nature. (This, as much as the Serpent business, is what got him burnt by the Church.) He proposes that the Serpent's teeth are towers, that the Serpent's mouth is a gate, that the Serpent is the 'devourer of Ys'... and 'therefore' that the Serpent's other eye is amber.
the_other_eye_of_the_serpent = card_type("the_other_eye_of_the_serpent",
    attributes(tally_price=4, mystery_sky=10, readable=1, thing=1, solar_gothic_period=1, subject_anbary_and_lapidary=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# The Other Line
#
# One of Samuel Savage's more thoughtful works: an allegorical play about the City Clarity, a city that is also a book, and the sentences which inhabit it.
# ---
# I'm Reading...
#
# The Lords Proverbial and Lords Disquisitional war in the streets of Clarity, while the Punctuants get drunk on ink and supply the jokes (though, by Savage's usual standards, there aren't very many jokes.)
# ---
# I've Read...
#
# The final act sees the Lords Proverbial unsealing the City Clarity's gate to expel the population into the unknown. (The formula that they use for the unsealing is a real one - it can be used with Knock and Preliminal Meter to create a gate-sign of power.)
the_other_line = card_type("the_other_line",
    attributes(tally_price=3, mystery_heart=4, readable=1, thing=1, subject_preliminal_meter=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.confounding_parable,
)


# The Queens of the Rivers
#
# A surreal contemporary play by the enigmatic Monica Medina, in which the Queens of the Rivers are murdered, one by one.
# ---
# I'm Reading...
#
# The Queen of the Vistula is poisoned. The Queen of the Dnieper chokes on a fish-hook. The Queen of the Tagus is burnt alive...
# ---
# I've Read...
#
# The culprit, it transpires, is the audience. The surviving Queens are directed to execute whatever audience members do not escape. A surprisingly lucid epilogue suggests that the correspondence of river-names with historical events does provide clues to secret histories behind our own.
the_queens_of_the_rivers = card_type("the_queens_of_the_rivers",
    attributes(tally_price=1, mystery_scale=4, readable=1, thing=1, nocturnal_period=1, subject_path_and_pilgrim=1, codex=1),
    lessons=1,
    provides=memory.gossip,
)


# The Queen's Turn
#
# A sixteenth-century translation of the Barrowchild's account of 'Lagiah's Turn' - when Lagiah, the Queen Unsated, was offered the opportunity to enter the service of the Hours of the Triple Knot, as long as she repudiated her brother-lover Antaios.
# ---
# I'm Reading...
#
# Lagiah accepts, setting aside 'the arts of the low red sun' associated with Antaios. She bargains, however, for freedom for her daughters. The Hours of the Triple Knot accept casually, knowing that Lagiah has devoured her daughters - but wily Lagiah has decided, 'in the secret hollow of her heart', that she will adopt any who ask, if they can prove their fierceness.
# ---
# I've Read...
#
# The traditions described here - the ones generally described as 'Hill and Hollow' - are associated with Lagiah before her Turn; but now that she's a Name of the Red Grail, they might also be safely used before an altar of the Triple Knot.
the_queens_turn = card_type("the_queens_turn",
    attributes(tally_price=3, mystery_moon=10, readable=1, thing=1, subject_hill_and_hollow=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.salt,
)


# The Radical Measure
#
# Manifesto for experimental and dangerous-sounding invocatory poetry, written some time in the nineteenth century by Dr Arun Peel. A notoriously inconsistent and incoherent text, apparently produced in a tearing hurry.
# ---
# I'm Reading...
#
# 'The Hours have little time for poetry,' Dr Peel avers, 'but they have a tremendous amount of time for poets.'
# ---
# I've Read...
#
# 'As the Rose opens,' Dr Peel explains, 'an Enduring memory opens to the Horizon. This is a way of saying something that cannot otherwise be said, and is best only written with one's eyes firmly closed.'
the_radical_measure = card_type("the_radical_measure",
    attributes(tally_price=2, mystery_rose=10, readable=1, thing=1, curia_period=1, subject_preliminal_meter=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# The Radical Measure (Glossed)
#
# The original 'Radical Measures' was a manifesto for experimental poetry with occult properties, written in the nineteenth century by Dr Arun Peel. The original is notoriously incoherent - much later, Christopher Illopoly took on the task of editing and glossing it. He has taken some liberties, but the updated version is generally well regarded.
# ---
# I'm Reading...
#
# 'The Hours have little time for poetry,' Dr Peel avers, 'but they have a tremendous amount of time for poets.' (Illopoly has added a note suggesting this should in fact be 'the most tremendous time with poets'.)
# ---
# I've Read...
#
# 'As the Rose opens,' Dr Peel explains, 'Enduring Memory opens to the Horizon. This is a way of saying something that cannot otherwise be said, and is best only written with one's eyes firmly closed.' (Illopoly's gloss reads: Horizon-Sight synthesis method. Reverse procedure, with Knock, to elaborate Gervinite in the Chronsichord mode.)
the_radical_measure_glossed = card_type("the_radical_measure_glossed",
    attributes(tally_price=1, mystery_rose=12, readable=1, thing=1, subject_preliminal_meter=1, nocturnal_period=1, codex=1),
    lessons=2,
    period="curia", # game bug?
    provides=memory.pattern,
)


# The Raptures of Forculus
#
# The first volume of Abbot Geffrey's hypothetical theological debates in the Socratic mode.
# ---
# I'm Reading...
#
# 'If Janus were an Hour, Forculus might be counted among his Names, but that door remains closed, and so Forculus is not…'
# ---
# I've Read...
#
# Geffrey discusses 'the signs that mark Doors', which might permit or forbid access to certain thoughts and dreams, speculating (carefully) on which of the sanctioned Hours might teach or govern each sign.
the_raptures_of_forculus = card_type("the_raptures_of_forculus",
    attributes(tally_price=4, mystery_knock=4, written_in_latin=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=1,
    provides=memory.pattern,
)


# The Red Book of Brittany
#
# A volume of ink-lore gifted to St Brandan's by Brian of Brittany, who was made Earl of Cornwall after the Norman Conquest.
# ---
# I'm Reading...
#
# 'The Red Flower lies heavy, but the roots of the Watchman's Tree are constant…''
# ---
# I've Read...
#
# The Red Flower is described as 'the temptation of suffering'; but its suffering can apparently be allayed when 'the Copper Fruit' is enspelled with Nectar-aspect alongside Herbs and Infusions techniques. A variant of the same approach, with the Inks of Power techniques outlined here, can 'gentle Leathy into a Great Ink...'
the_red_book_of_brittany = card_type("the_red_book_of_brittany",
    attributes(tally_price=4, mystery_rose=12, readable=1, thing=1, solar_gothic_period=1, subject_inks_of_power=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Republic of Teeth
#
# An eccentric political tract by Valentine Dewulf.
# ---
# I'm Reading...
#
# Valentine suggests that rulers should be elected to govern by serpents, not their subjects, 'for the Serpent, being cold-blooded in its Nature, is incorruptible.'
# ---
# I've Read...
#
# Valentine's initial proposal is that a college of electors should subject themselves to the bites of venomous serpents - which he grades and details, preferring the least dangerous - and should allow the resulting deliria to guide them in their choice of people's representatives. He becomes concerned, however, by the practicalities of ensuring equal quantities of venom in each case, and gets half-way into a proposal for using birds instead in the selection process, before giving up mid-sentence.
the_republic_of_teeth = card_type("the_republic_of_teeth",
    attributes(tally_price=3, mystery_scale=6, readable=1, thing=1, codex=1, baronial_period=1, subject_serpents_and_venoms=1),
    lessons=1,
    provides=memory.intuition,
)


# The Road to Janus
#
# The Limian Burzghash makes a series of prophecies regarding 'the Initiates of the House of Silence', with intricate, if unhelpful, predictions on their passage through the House.
# ---
# I'm Reading...
#
# 'The Sixth Initiate is Priest and Key, Gate and Church. He shall cross the sea and open the tide. He shall not be the Eleventh, yet shall there be Seven between them. In the first Year of his Time, the Flower-Door is opened…'
# ---
# I've Read...
#
# 'The Twelfth Initiate is Salvation and Wrack, Steed and Rider, who chooseth one Blossom of Three, who casteth away the Key and whom the Key shall not cast away, who comes after the Flame and before the Snow….'
the_road_to_janus = card_type("the_road_to_janus",
    attributes(tally_price=5, mystery_knock=18, written_in_vak=1, readable=1, thing=1, subject_door_and_wall=1, dawn_period=1, codex=1),
    lessons=3,
    provides=memory.pattern,
)


# The Rose of Hypatia
#
# A volume of collected teachings of the Sisterhood of the Knot, that arcane-contemplative order that existed in all histories, but in some was very powerful indeed. This was recorded by 'Hypatia', and dedicated to St Nympha.
# ---
# I'm Reading...
#
# St Nympha is described as 'not born, but cultivated'. The sentience that became the saint, 'Hypatia' indicates, inhabited a sinner's corpse in order to enable that sinner's redemption.
# ---
# I've Read...
#
# 'Not all the Dead enter the Mansus by the Winter Door. Not all the Dead enter the Mansus at all.'
the_rose_of_hypatia = card_type("the_rose_of_hypatia",
    attributes(tally_price=4, written_in_greek=1, mystery_moth=8, readable=1, thing=1, solar_gothic_period=1, subject_weaving_and_knotworking=1, codex=1),
    lessons=2,
    provides=memory.solace,
)


# The Rose of Nuriel
#
# A volume of collected teachings of the Sisterhood of the Knot, that arcane-contemplative order that existed in all histories, but in some was very powerful indeed. This was recorded by 'Nuriel', and dedicated to St Tryphon.
# ---
# I'm Reading...
#
# St Tryphon, Nuriel explains, performed secret miracles in the name of 'She who Bleeds and Bears'' and 'She who Opens'. Thus St Tryphon opened the way to the House of the Sun; thus St Tryphon underwent the Great Birth, an ascension to immortality.
# ---
# I've Read...
#
# St Tryphon began his ascension by passing the 'Horned Door'. St Tryphon continued his ascension by learning the 'Invocation Thiatic' - which Nuriel does not here record, on account of its extreme holiness. And, Nuriel explains grimly, to achieve the Seven Marks of the Great Birth, St Tryphon consumed 'those whose soul had left them, and even those in whom the soul remained.'
the_rose_of_nuriel = card_type("the_rose_of_nuriel",
    attributes(tally_price=4, mystery_grail=10, written_in_greek=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_the_great_signs_and_the_great_scars=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The Rose of Waznei
#
# The heretical teachings of a disgraced offshoot of the Sisterhood of the Knot, that arcane-contemplative order that existed in all histories. This was recorded by 'Waznei', and dedicated to St Respicius.
# ---
# I'm Reading...
#
# The offshoot favoured by Waznei - 'the True Sisterhood' - followed St Respicius in pursuing ascension in the name of the Door-in-the-Eye, the merciless Hour of light. St Respicius failed, perhaps because the larger Sisterhood tracked him down and ritually strangled him, but Waznei outlines steps for those who hope to succeed.
# ---
# I've Read...
#
# 'Seek in dreams; seek the Mansus. The Third Mark can be achieved only when one has passed the Stag Door. One must pass the Wood. One must rise to the White Door. The Stag Door awaits the light-bearer, in the sight of Ghirbi.'
the_rose_of_waznei = card_type("the_rose_of_waznei",
    attributes(tally_price=3, written_in_greek=1, mystery_lantern=8, readable=1, thing=1, subject_auroral_contemplations=1, codex=1, baronial_period=1),
    lessons=2,
    provides=memory.revelation,
)


# The Scar in the Sky
#
# Nyn wrote this, and came to regret it.
# ---
# I'm Reading...
#
# Each page of this book contains one word only, but as each page is turned, a knowledge creeps in.
# ---
# I've Read...
#
# The final page is crowded. Each reader of the book records the same word. Now it is my turn.
the_scar_in_the_sky = card_type("the_scar_in_the_sky",
    attributes(tally_price=5, written_in_fucine=1, mystery_winter=14, readable=1, thing=1, dawn_period=1, subject_quenchings_and_quellings=1, codex=1),
    lessons=2,
    provides=memory.regret,
)


# The Sea Does Not Regret
#
# Ehsan Fekri, one-time Secretary Salvant of the Curia of the Isle - responsible for the Curia's healing efforts - writes of his experiences in Brancrug, and hints at his travels elsewhere.
# ---
# I'm Reading...
#
# 'The Sea does not regret the tide,' Fekri writes, 'for when the tide has passed, it leaves its traces on the sand; which traces are the Sea's memory.'
# ---
# I've Read...
#
# Fekri is a keen fisherman, and speaks glowingly of the fish suppers of Brancrug. He also admits that his enthusiasm for 'the bounty of the sea' has altered him - that before he came to Brancrug, he consumed only those things found in the earth. 'I was the greater thereby, but all of us give up what we were, to become what we are.'
the_sea_does_not_regret = card_type("the_sea_does_not_regret",
    attributes(tally_price=2, mystery_moon=6, readable=1, thing=1, curia_period=1, subject_pearl_and_tide=1, codex=1),
    lessons=1,
    period="baronial", # game bug?
    provides=memory.salt,
)


# The Secret Colours
#
# Black Elie, disgraced Damascene Matriarch of the Sisterhood of the Triple Knot, wrote this while fleeing the 'agents of the Duty.'
# ---
# I'm Reading...
#
# Elie writes of the 'secret colours of the Sun' - the blessed 'traces of Error' - weaknesses in sunlight, balancing principles in its reflection.
# ---
# I've Read...
#
# A deeper account of these secret colours, Elie reveals, was kept at a shrine to the Three Hours of the Chancel at the 'grey rock in the sea', far from the intrigues of Sisterhood and Church. It is hidden from the common eye, but can be revealed with the arts of Sickle and Eclipse.
the_secret_colours = card_type("the_secret_colours",
    attributes(tally_price=4, written_in_greek=1, mystery_moon=14, readable=1, thing=1, solar_gothic_period=1, subject_sickle_and_eclipse=1, codex=1),
    lessons=2,
    provides=memory.revelation,
)


# The Serenity of the Black Wood
#
# An allegorical history of the House of Lethe, which it is here implied was inspired by the Centipede. 'Sereno Blackwood' is an occult alias to this day.
# ---
# I'm Reading...
#
# 'The Proverbial Footloose' gathers travellers in a wood, and leads them through, but abandons them part-way. They find themselves beset by 'glorious monsters'.
# ---
# I've Read...
#
# The travellers discover they can survive if they close their eyes (they adopt a closed eye as their sign) and that they can go unnoticed if they drink from the clear cold streams. They never forget 'that proverbial footloose, the Centipede' but they never forgive her either.
the_serenity_of_the_black_wood = card_type("the_serenity_of_the_black_wood",
    attributes(tally_price=4, written_in_greek=1, mystery_moth=12, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_sacra_limiae=1),
    lessons=2,
    provides=memory.confounding_parable,
)


# The Sevenfold Slaying of the Seven-Coiled
#
# An account of the destruction of a primaeval Hour, a god-who-was-Stone.
# ---
# I'm Reading...
#
# There are twelve verses. In the first, an ascendant Hour identified as the Scarred One enumerates his justifications for destroying the Seven-Coiled: its appetites, its growth, its enmity to humanity. In the second, a priestess puts out his eyes and scars his skin to protect him against the Seven-Coiled's magics. In each of the next seven verses, he destroys one aspect of the Seven-Coiled....
# ---
# I've Read...
#
# In the tenth verse, the Scarred One bathes his priestess-patron in the blood of the Seven-Coiled, to lend her power. In the eleventh, they assault the 'temple behind the world', entering it by force. In the twelfth, they swear a tripartite oath to protect their ancestors, their descendants, and themselves.
the_sevenfold_slaying_of_the_seven_coiled = card_type("the_sevenfold_slaying_of_the_seven_coiled",
    attributes(tally_price=5, mystery_edge=16, written_in_fucine=1, readable=1, thing=1, dawn_period=1, subject_disciplines_of_the_scar=1, codex=1),
    lessons=3,
    provides=memory.fear,
)


# The Shadow in the Stair
#
# Ernestine Peterhans records her conversations with the 'little darkness' in Hush House's Stair Tenebrous, which she calls 'Donkerling'.
# ---
# I'm Reading...
#
# Ernestine's business in the cellars of Hush House often took her up and down the Stair Tenebrous, although it is avoided by every other servant. 'Donkerling' attempted first to consume her and then to demand sacrifices from her; Ernestine consented to bring it mice, but became very stern when it asked for a 'new-drowned child...'
# ---
# I've Read...
#
# 'Donkerling' claims to be an imprisoned Long under the protection of 'the deepest power of the Sea'. It is prone to occasional bouts of raving about how, when it has its freedom, its patron will drown the Isle. Ernestine renders most of these long speeches as '...', but is very interested in what it can tell her about the circumstances of shipwrecks; there are hints that she may have been planning a salvage expedition.
the_shadow_in_the_stair = card_type("the_shadow_in_the_stair",
    attributes(tally_price=3, mystery_nectar=6, readable=1, thing=1, subject_coil_and_chasm=1, baronial_period=1, codex=1),
    lessons=1,
    provides=memory.impulse,
)


# The Shaven Lock Tantra
#
# Also known as 'The One Who Has Shaven His Hair'. This, the story goes, is the lore that even the shapechanging Vanaras rejected.
# ---
# I'm Reading...
#
# The Tantra speaks glowingly of those who are prepared to abandon their old self to seek a new and higher self. It warns that once the change has truly begun - 'past the Third Mark' - a return to the old self is dangerous and painful.
# ---
# I've Read...
#
# 'Whisper your secrets into the earth, burn them in fire, scatter them in the sea. Still they will cling to your hair,' the Tantra cautions. It provides an occult riddle that it claims is sometimes the answer to the Riddle of the Hunter's Gate.
the_shaven_lock_tantra = card_type("the_shaaven_lock_tantra",
    attributes(tally_price=5, mystery_moth=6, written_in_sanskrit=1, readable=1, thing=1, dawn_period=1, codex=1, subject_rites_of_the_roots=1),
    lessons=1,
    provides=memory.impulse,
)


# The Silver Book
#
# A manual of the Ordo Limiae, an order of quasi-immortals who maintained a secret enclave at the source of the river Limia, in the Roman province of Hispania Gallaecia. This manual was compiled by one Burzghash, who explains that he came to join the Ordo from the 'city of messenger eagles' after he abandoned the service of the Ivory Dove.
# ---
# I'm Reading...
#
# Members of the Ordo took an oath, the Silver Chain, that forbade men to lie with woman, or women with men: 'for what may come is not always the Crime of the Sky, yet that is a furious danger.' It was apparently permissible for men to lie with men, and women with women - in fact, Burzghash suggests that should be encouraged, to distract from other temptations.
# ---
# I've Read...
#
# The manual prescribes potential countermeasures to protect those who might be tempted to go against the oath: masks, disfigurement, severe poetic disciplines. Those who do break it are to be punished with death, although there are lesser punishments prescribed for various acts that don't involve actual coitus. Death is to be administered with 'the Glassfinger Toxin', which can be created with the assistance of the techniques described earlier in the manual, and with sufficient Knock aspect.
the_silver_book = card_type("the_silver_book",
    attributes(tally_price=5, written_in_fucine=1, mystery_moth=8, readable=1, thing=1, dawn_period=1, codex=1, subject_edicts_liminal=1),
    lessons=2,
    provides=memory.impulse,
)


# The Six Letters on Necessity
#
# Warnings and confessions about the cost of the secret arts, addressed to a student by the seventeenth-century magus (and reputed immortal) Julian Coseley
# ---
# I'm Reading...
#
# Coseley's tone is urgent - as if he suspected he might have little time left.
# ---
# I've Read...
#
# 'Even the Sunne can be divided, though it require the Forge of Dayes for its division.'
the_six_letters_on_necessity = card_type("the_six_letters_on_necessity",
    attributes(tally_price=2, mystery_moth=4, readable=1, thing=1, subject_transformations_and_liberations=1, curia_period=1, codex=1),
    lessons=1,
    provides=memory.foresight,
)


# The Skeleton Songs
#
# Poems of greedy delight composed by the possibly pseudonymous Arabella Dusk, the rumoured heiress-turned-madam-turned-poetess.
# ---
# I'm Reading...
#
# In Arabella's introduction, she explains that the book was to be illustrated, but that the Suppression Bureau would not permit it. She hints that the illustrations still exist somewhere. The book is dedicated to 'Sir Parsival of the Red Cup'.
# ---
# I've Read...
#
# The Twenty-Six Delightful Fruits; the Seven Chastisements; the Nine Gardens; the Four Regrets.
the_skeleton_songs = card_type("the_skeleton_songs",
    attributes(tally_price=1, mystery_grail=4, readable=1, thing=1, subject_resurgences_and_emergences=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.beguiling_melody,
)


# The Sky in the Scar
#
# Gnomic exhortations that might be described as 'emergency procedures' for the return of the travelling kinds of the Carapace Cross. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# Each page of this book except the last bears a single sign, clear and irrefutable as a gem...
# ---
# I've Read...
#
# …the final page is empty. The travelling kinds of the Carapace Cross might never return.
the_sky_in_the_scar = card_type("the_sky_in_the_scar",
    attributes(tally_price=8, mystery_edge=10, written_in_sabazine=1, readable=1, thing=1, dawn_period=1, subject_sickle_and_eclipse=1, codex=1),
    lessons=2,
    provides=memory.back_into_balance,
)


# The Sky, the Soul
#
# The grand labour of Kalle, an ascetic poet writing at the court of the Shadowless Kings.
# ---
# I'm Reading...
#
# Kalle's verses are brief, obscure, and often dominated by images of violence. 'A star is a pin-prick, but the Sun is a wound.'
# ---
# I've Read...
#
# It's always possible to be deader,' Kalle states. 'The Watchman goes before; none but seven may go after.' 'Yet surely we are born to the Glory as the sparks fly upwards.'
the_sky_the_soul = card_type("the_sky_the_soul",
    attributes(tally_price=5, written_in_aramaic=1, mystery_lantern=12, readable=1, thing=1, subject_pyroglyphics=1, dawn_period=1, codex=1),
    lessons=2,
    provides=memory.foresight,
)


# The Songs of the Carapace Cross
#
# Micah Xi, sometimes called the Magus of Quartz, etched this work in acid on stone. It has been reproduced many times in many languages since, but the reproductions are often lost to landslides.
# ---
# I'm Reading...
#
# Xi describes the rites of the gods-who-were-stone, the first Hours, as practiced before the existence of human civilisation by the 'Carapace Cross'. He claims a final survivor of the Cross shared the information with him.
# ---
# I've Read...
#
# The rites are largely obsolete now. Few have been observed, in the last thousand years at least, to have any effect at all. Nevertheless, Xi identifies at least one invocation of particular power. He warns that it should be used with caution, lest the gods-who-were-stone might find their way back from Nowhere.
the_songs_of_the_carapace_cross = card_type("the_songs_of_the_carapace_cross",
    attributes(tally_price=5, written_in_fucine=1, mystery_moth=16, readable=1, thing=1, dawn_period=1, codex=1, subject_edicts_liminal=1),
    lessons=3,
    provides=memory.pattern,
)


# The Sun's Lament
#
# The first volume of the meditations of Abbot Thomas of the Abbey of the Black Dove.
# ---
# I'm Reading...
#
# 'The thorn-beaked crows took my eyes from me in justice for my crimes, but though I lost my Sight, I found my Light.'
# ---
# I've Read...
#
# Abbot Thomas speaks of the breaking of his oaths to his sword-brother Trygve, and to the 'Lord of Scars' that he served before he came to the Abbey. He writes of the power of oath-bonds, and considers the means and morality of their sundering.
the_suns_lament = card_type("the_suns_lament",
    attributes(tally_price=4, mystery_edge=4, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_ragged_crossroads=1),
    lessons=1,
    provides=memory.fear,
)


# The Tantra of Worms
#
# The entomologist Juliana Zawistowski eventually came to insist that this text was written by insects inhabiting a human skin. She never presented evidence for her claim. There are diagrams. The diagrams are not good to look upon.
# ---
# I'm Reading...
#
# The Tantra explains various less than practical countermeasures against the Worms, the 'Serpents Which Are Not Serpents'. Moth and Winter are closest to them, and so understand their weaknesses, but both have their own perils. The Lionsmith crushes them, but that's not recommended for mortals.
# ---
# I've Read...
#
# 'The Worms have always been eager to inhabit us. Here are the practices which make us inhospitable to them.' There are diagrams. The diagrams are not good to look upon, and none of the practices they show would allow the subject to survive.
the_tantra_of_worms = card_type("the_tantra_of_worms",
    attributes(tally_price=1, written_in_sanskrit=1, mystery_scale=8, readable=1, thing=1, subject_coil_and_chasm=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.fear,
)


# The Temptations of Architecture
#
# The antiquarian and nyctodromist Ambrose Westcott writes of the 'dangers of doors', with particular reference to a house in the bounds named 'Treowen'.
# ---
# I'm Reading...
#
# No doubt they have come to regret the ambitions of their Winding Stair; even now in Treowen, a silver sea is unwisely visible from a rash window…'
# ---
# I've Read...
#
# Westcott explains that the Wheelocks, the 'charge-holders of Treowen', have had recourse to dramatic measures to prevent oneiric encroachment, removing the entire top floor of the building. 'Nevertheless,' he writes, 'the business of the Moon-Hall has begun to touch the other business of the house...'
the_temptations_of_architecture = card_type("the_temptations_of_architecture",
    attributes(tally_price=2, mystery_forge=10, readable=1, thing=1, subject_door_and_wall=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.secret_threshold,
)


# The Three and the Three (Kerisham Manuscript)
#
# A more recent version of a much older text, this book describes the operations of the Chancel and the Calyptra, two triads of Hours with subtle, far-reaching powers and responsibilities. It has been heavily censored, but even so contains potent secrets.
# ---
# I'm Reading...
#
# 'The deepest knowledge is safeguarded by the Covenant of the Watchman's Tree, whose patrons are Calyptra - the three flowers on the Watchman's Tree - blood, soot, and snow…'
# ---
# I've Read...
#
# Calyptra may be known, as Night, Dawn, Eclipse. The Chancel may be known, as Threshold, Mirror, Shell. Calyptra and Chancel then are two: is Janus a third?'
the_three_and_the_three_kerisham_manuscript = card_type("the_three_and_the_three_kerisham_manuscript",
    attributes(tally_price=2, mystery_moon=10, readable=1, thing=1, subject_edicts_inviolable=1, curia_period=1, codex=1),
    lessons=2,
    provides=memory.intuition,
)


# The Three and the Three (St Chiavi Manuscript)
#
# This book describes the operations of the Chancel and the Calyptra, two triads of Hours with subtle, far-reaching powers and responsibilities. Of all the extant versions, this one has best survived the interventions of the Calyptra. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# 'Certain knowledge cannot be learnt by any entity below the rank of Know - outside the covenant of the Watchman's Tree. The enforcement of this rule is Calyptra. The three who enforce it are Calyptra also. It is said that Janus elects Calyptra, that the Chancel is the judgement of Janus, that Janus is the wound in the Law...'
# ---
# I've Read...
#
# 'The Watchman's Tree is a compromise. If Calyptra could end it, they would. If the Watchman could end Calyptra, he might. Between their planes conflicting, sparks illuminate the angles of unmade law…'
the_three_and_the_three_st_chiavi_manuscript = card_type("the_three_and_the_three_st_chiavi_manuscript",
    attributes(tally_price=8, mystery_moon=18, readable=1, thing=1, solar_gothic_period=1, subject_edicts_inviolable=1, codex=1),
    lessons=3,
    provides=memory.three_rules,
)


# The Three and the Three (Vatican Manuscript)
#
# A Church-authorised version of an older text, this book describes the Chancel and the Calyptra, two triads of Hours with subtle, far-reaching powers and responsibilities. It has clearly been reworked to fit Church doctrine.
# ---
# I'm Reading...
#
# 'The deepest knowledge is forbidden to all mortals except those who seek it beneath the Watchman's Tree. It is Calyptra that planted that tree, but it is the Chancel, the Cruciate, that has elected Calyptra. Who then elected the Cruciate? Or is this, as the saying goes, 'a matter of Janus'?
# ---
# I've Read...
#
# 'The Sister-and-Witch is Cruciate, but the Witch-and-Sister is not. Even those powers that demand a conjunction are not always conjoined. When the Sister is Nowhere, does this mean Nowhere sits <i>in crucem</i>?'
the_three_and_the_three_vatican_manuscript = card_type("the_three_and_the_three_vatican_manuscript",
    attributes(tally_price=4, mystery_moon=14, readable=1, thing=1, solar_gothic_period=1, subject_edicts_inviolable=1, codex=1),
    lessons=2,
    provides=memory.intuition,
)


# The Time of Division
#
# In which Amira Zahra prophesies the events later known as the Intercalate, when the Hour called Sun-in-Splendour will be divided.
# ---
# I'm Reading...
#
# The Sun will be divided that it might not sire children. Still its children shall be Four in number and its children shall be Seven in number and its children shall also be Numberless. The Numberless shall open the way for the Seven, and the Seven shall consume the Four...'
# ---
# I've Read...
#
# Amira prophesies four great wars before the Second Dawn, when the Sun-in-Splendour shall rise again. She cautions: 'Sunrise is blood, and I foretell now that the Sun shall rise from blood, yet not the colour of the blood, nor the hour of Night.' She includes a rite that she speculates will be necessary for the Second Dawn.
the_time_of_division = card_type("the_time_of_division",
    attributes(tally_price=5, mystery_heart=14, written_in_deep_mandaic=1, readable=1, thing=1, dawn_period=1, subject_surgeries_and_exsanguinations=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# The Treatise on Underplaces
#
# Herein, the seventeenth-century mystic and antiquarian Claude Hersault describes the 'Bounds' or 'Underplaces' on the borders of dream. He warns that they shift over time.
# ---
# I'm Reading...
#
# 'The walls of the Mansus,' Hersault begins, 'are the size of starlight.' Many of his directions are equally unhelpful, but common relationships do emerge.
# ---
# I've Read...
#
# A picaresque account of a journey through nightmare, interspersed with what might be partial rites. 'On the eighteenth Ascent is the bud. On the thirty-sixth Ascent, the blossom.'
the_treatise_on_underplaces = card_type("the_treatise_on_underplaces",
    attributes(tally_price=3, mystery_knock=4, readable=1, thing=1, subject_horns_and_ivories=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.fear,
)


# The Tripled Heart
#
# Sacred poems composed in honour of the Hours venerated by the Sisterhood of the Triple Knot.
# ---
# I'm Reading...
#
# The Grail is celebrated for her colours, the Malachite for her sweetness, the Axe for her constancy…
# ---
# I've Read...
#
# The Thunderskin, least of the Hours of the Knot when he is even counted among their number at all, is celebrated with an unexpectedly poignant elegy. 'What lives, departs; what is dead, remains.'
the_tripled_heart = card_type("the_tripled_heart",
    attributes(tally_price=4, mystery_grail=4, written_in_kernewek_henavek=1, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_tridesma_hiera=1),
    lessons=1,
    provides=memory.intuition,
)


# The Turquoise Hand
#
# A calligraphic manual of Ramsund which employs as exemplar-text Farid ud-Din's 'Conference of the Birds'. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# 'At noon the Sun moves like the beating of a wing. At sunset he sends the herald-child with her candle. At midnight, he sends the wind that extinguishes the candle-flame…'
# ---
# I've Read...
#
# Commentary, illustrations and interleavings carry revelations never intended in the original: a sense of history, and the senses of Histories.
the_turquoise_hand = card_type("the_turquoise_hand",
    attributes(tally_price=8, written_in_ramsund=1, mystery_rose=10, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_pentiments_and_precursors=1),
    lessons=2,
    provides=memory.that_old_lost_music,
)


# The Twelve Letters On Consequence
#
# Julian Coseley's epistolary treatise on 'what may come after', addressed to his once-friend Claude Hersault, the mystic and antiquarian.
# ---
# I'm Reading...
#
# By the time he wrote these letters, Coseley was identified with the oneiropolitical 'Worms' movement, and Hersault with the 'Birds' - meaning roughly that Hersault held the order of the Hours to be desirable, and Coseley held it to be oppressive.
# ---
# I've Read...
#
# Many of Coseley's arguments about consequence and finality are couched in erudite and practical alchemical terms. Others appear to be thinly-veiled threats directed at Hersault. Some are both.
the_twelve_letters_on_consequence = card_type("the_twelve_letters_on_consequence",
    attributes(tally_price=2, mystery_moon=4, readable=1, thing=1, curia_period=1, subject_putrefactions_and_calcinations=1, codex=1),
    lessons=1,
    provides=memory.regret,
)


# The Twin-Serpent Tantra
#
# Just before the outbreak of the Great War, 'Alexander Sparrow' - almost certainly a pseudonym - published leaflets claiming the influence of 'Snake Princes' on world affairs. The text called the Twin-Serpent Tantra was his primary inspiration.
# ---
# I'm Reading...
#
# The Tantra describes the Great Hooded Princes - a dynasty of unclear origin - engaging in prayers, sacrifices and poetry in honour of the Key-Serpent, the Crossroads-Twins and the Mirror-Queen. 'Nagi encircles; Nagi arises from wounds; Nagi spares those who are already harmed.'
# ---
# I've Read...
#
# The Great Hooded Princes are described as having 'escaped from the history of their death to a history where they yet live'. The text claims that there are now one hundred and eight of them, but - in one of many instances of twinnedness - before they crossed from their death chronicle, there were only fifty-four.
the_twin_serpent_tantra = card_type("the_twin_serpent_tantra",
    attributes(tally_price=1, mystery_knock=8, written_in_sanskrit=1, readable=1, thing=1, subject_edicts_liminal=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.pattern,
)


# The Victory of Crowns
#
# Erratic accounts by 'Arun' of the hunting and consumption of supposed immortals by shadowy assassins. Published in the late nineteenth century.
# ---
# I'm Reading...
#
# The assassins are, according to 'Arun', the agents of a power called the Coronel, a 'soldier of the Secret Masters'. The accounts date back to Roman times.
# ---
# I've Read...
#
# Arun's scholarship is dubious, but he (she?) writes pithily. Incidents of sudden and violent death are interspersed with aphorisms: 'Hours don't dream. Long try not to.'
the_victory_of_crowns = card_type("the_victory_of_crowns",
    attributes(tally_price=2, mystery_edge=4, readable=1, thing=1, curia_period=1, subject_sharps=1, codex=1),
    lessons=1,
    provides=memory.contradiction,
)


# The Viennese Conundra
#
# Van Driel describes odd events in Vienna - the disappearance of children; epidemics of parasite activity; animal mutilations; nightmares of worms; the activities of a charitable organisation, the New Ligeians, that funds the burial of the poor. She proposes peculiar connections between these activities.
# ---
# I'm Reading...
#
# 'When the individual K. attends the meetings, black dogs are sacrificed and quartered. When the element M. is in attendance, black mares are found with their throats slashed. I propose that these sacrifices are not necessary, but that our Ligeian friends may consider them 'fitting'. Herewith diagrams of the mutilations -'
# ---
# I've Read...
#
# 'Medusa's Riddle, then, I choose to render as 'What is Not Seen?' There is another riddle, one I have heard rendered as 'What may be Lost?' I will delineate some historic attempts to answer it- these are in themselves, in some sense, sacrifices - '
the_viennese_conundra = card_type("the_viennese_conundra",
    attributes(tally_price=2, mystery_moon=4, readable=1, thing=1, curia_period=1, subject_wolf_stories=1, codex=1),
    lessons=1,
    provides=memory.fear,
)


# The Vinzant Inscriptions
#
# Everett Vinzant transcribed these from a cliff in Anatolia, where he famously survived a lightning-strike. He died seven years later to the day. His bones, the legend has it, were hot to the touch.
# ---
# I'm Reading...
#
# Long ago, the Sisterhood of the Knot recounted, the Forge loved the Hour called the Sun-in-Splendour. The Red Grail long anticipated their union, and the Grail-priestesses prophesied it...
# ---
# I've Read...
#
# The remainder of the text consists of gloating remarks by the Grail-priestesses of the Shaping that will come, interpolated with warnings and laments from those of the Sisterhood who serve the Ring-Yew and especially the Horned Axe. Nevertheless, an invocation to the Forge is included as part of an attempt to urge it onwards.
the_vinzant_inscriptions = card_type("the_vinzant_inscriptions",
    attributes(tally_price=5, mystery_forge=6, written_in_phrygian=1, readable=1, thing=1, subject_transformations_and_liberations=1, codex=1, dawn_period=1),
    lessons=1,
    provides=memory.foresight,
)


# The Voyages of Ferninshun of Oreol
#
# The impossible travels of a sea-captain of the late Phoenician era. Suppressed throughout recorded history: those who read it were said to disappear.
# ---
# I'm Reading...
#
# Ferninshun clearly visited the Mansus, sailing the length of the Painted River. He also claims to have traversed a sea of finest sand, to have dared the blazing waves of the Sun's surface, and to have descended to an underworld ocean lit by lamps of black nephrite...
# ---
# I've Read...
#
# Ferninshun's final voyage is to retirement on a peaceful island across an evening sea, where he identifies a spring whose waters will keep him safe. 'I will be forgotten,' he declares, 'and this work my only trace.'
the_voyages_of_ferninshun_of_oreol = card_type("the_voyages_of_ferninshun_of_oreol",
    attributes(tally_price=5, written_in_fucine=1, mystery_moon=18, readable=1, thing=1, subject_sea_stories=1, dawn_period=1, codex=1),
    lessons=3,
    provides=memory.salt,
)


# The War of the Roads, 1451-1551
#
# Willis-Ford describes the War of the Roads, an event in a History other than our own, in detail - from its beginnings as a martial-philosophical dispute between the Dawn and Sunset Roads of alchemy, to a war which ravaged half of Europe.
# ---
# I'm Reading...
#
# 'It is not now widely believed that the sons and daughters of the Red Rose were forged into immortals. Understandably: they are, after all, now all long dead. The Forge itself devoured the greatest among them.'
# ---
# I've Read...
#
# The royalty of England, according to Willis-Ford, became the Sovereigns of the Leashed Flame, destroying or transforming their enemies, conquering Europe, establishing grand cathedrals to St Spark. The alliance with the Forge begins to take its toll. At last, the Bronze King undergoes his 'Great Misfortune' and 'Great Debasement', and is afterwards known as the Copper King. His attempt to cheat the Forge ends badly, the Leashed Flame is released, and the King's heirs are merely mortal sovereigns.
the_war_of_the_roads = card_type("the_war_of_the_roads",
    attributes(tally_price=2, mystery_edge=4, readable=1, thing=1, curia_period=1, codex=1, subject_meniscate_reflections=1),
    lessons=1,
    provides=memory.foresight,
)


# The White Book of Brittany
#
# A volume of death-lore gifted to St Brandan's by Brian of Brittany, who was made Earl of Cornwall after the Norman Conquest.
# ---
# I'm Reading...
#
# 'The White Flower lies heavy, but the roots of the Watchman's Tree run deeper than snow...'
# ---
# I've Read...
#
# The White Flower is described as the 'death of wisdom' - but wisdom can pass into sleep, not death, when 'the Rage of Glass' is subjected to sufficiently powerful Winter-aspect while the Ragged Crossroads arts are invoked.
the_white_book_of_brittany = card_type("the_white_book_of_brittany",
    attributes(tally_price=4, mystery_winter=10, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_ragged_crossroads=1),
    lessons=2,
    provides=memory.hindsight,
)


# The Wind's Ruin
#
# The second volume of the meditations of Abbot Thomas of the Abbey of the Black Dove.
# ---
# I'm Reading...
#
# Abbot Thomas speaks of his time as a raider, when his name was not Thomas but Toke, 'scything the sea, striving for plunder'…
# ---
# I've Read...
#
# Abbot Thomas clearly regrets his 'storm-years', and much of the book is taken up with his thoughts on penitence; but there are hints also that he misses those years, and the companionship of his 'sword-brother, ship-brother' Trygve.
the_winds_ruin = card_type("the_winds_ruin",
    attributes(tally_price=4, mystery_grail=4, readable=1, thing=1, solar_gothic_period=1, subject_applebright_euphonies=1, codex=1),
    lessons=1,
    provides=memory.beguiling_melody,
)


# The Wonderful Shape
#
# Blessings and invocations of the Triple Knot recorded at a sanctuary in Cyprus notable for its weavers, sculptors, and gardeners.
# ---
# I'm Reading...
#
# 'The roots go deep. The knots remain…'
# ---
# I've Read...
#
# The final invocation is one for the 'Restoration of the Roots', to be spoken before an altar of the Triple Knot - but, puzzlingly, it should not be spoken by any priestess of the Knot, or even by one who has been initiated into their Mysteries.
the_wonderful_shape = card_type("the_wonderful_shape",
    attributes(tally_price=5, mystery_grail=10, written_in_killasimi=1, readable=1, thing=1, dawn_period=1, codex=1, subject_tridesma_hiera=1),
    lessons=2,
    provides=memory.satisfaction,
)


# The World Despoil'd
#
# Subtitled 'the Flowers in the Waste': an epic poem that presents a medical treatise through allegory. The author is Gideon Dewulf, 5th Baron Brancrug, sometimes unkindly called 'the Cutter'.
# ---
# I'm Reading...
#
# The poem is a substantial variation on the Fisher-King tale. A wounded wasteland monarch learns that he and his land can be cured, but that the cure is their own response to ever more savage maladies…
# ---
# I've Read...
#
# Gideon concludes with a concrete example: that the Mysteries can be used to despoil 'mine own Soaks', but then the Soak can then be refined with sufficient Heart into 'the sanguis saltandis'.
the_world_despoild = card_type("the_world_despoild",
    attributes(tally_price=3, mystery_moon=6, readable=1, thing=1, subject_maggephene_mysteries=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.solace,
)


# The World Does Not Weep
#
# 'Brown' Joshua found this in a well in Hamath. There's an unlikely story that it was abandoned by Alexander during his retreat from Issus.
# ---
# I'm Reading...
#
# The unknown adept who wrote this proclaims: the world forgets, but the Ivory Dove does not. The text contains a number of prescriptions for ensuring that certain acts are remembered, including a rite which requires a sacrifice in a particularly monstrous mode...
# ---
# I've Read...
#
# The Hours tried to bury the memory of what happened to the Wheel, the Flint, the Tide, and the Seven-Coiled, but the Dove won't permit it. Nor will he permit what happened to the First Egg to be forgotten, although it is perhaps the one thing that the Watchman might ever forgive...
the_world_does_not_weep = card_type("the_world_does_not_weep",
    attributes(tally_price=4, written_in_aramaic=1, mystery_winter=10, readable=1, thing=1, solar_gothic_period=1, codex=1, subject_putrefactions_and_calcinations=1),
    lessons=2,
    provides=memory.hindsight,
)


# The Wound-Wounds
#
# 'A history of a hundred wars', sewn into a design of metallic threads that pursues itself across every page...
# ---
# I'm Reading...
#
# Darius and Alexander at Issus - the incandescent strivings of the Houses of Lancaster and York - the Second Worm War -
# ---
# I've Read...
#
# The final page of the book depicts the first battles of a war among Hours, but the threads fray into alternatives, unbraiding from History. One of those threads is a coarse iron wire whose twists suggest the Disciplines of the Scar invoked before a subterranean configuration of iron, fire, and night...
the_wound_wounds = card_type("the_wound_wounds",
    attributes(tally_price=2, mystery_edge=18, written_in_killasimi=1, readable=1, thing=1, curia_period=1, subject_disciplines_of_the_scar=1, codex=1),
    lessons=3,
    provides=memory.regret,
)


# Those Indignities Perpetrated By the Deceitful Fraternity of Obliviates
#
# It's not clear whether 'C.R.O.D', who is identified only by his initials, was in fact an initiate of the Obliviate order of immortal adepts. He wrote in the sixteenth century, after the order - if he is to be believed - had passed the height of its power.
# ---
# I'm Reading...
#
# 'FIFTY-EIGHT. That they did claim inheritance of the traditions of the House of Lethe, but that they have DISREGARDED both its most sacred and its most beautiful ceremonies where they are not found CONVENIENT. FIFTY-NINE...'
# ---
# I've Read...
#
# 'SEVENTY-ONE. The Glassfinger Toxin is no mere assassin's convenience for the Obliv-IDIOTS to confine to the disposal of their enemies. It has higher uses! Certainly it is a great matter of Winter, but I have already outlined the technique by which it may be fitted for its ultimate destiny...'
those_indignities_perpetrated_by_the_deceitful_fraternity_of_obliviates = card_type("those_indignities_perpetrated_by_the_deceitful_fraternity_of_obliviates",
    attributes(tally_price=3, written_in_latin=1, mystery_winter=6, readable=1, thing=1, baronial_period=1, codex=1, subject_ragged_crossroads=1),
    lessons=1,
    provides=memory.contradiction,
)


# Those Who Do Not Sleep
#
# The mystic Brodnax discusses the origins of the Sister-and-Witch, and of the Thunderskin.
# ---
# I'm Reading...
#
# The Sister-and-Witch were born in two wombs, one poor one rich, across the sea. The Sister was stronger in the aspect of Heart, and so their survival was assured; the Witch was stronger in the aspect of Grail, and so they were not satisfied...'
# ---
# I've Read...
#
# When the Sister and Witch came West, the Red Grail permitted their ascension, but then grew jealous of their power. It lured a great musician into the ranks of its Names, and caused him to be reborn from blood as a Heart-hour, so that the Grail might maintain dominion there also. But its victory is not assured.'
those_who_do_not_sleep = card_type("those_who_do_not_sleep",
    attributes(tally_price=5, written_in_fucine=1, mystery_heart=12, readable=1, thing=1, dawn_period=1, subject_surgeries_and_exsanguinations=1, codex=1),
    lessons=2,
    provides=memory.storm,
)


# Three Flowers Hath the Tree
#
# Ernestine Peterhans records her observations of the growths of trees and flowers around the Isle, and the omens and portents she attempts to draw from them - particularly the yew-tree in Earl Brian's Meadow, whose flowerings are sometimes eccentric.
# ---
# I'm Reading...
#
# Ernestine observes that in years when the tree flowers black, 'troubling Secrets arise'; when it flowers red, war and fires follow; and that no Dewulf heir has ever been born in a year when it flowers white...
# ---
# I've Read...
#
# Ernestine attempts to use the tree's growths to advantage in her business affairs, but it fails. She is evidently very concerned when Hendrik Dewulf's grandson Giles runs off with 'the Pale Trollop Hafren' in a year when the tree flowers white - she begins to fear she has entirely misinterpreted all the relevant omens. She is deeply concerned for the continuation of the Dewulf line, and prays for Giles' return.
three_flowers_hath_the_tree = card_type("three_flowers_hath_the_tree",
    attributes(tally_price=3, mystery_nectar=4, readable=1, thing=1, subject_leaves_and_thorns=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.gossip,
)


# To a Pale Lady
#
# A collection of Franklin Bancroft's letters to Eva Dewulf.
# ---
# I'm Reading...
#
# There is a substantial body of erotic pleading and half-finished poetry, but also learned discursions on matters mythical and marine, as well as notes towards a comic opera on which Franklin and Eva were apparently collaborating.
# ---
# I've Read...
#
# 'Do not return, O my Light, to the Sea. None of us can be what we were; that is History's curse. None of us know what we may be; that is History's gift. Your mothers, and the mothers of your mothers, are caught in Eternity's jaws like a robe-hem in a trap. It is the pearl that shines; but the tide that returns.'
to_a_pale_lady = card_type("to_a_pale_lady",
    attributes(tally_price=2, mystery_moon=8, readable=1, thing=1, curia_period=1, subject_pearl_and_tide=1, codex=1),
    lessons=2,
    provides=memory.salt,
)


# Towards a Fundamental Aesthetic
#
# Or, 'The House of Glass'. Julian Coseley considered this his masterwork. [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...
#
# Techniques for perception and analysis which permit invidious and apocalyptic conclusions. Probably the most assiduously suppressed book in history. The entire run was destroyed - even the presses were melted and dispersed - but the manuscript edition has survived.
# ---
# I've Read...
#
# The perfect hegemony of the Hours is, perhaps, eternal. But Coseley proposes and describes 'Confinement Inescapable', aesthetic and optical techniques which might contain even an Hour, profoundly disrupting the order of the Mansus. He presents this as his own work, but there are hints here and there that he received inspiration or even assistance from the Nowhere-Hour named Snow.
towards_a_fundamental_aesthetic = card_type("towards_a_fundamental_aesthetic",
    attributes(tally_price=8, written_in_ericapaean=1, mystery_knock=10, readable=1, thing=1, curia_period=1, subject_glassblowing_and_vesselcrafting=1, codex=1),
    lessons=2,
    provides=memory.inescapable_confinement,
)


# Towards a Fundamental Aesthetic: Second Edition
#
# Or, 'The Refinements of Light'. Julian Coseley had never wanted or expected to write a second edition of his masterwork... [This book houses a <i>numen</i> - a truth so powerful it can perhaps believe itself.]
# ---
# I'm Reading...

# Julian Coseley long regarded Solomon Husher as a charlatan. But his friend Nina Lagasse painted three paintings before her death in 1895… and these paintings apparently convinced Coseley to change his mind. With considerable irritation, he revised his magnum opus.
# ---
# I've Read...

# The perfect hegemony of the Hours is, perhaps, eternal. Coseley had always championed History rather than Eternity - the exceptions, limitations, contradictions of freedom. But Husher's and Lagasse's work convinced him to believe in the 'paradox of the eternal ending', a means in which perfection might be reconciled with freedom. He's not happy about it. This is perhaps the angriest book ever written in support of a peaceful philosophy of acceptance. But Coseley was always scrupulous about his conclusions.
towards_a_fundamental_aesthetic_second_edition = card_type("towards_a_fundamental_aesthetic_second_edition",
    attributes(tally_price=8, written_in_ericapaean=1, mystery_winter=10, readable=1, thing=1, subject_sights_and_sensations=1, codex=1, nocturnal_period=1),
    lessons=2,
    provides=memory.a_final_understanding,
)


# Travelling at Night, vol 1
#
# The annotated dream-journals of Christopher Illopoly, sometimes called 'the only readable occultist': literate, entertaining, bewildering.
# ---
# I'm Reading...
#
# 'The Wood lies outside the walls of the Mansus. As any student of the Histories knows, the Mansus has no walls.'
# ---
# I've Read...
#
# Illopoly describes how he came to make repeated visits to a dream-Wood via what he calls silver dreams. 'Trying to think your way to the Wood,' he explains, 'is like thinking your way to being in love. But I did find a Secret that helped.'
travelling_at_night_vol_1 = card_type("travelling_at_night_vol_1",
    attributes(tally_price=1, mystery_knock=4, readable=1, thing=1, subject_edicts_liminal=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.impulse,
)


# Travelling at Night, vol 2
#
# The annotated dream-journals of Christopher Illopoly, sometimes called 'the only readable occultist': literate, entertaining, bewildering.
# ---
# I'm Reading...
#
# There is an extensive discussion of the comparisons between Illopoly's own dreams and those of the Emperor Elagabalus, who Illopoly regards as a dupe or avatar of the Sun-in-Rags. 'The White is west of the world,' Illopoly remarks, 'and Winter does not wait forever.'
# ---
# I've Read...
#
# 'Elagabalus found his way to the White Door at last, thankfully. Speech can't pass the White Door, and honestly, Elagabalus never had anything very interesting to say. I tried to follow in his footsteps, but I never learnt enough of the White. I suppose I'm thankful for that, too. But here's what I do know...'
travelling_at_night_vol_2 = card_type("travelling_at_night_vol_2",
    attributes(tally_price=1, mystery_sky=6, readable=1, thing=1, subject_sights_and_sensations=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.solace,
)


# Travelling at Night, vol 3
#
# The annotated dream-journals of Christopher Illopoly, sometimes called 'the only readable occultist': literate, entertaining, bewildering.
# ---
# I'm Reading...
#
# Illopoly's disquisitions on fire and the Unburnt God are interrupted by passages of distractingly erotic poetry addressed to 'Baldomera'.
# ---
# I've Read...
#
# 'To reach the Stag Door, I believe that all you really need is to want something enough. But I've never wanted anything that much, except of course Baldomera, and I'm very much afraid that the knot in the story is this: what Baldomera wants is the Stag Door. But here's something I learnt in Persia. Perhaps it'll teach you what *you* want.'
travelling_at_night_vol_3 = card_type("travelling_at_night_vol_3",
    attributes(tally_price=1, mystery_knock=4, readable=1, thing=1, subject_door_and_wall=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.pattern,
)


# Twenty-Six Enticements, Seven Torments
#
# The painter Niels Frederik Malskær, notoriously, attempted a series of paintings based on the Torments. By the Fifth Torment, the demands of the painting had grown so dire that he died of blood loss. The diagrams in this text are thankfully less detailed.
# ---
# I'm Reading...
#
# The Enticements of the Grail outnumber its Torments, but its Torments are its final nature. Birth is the First Torment, and Thirst the Seventh'.
# ---
# I've Read...
#
# Through the enumeration of the Grail's enticements and torments winds the sorrowful history of the Witches of the Dry Land: the ordeal of birth from two wombs, their struggle from and supplication of the Grail, the yearning for union which drives them all.
twenty_six_enticements_seven_torments = card_type("twenty_six_enticements_seven_torments",
    attributes(tally_price=1, written_in_fucine=1, mystery_grail=14, readable=1, thing=1, subject_resurgences_and_emergences=1, nocturnal_period=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# Two Wombs, One Heart
#
# A fanciful account by Thirza Blake of the early life of the Twins - their time as mortals before they became Hours or even Long, in a 'dry kingdom beyond the Western Sea' which Thirza suggests might have been ancient Mexico.
# ---
# I'm Reading...
#
# 'It is widely known that the Sister was rich and the Witch poor. It is widely known that the Witch loved the Sister first. It is not widely known that the Witch was first employed to teach the Sister the arts of embroidery…'
# ---
# I've Read...
#
# Although Thirza is very probably just making up much of the story, there are long passages expounding notable techniques of weave-work and thread-feit. In particular, when Witch and Sister flee across the Sea to be together, Thirza explains how they fashioned a 'peace-weave' with Heart and these arts, and then, to tame the winds, called on Heart again to swaddle the thunder in the peace-weave.
two_wombs_one_heart = card_type("two_wombs_one_heart",
    attributes(tally_price=2, mystery_heart=8, written_in_killasimi=1, readable=1, thing=1, curia_period=1, subject_stitching_and_binding=1, codex=1),
    lessons=2,
    provides=memory.satisfaction,
)


# Ud Rocashaas
#
# An anonymous confessional account of unsanctioned activities by the nuns of St Brandan's. The title is a Henavek phrase that might be translated as 'the spirit flees the shadowed places.'
# ---
# I'm Reading...
#
# The author writes guiltily of her dealings with hill-children and Carapace-relics - she suggests she herself has a connection with one of the Carapace-kinds. Most of these dealings are trivial, but she claims to have arranged the death of the Marcher Lord William de Braose, called Black William...
# ---
# I've Read...
#
# De Braose' wife, Eva, evidently seeks the Abbey's help to free her from her hated husband. Subsequently he is found in the bed-chamber of the wife of Llywelyn the Great, Prince of the Welsh, while attempting to negotiate the marriage of his daughter (also Eva) to Llywelyn's son. Llywellyn takes this badly, de Braose is hanged, the elder Eva inherits his estates and makes a substantial endowment to St Brandan's. In the author's telling, de Braose was 'innocent of all but cruelty' and the adulterer found in the bed-chamber was a shape-changing 'undergoer'...
ud_rocashaas = card_type("ud_rocashaas",
    attributes(tally_price=4, written_in_kernewek_henavek=1, mystery_scale=10, readable=1, thing=1, solar_gothic_period=1, subject_stone_stories=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# Unhatched Hymns
#
# Hymns attributed to Saint Lucia the Eyeless, patron of glassworkers and Name of the Hour called Meniscate.
# ---
# I'm Reading...
#
# The hymns venerate every sanctioned Hour, celebrating them as the Sun Undivided, but also suggesting that each Hour may <i>become</i> the next - Madrugad to Watchman, Watchman to Wolf, and so on.
# ---
# I've Read...
#
# The Hymn of the Phases celebrates the Meniscate 'from whom we do not turn', for the truth which is beauty, the beauty which is truth, and the perfect balance between the two. The Hymn of the Reflections, more puzzlingly, celebrates the Meniscate as the 'Sister of Janus, Mother of Shadow', whose 'visage wondrous in emptiness' can reveal all truths.
unhatched_hymns = card_type("unhatched_hymns",
    attributes(tally_price=4, mystery_lantern=10, written_in_sabazine=1, readable=1, thing=1, solar_gothic_period=1, subject_sacra_solis_invicti=1, codex=1),
    lessons=2,
    provides=memory.savage_hymn,
)


# Vinzant's Minglings
#
# The metallurgist and 'sky-smith' Everett Vinzant speaks of 'the sacred alloys', 'the alloys eternal', 'the alloys sufficient', 'the alloys intendant'…
# ---
# I'm Reading...
#
# Everett describes the voices and powers of mortals and immortals based on their composition by analogy to the sounds and strengths of bells based on the metals of their casting…
# ---
# I've Read...
#
# Vinzant warns that the mingling of metals of 'too great a nobility' can produce 'the alloys incestuous'. He suggests very cautiously that the means used by the Sovereigns of the Leashed Flame to produce their heirs may have analogous issues: 'for though the Crime of the Sky might be circumvented, yet the Law remaineth the Law, in Spirit as in Letter'.
vinzants_minglings = card_type("vinzants_minglings",
    attributes(tally_price=3, mystery_forge=4, readable=1, thing=1, codex=1, baronial_period=1, subject_bells_and_brazieries=1),
    lessons=1,
    provides=memory.foresight,
)


# Wainscot Histories
#
# Subtitled 'Stories from Behind the Walls': a miscellany of non-traditional histories, including battles not generally acknowledged and countries which appear on no map, told in a playful, apparently fictional manner.
# ---
# I'm Reading...
#
# Gore does not mention the Mansus directly, but constant coy metaphorical references to 'Ascending the Staircase of Years', to 'the Doors of Sleep', and to 'the Blue Light of Dawn' suggest he had commerce with the unseen world.
# ---
# I've Read...
#
# 'It was common in that time to speak of the Division of the Sun; by which Contemporaries understood, the irruption of Barbarian Forces, and of their uncouth Gods.'
wainscot_histories = card_type("wainscot_histories",
    attributes(tally_price=3, mystery_lantern=6, readable=1, thing=1, subject_auroral_contemplations=1, codex=1, baronial_period=1),
    lessons=1,
    provides=memory.contradiction,
)


# Warming Draughts to Uplift the Heart
#
# A wonderful compendium of healing tisanes compiled by Natan of Regensburg.
# ---
# I'm Reading...
#
# Natan and his family sought sanctuary at Brancrug but were confined to the Barber's Tower (as it was then known) by the suspicions of the monks, but won more freedom over time…
# ---
# I've Read...
#
# Natan records his delight on the day he was finally permitted access to Earl Brian's Meadow. He speaks very carefully of the black bird he met in its branches, and the 'treasures of music and history' that it brought him when he healed its wing.
warming_draughts_to_uplift_the_heart = card_type("warming_draughts_to_uplift_the_heart",
    attributes(tally_price=2, written_in_greek=1, mystery_heart=8, readable=1, thing=1, curia_period=1, subject_herbs_and_infusions=1, codex=1),
    lessons=2,
    provides=memory.impulse,
)


# What Does Not Bark
#
# Alexander Probst writes warily of 'Calyptra' - a law, principle or society which prevents the dissemination of dangerous knowledge.
# ---
# I'm Reading...
#
# 'Calyptra, like the planet that occludes the star, or the Doylian dog that fails to bark, can be identified only by its absence. Even the name, I think, must be a mask…'
# ---
# I've Read...
#
# 'Calyptra is said to make exceptions specifically for the libraries of the Watchman's Tree. Does it make those exceptions so the Hours can make use of them?'
what_does_not_bark = card_type("what_does_not_bark",
    attributes(tally_price=1, mystery_moon=4, readable=1, thing=1, subject_edicts_inviolable=1, nocturnal_period=1, codex=1),
    lessons=1,
    provides=memory.storm,
)


# Where Has She Gone?
#
# 'The Speeth' - perhaps a single adept, perhaps a council of scholars - hypothesises secret events from limited evidence with persuasive accuracy.
# ---
# I'm Reading...
#
# The Vagabond is recorded to have travelled not only the Mansus and the Wood, not only all nine continents, but also places forbidden to other Hours...
# ---
# I've Read...
#
# From Hour-gossip and invisible lore, Speeth deduces that the Vagabond has visited Nowhere, but that she will not return. He also asserts that she has yet to visit the Glory, but that inevitably, this must be her goal.
where_has_she_gone = card_type("where_has_she_gone",
    attributes(tally_price=5, mystery_rose=16, written_in_vak=1, readable=1, thing=1, subject_sand_stories=1, dawn_period=1, codex=1),
    lessons=3,
    provides=memory.intuition,
)


# White Jade Tablet
#
# Supposedly copied from a tablet of white jade which serves as the Covenant-stone of the Grove of the Green Immortals - the token which gives that Library shelter beneath the Watchman's Tree.
# ---
# I'm Reading...
#
# 'When humankind emerged from the weft of the Roots, we were smeared with the filth of crumbled ages. The foolish sought to wash it from themselves, but our skins were yet soft, and fell easily from us…'
# ---
# I've Read...
#
# The Tablet expounds the dangers (and pleasures) of abandoning appearances in search of essence. Along the way, it reveals the secret of Skinshuck Mead, which can be brewed from honey by application of the Rites of the Roots, if enough Moth-aspect is present.
white_jade_tablet = card_type("white_jade_tablet",
    attributes(tally_price=5, written_in_cracktrack=1, mystery_moth=14, readable=1, thing=1, dawn_period=1, codex=1, subject_rites_of_the_roots=1),
    lessons=2,
    provides=memory.impulse,
)


# Xenodicene Odes
#
# Poetry attributed to Xenodice, Name of the Horned-Axe.
# ---
# I'm Reading...
#
# In the House of Lethe's heyday, it held an annual competition where its initiates competed to produce the best ode in Xenodice's honour. So there are still a lot of odes out there.
# ---
# I've Read...
#
# It has never been clear why the Letheans, who avoided traffic with the Hours with the occasional exception of the Elegiast, would devote effort to a Name of the Horned-Axe. Perhaps Xenodice was just a suitably challenging subject…
xenodicene_odes = card_type("xenodicene_odes",
    attributes(tally_price=5, mystery_knock=21, written_in_vak=1, readable=1, thing=1, multitudinuous=1, dawn_period=1, subject_preliminal_meter=1, codex=1),
    lessons=3,
    provides=memory.confounding_parable,
)

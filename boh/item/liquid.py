from ..item import memory
from ..model import attributes, card_type


# Amethyst Ampoule
#
# Were it released from the glass, it would be quite another colour.
# ---
# Scrutiny
#
# A violet stain; then nothing. [There are Prentice-level Knock recipes that can craft this.]
amethyst_ampoule = card_type("amethyst_ampoule",
    attributes(heart=2, knock=2, thing=1, liquid=1, glass=1),
    consider_output = memory.regret,
)


# Ashartine
#
# Lies written in Ashartine tend to fade or be misspelt. It's legible in the dark. An Ink of Revelation.
# ---
# Scrutiny
#
# If dark were light… [There are Keeper-level Sky and Lantern recipes that can craft this from Ichor Vitreous.]
ashartine = card_type("ashartine",
    attributes(forge=1, lantern=6, sky=2, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Asimel
#
# A silver ink that can only be made and used in dreams. An Ink of Revelation.
# ---
# Scrutiny
#
# A silvery glimmer like a spilt star. [Scholar-level Moon and Moth recipes exist that can craft this with lenses or liquids.]
asimel = card_type("asimel",
    attributes(knock=3, moon=5, moth=1, rose=1, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Azoth
#
# A solvent of frightening voracity.
# ---
# Scrutiny
#
# Once spilt, nothing remains.  [There are Keeper-level Forge recipes that can create this with the assistance of Orichalcum, among other things.]
azoth = card_type("azoth",
    attributes(forge=2, knock=6, thing=1, liquid=1),
    consider_output = memory.foresight,
)


# Black Sapphire Wash
#
# The colour, perhaps, of the doors of the House of the Moon.
# ---
# Scrutiny
#
# 'When the light is extinguished, the shadow persists. After the House of the Sun, the House of the Moon.' [There are Keeper-level Moon recipes which can create this from Asimel.]
black_sapphire_wash = card_type("black_sapphire_wash",
    attributes(moon=6, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Bucket of Seawater
#
# Flecks of foam float on the surface.
# ---
# Scrutiny
#
# Fingers rock-pool chill…
bucket_of_seawater = card_type("bucket_of_seawater",
    attributes(moon=1, comfort=1, liquid=1),
    consider_output = memory.sight,
)


# Catwink
#
# The smell of catwink puts off vermin; but it is very difficult to read in sunlight. An Ink of Containment.
# ---
# Scrutiny
#
# On close exposure, the smell tends to put off humans, too. [There are Prentice-level Moon recipes that can craft this.]
catwink = card_type("catwink",
    attributes(edge=1, grail=1, moon=2, scale=2, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Cuckoo-Honey
#
# The Blomberende were rogues and trickster-heroes among the Carapace-kinds: ingenious, brave, prolific, untrustworthy. In Numa, their children might yet bring their gifts to ordinary hives…
# ---
# Scrutiny
#
# A fleetingly familiar taste, and a prickling in the skull…  not surprising, perhaps, that it can be brewed into Skinshuck Mead with the great arts of Moth.
cuckoo_honey = card_type("cuckoo_honey",
    attributes(edge=2, heart=1, knock=1, moth=3, nectar=2, scale=3, thing=1, sustenance=1, cooking_ingredient=1, liquid=1),
    consider_output = memory.old_moment,
)


# Gideon's Soaks
#
# A therapeutic collection of beneficial bottles.
# ---
# Scrutiny
#
# Invigorating. [There are Scholar-level Heart recipes which can craft this from suitable liquids.]
gideons_soaks = card_type("gideons_soaks",
    attributes(forge=2, heart=4, nectar=3, winter=2, thing=1, liquid=1),
    consider_output = memory.solace,
)


# Glassfinger Toxin
#
# 'What is within, without; what is without, within.' A poison sacred to the votaries of the Meniscate.
# ---
# Scrutiny
#
# Careful… [There are Scholar-level Knock recipes - sometimes Scale - that can be used with a suitable liquid to craft this.]
glassfinger_toxin = card_type("glassfinger_toxin",
    attributes(forge=2, knock=4, lantern=2, thing=1, liquid=1),
    consider_output = memory.regret,
)


# Holiest Hemolymph
#
# Thirza Blake claimed that she first synthesised this from her own tears. She was almost certainly lying.
# ---
# Scrutiny
#
# The faintest beating of wings…
holiest_hemolymph = card_type("holiest_hemolymph",
    attributes(moth=4, nectar=4, scale=4, thing=1, liquid=1),
    consider_output = memory.impulse,
)


# Honey
#
# The blood of the Hour called Malachite; also and furthermore, wonderful on toast.
# ---
# Scrutiny
#
# The source, among other things, of Skinshuck Mead, when brewed with the great arts of Moth…
honey = card_type("honey",
    attributes(heart=1, moth=1, nectar=1, thing=1, sustenance=1, liquid=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Houndsgall
#
# Books written in Houndsgall are more likely to return to their owner, or one to whom they have been legitimately sold. An Ink of Containment.
# ---
# Scrutiny
#
# It'll be hell to get off my fingers. [There are Keeper-level Scale recipes that can produce this with the tacit assistance of a Living Relic.]
houndsgall = card_type("houndsgall",
    attributes(edge=1, heart=2, scale=5, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Ichor Auroral
#
# No dawn knows only a single colour. No sky knows only a single dawn.
# ---
# Scrutiny
#
# A soft sense of morning… [There are Scholar-level Rose and Sky recipes that can be used to craft this in the presence of a light source.]
ichor_auroral = card_type("ichor_auroral",
    attributes(lantern=4, rose=2, thing=1, liquid=1, pigment=1),
    consider_output = memory.intuition,
)


# Ichor Vitreous
#
# A pale and watchful fluid that can be gathered, sometimes, when the Door-in-the-Eye is opened.
# ---
# Scrutiny
#
# It stings like wasps. [There are Scholar-level Lantern recipes that can be used to craft this with glass.]
ichor_vitreous = card_type("ichor_vitreous",
    attributes(lantern=4, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Iotic Essence
#
# 'In the later operations of the Forge, the Madrugad yields to the true Forge of Days, and the essence begins to redden.' The bit about the 'true Forge of Days' nearly got St Melancthe burned for heresy, but no-one ever said she was wrong about the second part.
# ---
# Scrutiny
#
# Redder than sunset. [A range of Forge recipes can be used to create Iotic Essence from a range of precursors.]
iotic_essence = card_type("iotic_essence",
    attributes(forge=5, lantern=3, thing=1, liquid=1, pigment=1, fuel=1),
    consider_output = memory.foresight,
)


# January Sanguinary
#
# Also called <i>sanguis saltandis</i> or, by the ignorantly superstitious, 'true blood of St Januarius'.
# ---
# Scrutiny
#
# 'And so it will not, will not, will not stop dancing.' [With Keeper-level Heart recipes, this can be crafted from Gideon's Soaks.]
january_sanguinary = card_type("january_sanguinary",
    attributes(heart=5, knock=3, sky=3, thing=1, liquid=1),
    consider_output = memory.thunderskins_paean,
)


# Kerosene
#
# For the brightest flame.
# ---
# Scrutiny
#
# Reeking.
kerosene = card_type("kerosene",
    attributes(forge=3, thing=1, liquid=1, fuel=1),
    consider_output = memory.touch,
)


# Marakat
#
# The <i>encaustum terminale</i> of the Fifth History. The colour of the Principle that once occupied the place that Heart does now. In the Fifth History itself, the cult of Marakat was everywhere suppressed, but it's sometimes been venerated otherwise. [Use an Encaustum ink with your Journal to make Determinations and record Histories. If the Hours listen, the world changes.]
# ---
# Scrutiny
#
# Another history spilt… [There are Keeper-level Nectar recipes that can craft this from Leathy.]
marakat = card_type("marakat",
    attributes(grail=7, knock=7, nectar=7, thing=1, liquid=1, encaustum_terminale=1, ink=1),
    consider_output = memory.scent,
)


# Nillycant
#
# The <i>encaustum terminale</i> of the Third History. It's the bleak white-blue of Winter. It has spawned an itinerant order of secret celebrants who regard Worms as semi-gods, and who are sometimes called on to celebrate difficult funerals. [Use an Encaustum ink with your Journal to make Determinations and record Histories. If the Hours listen, the world changes.]
# ---
# Scrutiny
#
# Another history spilt… [There are Keeper-level Winter recipes that can craft this from Solomon's Preparation, or from Glassfinger Toxin]
nillycant = card_type("nillycant",
    attributes(edge=7, scale=7, winter=7, thing=1, liquid=1, ink=1, encaustum_terminale=1),
    consider_output = memory.scent,
)


# Orpiment Exultant
#
# The <i>encaustum terminale</i> of the Fourth History. It's the incandescent orange of Forge. One ingredient - it's been, as it were, long-rumoured - is the blood of candescents. Certain Masonic and related traditions venerate what they call 'O.E'.  [Use an Encaustum ink with your Journal to make Determinations and record Histories. If the Hours listen, the world changes.]
# ---
# Scrutiny
#
# Another history spilt… [There are Keeper-level Forge recipes that can craft this from Iotic Essence.]
orpiment_exultant = card_type("orpiment_exultant",
    attributes(forge=7, heart=7, sky=7, thing=1, liquid=1, ink=1, encaustum_terminale=1),
    consider_output = memory.scent,
)


# Oscillate Oil
#
# Cater & Hero's Finest Oscillate Oil.
# ---
# Scrutiny
#
# A volatile substance useful for agitation, lubrication and acceleration.
oscillate_oil = card_type("oscillate_oil",
    attributes(forge=1, moth=2, thing=1, liquid=1, fuel=1),
    consider_output = memory.impulse,
)


# Paint: Bosk-Green
#
# The Wood is probably not this colour.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_bosk_green = card_type("paint_bosk_green",
    attributes(nectar=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Dusk-Blue
#
# This paint is the precise colour of the Atlantic Ocean at four o'clock on a clear autumn afternoon.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_dusk_blue = card_type("paint_dusk_blue",
    attributes(moon=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Green
#
# Trees are rarely this colour.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_green = card_type("paint_green",
    attributes(nectar=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Moth-Gold
#
# Moths are seldom this colour.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink. [There is a Prentice-level Moth recipe which can be used to create more.]
paint_moth_gold = card_type("paint_moth_gold",
    attributes(moth=2, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Palest Blue
#
# Snow is not quite this colour.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_palest_blue = card_type("paint_palest_blue",
    attributes(winter=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Pink
#
# People are never this colour.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_pink = card_type("paint_pink",
    attributes(heart=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Red
#
# Blood is only occasionally this colour. If they say more research is needed, don't listen.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_red = card_type("paint_red",
    attributes(rose=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paint: Yellow
#
# This paint is nothing like the sun.
# ---
# Scrutiny
#
# Spilt paint is worse even than spilt ink.
paint_yellow = card_type("paint_yellow",
    attributes(lantern=1, thing=1, liquid=1, pigment=1),
    consider_output = memory.sight,
)


# Paraffin
#
# For a bright flame.
# ---
# Scrutiny
#
# Reeking.
paraffin = card_type("paraffin",
    attributes(forge=2, thing=1, liquid=1, fuel=1),
    consider_output = memory.touch,
)


# Perhibiate
#
# Which binds to the one whose name is there written. A minor Ink of Power.
# ---
# Scrutiny
#
# And so my name be not forgotten… [Perhibiate can be crafted with certain Prentice-leve Heart recipes.]
perhibiate = card_type("perhibiate",
    attributes(heart=2, lantern=2, scale=2, winter=1, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Perinculate
#
# Deadly. Use gloves to read texts produced with this pigment. An Ink of Power (sometimes considered an Unsanctioned Ink).
# ---
# Scrutiny
#
# Perilous indeed. [There are Scholar-level Edge recipes that can craft this from leaves.]
perinculate = card_type("perinculate",
    attributes(edge=4, grail=1, scale=4, thing=1, liquid=1, ink=1),
    consider_output = memory.fear,
)


# Petrol
#
# Black oil rendered pale.
# ---
# Scrutiny
#
# Reeking.
petrol = card_type("petrol",
    attributes(forge=2, thing=1, liquid=1, fuel=1),
    consider_output = memory.touch,
)


# Porphyrine
#
# The <i>encaustum terminale</i> of the Second History. It's the glowing crimson-mauve of the Secret Histories. Porphyrine was venerated in secret by a confraternity of corresponding Cluniacs and Benedictines. [Use an Encaustum ink with your Journal to make Determinations and record Histories. If the Hours listen, the world changes...
#
# Porphyrine might also be used to compose a petition for the labyrinth season, if you can provide at least 20 of <sprite name=knock>, <sprite name=rose>, or <sprite name=moon>; no <sprite name=edge>, <sprite name=heart>, or <sprite name=winter> at all; and suitable writing material.]
# ---
# Scrutiny
#
# Another history spilt… [Certain Keeper-level Lantern and Rose recipes can brew this from Ichor Auroral, and perhaps from other things.]
porphyrine = card_type("porphyrine",
    attributes(knock=7, moon=7, rose=7, thing=1, liquid=1, ink=1, encaustum_terminale=1),
    consider_output = memory.scent,
)


# Regensburg Balm
#
# An invaluable herbal cure introduced to Hush House by the physician Natan after his exile from Regensburg.
# ---
# Scrutiny
#
# Soothing. [There are Prentice-level Heart recipes which can be used to craft this.]
regensburg_balm = card_type("regensburg_balm",
    attributes(heart=2, nectar=2, thing=1, liquid=1),
    consider_output = memory.sight,
)


# Scintillate Oil
#
# Cater & Hero's Finest Scintillate Oil.
# ---
# Scrutiny
#
# A shimmering substance useful for ignition, illumination and chromatiferation.
scintillate_oil = card_type("scintillate_oil",
    attributes(forge=2, lantern=1, thing=1, liquid=1, fuel=1),
    consider_output = memory.foresight,
)


# Stargall Ink
#
# An ink traditionally (but only rarely) made with meteoric iron; a minor Ink of Power.
# ---
# Scrutiny
#
# Faintly glimmering. [There are Prentice-level Sky recipes which can create this.]
stargall_ink = card_type("stargall_ink",
    attributes(forge=1, rose=1, sky=2, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)


# Turpentine
#
# An odorous eraser of errors.
# ---
# Scrutiny
#
# Well, my hands are clean…
turpentine = card_type("turpentine",
    attributes(forge=1, winter=1, thing=1, liquid=1, fuel=1),
    consider_output = memory.touch,
)


# Umbrous Oil
#
# Cater & Hero's First-Grade Umbrous Oil.
# ---
# Scrutiny
#
# A shadowy substance useful in embrocation, dissimulation, and disillumination. (Not flammable under most rational conditions.)
umbrous_oil = card_type("umbrous_oil",
    attributes(forge=1, moon=2, thing=1, liquid=1),
    consider_output = memory.intuition,
)


# Uzult
#
# The ink in which the First History was recorded by the Unwise Mortal. Uzult is the bright yellow-gold of Lantern. Light lingers on it for a little while even in the dark. Gold is not needed to mix Uzult, but amber is. Unobtrusive shrines to Uzult could sometimes be found in the churches of the Unconquered Sun.  [Use an Encaustum ink with your Journal to make Determinations and record Histories. If the Hours listen, the world changes.]
# ---
# Scrutiny
#
# Another history spilt… [There are Keeper-level Lantern recipes which can be used to craft this from Xanthotic Essence.]
uzult = card_type("uzult",
    attributes(lantern=7, moth=7, sky=7, thing=1, liquid=1, ink=1, encaustum_terminale=1),
    consider_output = memory.scent,
)


# Wolf-Snow Ampoule
#
# Far too cold ever to melt in anything but the hottest noonday sun. It will, very gradually, consume human flesh.
# ---
# Scrutiny
#
# That could have been worse.
wolf_snow_ampoule = card_type("wolf_snow_ampoule",
    attributes(winter=4, thing=1, liquid=1),
    consider_output = memory.sight,
)


# Xanthotic Essence
#
# The rich gold of a summer afternoon. 'If sunlight precedes moonlight,' St Anselm observed, 'the Meniscate must precede the Madrugad; and the light that was lost will remain.'
# ---
# Scrutiny
#
# Yellower than buttercups. [Various Lantern recipes can be used to create Xanthotic Essence from various precursors.]
xanthotic_essence = card_type("xanthotic_essence",
    attributes(forge=2, knock=2, lantern=5, thing=1, liquid=1, pigment=1),
    consider_output = memory.revelation,
)


# Yewgall Ink
#
# A variant of iron gall ink, particularly difficult to erase; a minor Ink of Power.
# ---
# Scrutiny
#
# The deepest of blackish greens. [There are Prentice-level Nectar recipes which can create this.]
yewgall_ink = card_type("yewgall_ink",
    attributes(moth=1, nectar=2, thing=1, liquid=1, ink=1),
    consider_output = memory.scent,
)

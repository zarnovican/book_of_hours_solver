from ..item import memory
from ..model import attributes, card_type


# Armagnac d'Ys (Glass)
#
# Armagnac can only come from Gascony… but, if you believe M. Corentin, his vineyard began with vine-cuttings from Ys beyond the sea.
# ---
# Scrutiny
#
# Spiced amber and midnight berries.
armagnac_dys_glass = card_type("armagnac_dys_glass",
    attributes(grail=1, moon=2, nectar=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Armagnac d'Ys (Bottle)
#
# Armagnac can only come from Gascony… but, if you believe M. Corentin, his vineyard began with vine-cuttings from Ys beyond the sea.
# ---
# Scrutiny
#
# Spiced amber and midnight berries.
armagnac_dys_bottle = card_type("armagnac_dys_bottle",
    attributes(grail=1, moon=2, nectar=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, armagnac_dys_glass),
)


# Black Dove Wine
#
# A bottle of extraordinary age; a modest slosh of dark, heavily sedimented liquid behind the grimy glass. Just how old is this? Might it still be drinkable? [This wine cannot be served into glasses; drink it, gift it, or keep it.]
# ---
# Scrutiny
#
# The taste is not 'good' in any reasonable sense, and since no trace of alcohol remains, neither is this wine in any reasonable sense. But the layers and flavours go on and down, as if I were descending a cramped passage into the earth: moss, oak, deep tar, a sudden bright wince like grapes, and then at last stone's long savour fading. I'll taste it again tonight in every dream.
black_dove_wine = card_type("black_dove_wine",
    attributes(grail=4, heart=4, moon=4, nectar=4, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.old_moment,
)


# C&H Second Flush Assam (Cup)
#
# Tea from the land of the <i>real</i> unicorn, imported by Cater & Hero.
# ---
# Scrutiny
#
# A wonderfully full-bodied taste, bright as morning.
ch_second_flush_assam_cup = card_type("ch_second_flush_assam_cup",
    attributes(edge=1, knock=1, lantern=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# C&H Second Flush Assam (Pot)
#
# Tea from the land of the <i>real</i> unicorn, imported by Cater & Hero.
# ---
# Scrutiny
#
# A wonderfully full-bodied taste, bright as morning.
ch_second_flush_assam_pot = card_type("ch_second_flush_assam_pot",
    attributes(edge=1, knock=1, lantern=1, thing=1, liquid=1, beverage=1, restorative=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, ch_second_flush_assam_cup),
)


# Dandelion Wine (Glass)
#
# Home-made flower wine.
# ---
# Scrutiny
#
# Bottled summer, they call it, and this is why.
dandelion_wine_glass = card_type("dandelion_wine_glass",
    attributes(lantern=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Dandelion Wine
#
# Home-made flower wine.
# ---
# Scrutiny
#
# Bottled summer, they call it, and this is why.
dandelion_wine = card_type("dandelion_wine",
    attributes(lantern=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, dandelion_wine_glass),
)


# Dawnlion Coffee (Cup)
#
# Coffee from beyond the great deserts.
# ---
# Scrutiny
#
# Rich fruity flavours.
dawnlion_coffee_cup = card_type("dawnlion_coffee_cup",
    attributes(forge=1, lantern=2, scale=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Dawnlion Coffee (Pot)
#
# Coffee from beyond the great deserts.
# ---
# Scrutiny
#
# Rich fruity flavours.
dawnlion_coffee_pot = card_type("dawnlion_coffee_pot",
    attributes(forge=1, lantern=2, scale=1, thing=1, liquid=1, beverage=1, restorative=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, dawnlion_coffee_cup),
)


# Domaine Raveline (Glass)
#
# The Ravelines abandoned their lands, and yet, someone is still making this wine.
# ---
# Scrutiny
#
# Plummy; almost meaty.
domaine_raveline_glass = card_type("domaine_raveline_glass",
    attributes(grail=2, scale=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Domaine Raveline (Bottle)
#
# The Ravelines abandoned their lands, and yet, someone is still making this wine.
# ---
# Scrutiny
#
# Plummy; almost meaty.
domaine_raveline_bottle = card_type("domaine_raveline_bottle",
    attributes(grail=2, scale=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, domaine_raveline_glass),
)


# Eigengrau
#
# 'If Greydawn Oil were drinkable…'
# ---
# Scrutiny
#
# A bitter but heady liquor. Drink it, and vision persists even after you close your eyes. [There are Prentice-level recipes to craft this with Winter - or, occasionally, Lantern.]
eigengrau = card_type("eigengrau",
    attributes(moon=1, winter=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Elderflower Cordial
#
# Wrung from sweet white flowers.
# ---
# Scrutiny
#
# Favoured by the brethren of St Brandan's in the days before the Dissolution.
elderflower_cordial = card_type("elderflower_cordial",
    attributes(heart=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Evening Isles Coffee (Cup)
#
# Coffee from beyond the sunset sea.
# ---
# Scrutiny
#
# Bright floral flavours.
evening_isles_coffee_cup = card_type("evening_isles_coffee_cup",
    attributes(forge=1, lantern=2, rose=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Evening Isles Coffee (Pot)
#
# Coffee from beyond the sunset sea.
# ---
# Scrutiny
#
# Bright floral flavours.
evening_isles_coffee_pot = card_type("evening_isles_coffee_pot",
    attributes(forge=1, lantern=2, rose=1, thing=1, liquid=1, beverage=1, restorative=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, evening_isles_coffee_cup),
)


# Isle-Water (Glass)
#
# From Brancrug's deep springs.
# --
# Scrutiny
#
# The water of the isle has a very faint, very distinctive taste sometimes described as 'appleshroomy'.
isle_water_glass = card_type("isle_water_glass",
    attributes(heart=1, moon=1, winter=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Isle-Water (Pitcher)
#
# From Brancrug's deep springs.
# ---
# Scrutiny
#
# The water of the isle has a very faint, very distinctive taste sometimes described as 'appleshroomy'.
isle_water_pitcher = card_type("isle_water_pitcher",
    attributes(heart=1, moon=1, winter=1, thing=1, liquid=1, beverage=1, restorative=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, isle_water_glass),
)


# Lambig Broceliande (Chalice)
#
# Distilled from apples in the oldest forest of the western Continent.
# ---
# Scrutiny
#
# '<i>Lambig</i> and <i>alembic</i>,' Thirza Blake once observed, 'arise from the same root. As do <i>alchemy</i>, and <i>khemia</i>, which is the land of the black earth. When you plant an apple-seed, speak these sounds to the soil.'
lambig_broceliande_chalice = card_type("lambig_broceliande_chalice",
    attributes(grail=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Lambig Broceliande (Bottle)
#
# Distilled from apples in the oldest forest of the western Continent.
# ---
# Scrutiny
#
# '<i>Lambig</i> and <i>alembic</i>,' Thirza Blake once observed, 'arise from the same root. As do <i>alchemy</i>, and <i>khemia</i>, which is the land of the black earth. When you plant an apple-seed, speak these sounds to the soil.'
lambig_broceliande_bottle = card_type("lambig_broceliande_bottle",
    attributes(grail=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, lambig_broceliande_chalice),
)


# Leathy
#
# A dark and syrupy liquor favoured in unnamed forest villages.
# ---
# Scrutiny
#
# Exhausted.
leathy = card_type("leathy",
    attributes(grail=2, moth=4, nectar=2, scale=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1),
    consider_output = memory.taste,
)


# Mist-Kissed Water (Glass)
#
# The faintest of vapours still ghosts the water's surface.
# ---
# Scrutiny
#
# This is the nature of the taste of mist-kissed water: that one forgets it even as the taste passes from the tongue.
mist_kissed_water_glass = card_type("mist_kissed_water_glass",
    attributes(heart=1, knock=2, moon=2, winter=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Mist-Kissed Water (Pitcher)
#
# The faintest of vapours still ghosts the water's surface.
# ---
# Scrutiny
#
# This is the nature of the taste of mist-kissed water: that one forgets it even as the taste passes from the tongue.
mist_kissed_water_pitcher = card_type("mist_kissed_water_pitcher",
    attributes(heart=1, knock=2, moon=2, winter=1, thing=1, liquid=1, beverage=1, restorative=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, mist_kissed_water_glass),
)


# Roscraggan Whisky (Glass)
#
# The favourite tipple of Sir David Greene, eighth Librarian of Hush House.
# ---
# Scrutiny
#
# Strong as sunset.
roscraggan_whisky_glass = card_type("roscraggan_whisky_glass",
    attributes(forge=1, rose=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Roscraggan Whisky (Bottle)
#
# The favourite tipple of Sir David Greene, eighth Librarian of Hush House.
# ---
# Scrutiny
#
# Strong as sunset.
roscraggan_whisky_bottle = card_type("roscraggan_whisky_bottle",
    attributes(forge=1, rose=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, roscraggan_whisky_glass),
)


# Rubywise Ruin
#
# A ruddy liquor wrung from flowers - even when the flowers aren't red.
# ---
# Scrutiny
#
# A ruddy liquor wrung from flowers - even when the flowers aren't red. [There are Scholar-level Grail recipes that can brew this from flowers.]
rubywise_ruin = card_type("rubywise_ruin",
    attributes(grail=4, heart=2, moth=2, nectar=2, rose=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Sacrament Ascite
#
# Back in the Dawn Period, the Sisterhood of the Triple Knot used this in the rites of the Horned-Axe.
# ---
# Scrutiny
#
# Tart and tangy. 'Whoso drinketh may afterwards speak only in the voice of the owl, the cat, or the hawthorn.' Which might just mean it effectively numbs your tongue. [There are Keeper-level recipes that can render certain knock-toxins into this - in the presence of sufficient Knock.]
sacrament_ascite = card_type("sacrament_ascite",
    attributes(knock=6, thing=1, liquid=1, beverage=1, restorative=1, cooking_ingredient=1, intoxicating=1),
    consider_output = memory.sight,
)


# Sacrament Calicite
#
# Back in the Dawn Period, the Sisterhood of the Triple Knot used this in the rites of the Red Grail.
# ---
# Scrutiny
#
# Floral, musky. Traditionally drunk from the Chalice Murmurous, but you'll generally regret over-indulging even if you drink it from a tin mug in a pub. Especially in a pub. [There are Keeper-level recipes that can brew this from certain ruddy liquors, in the presence of sufficient Grail.]
sacrament_calicite = card_type("sacrament_calicite",
    attributes(grail=6, thing=1, liquid=1, beverage=1, restorative=1, cooking_ingredient=1, intoxicating=1),
    consider_output = memory.sight,
)


# Sacrament Malachite
#
# Back in the Dawn Period, the Sisterhood of the Triple Knot used this in the rites of the Ring-Yew, the Hour which has also been called the Malachite.
# ---
# Scrutiny
#
# Syrupy, applesome. Sleep too soon after drinking this, and there's a real chance you'll put down tiny roots. [There are Keeper-level recipes that can brew this from <i>pyrus auricalcinus</i> , in the presence of sufficient Nectar.]
sacrament_malachite = card_type("sacrament_malachite",
    attributes(nectar=6, thing=1, liquid=1, beverage=1, restorative=1, cooking_ingredient=1, intoxicating=1),
    consider_output = memory.sight,
)


# Schloss Jannings (Glass)
#
# A dry, aromatic white wine.
# ---
# Scrutiny
#
# Is this really from a Bavarian vineyard? It's much better than it has any right to be.
schloss_jannings_glass = card_type("schloss_jannings_glass",
    attributes(edge=2, heart=1, scale=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Schloss Jannings (Bottle)
#
# A dry, aromatic white wine.
# ---
# Scrutiny
#
# Is this really from a Bavarian vineyard? It's much better than it has any right to be.
schloss_jannings_bottle = card_type("schloss_jannings_bottle",
    attributes(edge=2, heart=1, scale=1, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, schloss_jannings_glass),
)


# Scrumpy
#
# The West Country's most unregenerate achievement; perhaps at its best when pressed from stolen apples.
# ---
# Scrutiny
#
# That buttonholing back-of-the-throat tang-grab unique to the very roughest of apples.
scrumpy = card_type("scrumpy",
    attributes(grail=2, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Serpent-Milk
#
# It does look almost like milk, and it is drinkable, but don't give it to cats or babies.
# ---
# Scrutiny
#
# Sssatisfying. [There are Keeper-level Edge - and perhaps Scale - recipes that can craft this from Perinculate.]
serpent_milk = card_type("serpent_milk",
    attributes(edge=6, knock=2, scale=3, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1),
    consider_output = memory.old_moment,
)


# Skinshuck Mead
#
# A murky, sweet-smelling liquid crowded with sediment.
# ---
# Scrutiny
#
# Moth's gift to the devotees of the Old Form, so they could shed their skins and don the skins of beasts. After a few gulps, my skin will begin to peel as if I had spent too long in the sun. [With the great arts of Moth-aspect, perhaps this could be brewed from honey.]
skinshuck_mead = card_type("skinshuck_mead",
    attributes(heart=2, moth=6, nectar=2, scale=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.sight,
)


# Sloe Gin (Glass)
#
# Home-made berry gin.
# ---
# Scrutiny
#
# This stuff is tasty, but don't underestimate it.
sloe_gin_glass = card_type("sloe_gin_glass",
    attributes(grail=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Sloe Gin (Bottle)
#
# Home-made berry gin.
# ---
# Scrutiny
#
# This stuff is tasty, but don't underestimate it.
sloe_gin_bottle = card_type("sloe_gin_bottle",
    attributes(grail=1, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, sloe_gin_glass),
)


# Sly Alembic
#
# A cheeky decanter of wine fortified with unusual influences.
# ---
# Scrutiny
#
# An oddly satisfying chemical tang overlays the wine-flavours.
sly_alembic = card_type("sly_alembic",
    attributes(grail=3, heart=3, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.satisfaction,
)


# Solomon's Preparation
#
# Solomon Husher would take this every night without fail before sleep, to close his ears to the sound of the waves. But on the 9th of January 1838, a heavy snow fell on Hush House. When the other residents dug themselves out, Husher was nowhere to be found. He had left a resignation letter, and an undrunk measure of his Preparation.
# ---
# Scrutiny
#
# The sounds around me remain, but I find that I can attend to each one, diminishing it or returning it as if I were closing a door on a troublesome draught. For no obvious reason, I find myself recalling that the 9th of January is the Agonalia of Janus. [There are Scholar-level recipes that can use flower-petals alongside Moon or Winter to craft this.]
solomons_preparation = card_type("solomons_preparation",
    attributes(moon=1, moth=1, winter=4, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.hindsight,
)


# Strathcoyne Whisky (Glass)
#
# The Collector has collected a distillery, it seems.
# ---
# Scrutiny
#
# Peaty as a heathered serpent.
strathcoyne_whisky_glass = card_type("strathcoyne_whisky_glass",
    attributes(nectar=1, scale=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1),
    consider_output = memory.taste,
)


# Strathcoyne Whisky (Bottle)
#
# The Collector has collected a distillery, it seems.
# ---
# Scrutiny
#
# Peaty as a heathered serpent.
strathcoyne_whisky_bottle = card_type("strathcoyne_whisky_bottle",
    attributes(nectar=1, scale=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(3, strathcoyne_whisky_glass),
)


# Thirza's Cordials
#
# Separately, each is undrinkable. But mix them, and they're only undrinkable after fifteen minutes.
# ---
# Scrutiny
#
# Something like pine, something like vanilla. [There are Prentice-level recipes that use the aspect Nectar to craft this.]
thirzas_cordials = card_type("thirzas_cordials",
    attributes(moth=2, nectar=2, thing=1, liquid=1, beverage=1, restorative=1, intoxicating=1),
    consider_output = memory.sight,
)


# T.R.N. Limited Drinking Cocoa (Cup)
#
# T.R.N.'s Spices and Savours Department markets this as 'the Secret Sacrament of the Last Inca!'
# ---
# Scrutiny
#
# Dark as mud and much tastier.
trn_limited_drinking_cocoa_cup = card_type("trn_limited_drinking_cocoa_cup",
    attributes(grail=2, heart=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# T.R.N. Limited Drinking Cocoa (Pot)
#
# T.R.N.'s Spices and Savours Department describes this as 'the Secret Sacrament of the Last Inca!'
# ---
# Scrutiny
#
# Dark as mud and much tastier.
trn_limited_drinking_cocoa_pot = card_type("trn_limited_drinking_cocoa_pot",
    attributes(grail=2, heart=1, thing=1, liquid=1, beverage=1, restorative=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, trn_limited_drinking_cocoa_cup),
)


# Veiled Goddess Lapsang Souchong (Cup)
#
# Named for an enigmatic minor deity whose charge is the healing of burns.
# ---
# Scrutiny
#
# Smoky and astringent, like pine-scented dragon's breath.
veiled_goddess_lapsang_souchong_cup = card_type("veiled_goddess_lapsang_souchong_cup",
    attributes(forge=2, sky=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)


# Veiled Goddess Lapsang Souchong  (Pot)
#
# Named for an enigmatic minor deity whose charge is the healing of burns.
# ---
# Scrutiny
#
# Smoky and astringent, like pine-scented dragon's breath.
veiled_goddess_lapsang_souchong_pot = card_type("veiled_goddess_lapsang_souchong_pot",
    attributes(forge=2, sky=1, thing=1, liquid=1, beverage=1, restorative=1, cooking_ingredient=1, to_serve=1),
    consider_output = memory.taste,
    serve_into=(2, veiled_goddess_lapsang_souchong_cup),
)


# Witching Tisane
#
# 'To mend a broken heart, to colour a pale soul.'
# ---
# Scrutiny
#
# The taste is like a lingering kiss at the mouth's edge. [There are Prentice-level Grail recipes that can craft this.]
witching_tisane = card_type("witching_tisane",
    attributes(grail=2, heart=1, thing=1, liquid=1, beverage=1, restorative=1),
    consider_output = memory.taste,
)

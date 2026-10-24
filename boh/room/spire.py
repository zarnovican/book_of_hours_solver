from ..item import beverage, liquid, thing
from ..model import attributes, condition, room, slot, station


# Spire Prospect
#
# Take counsel with the skies.
spire_prospect = station("spire_prospect",
    attributes(evolve_via_hushery=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moth=1, sky=1),
        ),
        slot(
            required=condition(soul=1, co_operative=1, blank=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1, pigment=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Wyrd-Cursed Spire
#
# Seven years ago, someone pronounced a curse here, in the name of the Sun and its many selves. This place was not the curse's target, and nor was I, but its poison fills the air around me. I should not enter here until it's cleansed.
# ---
# Spire
#
# Here Hendrik Dewulf met in secret with King Henry - once the Bronze King, now 'Old Coppernose', for the Great Debasement had ended the supremacy of the Leashed Flame, and Henry's heirs were no more than human. There is a story that Hendrik's son Thomas listened from the rafters - that three times he heard Henry ask his father to break a certain promise in the matter of Caer Ys beyond the wave, and the third time, the father did not refuse the king. This, says the story, is why Thomas never liked to make a promise thereafter, for fear of breaking it.
spire = room("spire",
    attributes(solar_gothic_period=1),
    inventory = (
        beverage.evening_isles_coffee_cup,
        beverage.evening_isles_coffee_pot,
        liquid.houndsgall,
        thing.brian_levinsen,
    ),
    neighbors = ("bells", ),
    power_requirements = attributes(lantern=12, moth=12, sky=12),
    stations = (
        spire_prospect,
    ),
)

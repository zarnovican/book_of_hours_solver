from ..model import attributes, condition, room, slot, station


# Deeplight Corals
#
# Where the wild few traffic with the tides.
deeplight_corals = station("deeplight_corals",
    attributes(evolve_via_bosk=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(moon=1, nectar=1, rose=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(moon=1, nectar=1, rose=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(moon=1, nectar=1, rose=1, scale=1),
        ),
        slot(
            required=condition(soul=1),
            forbidden=condition(fatigued=1),
        ),
        slot(
            required=condition(memory=1),
            forbidden=condition(fatigued=1),
        ),
    ),
)


# Menacing Phosphorescence
#
# The pumps have drained enough water to splash through, but everything is spatched and splotted with sickly, alien, wonderous, mesmeric light. When I retreat, I find the same glow on my boots. Whatever I do, I should not do it hastily.
# ---
# Deeplight Caves
#
# When the gods-from-stone were swept away, the Carapace Cross who had served them were swept away too. The Seglaz-kind, the Wyrmefota-kind, the Glaeterfloge-kind, all those wise and mighty ones are gone, into Nowhere or hiding or us. Here in the fire-warmed waters, away from the justice of sunlight, their legacy quietly thrives.
deeplight_caves = room("deeplight_caves",
    attributes(dawn_period=1),
    neighbors = ("sea_caves", ),
    power_requirements = attributes(moon=14, nectar=14),
    stations = (
        deeplight_corals,
    ),
)

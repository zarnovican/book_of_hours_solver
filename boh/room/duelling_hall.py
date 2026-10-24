from ..item import comfort, thing, wall_art
from ..model import attributes, condition, room, slot, station


# Practice Equipment
#
# Still the best place in the House to get hurt.
practice_equipment = station("practice_equipment",
    attributes(evolve_via_illumination=1, prentice_level_challenges=1, scholar_level_challenges=1, keeper_level_challenges=1),
    slots = (
        slot(
            essential=condition(soul=1),
            required=condition(edge=1, heart=1, lantern=1, scale=1),
        ),
        slot(
            essential=condition(skill=1),
            required=condition(edge=1, heart=1, lantern=1, scale=1),
        ),
        slot(
            essential=condition(memory=1),
            required=condition(edge=1, heart=1, lantern=1, scale=1),
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


# Dim Hall
#
# The walls are hung with weapons. As I essay the threshold, a whisper troubles the still air, and a pair of wall-hung swords glints menacingly. More of van Lauren's protections. They seem much stronger on the seaward than the landward side of the House. One might begin to wonder if they were intended to protect against outsiders at all.
# ---
# Duelling Hall
#
# In Baronial times, this was a ballroom, but in the nineteenth century, during Brulleau's time as Librarian, a dyad of eternally duelling Edge-long agreed to stay at Hush House for a year and a day to allow Natalia to study them, if she satisfied certain conditions. A properly equipped space was one of those conditions. (Ultimately, the business turned out to be a trap or trick played by one or both of the dyad, and they left after only a single battle.) Their names are recorded as 'Mistress Dearday' and 'Father Torgue'.
duelling_hall = room("duelling_hall",
    attributes(curia_period=1),
    inventory = (
        comfort.wine_dark_chair,
        comfort.wine_dark_chair,
        thing.natalia_brulleau,
        wall_art.azitas_practice_sword,
        wall_art.crossbow,
        wall_art.dappled_practice_sword,
        wall_art.dappled_quarterstaff,
        wall_art.deardays_foil,
        wall_art.frasers_practice_sword,
        wall_art.golden_lion_shield,
        wall_art.green_stag_shield,
        wall_art.greenes_practice_sword,
        wall_art.hunters_bow,
        wall_art.matched_flintlock_pistols,
        wall_art.mehrads_practice_sword,
        wall_art.natalias_practice_sword,
        wall_art.poachers_bow,
        wall_art.red_drake_shield,
        wall_art.red_practice_sword,
        wall_art.red_quarterstaff,
        wall_art.sebastians_swords,
        wall_art.sentrys_bow,
        wall_art.the_first_threshold,
        wall_art.torgues_foil,
    ),
    neighbors = ("map_room", ),
    power_requirements = attributes(edge=8, grail=8),
    stations = (
        practice_equipment,
    ),
)

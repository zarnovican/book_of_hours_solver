import enum
from pprint import pprint

from frozendict import frozendict

from .attributes import valid_attributes


all_powers = ("edge", "forge", "grail", "heart", "knock", "lantern", "moon", "moth", "nectar", "rose", "scale", "sky", "winter")
all_wisdoms = ("birdsong", "horomachistry", "hushery", "illumination", "ithastry", "nyctodromy", "preservation", "skolekosophy", "the_bosk")


class season(enum.StrEnum):
    any = enum.auto()

    # Spring
    #
    # The world warms.
    spring = enum.auto()

    # Summer
    #
    # The Grail at her greatest.
    summer = enum.auto()

    # Autumn
    #
    # The Elegiast's season.
    autumn = enum.auto()

    # Winter
    #
    # Now comes the White.
    winter = enum.auto()

    # Numa
    #
    # Numa, shortest season, labyrinth season, when the year loses its way, when Time is a river and Memory a winged bird. In Numa, oddities ripen in the gardens of the Isle - unexpected visitors arrive - memory departs. [When Numa ends, all Memories will vanish with it, even persistent ones. One of every nine seasons in Brancrug is Numa, but Numa is the vagabond, Numa has no heralds. Numa might arrive twice in one year - or four years might pass without the touch of its mists.]
    numa = enum.auto()


class time_of_day(enum.StrEnum):
    # Dawn
    #
    # At this time the sisters of the Abbey would raise their voices in praise of the Madrugad, for the office of Aurora.
    dawn = enum.auto()

    # Morning
    #
    # The third hour, when the office of Terce once was sung. Watch as the day opens like a door.
    morning = enum.auto()

    # Midday
    #
    # Before the great division, this was the Sixth Hour, when the priests led hymns to the Sun-in-Splendour. Now Noon, as they say, is not as it was. Perhaps the New King will change that.
    midday = enum.auto()

    # Afternoon
    #
    # The little hour called Nones, when the doors of the Mansus are most tightly closed. For the secular, the hours when we may anticipate tea, or celebrate it.
    afternoon = enum.auto()

    # Dusk
    #
    # Night from day; silver from gold. The vesper-hour when the priests would honour the rising of the evening-star Meniscate.
    dusk = enum.auto()

    # Night
    #
    # Night has fallen. Dawn will come soon. Keep vigil.
    night = enum.auto()


class soul_state(enum.StrEnum):
    normal   = enum.auto()
    fatigued = enum.auto()
    malady   = enum.auto()


def any_slot_match_mystery_item(slots):
    return any(slot.match_mystery_item() for slot in slots)


def is_consumable(card_or_type):
    return any(card_or_type.has_attribute(name) for name in (
        "assistance", "beast", "beverage", "cache", "candle", "device", "employable",
        "fabric_and_fibre", "flower", "fruit", "leaf", "lesson", "liquid", "mark",
        "material", "memory", "remains", "sustenance",
    ))


def is_mystery_item(card_type):
    # TODO (logic) is journal a mystery item or not ?
    return card_type.name_from_prefix("mystery_") is not None and not card_type.has_attribute("journal")


def make_slots_optional(slots):
    return tuple(slot.make_optional() for slot in slots)


def pop_slot_matching_attribute(name, slots):
    """return slot matching attribute and the remaining slots"""

    _slots = list(slots)
    for i, slot in enumerate(_slots):
        if slot.match_attribute(name):
            _slots.pop(i)
            return slot, tuple(_slots)

    return None, slots


def pop_slot_matching_mystery_item(slots):
    """return slot matching mystery item and the remaining slots"""

    for name in ("readable", "phonograph_record", "reel_of_film"):
        slot, slots = pop_slot_matching_attribute(name, slots)
        if slot is not None:
            return slot, slots

    return None, slots


class attributes(frozendict):
    """a set of 'book of hours' attributes (str->int), bool as int (1==True)

    ocd: this class inherits from 'frozendict' to preserve the insert order.
    Repr() then has the attributes in the same order has in the game.
    Unfortunatelly, the in-game order is not consistent. Different cards
    have the same attributes in different order."""


    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            if attribute not in valid_attributes:
                raise ValueError(f"invalid attribute \"{attribute}\"")
            if value <= 0:
                raise ValueError(f"value for attribute \"{attribute}\" is not positive integer")
        super().__init__(**kwargs)


    def __repr__(self):
        return " ".join( ( f"{k}={v}" if v > 1 else k ) for k, v in self.items() )


    def has(self, name):
        return name in self


    def name_from_prefix(self, prefix):
        return next((name for name in self if name.startswith(prefix)), None)


    def value(self, name):
        return self.get(name, 0)


class condition:


    def __init__(self, logical_and=False, one_of=None, **kwargs):
        self.one_of = one_of
        self._attributes = None

        # !! this code was hand-tweaked for performance !!
        if len(kwargs) > 0:
            self._attributes = attributes(**kwargs)

            if one_of is None:
                if logical_and:
                    # special case for 'essential' with more than one attribute
                    # (and no 'one_of') which seems to be by definition logical AND,
                    # but I found out very late in the implementation
                    self.match = self._match_on_all_attributes
                else:
                    self.match = self._match_on_attributes
            else:
                self.match = self._match_one_of_or_attributes

        else:
            if one_of is None:
                self.match = self._match_none
            elif len(one_of) > 0:
                self.match = self._match_one_of
            else:
                # logically, one_of=() should not match anything, but empty tuple is not
                # a valid value and I use it as an indicator for 'match any card'
                self.match = self._match_any

        self._hash = hash((self.one_of, self._attributes))


    def __hash__(self):
        return self._hash


    def _match_any(self, card):
        return True


    def match_attribute(self, name):
        """check if condition() is looking at specific attribute by name"""

        return self._attributes is not None and name in self._attributes


    def _match_on_all_attributes(self, card):
        return all(card.has_attribute(name) for name in self._attributes)


    def _match_on_attributes(self, card):
        return any(card.has_attribute(name) for name in self._attributes)


    def match_on_attributes_only(self, attributes):
        """special case for matching 'condition's attributes vs 'attributes(..)' instance"""

        return self.one_of is None and any(attributes.has(name) for name in self._attributes)


    def _match_one_of(self, card):
        return card.card_type in self.one_of


    def _match_one_of_or_attributes(self, card):
        return self._match_one_of(card) or self._match_on_attributes(card)


    def _match_none(self, card):
        return False


match_any_card = condition(one_of=())
match_no_card = condition()


class and_condition:
    """logical 'and' condition

    In-game 'condition' is always logical 'or'. This special case
    condition implements logical 'and'. Card has to match all
    condition's attributes.
    """


    def __init__(self, **kwargs):
        self._attributes = attributes(**kwargs)


    def __hash__(self):
        return hash(self._attributes)


    def match(self, card):
        return all(card.has_attribute(name) for name in self._attributes)


class simple_action:


    def __init__(self, name, slots, output, pennies=0):
        self.name = name
        self.output = output
        self.pennies = pennies
        self.slots = slots


    def slots_or_(self, station_slots):
        """value None indicate that station slots should be used"""
        return self.slots if self.slots is not None else station_slots


class simple_output:


    def __init__(self, card_type, probability=100, season=season.any):
        self.card_type = card_type
        self.probability = probability
        self.season = season


class slot:

    _match_cache = {}   # (card_or_type.cache_key, slot.cache_key) -> bool|None


    def __init__(self,
        essential = match_any_card,
        required = match_any_card,
        forbidden = match_no_card,
        consume_all = False,
        optional = False,
    ):
        self.essential = essential
        self.required = required
        self.forbidden = forbidden
        self.consume_all = consume_all
        self.optional = optional

        self.cache_key = hash((essential, required, forbidden))


    def has_plain_skill_condition(self):
        """True if slot essential condition is a plain single-attribute match"""

        return hash(self.essential) == hash(condition(skill=1))  # TODO (smell) implement __eq__ ?


    def match(self, card):
        _cache_key = (card.cache_key, self.cache_key)
        _value = self.__class__._match_cache.get(_cache_key, None)
        if _value is None:
            _value = self.essential.match(card) and self.required.match(card) and not self.forbidden.match(card)
            self.__class__._match_cache[_cache_key] = _value

        return _value


    def match_attribute(self, name):
        return self.essential.match_attribute(name) or self.required.match_attribute(name)


    def match_mystery_item(self):
        return any(self.match_attribute(name) for name in ("readable", "phonograph_record", "reel_of_film"))


    def make_optional(self):
        return slot(
            essential = self.essential,
            required = self.required,
            forbidden = self.forbidden,
            consume_all = self.consume_all,
            optional = True,
        )


    def update_essential(self, condition):
        return slot(
            essential = condition,
            required = self.required,
            forbidden = self.forbidden,
            consume_all = self.consume_all,
            optional = self.optional,
        )


class soul_slot:
    """fake slot that is matching soul cards by their
    power aspect, state and optionally also soul level"""
    # TODO (smell) this whole class is assuming too much


    def __init__(self,
        soul_type,
        level = None,
        required = match_any_card,
        forbidden = match_no_card,
    ):
        self.soul_type = soul_type
        self.level = level
        self.required = required
        self.forbidden = forbidden

        # mimic 'slot's public interface
        self.consume_all = False
        self.optional = False
        self.cache_key = hash((soul_type, level, required, forbidden))


    def match(self, soul_card):
        if not soul_card.card_type is self.soul_type:
            return False

        assert isinstance(soul_card, soul), f"expecting {soul_card} to be instance of 'soul'" # TODO (smell) 'isinstance()'

        if not self.required.match(soul_card) or self.forbidden.match(soul_card):
            return False

        if self.level is None:
            return True

        return self.level == soul_card.level


class brewing:
    """brew one card (like leaf) into something else (like pot of tea)"""

    _into = {}  # card_type -> card_type


    @classmethod
    def into(cls, card_type):
        assert card_type in cls._into, f"{card_type} is not brewable"
        return cls._into[card_type]


    @classmethod
    def register(cls, card_type, brew_into):
        if brew_into is None:
            return

        assert card_type not in cls._into, f"double registration for {card_type}"
        cls._into[card_type] = brew_into


class cataloguing:
    """mapping from mystery item's period to uncatalogued book"""

    _mystery_item_period = {}       # card_type -> str|None
    _uncatalogued_for_period = {}   # str -> uncatalogued_card_type


    @classmethod
    def register(cls, card_type, period=None):
        if card_type.has_attribute("journal"):  # journal cataloguing logic is very different from mystery items, ignore it for now
            assert period is None, f"'period' attribute not expected for {card_type}"
            
        elif card_type.has_attribute("uncatalogued"):
            assert period is not None, f"mandatory attribute 'period' missing for {card_type}"
            assert period not in cls._uncatalogued_for_period, f"double registration for {card_type}"
            cls._uncatalogued_for_period[period] = card_type

        elif is_mystery_item(card_type):
            assert card_type not in cls._mystery_item_period, f"double registration for {card_type}"
            cls._mystery_item_period[card_type] = period

        else:
            assert period is None, f"'period' attribute not expected for {card_type}"


    @classmethod
    def uncatalogued_for(cls, card_type):
        assert card_type in cls._mystery_item_period, f"unregistered mystery item {card_type}"

        period = cls._mystery_item_period[card_type]

        # if the mystery item has period override, use it
        if period is not None:
            return cls._uncatalogued_for_period[period]

        # autodetect mystery item's period at runtime (cannot do it at registration-time)
        for period, uncatalogued_card_type in cls._uncatalogued_for_period.items():
            if card_type.has_attribute(f"{period}_period"):
                return uncatalogued_card_type

        raise ValueError(f"mystery item {card_type} without a known period")


class committing:
    """logic related to skill commit"""

    _output_by_skill = {}       # card_type -> frozendict()


    @classmethod
    def info(cls, card_type, wisdom):
        """return (soul_card_type, attuned_attribute, unused_wisdom) for committing skill to wisdom"""

        assert card_type in cls._output_by_skill, f"unknown skill {card_type}"
        assert wisdom in cls._output_by_skill[card_type], f"incorrent wisdom {wisdom} for {card_type}"

        _soul_card_type = cls._output_by_skill[card_type][wisdom]
        _both_wisdoms = list(cls._output_by_skill[card_type].keys())
        _both_wisdoms.remove(wisdom)

        return (_soul_card_type, f"attuned_{_soul_card_type.name}", _both_wisdoms[0])


    @classmethod
    def register(cls, card_type, commit_output):
        if card_type.has_attribute("skill"):
            assert commit_output is not None, f"mandatory attribute 'commit_output' missing for {card_type}"
            assert len(commit_output.keys()) == 2, f"expecting two wisdoms in {commit_output}"
            assert all((wisdom in all_wisdoms) for wisdom in commit_output.keys()), f"invalid wisdom name in {commit_output}"
            assert all(card_type.has_attribute(wisdom) for wisdom in commit_output.keys()), f"invalid wisdom name in {commit_output}"
            assert all(soul_output.has_attribute("soul") for wisdom, soul_output in commit_output.items()), \
                f"non-soul output {commit_output}"

            assert card_type not in cls._output_by_skill, f"double registration for {card_type}"
            cls._output_by_skill[card_type] = commit_output

        else:
            assert commit_output is None, f"'commit_output' attribute not expected for {card_type}"


    @classmethod
    def valid_wisdoms_for(cls, card_type):
        assert card_type in cls._output_by_skill, f"unknown skill {card_type}"

        return tuple(cls._output_by_skill[card_type].keys())


class considering:
    """map relation of producing one card_type via 'consider' action from another card"""

    _into = {}  # card_type -> card_type


    @classmethod
    def into(cls, card_type):
        return cls._into.get(card_type, None)


    @classmethod
    def register(cls, card_type, consider_output):
        if consider_output is not None:     # it is pointless to figure out which card_type could have consider
            assert card_type not in cls._into, f"double registration for {card_type}"
            cls._into[card_type] = consider_output


    @staticmethod
    def soul_slots():
        return ( slot(required=condition(soul=1), forbidden=condition(fatigued=1, malady=1)), )


class crafting:

    _output_recipes = {}        # card_type -> list of 'craft_recipe' (recipes, grouped by output card)
    _station_attributes = {}    # str -> attributes
    _station_slots = {}         # str -> tuple of 'slot'


    @classmethod
    def outputs(cls):
        return cls._output_recipes.keys()


    @classmethod
    def register_station(cls, station_name, slots, attributes):
        if not attributes.has("prentice_level_challenges"):
            return

        assert station_name not in cls._station_slots, f"double registration for station {station_name}"

        soul_slot, slots  = pop_slot_matching_attribute("soul",  slots)
        skill_slot, slots = pop_slot_matching_attribute("skill", slots)

        assert skill_slot.has_plain_skill_condition(), f"skill slot {skill_slot} should have essential=condition(skill=1)"

        cls._station_slots[station_name] = (soul_slot, skill_slot, *make_slots_optional(slots))
        cls._station_attributes[station_name] = attributes


    @classmethod
    def register_recipe(cls, item):
        cls._output_recipes.setdefault(item.output, [])
        cls._output_recipes[item.output].append(item)


    @classmethod
    def slots_for(cls, output):
        """return slots for all combinations of recipe and crafting station producing the 'output'"""

        for recipe in cls._output_recipes[output]:
            for station_name, slots in cls._station_slots.items():
                # skip recipe-station combinations, where no recipe skill matches the station skill slot
                skill_slot = cls._station_slots[station_name][1]
                if all(not skill_slot.match(skill) for skill in recipe.skills):
                    continue

                power_aspect, power_requirement = list(recipe.power_requirements.items())[0]

                # take station slots
                soul_slot, skill_slot, *other_slots = slots

                # update station skill slot to require skills from the recipe, we must preserve station's power requirements
                skill_slot = skill_slot.update_essential(condition(one_of=recipe.skills))

                # if the station already fullfils the 'solution_must_include', then solution cards don't have to
                _solution_must_include = recipe.solution_must_include
                if _solution_must_include is not None and _solution_must_include.match_on_attributes_only(cls._station_attributes[station_name]):
                    _solution_must_include = None

                yield station_name, (soul_slot, skill_slot, *other_slots), power_aspect, power_requirement, _solution_must_include


class evolving:
    """upgrade soul via evolving
    Evolve two identical healthy soul cards into next-level soul.
    - skill must be "attuned" to that soul (committed to wisdom)
    - station or optional memory must have 'evolve_via' attribute that is
      matching the wisdon skill is committed to
    """

    _soul_attune_attribute = {} # card_type -> str
    _station_attributes = {}    # str -> attributes
    _station_slots = {}         # str -> tuple of 'slot'


    @classmethod
    def all_souls(cls):
        return cls._soul_attune_attribute.keys()


    @classmethod
    def register_soul(cls, card_type):
        if not card_type.has_attribute("soul") or card_type.has_attribute("malady"):
            return

        assert card_type not in cls._soul_attune_attribute, f"double registration for {card_type}"
        cls._soul_attune_attribute[card_type] = f"attuned_{card_type.name}"


    @classmethod
    def register_station(cls, station_name, slots, attributes):
        soul_slot1, slots  = pop_slot_matching_attribute("soul",  slots)
        soul_slot2, slots  = pop_slot_matching_attribute("soul",  slots)

        # there is a 'condignator' station with 3x soul slot, but it would be complicated
        # to map it, since they are also memory slot, so I would have to push it back (un-pop)
        # let's just ignore 'evolving' solutions using the third soul slot
        #soul_slot3, slots  = pop_slot_matching_attribute("soul",  slots)
        #assert soul_slot3 is None, "station {station_name} with more than two soul slots"

        skill_slot, slots = pop_slot_matching_attribute("skill", slots)

        memory_slots = tuple(slot for slot in slots if slot.match_attribute("memory"))

        # ignore stations which cannot place two souls at once
        if soul_slot1 is None or soul_slot2 is None or skill_slot is None:
            return

        assert len(memory_slots) == 2, "evolving stations always have two memory slots" # is it generally true ?
        assert station_name not in cls._station_slots, f"double registration for station {station_name}"

        cls._station_slots[station_name] = (soul_slot1, soul_slot2, skill_slot)
        cls._station_attributes[station_name] = attributes


    @classmethod
    def slots_for(cls, soul_card_type):
        """return slots for all combinations of station and wisdom"""

        _attune_attribute = f"attuned_{soul_card_type.name}"
        _soul_condition = condition(one_of=(soul_card_type, ))
        for wisdom in all_wisdoms:
            for station_name, slots in cls._station_slots.items():
                for level in (1, 2, 3, 4):
                    soul_slot1, soul_slot2, skill_slot = slots

                    # from the original workstation slot, we use only 'required' condition (power aspect)
                    # 'essential' had to be replaced to match only particular 'soul'
                    # 'forbidden' had to be replaced to rule out maladied souls
                    soul_slot1 = soul_slot(soul_card_type, level=level, required=soul_slot1.required, forbidden=condition(fatigued=1, malady=1))
                    soul_slot2 = soul_slot(soul_card_type, level=level, required=soul_slot2.required, forbidden=condition(fatigued=1, malady=1))

                    # skill must match the power aspects of the slot (required), must be attuned to soul and commited to right wisdom
                    # note: there is logical 'and' between attributes of 'essential'
                    skill_slot = skill_slot.update_essential(and_condition(**{ "skill": 1, _attune_attribute: 1, wisdom: 1 }))

                    # the whole action must have 'evolve_via_' attribute either on station or on (optional) memory
                    _evolve_attribute = f"evolve_via_{wisdom}" if wisdom != "the_bosk" else "evolve_via_bosk"   # TODO (hack)

                    if cls._station_attributes[station_name].has(_evolve_attribute):
                        yield station_name, (soul_slot1, soul_slot2, skill_slot)
                    else:
                        # since station does not have 'evolve_via_' attribute, memory has to provide it
                        # note: workstations with two 'soul' slots (so far) always have two memory slots, where second memory has no power aspect requirements
                        memory_slot = slot(essential=condition(memory=1), required=condition(**{ _evolve_attribute: 1 }))
                        yield station_name, (soul_slot1, soul_slot2, skill_slot, memory_slot)


# TODO (idea) make 'language' part of 'mastering'
class language:
    """map lesson to skill by their name"""

    # languages with 'written_in_' attribute, but no associated skill card (and 'english' as fallback)
    _known_to_librarian = ("aramaic", "english", "greek", "latin", "phrygian", "sanskrit")

    _skill_by_name = {}         # str -> card_type


    @classmethod
    def known_to_librarian(cls, name):
        return name in cls._known_to_librarian


    @classmethod
    def name_from_item(cls, mystery_item):
        attribute_name = mystery_item.name_from_prefix("written_in_")
        language_name = attribute_name[11:] if attribute_name is not None else "english"
        assert cls.known_to_librarian(language_name) or language_name in cls._skill_by_name, f"unknown language {language_name}"
        return language_name


    @classmethod
    def register(cls, card_type):
        if card_type.has_attribute("skill") and card_type.has_attribute("language"):
            assert card_type.name not in cls._skill_by_name, f"double registration for {card_type}"
            cls._skill_by_name[card_type.name] = card_type


    @classmethod
    def skill_for(cls, name):
        assert name in cls._skill_by_name, f"unknown language name {name}"
        return cls._skill_by_name[name]


class learning:
    """map lesson to skill by their name"""

    _skill_by_name = {} # str -> card_type


    @classmethod
    def is_skill_lesson(cls, lesson_type):
        # exclude special lesson 'A Lesson of Many Facets', not linked to any skill
        return lesson_type.has_attribute("lesson") and lesson_type.name in cls._skill_by_name


    @classmethod
    def register(cls, card_type):
        if card_type.has_attribute("skill"):
            assert card_type.name not in cls._skill_by_name, f"double registration for {skill_type}"
            cls._skill_by_name[card_type.name] = card_type


    @classmethod
    def skill_for(cls, lesson_type):
        assert lesson_type.name in cls._skill_by_name, f"no skill for lesson {lesson_type}"
        return cls._skill_by_name[lesson_type.name]


class lookup:
    """helper class to map string (type, name) to card_type object"""

    _card_type    = {} # type(str) -> name(str) -> card_type
    _mystery_item = {} # type(str) -> name(str) -> card_type


    @classmethod
    def card_type(cls, _type, name):
        assert _type in cls._card_type, f"unknown card type {_type}"
        assert name in cls._card_type[_type], f"unknown card type {_type}.{name}"
        return cls._card_type[_type][name]


    @classmethod
    def card_types(cls):
        return sorted(cls._card_type.keys())


    @classmethod
    def items_for(cls, _type):
        return sorted(cls._card_type[_type].items())


    @classmethod
    def mystery_item_names_for(cls, _type):
        return sorted(cls._mystery_item[_type].keys())


    @classmethod
    def mystery_item_types(cls):
        return sorted(cls._mystery_item.keys())


    @classmethod
    def names_for(cls, _type):
        assert _type in cls._card_type, f"unknown card type {_type}"
        return tuple(sorted(cls._card_type[_type].keys()))


    @classmethod
    def register(cls, card_type):
        cls._card_type.setdefault(card_type.type, {})
        assert card_type.name not in cls._card_type[card_type.type], f"double registration for {card_type}"
        cls._card_type[card_type.type][card_type.name] = card_type

        if is_mystery_item(card_type):
            cls._mystery_item.setdefault(card_type.type, {})
            cls._mystery_item[card_type.type][card_type.name] = card_type


    @classmethod
    def skills(cls):
        return sorted(cls._card_type["skill"].items())


class mastering:
    """map mystery item to lessons learned by mastering it"""

    _lesson_by_name = {}                # str -> card_type
    _mystery_item_lesson_count = {}     # card_type -> int
    _provides = {}                      # card_type -> memory_card_type
    _station_slots = {}                 # str -> tuple of slots


    @classmethod
    def lessons_from(cls, card_type):
        for lesson_name, lesson_type in cls._lesson_by_name.items():
            if card_type.has_attribute(f"subject_{lesson_name}"):
                return (lesson_type, ) * cls._mystery_item_lesson_count[card_type]

        return tuple()


    @classmethod
    def _mystery_item_match_station(cls, mystery_item, station_name):
        """True if mystery item match station's mystery item slot"""
        return cls._station_slots[station_name][1].match(mystery_item)


    @classmethod
    def provides(cls, card_type):
        return cls._provides.get(card_type)


    @classmethod
    def register(cls, card_type, lessons, provides):
        if is_mystery_item(card_type):
            assert 0 < lessons <= 3, f"unexpected number of lesson {lessons} for {card_type}"
            assert provides is not None, f"missing mandatory 'provides' for {card_type}"
            assert card_type not in cls._mystery_item_lesson_count, f"double registration for {card_type}"

            cls._mystery_item_lesson_count[card_type] = lessons

            if provides is not None:    # memory card_type provided by re-reading the mystery item
                assert card_type not in cls._provides, f"double registration for {card_type}"
                cls._provides[card_type] = provides
        else:
            assert lessons == 0, f"'lessons' attribute not expected for {card_type}"
            assert provides is None, f"'provides' attribute not expected for {card_type}"

        if card_type.has_attribute("lesson"):
            assert card_type.name not in cls._lesson_by_name, f"double registration for {card_type}"
            cls._lesson_by_name[card_type.name] = card_type


    @classmethod
    def register_station(cls, station_name, slots):
        if not any_slot_match_mystery_item(slots):
            return

        assert station_name not in cls._station_slots, f"double registration for station {station_name}"

        soul_slot, slots = pop_slot_matching_attribute("soul", slots)
        assert soul_slot is not None, f"no match for soul in {slots}"

        mystery_item_slot, slots = pop_slot_matching_mystery_item(slots)
        assert mystery_item_slot is not None, f"no match for mystery item in {slots}"

        cls._station_slots[station_name] = (soul_slot, mystery_item_slot, *make_slots_optional(slots))


    @classmethod
    def rereading(cls):
        """return all combinations of station and matching mystery item, including
        the "soul slot" for station and output memory card_type after re-reading

        return (station_name, (soul_slot), ((mystery_item, provided_card), ..)"""

        for station_name, slots in cls._station_slots.items():
            output = tuple(
                (mystery_item, provided_card) for mystery_item, provided_card in cls._provides.items()
                if cls._mystery_item_match_station(mystery_item, station_name)
            )
            if len(output) > 0:
                yield station_name, (slots[0], ), output


    @classmethod
    def slots_for(cls, card_type):
        """return slots for stations matching 'card_type' mystery item"""

        for station_name, slots in cls._station_slots.items():
            # skip mystery_item-station combinations, where mystery_item does not match station mystery_item slot
            if not cls._mystery_item_match_station(card_type, station_name):
                continue

            # take station slots, except mystery_item
            # (we know the mystery item match it and the mystery item does not contribute any power or cost)
            soul_slot, _, *other_slots = cls._station_slots[station_name]

            # add slot for language, if the item is written in language which is not known to librarian
            # (since the language card can contribute power to solution)
            language_slot = ()
            item_language = language.name_from_item(card_type)
            if not language.known_to_librarian(item_language):
                language_slot = ( slot(required=condition(one_of=(language.skill_for(item_language), ))), )

            yield station_name, (soul_slot, *language_slot, *other_slots)


# TODO (idea) make 'opportunity' part of 'mastering'
class opportunity:
    """opportunity slot is randomly available during actions to unlock
    mystery items.

    'opportunity' allows you to add matching card from your inventory.
    Opportunity is a slot with condition.

    'mood' is a opportunity that only accepts its own "mood card"
    ('Awen', 'Duende', 'Epiphany', 'Ubi Sunt'). Mood cards are created
    on-the-fly during item unlock action. Mood it both a card_type
    and slot with condition accepting only its own card."""

    _mood_card_type = {}    # str -> card_type
    _slot           = {}    # str -> slot


    @classmethod
    def is_mood(cls, name):
        return name in cls._mood_card_type


    @classmethod
    def mood_card_types_for(cls, *names):
        assert all((name in cls._slot) for name in names), f"unknown opportunity in ({names})"
        return tuple(cls._mood_card_type[name] for name in names if name in cls._mood_card_type)


    @classmethod
    def register_mood(cls, name, mood_card_type):
        assert name not in cls._mood_card_type, f"double registration for {name}"
        cls._mood_card_type[name] = mood_card_type
        cls.register_opportunity(name, condition(one_of=(mood_card_type, )))


    @classmethod
    def register_opportunity(cls, name, condition):
        assert name not in cls._slot, f"double registration for {name}"
        cls._slot[name] = slot(required=condition, optional=True)


    @classmethod
    def slots_for(cls, *names):
        assert all((name in cls._slot) for name in names), f"unknown opportunity in ({names})"
        return tuple(cls._slot[name] for name in names)


class room_unlocking:

    _inventory = {}                 # room_name -> ( card_type, .. )
    _locked_stations = {}           # room_name -> ( station_name, .. )
    _neighbors = {}                 # room_name -> [ room_name, .. ]
    _power_requirements = {}        # room_name -> attributes
    _stations = {}                  # room_name -> ( station_name, .. )
    _unique_collabotation = {}      # card_type -> condition|None
    _unlock_at_start = []           # [ room_name, .. ]


    @classmethod
    def inventory_for(cls, room_name):
        assert room_name in cls._inventory, f"unknown room {room_name}"
        return cls._inventory[room_name]


    @classmethod
    def locked_stations_for(cls, room_name):
        assert room_name in cls._locked_stations, f"unknown room {room_name}"
        return cls._locked_stations[room_name]


    @classmethod
    def neighbors_for(cls, room_name):
        assert room_name in cls._neighbors, f"unknown room {room_name}"
        return tuple(cls._neighbors[room_name])


    @classmethod
    def register_assistance(cls, card_type, unique_collabotation):
        if card_type.has_attribute("assistance"):
            assert card_type not in cls._unique_collabotation, f"double registration for {card_type}"
            cls._unique_collabotation[card_type] = unique_collabotation

        else:
            assert unique_collabotation is None, f"'unique_collabotation' attribute not expected for {card_type}"


    @classmethod
    def register_room(cls, room_name, power_requirements, inventory, locked_stations, neighbors, stations, unlock_at_start):
        assert room_name not in cls._power_requirements, f"double registration for {room_name}"

        cls._inventory[room_name] = inventory
        cls._power_requirements[room_name] = power_requirements
        cls._stations[room_name] = stations
        cls._locked_stations[room_name] = locked_stations

        cls._neighbors.setdefault(room_name, [])
        for neighbor_name in neighbors:
            cls._neighbors.setdefault(neighbor_name, [])

            assert neighbor_name not in cls._neighbors[room_name], f"dual neighbors {room_name} -> {neighbor_name}"
            cls._neighbors[room_name].append(neighbor_name)

            assert room_name not in cls._neighbors[neighbor_name], f"dual neighbors {neighbor_name} -> {room_name}"
            cls._neighbors[neighbor_name].append(room_name)

        if unlock_at_start:
            cls._unlock_at_start.append(room_name)


    @classmethod
    def requirements_for(cls, room_name):
        return cls._power_requirements[room_name]


    @classmethod
    def slots_for(cls, room_name):
        assert room_name in cls._power_requirements, f"unknown room {room_name}"
        for power_aspect, power_value in cls._power_requirements[room_name].items():
            for assistance_type, unique_collabotation in cls._unique_collabotation.items():
                slots = [
                    # mandatory 'assistance' slot, matching only itself
                    slot(
                        required=condition(one_of=(assistance_type, )),
                    ),
                    # collaboration slots common to any assistance
                    slot(
                        required=condition(beverage=1),
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ),
                    slot(
                        required=condition(memory=1),
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ),
                    slot(
                        required=condition(soul=1),
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ),
                    slot(
                        required=condition(sustenance=1),
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ),
                    slot(
                        required=condition(tool=1),
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ),
                ]
                if unique_collabotation is not None:
                    # collaboration slot specific to this assistance
                    slots.append(slot(
                        required=unique_collabotation,
                        forbidden=condition(fatigued=1, malady=1),
                        optional=True,
                    ))

                yield slots, power_aspect, power_value


    @classmethod
    def stations_for(cls, room_name):
        assert room_name in cls._stations, f"unknown room {room_name}"
        return cls._stations[room_name]


    @classmethod
    def unlock_at_start(cls):
        return tuple(cls._unlock_at_start)


class serving:
    _into = {}  # card_type -> tuple(card_type, ..)


    @classmethod
    def register(cls, card_type, count, into):
        if card_type.has_attribute("to_serve"):
            assert count > 0, f"card {card_type} with 'to_serve' attribute, but no serve_into"
            assert card_type not in cls._into, f"double registration for {card_type}"
            cls._into[card_type] = (into, ) * count

        else:
            assert count == 0, f"'serve_into' attribute not expected for {card_type}"


    @classmethod
    def into(cls, card_type):
        assert card_type in cls._into, f"cannot serve {card_type}"
        return cls._into[card_type]


class simple_solving:
    """common register for actions that require only a simple solver
    over known slots and return output(s).

    Including:
    * gathering
    * hiring
    * misc actions - like renounce, release, swim
    """

    _simple_actions = []  # list of tuple(station_name, action_name, output=tuple((card_type, probability, season), ..), slots, pennies)


    @classmethod
    def register(cls, station_name, action_name, output, slots, pennies):
        cls._simple_actions.append((station_name, action_name, output, slots, pennies))


    @classmethod
    def actions(cls):
        return tuple(cls._simple_actions)


class skill_resetting:

    a_lesson_of_many_facets = None


    @classmethod
    def register_lesson(cls, card_type):
        if card_type.has_attribute("lesson") and not card_type.has_attribute("persistent"):
            assert cls.a_lesson_of_many_facets is None, f"multiple 'a_lesson_of_many_facets' card types"
            cls.a_lesson_of_many_facets = card_type


    @classmethod
    def output_for(cls, level):
        _count = max(1, int(level * (level+1) / 2) - 2)
        return (cls.a_lesson_of_many_facets, ) * _count


class skill_upgrading:


    @staticmethod
    def match(skill_type, lesson_type):
        return skill_upgrading.power_condition(skill_type).match(lesson_type)


    @staticmethod
    def power_condition(skill_type):
        # soul, lesson, memory must have at least one common power with skill
        return condition(**{ power: 1 for power in all_powers if skill_type.has_attribute(power) })


    @staticmethod
    def slots_for(skill_type, level):
        _power_condition = skill_upgrading.power_condition(skill_type)

        slots = [
            slot(
                essential=condition(soul=1),
                required=_power_condition,
            ),
            slot(
                essential=condition(lesson=1),
                required=_power_condition,
            ),
        ]

        for _ in range(level):
            slots.append(
                slot(
                    essential=condition(memory=1),
                    required=_power_condition,
                    forbidden=condition(lesson=1),          # don't waste lesson as memory
                )
            )

        return tuple(slots)


class soul_transitioning:

    _into = {}  # card_type -> dict(state -> (attributes, name_suffix))


    @classmethod
    def into(cls, card_type, level, soul_state):
        assert card_type in cls._into, f"unknown soul type {card_type}"
        assert (level, soul_state) in cls._into[card_type], f"undefined state {soul_state} for {card_type} level {level}"

        return cls._into[card_type][(level, soul_state)]


    @classmethod
    def register(cls, card_type, soul_states):
        if not card_type.has_attribute("soul"):
            assert soul_states is None, f"'soul_states' attribute not expected for {card_type}"
            return

        if soul_states is None:
            soul_states = ()

        assert card_type not in cls._into, f"double registration for {card_type}"
        cls._into[card_type] = {}

        for i, states in enumerate(soul_states):
            level = i+1
            _normal_attributes = states.get("normal", card_type.attributes)
            cls._into[card_type][(level, soul_state.normal)] = (_normal_attributes, "")

            if "fatigued" in states:
                cls._into[card_type][(level, soul_state.fatigued)] = (states["fatigued"], "_fatigued")

            if "malady" in states:
                assert "malady_name" in states, f"missing 'malady_name' for {card_type}"
                _malady_name = states["malady_name"]
                cls._into[card_type][(level, soul_state.malady)] = (states["malady"], f"_{_malady_name}")


class talking:
    """register talking output from various assistants"""

    _output = {}    # card_type -> tuple( memory, probability )


    @classmethod
    def register(cls, card_type, output):
        assert card_type not in cls._output, f"double registration for {card_type}"
        cls._output[card_type] = output


    @classmethod
    def output(cls):
        return cls._output.items()


class room:


    def __init__(self, name, attributes,
        inventory = (),
        locked_stations = (),
        neighbors = (),
        power_requirements = attributes(),
        stations = (),
        unlock_at_start = False,
    ):
        self.name = name
        self.attributes = attributes

        room_unlocking.register_room(self.name,
            power_requirements = power_requirements,
            inventory = inventory,
            locked_stations = tuple( station.name for station in locked_stations ),
            neighbors = neighbors,
            stations = tuple( station.name for station in stations ),
            unlock_at_start = unlock_at_start,
        )


class station:
    """This is the 'pop-up' for running actions. It starts with at least
    one slot. As you place cards in slots, then more slots can appear,
    while the description may change as well. Ultimately, you reach either
    dead end (all slots are filled, but "start" is disabled), or you have
    reached the leaf node with action.

    Some slots appear _after_ you start an action, changing the result.

    Some initial station _completelly_ change in-place, as you "unlock"
    the station, meaning there are more than one actions tree for a station.

    I was too lame/lazy to model the whole tree and each slot in it. I'll
    model only the leaf actions and keep only the descriptions for nonleaf
    nodes for grep-ing."""


    def __init__(self,
        name,
        attributes,
        mastering_slots = None,
        nonleaf_description = (),
        simple_actions = (),
        slots = (),
    ):
        self.name = name
        self.attributes = attributes

        crafting.register_station(self.name, slots, attributes=self.attributes)
        evolving.register_station(self.name, slots, attributes=self.attributes)
        mastering.register_station(self.name, slots if mastering_slots is None else mastering_slots)

        for simple_action in simple_actions:
            simple_solving.register(
                station_name = self.name,
                action_name = simple_action.name,
                output = tuple( (o.card_type, o.probability, o.season) for o in simple_action.output ),
                slots = simple_action.slots_or_(slots),
                pennies = simple_action.pennies,
            )


    def __repr__(self):
        return self.name


    def has_attribute(self, name):
        return self.attributes.has(name)


class craft_recipe:
    """crafting recipe, independent of any crafting station (action)"""


    def __init__(self,
        output = None,
        power_requirements = attributes(),              # goal to meet, eg "sum of all card must have 'moon' >= 10"
        skills = (),
        solution_must_include = None,                   # scholar and keeper level recipes have an addition requirement
    ):
        self.output = output
        self.power_requirements = power_requirements
        self.skills = skills
        self.solution_must_include = solution_must_include

        crafting.register_recipe(self)


    def __lt__(self, other):
        return self.output < other.output


    def __repr__(self):
        return repr(self.output)


    def __str__(self):
        return str(self.output)


class card_type:


    def __init__(self,
        name,
        attributes,
        brew_into = None,
        commit_output = None,
        consider_output = None,
        lessons = 0,
        period = None,
        provides = None,
        serve_into = (0, None),
        soul_states = None,
        unique_collabotation = None,
    ):
        self.name = name
        self.attributes = attributes
        self.type = card_type.internal_type(attributes)

        self.cache_key = hash(attributes)

        brewing.register(self, brew_into)
        cataloguing.register(self, period)
        committing.register(self, commit_output)
        considering.register(self, consider_output)
        evolving.register_soul(self)
        language.register(self)
        learning.register(self)
        lookup.register(self)
        mastering.register(self, lessons, provides)
        room_unlocking.register_assistance(self, unique_collabotation)
        serving.register(self, count=serve_into[0], into=serve_into[1])
        skill_resetting.register_lesson(self)
        soul_transitioning.register(self, soul_states)


    def __lt__(self, other):
        return str(self) < str(other)


    def __repr__(self):
        return f"{str(self)}({self.attributes})"


    def __str__(self):
        return f"{card_type.internal_type(self.attributes)}.{self.name}"


    def attribute_value(self, name):
        return self.attributes.value(name)


    def has_attribute(self, name):
        return self.attributes.has(name)


    @staticmethod
    def internal_type(attributes):
        """get internal type from its 'primary' attribute

        Some cards have more than one (eg 'beast'+'comfort'). We want the type
        to be 'beast', that's why this list has to be sorted by priority,
        which attribute is more important to determine the type.

        Internal type is used only for visual representations (eg 'str()') and
        to construct unique id (weather.storm vs memory.storm)."""

        types = (
            "assistance",
            "beast",
            "beverage",
            "cache",
            "candle",
            "circumstance",
            "codex",
            "device",
            "employable",
            "fixed_in_place",
            "flower",
            "fruit",
            "incident",
            "journal",
            "leaf",
            "lesson",
            "liquid",
            "mark",
            "material",
            "pence",
            "phonograph_record",
            "reel_of_film",
            "remains",
            "root",
            "scroll",
            "skill",
            "soul",
            "soul_option",
            "sustenance",
            "tablet",
            "tally",
            "tool",
            "uncatalogued",
            "visitor",
            "wall_art",
            "weather",

            "an_introduction",  # must be after 'assistance'
            "comfort",          # must be after 'beast', 'liquid', 'material', 'tool'
            "memory",           # must be after 'soul_option', 'weather'
            "thing",            # must be after 'uncatalogued'
        )

        for name in types:
            if attributes.has(name):
                return name

        return "notype"


    def name_from_prefix(self, prefix):
        return self.attributes.name_from_prefix(prefix)


    def power_aspect_and_value(self):
        """return pair of 'power_aspects' (str) and 'power_requirement' (int)"""

        _name = self.name_from_prefix("mystery_")
        if _name is None:
            raise ValueError(f"no attribute with 'mystery_' prefix in {self}")

        return (_name[8:], self.attribute_value(_name))


class card:


    def __init__(self, card_type):
        self.attributes = card_type.attributes  # perf tweak: flatten python attribute lookup
        self.card_type = card_type

        self.cache_key = card_type.cache_key


    # perf tweak: don't create custom hash(), it is called ~5M times
    #def __hash__(self):
    #    return hash(self.card_type)


    def __lt__(self, other):
        return str(self) < str(other)


    def __repr__(self):
        return repr(self.card_type)


    def __str__(self):
        return str(self.card_type)


    def contribute_power(self, power_aspect):
        return self.attributes.value(power_aspect)


    @staticmethod
    def for_(card_type):
        if card_type.has_attribute("skill"):
            return skill(card_type)
        elif card_type.has_attribute("soul"):
            return soul(card_type)
        elif is_mystery_item(card_type):
            return mystery_item(card_type)
        else:
            return card(card_type)


    def has_attribute(self, name):
        return self.attributes.has(name)


class skill:
    """skill changes state over time by upgrading and committing to tree of wisdom"""


    def __init__(self,
        card_type,
        level = 1, 
        committed_to = None,
        fulfilled = False,
    ):
        self.card_type = card_type
        self.level = level
        self.committed_to = committed_to
        self.fulfilled = fulfilled

        self._commit_output = None

        _attributes = {
            name: base_value + (self.level-1 if name in all_powers else 0)
            for name, base_value in self.card_type.attributes.items()
        }

        # TODO (smell) skill __init__ depends on skill/soul card_type registration
        #   rewrite 'committing' unused_wisdom, attuned_attribute to @staticmethods ?
        if self.committed_to is not None:
            soul_card_type, attuned_attribute, unused_wisdom = committing.info(self.card_type, self.committed_to)

            # when skill is committed to wisdom, the unused wisdom is removed from attributes..
            del _attributes[unused_wisdom]
            # ..and two new attributes are added: 'committed' and 'attuned_<soul>'
            _attributes["committed"] = 1
            _attributes["attunement_fulfilled" if fulfilled else attuned_attribute] = 1

            self._commit_output = soul_card_type

        self.attributes = attributes(**_attributes)
        self.cache_key = hash(self.attributes)


    def __lt__(self, other):
        return str(self) < str(other)


    def __repr__(self):
        return f"{self}({self.attributes})"


    def __str__(self):
        return str(self.card_type)


    def commit(self, wisdom):
        assert self.committed_to is None, f"skill {self} is already committed to {self.committed_to}"

        return self.update(committed_to=wisdom)


    def commit_output(self):
        return self._commit_output


    def contribute_power(self, power_aspect):
        return self.attributes.value(power_aspect)


    def fulfill(self):
        assert not self.fulfilled, f"skill {self} is already fulfilled"

        return self.update(fulfilled=True)


    def has_attribute(self, name):
        return self.attributes.has(name)


    def reset(self):
        assert self.committed_to is None, f"cannot reset committed skill {self}"

        if self.level == 1:
            return None         # resetting a level1 skill will "unlearn" it

        return self.update(level=1)


    def update(self, level=None, committed_to="", fulfilled=None):
        _level        = self.level if level is None else level
        _committed_to = self.committed_to if committed_to == "" else committed_to # 'None' is a valid 'committed_to' value
        _fulfilled    = self.fulfilled if fulfilled is None else fulfilled

        if self.level == _level and self.committed_to == _committed_to and self.fulfilled == _fulfilled:
            return self

        return skill(self.card_type, level=_level, committed_to=_committed_to, fulfilled=_fulfilled)


    def upgrade(self, to_level=None):
        if self.level >= 9:
            raise ValueError(f"upgrading skill {self} beyond level {self.level}")

        return self.update(level = (self.level + 1) if to_level is None else to_level)


class soul:


    def __init__(self, card_type, level=1, state=soul_state.normal):
        self.card_type = card_type
        self.level = level
        self.state = state

        assert 1 <= level <= 4, f"invalid soul level {level}"
        self._level_suffix = str(self.level) if self.level > 1 else ""

        assert self.state in (soul_state.normal, soul_state.fatigued, soul_state.malady), \
            f"invalid state {self.state}"

        self.attributes, self._name_suffix = soul_transitioning.into(card_type, level=self.level, soul_state=self.state)

        self.cache_key = hash(self.attributes)


    def __lt__(self, other):
        return str(self) < str(other)


    def __repr__(self):
        return f"{self}({self.attributes})"


    def __str__(self):
        return f"{self.card_type}{self._level_suffix}{self._name_suffix}"


    def contribute_power(self, power_aspect):
        return self.attributes.value(power_aspect)


    def cure(self):
        assert self.state == soul_state.malady, f"soul {self} is not maladied"
        return self.update(state=soul_state.normal)


    def fatigue(self):
        if self.state == soul_state.malady:
            return self

        assert self.state == soul_state.normal, f"soul {self} is already fatigued"
        return self.update(state=soul_state.fatigued)


    def has_attribute(self, name):
        return self.attributes.has(name)


    def malady(self):
        assert self.state == soul_state.normal, f"soul {self} is not healthy"
        return self.update(state=soul_state.malady)


    def recover(self):
        if self.state in (soul_state.malady, soul_state.normal):
            return self # maladied souls cannot recover by resting

        return self.update(state=soul_state.normal)


    def update(self, level=None, state=None):
        _level = level or self.level
        _state = state or self.state

        if self.level == _level and self.state == _state:
            return self

        return soul(self.card_type, level=_level, state=_state)


    def upgrade(self):
        assert self.state == soul_state.normal, f"soul {self} is not healthy"
        return self.update(level=self.level+1)


class mystery_item:


    def __init__(self, card_type, mastered=False):
        self.card_type = card_type
        self.mastered = mastered

        if self.mastered:
            _attributes = {}
            # ocd: preserve attribute order and insert 'mastery_<power>' right after 'mystery_<power>'
            #   which is the in-game attribute possition for most mastered items
            for k, v in self.card_type.attributes.items():
                _attributes[k] = v
                if k.startswith("mystery_"):
                    _attributes[f"mastery_{k[8:]}"] = v

            self.attributes = attributes(**_attributes)
        else:
            self.attributes = self.card_type.attributes

        self.cache_key = hash(self.attributes)


    def __lt__(self, other):
        return self.card_type < other.card_type


    def __repr__(self):
        return f"{self}({self.attributes})"


    def __str__(self):
        return str(self.card_type)


    def attribute_value(self, name):
        return self.attributes.value(name)


    def contribute_power(self, power_aspect):
        return self.attributes.value(power_aspect)


    def has_attribute(self, name):
        return self.attributes.has(name)


    def is_mastered(self):
        return self.mastered


    def master(self):
        return self.update(mastered=True)


    def unlockable(self):
        return not self.is_mastered()


    def update(self, mastered=None):
        _mastered = self.mastered if mastered is None else mastered

        if self.mastered == _mastered:
            return self

        return mystery_item(self.card_type, mastered=_mastered)


# aliases of 'card_type' class for backward compatibility
# TODO (cleanup) handle 'journal' as mystery item, including lesson output
journal = card_type

from pprint import pprint

from frozendict import frozendict

from .model import (
    brewing,
    card,
    cataloguing,
    condition,
    is_mystery_item,
    learning,
    mastering,
    match_any_card,
    room_unlocking,
    season,
    serving,
    skill_resetting,
    skill_upgrading,
    slot,
    soul_slot,
)


# TODO (cleanup) rewrite this slot() into funtions; or do immutable souls
is_fatigued_soul    = slot(essential=condition(soul=1), required=condition(fatigued=1))
is_healthy_soul     = slot(essential=condition(soul=1), forbidden=condition(fatigued=1, malady=1))
is_malady_soul      = slot(essential=condition(soul=1), required=condition(malady=1))


def cannot_duplicate(card_or_type):
    """check is card_type can have only one copy in inventory"""

    if card_or_type.has_attribute("assistance") or card_or_type.has_attribute("employable"):
        return True

    if card_or_type.has_attribute("memory") and not card_or_type.has_attribute("lesson"):
        return True

    return False


def perish_at_dawn(card_or_type):
    if card_or_type.has_attribute("assistance") or card_or_type.has_attribute("employable"):
        return True

    if card_or_type.has_attribute("memory") and not card_or_type.has_attribute("persistent"):
        return True

    return False


class state:


    def __init__(self):
        self._inventory = []                        # [ card, .. ]
        self._inventory_counts = {}                 # card_type -> int
        self.current_season = season.spring
        self._opportunities = ()
        self._room_inventory = {}                   # room_name -> None
        self._skill_cap = {}                        # skill_type -> int (max level)
        self._station_inventory = {}                # station_name -> None
        self._station_inventory_locked = {}         # station_name -> None

        self._cache_key = None
        self._inventory_cards = {}

        for room_name in room_unlocking.unlock_at_start():
            self.unlock_room_by_name(room_name)


    def brew(self, card_type):
        self._inventory_remove(card_type)
        self.inventory_add(brewing.into(card_type))


    def cache_key(self):
        if self._cache_key is None:
            self._cache_key = hash((*self._inventory, self.current_season, self._opportunities, *self._station_inventory.keys()))

        return self._cache_key


    def catalogue(self, *items):
        for item in items:
            self._inventory_remove(cataloguing.uncatalogued_for(item))
            self._inventory_add(item)


    def commit(self, skill_type, wisdom):
        old_card = self.inventory_lookup(skill_type)
        assert old_card is not None, f"skill {skill_type} not in inventory"
        new_card = old_card.commit(wisdom)
        self._inventory_replace(old_card, new_card)
        self._inventory_add(new_card.commit_output())


    def cure(self, soul_type, level=1):
        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=level, required=condition(malady=1)))
        assert old_card is not None, f"malady soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_replace(old_card, old_card.fatigue())


    def fatigue(self, soul_type, level=1):
        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=level, forbidden=condition(fatigued=1, malady=1)))
        assert old_card is not None, f"healthy soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_replace(old_card, old_card.fatigue())


    def _inventory_add(self, card_type, _card=None):
        if _card is None:
            _card = card.for_(card_type)
        self._inventory.append(_card)
        self._inventory_counts[card_type] = None    # invalidate counts cache
        self._cache_key = None                      # invalidate state cache key


    def inventory_add(self, *card_types):
        for card_type in card_types:

            # autoserve logic (eg pot -> 3x cups)
            if card_type.has_attribute("to_serve"):
                for item in serving.into(card_type):
                    self._inventory_add(item)

            # autolearn logic (lesson -> skill)
            elif learning.is_skill_lesson(card_type):
                skill_learned = learning.skill_for(card_type)
                if self.inventory_lookup(skill_learned) is None:
                    self._inventory_add(skill_learned)
                else:
                    self._inventory_add(card_type)

            else:
                self._inventory_add(card_type)


    def inventory_add_card(self, card):
        self._inventory_add(card.card_type, card)


    def inventory_card_count(self, card_type):
        if self._inventory_counts.get(card_type, None) is None:
            self._inventory_counts[card_type] = sum(1 for card in self._inventory if card.card_type is card_type)

        return self._inventory_counts[card_type]


    def inventory_card_types(self):
        return self._inventory_counts.keys()


    def inventory_cards(self):
        _val = self._inventory_cards.get(self.cache_key(), None)
        if _val is None:
            _val = tuple(self._inventory)
            self._inventory_cards[self.cache_key()] = _val

        return _val


    def inventory_lookup(self, card_type, condition=match_any_card):
        return next((card for card in self._inventory if card.card_type is card_type and condition.match(card)), None)


    def _inventory_remove(self, card_type, error_if_not_found=True):
        card = self.inventory_lookup(card_type)
        if card is None:
            if error_if_not_found:
                raise KeyError(f"{card_type} not found in inventory")
            else:
                return

        self._inventory_remove_card(card)


    def _inventory_remove_card(self, card):
        index = next((i for i, _card in enumerate(self._inventory) if _card is card), None)
        if index is None:
            raise KeyError(f"{card} not found in inventory")

        del self._inventory[index]
        self._inventory_counts[card.card_type] = None   # invalidate counts cache
        self._cache_key = None                          # invalidate state cache key


    def inventory_remove(self, *card_types, error_if_not_found=True):
        for card_type in card_types:
            self._inventory_remove(card_type, error_if_not_found)


    def inventory_remove_soul(self, soul_type, level=1, malady=False):
        condition_slot = soul_slot(soul_type, level=level, forbidden=condition(malady=1))
        if malady:
            condition_slot = soul_slot(soul_type, level=level, required=condition(malady=1))

        soul_card = self.inventory_lookup(soul_type, condition=condition_slot)
        assert soul_card is not None, f"soul {soul_type} (level={level}) not in inventory"

        self._inventory_remove_card(soul_card)


    def _inventory_replace(self, old_card, new_card):
        index = next((i for i, card in enumerate(self._inventory) if card is old_card), None)
        if index is None:
            raise KeyError(f"{old_card} not found in inventory")

        self._inventory[index] = new_card
        self._inventory_counts[old_card.card_type] = None   # invalidate counts cache
        self._inventory_counts[new_card.card_type] = None   # invalidate counts cache
        self._cache_key = None                              # invalidate state cache key


    def inventory_upsert_card(self, new_card):
        existing_card = next((card for card in self._inventory if card.card_type is new_card.card_type), None)
        if existing_card is None:
            self.inventory_add_card(new_card)
        else:
            self._inventory_replace(existing_card, new_card)


    def locked_neighbors(self):
        _already_yielded = {} # remove duplicate neighbors

        for room_name in self._room_inventory:
            for neighbor_name in room_unlocking.neighbors_for(room_name):
                if neighbor_name not in self._room_inventory and neighbor_name not in _already_yielded:
                    _already_yielded[neighbor_name] = None
                    yield neighbor_name


    def malady(self, soul_type, level=1):
        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=level, forbidden=condition(fatigued=1, malady=1)))
        assert old_card is not None, f"healthy soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_replace(old_card, old_card.malady())


    def master(self, *items):
        for item in items:
            old_card = self.inventory_lookup(item)
            assert old_card is not None, f"mystery item {item} not in inventory"
            self._inventory_replace(old_card, old_card.master())
            self.inventory_add(*mastering.lessons_from(item))


    def mastered_mystery_item_types(self):
        return tuple(card.card_type for card in self.inventory_cards() if is_mystery_item(card.card_type) and card.is_mastered())


    def new_day(self, season=None):
        if season is not None:
            self.current_season = season
            self._cache_key = None          # invalidate state cache key


    def next_opportunities(self, *names):
        self._opportunities = names
        self._cache_key = None          # invalidate state cache key


    def non_mastered_mystery_item_types(self):
        return tuple(card.card_type for card in self.inventory_cards() if is_mystery_item(card.card_type) and not card.is_mastered())


    def opportunities(self):
        return self._opportunities


    def recover(self, soul_type, level=1):
        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=level, required=condition(fatigued=1)))
        assert old_card is not None, f"fatigued soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_replace(old_card, old_card.recover())


    def skill_cap(self, updates):
        self._skill_cap.update(updates)


    def skill_cap_for(self, skill_type):
        return self._skill_cap.get(skill_type, 9)


    def skill_reset(self, skill_type):
        old_card = self.inventory_lookup(skill_type)
        assert old_card is not None, f"skill {skill_type} not in inventory"

        self.inventory_add(*skill_resetting.output_for(old_card.level))

        new_card = old_card.reset()
        if new_card is None:
            self.inventory_remove(old_card)
        else:
            self._inventory_replace(old_card, new_card)


    def upgrade(self, skill_type, using):
        old_card = self.inventory_lookup(skill_type)
        assert old_card is not None, f"skill {skill_type} not in inventory"
        self._inventory_replace(old_card, old_card.upgrade())
        if using is not None:
            assert skill_upgrading.match(skill_type, using), f"upgrading {skill_type} with incompatible {using}"
            self.inventory_remove(using)


    def upgrade_soul(self, soul_type, to_level, using):
        assert 2 <= to_level < 4, f"invalid target soul level {to_level}"

        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=to_level-1, forbidden=condition(fatigued=1, malady=1)))
        assert old_card is not None, f"soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_remove_card(old_card)

        old_card = self.inventory_lookup(soul_type, condition=soul_slot(soul_type, level=to_level-1, forbidden=condition(fatigued=1, malady=1)))
        assert old_card is not None, f"soul {soul_type} (level={to_level}) not in inventory"
        self._inventory_replace(old_card, old_card.upgrade())

        skill_card = self.inventory_lookup(using)
        assert skill_card is not None, f"skill {using} not in inventory"
        self._inventory_replace(skill_card, skill_card.fulfill())


    def unlock(self, room):
        self.unlock_room_by_name(room.name)


    def unlock_room_by_name(self, room_name):
        assert room_name not in self._room_inventory
        self._room_inventory[room_name] = None
        self._cache_key = None          # invalidate state cache key

        self.inventory_add(*room_unlocking.inventory_for(room_name))

        for station_name in room_unlocking.stations_for(room_name):
            self._station_inventory[station_name] = None

        for station_name in room_unlocking.locked_stations_for(room_name):
            self._station_inventory_locked[station_name] = None


    def unlock_station(self, station):
        assert station.name in self._station_inventory_locked, f"station {station.name} not locked"
        del self._station_inventory_locked[station.name]
        self._station_inventory[station.name] = None
        self._cache_key = None          # invalidate state cache key


    def unlocked_room_names(self):
        return tuple(self._room_inventory.keys())


    def unlocked_station_names(self):
        return tuple(self._station_inventory.keys())


    def upgradeable_skills(self):
        return tuple(
            card for card in self.inventory_cards()
            if card.has_attribute("skill") and card.level < self.skill_cap_for(card.card_type)
        )

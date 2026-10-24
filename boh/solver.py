from pprint import pprint

from frozendict import frozendict

from .model import (
    card,
    considering,
    crafting,
    evolving,
    is_consumable,
    is_mystery_item,
    language,
    mastering,
    match_any_card,
    opportunity,
    room_unlocking,
    season,
    simple_solving,
    skill_upgrading,
    soul_state,
    talking,
)

from .state import (
    cannot_duplicate,
    perish_at_dawn,
)

# temp
#from .item import codex


_cache_slot_candidates = {}
_cache_slot_assessed_cards = {}


def assess_inventory_card_cost(card, count, crafting_cost=None):
    """return tuple (cost_when_consumed, cost)"""

    _soul_cost_by_state = frozendict({
        # maladied soul is not consumed, but I need it to have >0 cost
        # otherwise, recipes have 0 total and feed cost-less resources to more recipes
        # TODO (hack) maladied souls cost=1, but in reality it should be cost=0 (?)
        soul_state.normal: 4,
        soul_state.malady: 1,
    })

    _card_type = card.card_type

    if _card_type.has_attribute("soul"):
        cost = _soul_cost_by_state.get(card.state, 0)
        return (cost, cost)
    elif _card_type.has_attribute("skill"):
        return (0, 0)
    elif perish_at_dawn(_card_type):
        return (0, 0)   # use perishable cards asap
    elif is_mystery_item(_card_type) or _card_type.has_attribute("lesson") or _card_type.has_attribute("uncatalogued"):
        return (16, 16) # some items have the same (high) value, even if you have more of them
    elif _card_type.has_attribute("memory") and _card_type.has_attribute("persistent"):
        return (1, 1)   # static cost for persistent memory (in inventory)
    else:
        match count:
            case 1: cost = 16
            case 2: cost = 8
            case 3: cost = 4
            case 4: cost = 2
            case _: cost = 1

        if crafting_cost is not None:
            # craft-able item usually get cost from their (static) crafting cost, rather than inventory count
            cost = min(cost, crafting_cost)

        if is_consumable(_card_type):
            return (cost, cost)
        else:
            return (cost, 0)


def best_solution(problems, assessed_cards, cost_limit=None, debug_name=None):
    """return lowest 'cost' solution under 'cost_limit' or 'None' if no solution found"""

    _cost_limit          = cost_limit
    best_solution_so_far = None

    for problem in problems:
        try:
            best_solution_so_far = problem.solve(assessed_cards, cost_limit=_cost_limit, debug_name=debug_name)
            _cost_limit = best_solution_so_far.cost
        except problem_exception:
            pass # no solution, or cost too high

    return best_solution_so_far


def cost_for_probability(cost, probability):
    # solution's cost is adjusted by output's inverse probability, eg:
    # probability   cost
    #        100%   cost
    #         50%   cost * 2
    #         20%   cost * 5
    #          4%   cost * 25
    return int(cost * 100.0/probability)


def dedup_assessed_cards(assessed_cards):
    _can_duplicate = tuple( assessed_card for assessed_card in assessed_cards if not cannot_duplicate(assessed_card.card) )

    _cannot_duplicate = {}
    for assessed_card in assessed_cards:
        if cannot_duplicate(assessed_card.card):
            if assessed_card.card.card_type not in _cannot_duplicate or \
                assessed_card.cost_when_consumed < _cannot_duplicate[assessed_card.card.card_type].cost_when_consumed:

                _cannot_duplicate[assessed_card.card.card_type] = assessed_card

    return _can_duplicate + tuple(_cannot_duplicate.values())


def room_unlocking_problems_for(room_name):
    return tuple(
        problem(
            slots = slots,
            power_aspect = power_aspect,
            power_requirement = power_requirement,
        )
        for slots, power_aspect, power_requirement in room_unlocking.slots_for(room_name)
    )


def slot_assessed_cards(slot, assessed_cards):
    """return a tuple of assessed cards matching a slot"""

    _cache_key = (slot.cache_key, hash(assessed_cards))
    _val = _cache_slot_assessed_cards.get(_cache_key, None)

    if _val is None:
        _val = tuple(assessed_card for assessed_card in assessed_cards if slot.match(assessed_card.card))
        _cache_slot_assessed_cards[_cache_key] = _val

    return _val


def slot_candidates(slot, assessed_cards, power_aspect=None, condition=None):
    """return a tuple of slot_card() of cards matching a slot (and 'condition') with cost evaluated
    with respect to 'power_aspect'. And the result sorted by relative cost (cost / power_contribution)"""

    _cache_key = (slot.cache_key, hash(assessed_cards), slot.consume_all, power_aspect, condition)
    _val = _cache_slot_candidates.get(_cache_key, None)

    if _val is None:
        _assessed_cards = slot_assessed_cards(slot, assessed_cards)     # cards matching the slot

        # if there is an extra condition, filter cards through it
        if condition is not None:
            _assessed_cards = tuple(assessed_card for assessed_card in _assessed_cards if condition.match(assessed_card.card))

        # assess card cost for specific slot and power aspect, and sort by relative power
        _val = tuple(sorted(
            slot_card(card=assessed_card.card, cost=assessed_card.cost_in_slot(slot.consume_all), power_aspect=power_aspect)
            for assessed_card in _assessed_cards
        ))

        _cache_slot_candidates[_cache_key] = _val

    return _val


def solve_simple(slots, assessed_cards):
    """take the best candidate for each of the slots"""
    # TODO (logic) 'solve_simple' can return duplicates in solution !!

    candidates = tuple(
        slot_candidates(slot, assessed_cards)
        for slot in slots
    )

    if any(len(candidates_for_slot) == 0 for candidates_for_slot in candidates):
        return None

    return tuple(candidates_for_slot[0] for candidates_for_slot in candidates)


class assessed_card:


    def __init__(self, card, cost, cost_when_consumed=None):
        self.card = card
        self.cost = cost
        self.cost_when_consumed = cost_when_consumed if cost_when_consumed is not None else cost


    def __lt__(self, other):
        return self.card < other.card


    def __repr__(self):
        return f"{self}(c+{self.cost_when_consumed})"


    def __str__(self):
        return str(self.card)


    def cost_in_slot(self, slot_consume_all=False):
        if slot_consume_all and self.cost_when_consumed is not None:
            return self.cost_when_consumed
        return self.cost


class computed_available_inventory:
    """cards available from running actions. For each card type we keep the best
    (cheapest) solution"""


    def __init__(self):
        self._card_solution = {}    # card_type -> solution_simple


    def card_solutions(self):
        return tuple(self._card_solution.items())


    def cost_for(self, card_type):
        if card_type not in self._card_solution:
            return None

        return self._card_solution[card_type].cost


    def update_if_better(self, card_type, solution):
        if card_type not in self._card_solution:
            self._card_solution[card_type] = solution
        elif solution.cost < self._card_solution[card_type].cost:
            self._card_solution[card_type] = solution


class problem_exception(Exception): pass


class problem:


    def __init__(self,
        slots,
        additional_slots = (),              # optional slots on top of action's "starting slots"
        station_name = "",                  # reference to station/action to pass to solution object for info
        power_aspect = None,                # power aspect (eg "grail") to maximize by; or None to find any solution
        power_requirement = 0,              # sum of all card's power aspect must be at least this; or 0 to find any solution
        solution_must_include = None,       # condition, that the sum of solution cards must satisfy (eg, flower=1)
    ):
        self.slots = tuple(slots) + additional_slots
        self.station_name = station_name
        self.power_aspect = power_aspect
        self.power_requirement = power_requirement
        self.solution_must_include = solution_must_include

        self._last_starting_slot_index = len(slots) - 1
        self._last_mandatory_slot_index = max((i for i, slot in enumerate(self.slots) if not slot.optional), default=None)
        assert self._last_mandatory_slot_index is not None, f"no mandatory slot for problem {slots}"

        # check if all optional slots are after all mandatory slots
        _first_optional_slot_index = min((i for i, slot in enumerate(self.slots) if slot.optional), default=None)
        if _first_optional_slot_index is not None:
            assert self._last_mandatory_slot_index < _first_optional_slot_index, f"mixed optional and mandatory slots"


    def solve(self, assessed_cards, n_candidates=5, cost_limit=None, debug_name=None):

        # for each slot, find suitable candidate cards, sort them by their relative cost
        # which is specific to the slot and then take 'n_candidates' best candidates (cheapest)
        candidates = tuple(
            slot_candidates(slot, assessed_cards, self.power_aspect)[:n_candidates]
            for slot in self.slots
        )

        #if debug_name == "ascendant_harmony" and self.station_name == "instrument_hallowed_drum":
        #    pprint(candidates)
        #if debug_name == "the_black_book_of_brittany" and self.station_name == "consider":
        #    pprint(candidates)

        # for each slot, find candidates that fit into the slot and match the 'solution_must_include'
        # if there is no 'solution_must_include' condition, then the tuples are empty
        if self.solution_must_include is not None:
            must_include_candidates = tuple(
                slot_candidates(slot, assessed_cards, self.power_aspect, condition=self.solution_must_include)[:n_candidates]
                for slot in self.slots
            )

            if all( len(candidates) == 0 for candidates in must_include_candidates ):
                # fail fast if there is no card matching 'solution_must_include' in any slot
                raise problem_exception(f"no solution: no match for 'solution_must_include'")
        else:
            must_include_candidates = tuple(tuple() for _ in self.slots)

        current_solution = {}
        best_solution = None
        best_cost = cost_limit

        def backtrack(slot_idx: int, sum_cost: int, sum_power: int, must_include_satisfied: bool):
            nonlocal best_cost, best_solution

            if best_cost is not None and sum_cost >= best_cost:
                return # cost is already too high, backtrack

            # all mandatory slots are filled
            remaining_slots_optional = slot_idx > self._last_mandatory_slot_index

            if sum_power >= self.power_requirement and remaining_slots_optional and must_include_satisfied:
                # power requirement is satisfied, filling more slots would only increase the cost, stop now
                best_solution = solution(
                    cost         = sum_cost,
                    power_aspect = self.power_aspect,
                    slot_cards   = tuple(current_solution.values()),
                    station_name = self.station_name,
                )
                best_cost = sum_cost
                #print("solution", best_cost, best_solution)
                return
            elif self.power_requirement > 0 and sum_power == 0 and slot_idx > self._last_starting_slot_index:
                return  # starting slots must contribute at least one power, backtrack
            else:
                pass # cost is still low, but we haven't met all requirements, continue

            if slot_idx >= len(candidates):
                return # all slots explored, backtrack

            if self.slots[slot_idx].optional:
                # try solution with no card in this slot
                backtrack(
                    slot_idx = slot_idx + 1,
                    sum_cost = sum_cost,
                    sum_power = sum_power,
                    must_include_satisfied = must_include_satisfied,
                )

            for slot_card in must_include_candidates[slot_idx]+candidates[slot_idx]:
                if slot_card.card in current_solution:
                    continue # card is already used by previous slot

                current_solution[slot_card.card] = slot_card
                backtrack(
                    slot_idx = slot_idx + 1,
                    sum_cost = sum_cost + slot_card.cost,
                    sum_power = sum_power + slot_card.power,

                    # switch 'must_include_satisfied' to true if this slot is matching the 'solution_must_include'
                    must_include_satisfied = (must_include_satisfied or self.solution_must_include.match(slot_card.card)),
                )
                del current_solution[slot_card.card]

            return # tried all candidates for this slot, backtrack

        backtrack(
            slot_idx = 0,
            sum_cost = 0,
            sum_power = 0,
            must_include_satisfied = (self.solution_must_include is None),
        )

        if best_solution is None:
            raise problem_exception(f"no solution found")

        return best_solution


class slot_card:
    """card, if used in specific slot with problem-specific power aspect"""


    def __init__(self, card: card, cost=0, power_aspect=None):
        self.card = card
        self.cost = cost

        self.power = card.contribute_power(power_aspect) if power_aspect is not None else 0
        self.relative_cost = self.cost / self.power if self.power > 0 else None


    def __lt__(self, other):
        """
        'less' means 'better'; lower cost, higher power

        sort candidates by
        * (relative_cost, 1/power) - if either of them contribute power
        * (cost)                   - if neither of them contribute power
        """
        if self.relative_cost is None:
            if other.relative_cost is None:
                return self.cost < other.cost               # neither contributes power => sort by cost
            else:
                return False                                # 'other' contributes power, 'self' does not => 'other' wins
        elif other.relative_cost is None:
            return True                                     # 'self' contributes power, 'other' does not => 'self' wins
        else:
            if self.relative_cost == other.relative_cost:   # both contribute power => sort by (relative_cost, 1/power)
                return self.power >= other.power
            else:
                return self.relative_cost < other.relative_cost


    def __repr__(self):
        return str(self)


    def __str__(self):
        contribution = []

        if self.cost > 0:
            contribution.append(f"c=+{self.cost}")

        if self.power > 0:
            contribution.append(f"p=+{self.power}")

        contribution_str = ", ".join(contribution)
        contribution_str = f"({contribution_str})" if len(contribution) > 0 else ""

        return f"{str(self.card)}{contribution_str}"


# TODO (idea) replace 'solution' with 'solution_simple' ?
class solution:


    def __init__(self, cost, power_aspect, slot_cards, station_name):
        self.cost         = cost
        self.power_aspect = power_aspect
        self.slot_cards   = slot_cards
        self.station_name = station_name


    def __str__(self):
        _str_list = [f"cost={self.cost}"]
        _str_list.extend([ str(slot_card) for slot_card in self.slot_cards ])

        if self.station_name:
            _str_list.append(f"(via {self.station_name})")

        return " ".join(_str_list)


class solution_simple:


    def __init__(self, station_name, solution_cards=(), pennies=0, probability=100):
        self.station_name = station_name
        self.solution_cards = solution_cards
        self.pennies = pennies
        self.probability = probability

        self.cost = cost_for_probability(sum(solution_card.cost for solution_card in self.solution_cards) + self.pennies, self.probability)


    def __str__(self):
        _str_list = [f"cost={self.cost}"]

        if self.probability < 100:
            _str_list.append(f"probability={self.probability}%")

        if self.pennies > 0:
            _str_list.append(f"pennies(c=+{self.pennies})")

        _str_list.extend([ str(solution_card) for solution_card in self.solution_cards ])

        _str_list.append(f"(via {self.station_name})")

        return " ".join(_str_list)


    def add_solution_card(self, solution_card):
        return solution_simple(
            self.station_name,
            solution_cards = (*self.solution_cards, solution_card),
            pennies = self.pennies,
            probability = self.probability,
        )


    def update_probability(self, probability):
        return solution_simple(
            self.station_name,
            solution_cards = self.solution_cards,
            pennies = self.pennies,
            probability = probability,
        )


class static_available_inventory:
    """output of recipes that is cheap enough that we could consider
    it is as part of inventory. It would be too expensive to solve recipes
    to get the list every time. That's why it is managed manually."""


    def __init__(self):
        self._cost = {}             # card_type -> int
        self._assessed_card = {}    # card_type -> assessed_card


    def assessed_cards(self):
        return tuple(self._assessed_card.values())


    def cost_for(self, card_type):
        return self._cost.get(card_type)


    def update(self, card_type, cost):
        self._cost[card_type] = cost
        self._assessed_card[card_type] = assessed_card(card.for_(card_type), cost=cost)


class solver:


    def __init__(self, state):
        self.state = state

        self.static_available_inventory = static_available_inventory()

        self._available_cards_cache = None
        self._cache_assessed_cards = {}


    def assessed_available_cards(self):
        return tuple(assessed_card(card.for_(card_type), cost=solution.cost) for card_type, solution in self.available_card_solutions())


    def assessed_cards(self):
        _val = self._cache_assessed_cards.get(self.state.cache_key(), None)

        if _val is None:
            _val = dedup_assessed_cards(self.assessed_inventory_cards_with_static() + self.assessed_available_cards())
            self._cache_assessed_cards[self.state.cache_key()] = _val

        return _val


    def assessed_inventory_cards(self):
        _assessed_cards = []
        for card in self.state.inventory_cards():
            cost_when_consumed, cost = assess_inventory_card_cost(card,
                count         = self.state.inventory_card_count(card.card_type),
                crafting_cost = self.static_available_inventory.cost_for(card.card_type),
            )
            _assessed_cards.append(assessed_card(card, cost, cost_when_consumed))

        return tuple(_assessed_cards)


    def assessed_inventory_cards_with_static(self):
        return tuple(sorted(dedup_assessed_cards(self.assessed_inventory_cards() + self.static_available_inventory.assessed_cards())))


    def assessed_mood_cards(self):
        return tuple(
            assessed_card(card.for_(card_type), cost=0)
            for card_type in opportunity.mood_card_types_for(*self.state.opportunities())
        )


    def available_card_solutions(self):

        # TODO (cleanup) caching for 'available_card_solutions'
        if self._available_cards_cache is not None:
            return self._available_cards_cache.card_solutions()

        _available_card = computed_available_inventory()
        assessed_inventory_cards = self.assessed_inventory_cards_with_static()
        mastered_mystery_item_types = self.state.mastered_mystery_item_types()
        unlocked_station_names = self.state.unlocked_station_names()

        # simple_solving
        for station_name, action_name, output, slots, pennies in simple_solving.actions():
            if station_name not in unlocked_station_names:
                continue # station not unlocked

            _solution_cards = solve_simple(slots, assessed_inventory_cards)
            if _solution_cards is None:
                continue # no solution

            _solution = solution_simple(station_name, _solution_cards, pennies=pennies)
        
            for output_card_type, probability, _season in output:
                if _season not in (season.any, self.state.current_season):
                    continue

                _available_card.update_if_better(output_card_type, _solution.update_probability(probability))

        # talking (should be after simple_solving, which provide assistance)
        for assistance_card_type, output in talking.output():
            cost = _available_card.cost_for(assistance_card_type)
            if cost is None:
                continue    # assistance not available for hire (yet)

            assessed_assistance = assessed_card(card.for_(assistance_card_type), cost=cost)
            for output_card_type, probability in output:
                _solution = solution_simple("talk", solution_cards=(assessed_assistance, ), probability=probability)
                _available_card.update_if_better(output_card_type, _solution)

        # rereading - solve mastering station soul slot and add all re-reading output for mastered items
        for station_name, slots, output in mastering.rereading():
            if station_name not in unlocked_station_names:
                continue # station not unlocked

            _solution_cards = solve_simple(slots, assessed_inventory_cards)
            if _solution_cards is None:
                continue # no matching soul for station

            _soul_solution = solution_simple(station_name, _solution_cards)

            for mystery_item, provided_card_type in output:
                if mystery_item not in mastered_mystery_item_types:
                    continue # mystery item not mastered yet

                assessed_mystery_item = assessed_card(card.for_(mystery_item), cost=0)
                _available_card.update_if_better(provided_card_type, _soul_solution.add_solution_card(assessed_mystery_item))

        # considering - solve considering soul and add consider output of all inventory cards
        _solution_cards = solve_simple(considering.soul_slots(), assessed_inventory_cards)
        if _solution_cards is not None: # there is matching soul for consider
            _soul_solution = solution_simple("consider", _solution_cards)
            for assessed_inventory_card in assessed_inventory_cards:
                inventory_card_type = assessed_inventory_card.card.card_type
                consider_output = considering.into(inventory_card_type)
                if consider_output is None:
                    continue # inventory item that cannot be considered

                slot_inventory_card = slot_card(assessed_inventory_card.card, cost=assessed_inventory_card.cost_in_slot())
                _soul_and_card_solution = _soul_solution.add_solution_card(slot_inventory_card)
                _available_card.update_if_better(consider_output, _soul_and_card_solution)

        self._available_cards_cache = _available_card
        return self._available_cards_cache.card_solutions()


    def evolving_problems_for(self, soul_card_type):
        unlocked_station_names = self.state.unlocked_station_names()
        return tuple(
            problem(
                station_name = station_name,
                slots = slots,
            )
            for station_name, slots in evolving.slots_for(soul_card_type)
            if station_name in unlocked_station_names
        )


    def mastering_problems_for(self, card_type, opportunity_slots):
        power_aspect, power_requirement = card_type.power_aspect_and_value()
        unlocked_station_names = self.state.unlocked_station_names()

        return tuple(
            problem(
                station_name = station_name,
                slots = slots,
                additional_slots = opportunity_slots,
                power_aspect = power_aspect,
                power_requirement = power_requirement,
            )
            for station_name, slots in mastering.slots_for(card_type)
            if station_name in unlocked_station_names
        )


    def print_available_card_solutions(self):
        print("available:")
        for card_type, solution in sorted(self.available_card_solutions()):
            print(f"{str(card_type):<40} {solution}")
        print()


    def print_evolving_solutions(self):
        assessed_cards = self.assessed_cards()
        print("upgradeable souls:")
        for soul_card_type in evolving.all_souls():
            solution = best_solution(self.evolving_problems_for(soul_card_type), assessed_cards)

            if solution is not None:
                print(f"{str(soul_card_type):<40} {solution}")
        print()


    def print_inventory_costs(self):
        print("inventory costs:")
        for assessed_card in sorted(self.assessed_inventory_cards()):
            print(f"{repr(assessed_card.card)}: {assessed_card.cost_when_consumed}")
        print()


    def print_inventory_counts(self):
        print("inventory counts:")
        for card_type in sorted(self.state.inventory_card_types()):
            _count = self.state.inventory_card_count(card_type)
            if _count > 0:
                print(f"{repr(card_type)}: {self.state.inventory_card_count(card_type)}")
        print()


    def print_item_unlock_solutions(self):
        assessed_cards = self.assessed_cards() + self.assessed_mood_cards()
        #pprint(assessed_cards)
        opportunity_slots = opportunity.slots_for(*self.state.opportunities())
        print("locked items:")
        for card_type in sorted(self.state.non_mastered_mystery_item_types()):
        #for card_type in (codex.the_black_book_of_brittany, ):
            solution = best_solution(self.mastering_problems_for(card_type, opportunity_slots), assessed_cards, debug_name=card_type.name)

            if solution is not None:
                print(f"{str(card_type):<40} {solution}")
        print()


    def print_recipe_solutions(self):
        assessed_cards = self.assessed_cards()
        _static_available_update = []

        print("recipe:")
        for output in sorted(crafting.outputs()):
            solution = best_solution(self.recipe_problems_for(output), assessed_cards, debug_name=output.name)

            if solution is not None:
                print(f"{str(output):<40} {solution}")

                # logic to print "update" python snippet for 'static_available_inventory'
                existing_static_available_cost = self.static_available_inventory.cost_for(output)
                if existing_static_available_cost is None:
                    existing_static_available_cost = 9

                if solution.cost < existing_static_available_cost:
                    _output_and_cost = f"{output}: {solution.cost},"
                    _static_available_update.append(f"    {_output_and_cost:<36}# {solution}")
        print()

        if len(_static_available_update) > 0:
            print("static_available_update:")
            print("\n".join(_static_available_update))
            print()


    def print_room_unlock_solutions(self):
        assessed_cards = self.assessed_cards()
        print("locked rooms:")
        for room_name in sorted(self.state.locked_neighbors()):
            solution = best_solution(room_unlocking_problems_for(room_name), assessed_cards)

            if solution is not None:
                print(f"{room_name:<40} {solution}")
        print()


    def print_skill_upgrade_solutions(self):
        assessed_cards = self.assessed_cards()
        print("upgradeable skills:")
        for skill_card in sorted(self.state.upgradeable_skills()):
            try:
                _problem = problem(slots=skill_upgrading.slots_for(skill_card.card_type, skill_card.level))
                solution = _problem.solve(assessed_cards, n_candidates=9)
                print(f"{str(skill_card):<40} (-> level{skill_card.level+1}) {solution}")
            except problem_exception:
                pass
        print()


    def print_static_available(self):
        print("static available:")
        for assessed_card in sorted(self.static_available_inventory.assessed_cards()):
            print(f"{str(assessed_card.card):<40} cost={assessed_card.cost}")
        print()


    def recipe_problems_for(self, output):
        """return dict of crafting output mapped to recipes/problems that create it"""

        unlocked_station_names = self.state.unlocked_station_names()
        return tuple(
            problem(
                station_name = station_name,
                slots = slots,
                power_aspect = power_aspect,
                power_requirement = power_requirement,
                solution_must_include = solution_must_include,
            )
            for station_name, slots, power_aspect, power_requirement, solution_must_include in crafting.slots_for(output)
            if station_name in unlocked_station_names
        )


    def static_available(self, static_available_update):
        for card_type, cost in static_available_update.items():
            self.static_available_inventory.update(card_type, cost)

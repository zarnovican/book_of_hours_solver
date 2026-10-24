import uuid

import streamlit as st

from boh import station
from boh.model import attributes, committing, is_mystery_item, lookup, mastering, mystery_item, season, skill, soul, soul_state
from boh.solver import problem_exception, solver
from boh.state import state


season_map = dict(
    spring = season.spring,
    summer = season.summer,
    autumn = season.autumn,
    winter = season.winter,
    numa   = season.numa,
)

soul_state_map = dict(
    normal   = soul_state.normal,
    fatigued = soul_state.fatigued,
    malady   = soul_state.malady,
)


def attributes_as_markdown(attributes):
    """card attributes as string of 'streamlit' badges with power aspects colored"""

    _badge_color = dict(
        edge            = "yellow",
        forge           = "orange",
        grail           = "red",
        heart           = "red",
        knock           = "violet",
        lantern         = "yellow",
        moon            = "grey",
        moth            = "grey",
        mystery_edge    = "yellow",
        mystery_forge   = "orange",
        mystery_grail   = "red",
        mystery_heart   = "red",
        mystery_knock   = "violet",
        mystery_lantern = "yellow",
        mystery_moon    = "grey",
        mystery_moth    = "grey",
        mystery_nectar  = "green",
        mystery_rose    = "violet",
        mystery_scale   = "orange",
        mystery_sky     = "blue",
        mystery_winter  = "blue",
        nectar          = "green",
        rose            = "violet",
        scale           = "orange",
        sky             = "blue",
        winter          = "blue",
    )

    return " ".join(
        ( f":{_badge_color.get(k, "grey")}-badge[{k}{f" {v}" if v > 1 else ""}]" )
        for k, v in attributes.items()
    )


def solution_cards_as_markdown(slot_cards, with_power=True):
    return "\n".join(
        "".join((
            f"* {slot_card.card}",
            f" :yellow-badge[+{slot_card.cost}]" if slot_card.cost > 0 else "",
            f" :violet-badge[+{slot_card.power}]" if with_power and slot_card.power > 0 else "",
        ))
        for slot_card in slot_cards
    )


class st_card:
    """generic immutable card"""


    def __init__(self, row_id, type, name):
        self.name   = name
        self.row_id = row_id
        self.type   = type

        self.delete_key = f"soul_{row_id}_delete"


class st_skill:


    def __init__(self, row_id, name, enable, level, level_cap, committed_to, fulfilled):
        self.committed_to = committed_to
        self.enable       = enable
        self.fulfilled    = fulfilled
        self.level        = level
        self.level_cap    = level_cap
        self.name         = name

        self.committed_to_key = f"skill_{row_id}_committed_to"
        self.enable_key       = f"skill_{row_id}_enable"
        self.fulfilled_key    = f"skill_{row_id}_fulfilled"
        self.level_key        = f"skill_{row_id}_level"
        self.level_cap_key    = f"skill_{row_id}_level_cap"

        self.update_derived()


    def as_card(self):
        return skill(lookup.card_type("skill", self.name), level=self.level, committed_to=self.committed_to, fulfilled=self.fulfilled)


    def update(self):
        self.committed_to = st.session_state.get(self.committed_to_key, self.committed_to)
        self.enable       = st.session_state.get(self.enable_key, self.enable)
        self.fulfilled    = st.session_state.get(self.fulfilled_key, self.fulfilled)
        self.level        = st.session_state.get(self.level_key, self.level)
        self.level_cap    = st.session_state.get(self.level_cap_key, self.level_cap)

        self.update_derived()


    def update_derived(self):
        _card = self.as_card()

        self.attributes    = attributes_as_markdown(_card.attributes)
        self.is_language   = _card.has_attribute("language")
        self.valid_wisdoms = (None, ) + committing.valid_wisdoms_for(_card.card_type)


class st_mystery_item:


    def __init__(self, row_id, type, name, mastered):
        self.mastered = mastered
        self.name     = name
        self.row_id   = row_id
        self.type     = type

        self.delete_key   = f"mystery_item_{row_id}_delete"
        self.mastered_key = f"mystery_item_{row_id}_mastered"

        self.update_derived()


    def as_card(self):
        return mystery_item(lookup.card_type(self.type, self.name), mastered=self.mastered)


    def update(self):
        self.mastered = st.session_state.get(self.mastered_key, self.mastered)

        self.update_derived()


    def update_derived(self):
        _card = self.as_card()

        power, value = _card.card_type.power_aspect_and_value()
        self.power_attributes = attributes_as_markdown(attributes(**{ power: value }))
        self.attributes       = attributes_as_markdown(_card.attributes)
        self.provided_memory  = mastering.provides(_card.card_type).name


class st_soul:


    def __init__(self, row_id, name, enable, level, state):
        self.enable = enable
        self.level  = level
        self.name   = name
        self.state  = state
        self.row_id = row_id

        self.delete_key = f"soul_{row_id}_delete"
        self.enable_key = f"soul_{row_id}_enable"
        self.level_key  = f"soul_{row_id}_level"
        self.state_key  = f"soul_{row_id}_state"

        self.valid_states = ("normal", "fatigued", "malady") if name != "mettle" else ("normal", "fatigued")

        self.update_derived()


    def as_card(self):
        return soul(lookup.card_type("soul", self.name), level=self.level, state=soul_state_map[self.state])


    def update(self):
        self.enable = st.session_state.get(self.enable_key, self.enable)
        self.level  = st.session_state.get(self.level_key, self.level)
        self.state  = st.session_state.get(self.state_key, self.state)

        self.update_derived()


    def update_derived(self):
        _card = self.as_card()

        _state_as_markdown = dict(
            normal   = ":green-badge[normal]",
            fatigued = ":grey-badge[fatigued]",
            malady   = ":violet-badge[malady]",
        )
        self.state_as_markdown = _state_as_markdown[self.state]
        self.attributes        = attributes_as_markdown(_card.attributes)


class dict_no_none(dict):
    """'dict()' that does not store None values"""

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if v is not None:
                self[k] = v


def solver_from_streamlit_state(data):
    """return 'boh.solver' from 'streamlit' state"""

    return solver(state_from_streamlit_state(data))


def state_from_streamlit_state(data):
    """return 'boh.state' from 'streamlit' state"""

    _state = state()

    _state.current_season = season_map[data["season"]]

    # out-of-map rooms, which are presumably already unlocked
    _state.unlock_room_by_name("brancrug_village")
    _state.unlock_room_by_name("cucurbit_bridge")
    _state.unlock_room_by_name("crowcross_sands")

    # all village households unlocked
    _state.unlock_station(station.the_rectory)
    _state.unlock_station(station.the_sweet_bones)
    _state.unlock_station(station.mr_and_mrs_kille)
    _state.unlock_station(station.the_smithy)

    for name in data["room"]:
        _state.unlock_room_by_name(name)

    for item in data["mystery_item"].values():
        # 'upsert', since some rooms contain mystery items as well
        _state.inventory_upsert_card(item.as_card())

    for name, in_inventory in data["memory"].items():
        if in_inventory:
            _state.inventory_add(lookup.card_type("memory", name))

    for item in data["soul"].values():
        if item.enable:
            _state.inventory_add_card(item.as_card())

    for item in data["skill"]:
        if item.enable:
            _card = item.as_card()
            _state.inventory_add_card(_card)
            _state.skill_cap({ _card.card_type: item.level_cap })

    for item in data["inventory_removal"].values():
        _state.inventory_remove(lookup.card_type(item.type, item.name), error_if_not_found=False)

    for item in data["inventory_addition"].values():
        _state.inventory_add(lookup.card_type(item.type, item.name))

    return _state


def app_state_from_boh(state, inventory_addition, inventory_removal):
    """generate app state from 'boh.state.state'"""

    lesson_card_types = tuple(card.card_type for card in state.inventory_cards() if card.has_attribute("lesson"))

    _inventory_addition = {}
    for card_type in inventory_addition + lesson_card_types:
        row_id = uuid.uuid4()
        _inventory_addition[row_id] = st_card(row_id, card_type.type, card_type.name)

    _inventory_removal = {}
    for card_type in inventory_removal:
        row_id = uuid.uuid4()
        _inventory_removal[row_id] = st_card(row_id, card_type.type, card_type.name)

    _mystery_item = {}
    for card in state.inventory_cards():
        if is_mystery_item(card.card_type):
            row_id = uuid.uuid4()
            _mystery_item[row_id] = st_mystery_item(
                row_id   = row_id,
                type     = card.card_type.type,
                name     = card.card_type.name,
                mastered = card.mastered,
            )

    _room_list = sorted(r for r in state.unlocked_room_names() if r not in (
        "brancrug_village",
        "crowcross_sands",
        "cucurbit_bridge",
        "global_room",
        "st_brandans_cove",
        "the_atlantic_ocean",
    ))

    # skill collection has all skills, because 'level_cap' may be defined even of skills we don't have yet
    _skill = []
    for name, skill_type in lookup.skills():
        skill_card = state.inventory_lookup(skill_type)
        _skill.append(st_skill(
            row_id       = uuid.uuid4(),
            name         = name,
            enable       = skill_card is not None,
            level        = skill_card.level if skill_card is not None else 1,
            level_cap    = state.skill_cap_for(skill_type),
            committed_to = skill_card.committed_to if skill_card is not None else None,
            fulfilled    = skill_card.fulfilled if skill_card is not None else False,
        ))

    _soul = {}
    for card in state.inventory_cards():
        if card.has_attribute("soul"):
            row_id = uuid.uuid4()
            _soul[row_id] = st_soul(
                row_id = row_id,
                name   = card.card_type.name,
                enable = True,
                level  = card.level,
                state  = card.state,
            )

    return dict(
        inventory_addition = _inventory_addition,
        inventory_removal  = _inventory_removal,
        memory             = {},                    # I've never tracked memories, not even persistent, in the main log
        mystery_item       = _mystery_item,
        room               = _room_list,
        season             = str(state.current_season),
        skill              = _skill,
        soul               = _soul,
        weather            = {},
    )


def app_state_load(app_state, data):
    """load 'data' (from json file) into 'app_state' (streamlit app)"""

    # inventory_removal and inventory_addition
    for inventory_op in ("inventory_removal", "inventory_addition"):
        app_state[inventory_op] = {}
        for card_type_name in data.get(inventory_op, []):
            type, name = card_type_name.split(".")
            row_id = uuid.uuid4()
            app_state[inventory_op][row_id] = st_card(
                row_id = row_id,
                type   = type,
                name   = name,
            )

    # memory
    app_state["memory"]  = { name: True for name in data.get("memory", []) }
    app_state["weather"] = { name: True for name in data.get("weather", []) }

    # mystery_item
    app_state["mystery_item"] = {}
    for name, item in data.get("mystery_item", {}).items():
        row_id = uuid.uuid4()
        app_state["mystery_item"][row_id] = st_mystery_item(
            row_id   = row_id,
            type     = item.get("type", "codex"),
            name     = name,
            mastered = item.get("mastered", True),
        )

    # room
    app_state["room"] = data.get("room", [])

    # skill
    app_state["skill"] = []
    for name, _ in lookup.skills():
        skill_entry = data.get("skill", {}).get(name, dict(enable=False))
        app_state["skill"].append(st_skill(
            row_id       = uuid.uuid4(),
            name         = name,
            enable       = skill_entry.get("enable", True),
            level        = skill_entry.get("level", 1),
            level_cap    = skill_entry.get("level_cap", 9),
            committed_to = skill_entry.get("committed_to"),
            fulfilled    = skill_entry.get("fulfilled", False),
        ))

    # soul
    app_state["soul"] = {}
    for item in data.get("soul", []):
        assert "name" in item, f"missing 'name' in soul {item}"
        row_id = uuid.uuid4()
        app_state["soul"][row_id] = st_soul(
            row_id = row_id,
            name   = item["name"],
            enable = item.get("enable", True),
            level  = item.get("level", 1),
            state  = item.get("state", "normal"),
        )

    app_state["season"]  = data.get("season", "spring")

    app_state["initialized"] = True


def minimize_app_state(app_state):
    """serialized 'app_state' to plain python data; remove defaults and empty entries"""

    _mystery_item = {
        item.name: dict_no_none(
            mastered = False if not item.mastered else None,
            type     = item.type if item.type != "codex" else None,
        )
        for item in app_state["mystery_item"].values()
    }

    _skill = {
        item.name: dict_no_none(
            committed_to = item.committed_to,
            enable       = False if not item.enable else None,
            fulfilled    = True if item.fulfilled else None,
            level        = item.level if item.level > 1 else None,
            level_cap    = item.level_cap if item.level_cap < 9 else None,
        )
        for item in app_state["skill"]
        if item.enable or item.level_cap < 9 # save disabled skills only if they have non-default 'level_cap'
    }

    _soul = [
        dict_no_none(
            enable = False if not item.enable else None,
            level  = item.level if item.level > 1 else None,
            name   = item.name,
            state  = item.state if item.state != "normal" else None,
        )
        for item in sorted(app_state["soul"].values(), key=lambda x: (x.name, x.level))
    ]

    return dict(
        inventory_addition = sorted(tuple(f"{card_type.type}.{card_type.name}" for card_type in app_state["inventory_addition"].values())),
        inventory_removal  = sorted(tuple(f"{card_type.type}.{card_type.name}" for card_type in app_state["inventory_removal"].values())),
        memory             = sorted(tuple(name for name, in_inventory in app_state["memory"].items() if in_inventory)),
        mystery_item       = dict(sorted(_mystery_item.items())),
        room               = sorted(app_state["room"]),
        season             = app_state["season"],
        skill              = _skill,
        soul               = _soul,
        weather            = sorted(tuple(name for name, in_inventory in app_state["weather"].items() if in_inventory)),
    )

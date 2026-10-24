import uuid

import streamlit as st

from boh.model import lookup
from streamlit_utils import st_card

hidden_type_names = (
    "an_introduction",
    "circumstance",
    "codex",
    "fixed_in_place",
    "incident",
    "journal",
    "memory",
    "notype",
    "pence",
    "phonograph_record",
    "reel_of_film",
    "scroll",
    "skill",
    "soul",
    "tablet",
    "tally",
    "uncatalogued",
    "visitor",
    "weather",
)

type_names = tuple(name for name in lookup.card_types() if name not in hidden_type_names)

add_cols = (
    150,    # type
    300,    # name
    100,    # add button
)

item_cols = (
    150,    # type
    300,    # name
    100,    # delete button
)

def inventory_list(state_key):
    c = st.container(gap="xxsmall", width=sum(add_cols))
    c1, c2, c3 = c.columns(add_cols)
    _type = c1.selectbox("type", options=type_names, label_visibility="collapsed", key=f"{state_key}_type")
    name = c2.selectbox("name", options=lookup.names_for(_type), label_visibility="collapsed", key=f"{state_key}_name")
    if c3.button("add", icon=":material/add:", key=f"{state_key}_add"):
        row_id = uuid.uuid4()
        st.session_state[state_key][row_id] = st_card(
            row_id = row_id,
            type   = _type,
            name   = name,
        )

    c = st.container(gap="xxsmall", width=sum(item_cols))
    if len(st.session_state[state_key]) > 0:
        col_type, col_name, _ = c.columns(item_cols)
        col_type.write("type")
        col_name.write("name")

        for item in tuple(sorted(st.session_state[state_key].values(), key=lambda x: (x.type, x.name))):
            col_type, col_name, col_delete = c.columns(item_cols, vertical_alignment="center")

            col_type.write(item.type)
            col_name.write(item.name)

            if col_delete.button("delete", icon=":material/delete:", key=item.delete_key):
                st.session_state[state_key].pop(item.row_id, None)
                st.rerun()

    else:
        c.write("(no item)")

st.header("inventory addition")
inventory_list(state_key="inventory_addition")

st.header("inventory removal")
inventory_list(state_key="inventory_removal")

import uuid

import streamlit as st

from boh.model import lookup
from streamlit_utils import st_mystery_item


assert "mystery_item" in st.session_state

st.header("mystery item")

cols = (
    200,    # type
    500,    # name
    150,    # button
)

# luckily, 'name' is unique across different types (codex, scroll, etc)
_mystery_item_in_inventory = tuple(x.name for x in st.session_state.mystery_item.values())

c1, c2, c3 = st.columns(cols, width=sum(cols))
_type = c1.selectbox("type", options=lookup.mystery_item_types(), label_visibility="collapsed")

_mystery_item_not_in_inventory = tuple(name for name in lookup.mystery_item_names_for(_type) if name not in _mystery_item_in_inventory)
name = c2.selectbox("name", options=_mystery_item_not_in_inventory, label_visibility="collapsed")

if c3.button("add", icon=":material/add:", disabled=(name is None)):
    row_id = uuid.uuid4()
    st.session_state.mystery_item[row_id] = st_mystery_item(
        row_id   = row_id,
        type     = _type,
        name     = name,
        mastered = False,
    )
    st.rerun()

cols = (
    600,    # name
    100,    # mystery
    200,    # provides
    150,    # attributes
    150,    # delete
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_mystery, col_provides, _, _ = c.columns(cols)
col_name.write("mastered")
col_mystery.write("mystery")
col_provides.write("provides")

for item in tuple(sorted(st.session_state.mystery_item.values(), key=lambda x: x.name)):
    col_name, col_mystery, col_provides, col_attributes, col_delete = c.columns(cols, vertical_alignment="center")

    if col_name.checkbox(item.name, value=item.mastered, on_change=item.update, key=item.mastered_key):
        col_provides.write(item.provided_memory)
    else:
        col_mystery.write(item.power_attributes)

    with col_attributes.popover("attributes"):
        st.write(item.attributes)

    if col_delete.button("delete", icon=":material/delete:", key=item.delete_key):
        st.session_state.mystery_item.pop(item.row_id, None)
        st.rerun()

import uuid

import streamlit as st

from boh.model import lookup
from streamlit_utils import st_soul

assert "soul" in st.session_state

st.header("soul")

c1, c2 = st.columns(2, width=300)
soul_type_name = c1.selectbox("type", options=lookup.names_for("soul"), label_visibility="collapsed")
if c2.button("add", icon=":material/add:"):
    row_id = uuid.uuid4()
    st.session_state.soul[row_id] = st_soul(
        row_id = row_id,
        name   = soul_type_name,
        enable = True,
        level  = 1,
        state  = "normal",
    )

cols = (
    150,    # name
     50,    # level
    100,    # state
    500,    # attributes
    100,    # edit
    100,    # delete
)

c = st.container(gap="xxsmall", width=sum(cols))
if len(st.session_state.soul) > 0:
    col_name, col_level, col_state, col_attributes, _, _ = c.columns(cols)
    col_name.write("enabled")
    col_level.write("level")
    col_state.write("state")
    col_attributes.write("attributes")

for item in tuple(sorted(st.session_state.soul.values(), key=lambda x: x.name)):
    col_name, col_level, col_state, col_attributes, col_edit, col_delete = c.columns(cols, vertical_alignment="center")

    if col_name.checkbox(item.name, value=item.enable, on_change=item.update, key=item.enable_key):
        with col_edit.popover("edit", icon=":material/edit:"):
            st.number_input("level", value=item.level, min_value=1, max_value=3, on_change=item.update, key=item.level_key)
            st.selectbox("state", options=item.valid_states, index=item.valid_states.index(item.state), on_change=item.update, key=item.state_key)

        col_attributes.write(item.attributes)

        if col_delete.button("delete", icon=":material/delete:", key=item.delete_key):
            st.session_state.soul.pop(item.row_id, None)
            st.rerun()

    else:
        col_edit.space(size="medium")

    col_level.text(item.level)
    col_state.markdown(item.state_as_markdown)

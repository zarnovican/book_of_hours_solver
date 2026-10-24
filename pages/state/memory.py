import streamlit as st

from boh.model import lookup, opportunity
from streamlit_utils import attributes_as_markdown

assert "memory" in st.session_state

cols = (
    200,    # name
    700,    # attributes
)

st.header("memory")
con_memory = st.container(gap="xxsmall", width=sum(cols))
col_name, col_attributes = con_memory.columns(cols)
col_name.write("in inventory")
col_attributes.write("attributes")

st.header("persistent memory")
con_persistent_memory = st.container(gap="xxsmall", width=sum(cols))
col_name, col_attributes = con_persistent_memory.columns(cols)
col_name.write("in inventory")
col_attributes.write("attributes")

st.header("numen")
con_numen = st.container(gap="xxsmall", width=sum(cols))
col_name, col_attributes = con_numen.columns(cols)
col_name.write("in inventory")
col_attributes.write("attributes")

for name, memory_type in lookup.items_for("memory"):
    if opportunity.is_mood(name):
        continue

    if memory_type.has_attribute("numen"):
        col_enable, col_attributes = con_numen.columns(cols)
    elif memory_type.has_attribute("persistent"):
        col_enable, col_attributes = con_persistent_memory.columns(cols)
    else:
        col_enable, col_attributes = con_memory.columns(cols)

    st.session_state.memory[name] = col_enable.checkbox(name, value=st.session_state.memory.get(name, False), key=f"memory_{name}_enable")
    if st.session_state.memory[name]:
        col_attributes.write(attributes_as_markdown(memory_type.attributes))

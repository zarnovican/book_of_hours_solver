import streamlit as st

from boh.model import lookup
from streamlit_utils import attributes_as_markdown, season_map

assert "weather" in st.session_state

cols = (
    200,    # name
    700,    # attributes
)

season_names = tuple(season_map.keys())

st.header("season")
st.session_state.season = st.selectbox("season",
    index            = season_names.index(st.session_state.season),
    key              = "season_selectbox",      # must be globally unique
    label_visibility = "collapsed",
    options          = season_names,
    persist_state    = "session",
    width            = 100,
)

st.header("weather")
c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_attributes = c.columns(cols)
col_name.write("in inventory")
col_attributes.write("attributes")

for name, memory_type in lookup.items_for("weather"):
    col_name, col_attributes = c.columns(cols)
    st.session_state.weather[name] = col_name.checkbox(name, value=st.session_state.weather.get(name, False), key=f"weather_{name}_enable")
    if st.session_state.weather[name]:
        col_attributes.write(attributes_as_markdown(memory_type.attributes))

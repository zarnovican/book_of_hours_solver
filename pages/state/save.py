import json

import streamlit as st

from streamlit_utils import minimize_app_state


st.write("## save")

st.write("save your progress to a '.json' file")

st.download_button(
    label="download",
    data=json.dumps(minimize_app_state(st.session_state), indent=2),
    file_name="boh_solver_save.json",
    mime="application/json",
    icon=":material/download:",
)

with st.expander("view"):
    st.json(minimize_app_state(st.session_state))

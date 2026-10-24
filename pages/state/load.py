import json

import streamlit as st

from streamlit_utils import app_state_load


st.write("## ['book of hours'](https://weatherfactory.biz/book-of-hours/) solver")

st.write("Get the same game state from..")

c = st.container(width="content", border=True)
col1, col2 = c.columns([1, 3], vertical_alignment="center", width=600, border=False)
col1.write("### new")
col1.caption("start from scratch")

if col2.button(":material/new_window: start"):
    app_state_load(st.session_state, {})
    st.rerun()

col1, col2 = c.columns([1, 3], vertical_alignment="center", border=False)
col1.write("### load")
col1.caption("load '.json' file created by this app")

save_file = col2.file_uploader("from `.json` file created by this app", label_visibility="collapsed", type="application/json", max_upload_size=1)
if save_file is not None:
    app_state_load(st.session_state, json.load(save_file))
    st.rerun()

col1, col2 = c.columns([1, 3], vertical_alignment="center", border=False)
col1.write("### sample")
col1.caption("load one of sample saves, just to look around")

con_samples = col2.container(horizontal=True)

if con_samples.button(":material/clock_loader_10: early"):
    app_state_load(st.session_state, json.load(open("sample_early.json")))
    st.rerun()

if con_samples.button(":material/clock_loader_40: mid"):
    app_state_load(st.session_state, json.load(open("sample_mid.json")))
    st.rerun()

if con_samples.button(":material/clock_loader_80: late"):
    app_state_load(st.session_state, json.load(open("sample_late.json")))
    st.rerun()

st.warning("do not 'reload this page' in browser or you will loose your changes", icon=":material/warning:")

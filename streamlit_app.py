import streamlit as st


st.set_page_config(layout="wide")

if st.session_state.get("initialized", False):
    st.logo(image=":material/menu_book:")
    pg = st.navigation(dict(
        home = [
            st.Page("pages/home/about.py", title="about"),
            st.Page("pages/home/documentation.py", title="documentation"),
            st.Page("pages/state/save.py", title="save"),
        ],

        state = [
            st.Page("pages/state/room.py", title="room"),
            st.Page("pages/state/inventory.py", title="inventory"),
            st.Page("pages/state/mystery_item.py", title="mystery item"),
            st.Page("pages/state/memory.py", title="memory"),
            st.Page("pages/state/soul.py", title="soul"),
            st.Page("pages/state/skill.py", title="skill"),
            st.Page("pages/state/season.py", title="season"),
        ],

        solve = [
            st.Page("pages/solve/simple.py", title="simple", url_path="solve_simple"),
            st.Page("pages/solve/crafting.py", title="crafting", url_path="solve_crafting"),
            st.Page("pages/solve/mystery_item.py", title="mystery item", url_path="solve_mystery_item"),
            st.Page("pages/solve/room.py", title="room", url_path="solve_room"),
            st.Page("pages/solve/skill.py", title="skill", url_path="solve_skill"),
            st.Page("pages/solve/soul.py", title="soul", url_path="solve_soul"),
        ],
    ))
else:
    pg = st.navigation([
        st.Page("pages/state/load.py", title="load", icon=":material/menu_book:"),
    ])

pg.run()

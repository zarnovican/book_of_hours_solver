import streamlit as st

st.title("'book of hours' solver")

st.markdown("""
For a given game state, this app will find available actions and
combination of cards that will trigger the action.

The solver will find the most efficient solution, using cards that are most
easily available.

This app supports solving:
* crafting using skill at a station
* room unlocking via supporting assistant
* mastering mystery items (books, scrolls, ..)
* upgrading skills
* evolving soul elements
* gathering / foraging for resources

Next:
1. update your game state (rooms, souls, skills, etc) via `state/..` menu
2. run different solvers via `solve/..` menu

For more details, see `home/documentation`.
""")

st.warning("do not 'reload this page' in browser or you will loose your changes", icon=":material/warning:")

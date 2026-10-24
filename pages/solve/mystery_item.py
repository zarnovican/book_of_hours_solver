import streamlit as st

from boh.model import opportunity
from boh.solver import best_solution
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("master mystery item")

st.subheader("opportunities")

possible_opportunities = dict(
    art_its_educational        = "wall_art",
    comfort_relevant_furniture = "comfort",
    extra_effort_soul          = "soul",
    only_connect_memory        = "memory",
    stuff_also_things          = "thing",
    the_right_skies_weather    = "weather",
    awen                       = "awen",
    duende                     = "duende",
    epiphany                   = "epiphany",
    ubi_sunt                   = "ubi_sunt",
)

if "next_opportunities" not in st.session_state:
    st.session_state.next_opportunities = []

c = st.container(horizontal=True)
for name, short_name in possible_opportunities.items():
    if c.button(short_name, icon=":material/add:"):
        st.session_state.next_opportunities.append(name)

if len(st.session_state.next_opportunities) > 3:
    st.session_state.next_opportunities.pop(0)

c = st.container(horizontal=True, vertical_alignment="center")
c.write(f"optional opportunities ({len(st.session_state.next_opportunities)}/3):")
for i, name in enumerate(st.session_state.next_opportunities):
    if c.button(possible_opportunities[name], icon=":material/remove:", key=f"opportunity_{i}"):
        st.session_state.next_opportunities.remove(name)
        st.rerun()

st.subheader("solutions")

s = solver_from_streamlit_state(st.session_state)
s.state.next_opportunities(*st.session_state.next_opportunities)

non_mastered_mystery_items = { card_type.name: card_type for card_type in sorted(s.state.non_mastered_mystery_item_types()) }

mystery_item_to_master = st.selectbox("mystery_item_to_master",
    index            = None,
    key              = "mystery_item_to_master",    # must be globally unique
    label_visibility = "collapsed",
    options          = ("all", ) + tuple(non_mastered_mystery_items.keys()),
    persist_state    = "session",
    placeholder      = "select non-mastered mystery item",
    width            = 500,
)

if mystery_item_to_master is None:
    items_to_solve = ()
elif mystery_item_to_master == "all":
    items_to_solve = tuple(non_mastered_mystery_items.values())
else:
    items_to_solve = (non_mastered_mystery_items[mystery_item_to_master], )

cols = (
    400,    # name
     60,    # cost
    100,    # power
    150,    # station
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_cost, col_power, col_station, col_solution = c.columns(cols)
col_name.write("name")
col_cost.write("cost")
col_power.write("power")
col_station.write("station")
col_solution.write("cards")

assessed_cards = s.assessed_cards() + s.assessed_mood_cards()
opportunity_slots = opportunity.slots_for(*s.state.opportunities())
for card_type in items_to_solve:
    col_name, col_cost, col_power, col_station, col_solution = c.columns(cols)

    solution = best_solution(s.mastering_problems_for(card_type, opportunity_slots), assessed_cards)

    if solution is not None:
        power_aspect, _ = card_type.power_aspect_and_value()
        _power = sum(sc.power for sc in solution.slot_cards)

        col_name.write(card_type.name)
        col_cost.write(f":yellow-badge[{solution.cost}]")
        col_power.write(f":violet-badge[{power_aspect} {_power}]")
        col_station.write(solution.station_name)
        col_solution.markdown(solution_cards_as_markdown(solution.slot_cards))

        c.write("---")

    else:
        if len(items_to_solve) <= 1:
            col_name.write("no solution")

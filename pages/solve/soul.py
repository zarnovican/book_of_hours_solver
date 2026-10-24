import streamlit as st

from boh.model import evolving
from boh.solver import best_solution
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("evolve soul")

cols = (
    100,    # name
     60,    # cost
    250,    # station
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_cost, col_station, col_solution = c.columns(cols)
col_name.write("name")
col_cost.write("cost")
col_station.write("station")
col_solution.write("cards")

s = solver_from_streamlit_state(st.session_state)

assessed_cards = s.assessed_cards()

for soul_card_type in evolving.all_souls():
    solution = best_solution(s.evolving_problems_for(soul_card_type), assessed_cards)

    if solution is None:
        continue

    col_name, col_cost, col_station, col_solution = c.columns(cols)
    col_name.write(soul_card_type.name)
    col_cost.write(f":yellow-badge[{solution.cost}]")
    col_station.write(solution.station_name)
    col_solution.markdown(solution_cards_as_markdown(solution.slot_cards))

    c.write("---")

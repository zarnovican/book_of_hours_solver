import streamlit as st

from boh.solver import best_solution, room_unlocking_problems_for
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("simple solutions")

cols = (
    300,    # name
     60,    # cost
     70,    # pennies
    100,    # probability
    250,    # station
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_cost, col_pennies, col_probability, col_station, col_solution = c.columns(cols)
col_name.write("name")
col_cost.write("cost")
col_pennies.write("pennies")
col_probability.write("probability")
col_station.write("station")
col_solution.write("cards")

s = solver_from_streamlit_state(st.session_state)

for card_type, solution in sorted(s.available_card_solutions()):
    col_name, col_cost, col_pennies, col_probability, col_station, col_solution = c.columns(cols)

    col_name.write(str(card_type))
    col_cost.write(f":yellow-badge[{solution.cost}]")

    if solution.pennies > 0:
        col_pennies.write(f":yellow-badge[{solution.pennies}]")

    if solution.probability < 100:
        col_probability.write(f"{solution.probability}%")

    col_station.write(solution.station_name)
    col_solution.markdown(solution_cards_as_markdown(solution.solution_cards, with_power=False))

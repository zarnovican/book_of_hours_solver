import streamlit as st

from boh.solver import best_solution, room_unlocking_problems_for
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("unlock room")

cols = (
    400,    # name
     60,    # cost
    100,    # power
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_cost, col_power, col_solution = c.columns(cols)
col_name.write("name")
col_cost.write("cost")
col_power.write("power")
col_solution.write("cards")

s = solver_from_streamlit_state(st.session_state)

for room_name in sorted(s.state.locked_neighbors()):
    col_name, col_cost, col_power, col_solution = c.columns(cols)

    solution = best_solution(room_unlocking_problems_for(room_name), s.assessed_cards())

    if solution is not None:
        _power = sum(sc.power for sc in solution.slot_cards)

        col_name.write(room_name)
        col_cost.write(f":yellow-badge[{solution.cost}]")
        col_power.write(f":violet-badge[{solution.power_aspect} {_power}]")
        col_solution.markdown(solution_cards_as_markdown(solution.slot_cards))

        c.write("---")

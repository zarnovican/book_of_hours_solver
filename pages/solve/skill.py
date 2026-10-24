import streamlit as st

from boh.model import skill_upgrading
from boh.solver import problem, problem_exception
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("upgrade skill")

cols = (
    400,    # name
    100,    # level
     60,    # cost
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_level, col_cost, col_solution = c.columns(cols)
col_name.write("name")
col_level.write("level (/cap)")
col_cost.write("cost")
col_solution.write("cards")

s = solver_from_streamlit_state(st.session_state)

assessed_cards = s.assessed_cards()
for skill_card in sorted(s.state.upgradeable_skills()):
    col_name, col_level, col_cost, col_solution = c.columns(cols)

    try:
        _problem = problem(slots=skill_upgrading.slots_for(skill_card.card_type, skill_card.level))
        solution = _problem.solve(assessed_cards, n_candidates=9)
        level_cap = s.state.skill_cap_for(skill_card.card_type)

        col_name.write(skill_card.card_type.name)
        col_level.write(f"{skill_card.level} (/{level_cap})" if level_cap < 9 else f"{skill_card.level}")
        col_cost.write(f":yellow-badge[{solution.cost}]")
        col_solution.markdown(solution_cards_as_markdown(solution.slot_cards))

        c.write("---")

    except problem_exception:
        pass

import streamlit as st

from boh.model import crafting
from boh.solver import best_solution
from streamlit_utils import solver_from_streamlit_state, solution_cards_as_markdown

st.header("crafting")

s = solver_from_streamlit_state(st.session_state)

craftable_items = { str(card_type): card_type for card_type in sorted(crafting.outputs()) }

item_name_to_craft = st.selectbox("item_name_to_craft",
    index            = None,
    key              = "item_name_to_craft",    # must be globally unique
    label_visibility = "collapsed",
    options          = ("all", ) + tuple(craftable_items.keys()),
    persist_state    = "session",
    placeholder      = "select item to craft",
    width            = 500,
)

if item_name_to_craft is None:
    items_to_solve = ()
elif item_name_to_craft == "all":
    items_to_solve = tuple(craftable_items.values())
else:
    items_to_solve = (craftable_items[item_name_to_craft], )

cols = (
    300,    # name
     60,    # cost
    100,    # power
    250,    # station
    500,    # solution
)

c = st.container(gap="xxsmall", width=sum(cols))
col_name, col_cost, col_power, col_station, col_solution = c.columns(cols)
col_name.write("name")
col_cost.write("cost")
col_power.write("power")
col_station.write("station")
col_solution.write("cards")

assessed_cards = s.assessed_cards()
for card_type in items_to_solve:
    col_name, col_cost, col_power, col_station, col_solution = c.columns(cols)

    solution = best_solution(s.recipe_problems_for(card_type), assessed_cards)

    if solution is not None:
        _power = sum(sc.power for sc in solution.slot_cards)

        col_name.write(str(card_type))
        col_cost.write(f":yellow-badge[{solution.cost}]")
        col_power.write(f":violet-badge[{solution.power_aspect} {_power}]")
        col_station.write(solution.station_name)
        col_solution.markdown(solution_cards_as_markdown(solution.slot_cards))

        c.write("---")

    else:
        if len(items_to_solve) <= 1:
            col_name.write("no solution")

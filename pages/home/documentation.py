import streamlit as st

st.title("documentation")

#######################################################################################################
st.subheader("usage", divider=True)

st.subheader("update game state")

st.markdown("""

Solver needs to know which stations have been unlocked, which cards you have in inventory,
what level are your skills, etc. You can input a subset of that information and still get
accurate results.

* `state`
  * `room` - by unlocking, you make room's stations and inventory available
  * `inventory`
    * addition - add extra items to inventory, typically items that were gathered/crafted, but also `lessons` are added here.
    * removal - manually remove items from inventory, typically items that were consumed by previous actions
  * `mystery item` - add books, scrolls, etc, that you have catalogued or acquired. Mastered books make their providing memory available for solutions.
  * `memory` - inventory of memories, including persistent ones
  * `soul` - acquired soul elements, their status and levels
  * `skill` - acquired skills, their levels and whether they have been committed/fulfilled. Optionally, also leveling cap.
  * `season` - year's season and current weather

**! SAVE !** your changes to local file via `home/save`. To go back to load screen, go to `home/about` and refresh the page.
""")

st.subheader("run solver")

st.markdown("""
Based on your game state, calculate which actions are possible and which cards are required.
Each item is assigned a virtual cost (see 'cost assessment' section below). Solver tries
to find the cheapest solution.

* `solve`
  * `simple` - solutions for simple actions (foraging/gathering/talking/considering/etc). Items produced by simple actions
    are also available for more complex solutions.
  * `crafting` - cratft items using skill recipes
  * `mystery item` - mastering mystery items (books, scrolls, etc)
  * `room` - unlock rooms by providing support items to an assistant
  * `skill` - upgrading skills. Only skills below their level cap are considered.
  * `soul` - evolving souls. Only committed and unfulfilled skills are considered. You must have two identical soul elements.

Solution will show cost for each card (:yellow-badge[+4]) and total sum for the whole solution (eg. :yellow-badge[6]).
Actions with power requirement (eg :violet-badge[scale 11]) will also show contribution of each card (:violet-badge[+4]).
""")

#######################################################################################################
st.subheader("minimum effort", divider=True)

st.markdown("""
Tracking your game state is time consuming. Here is the minimum requirement for each use-case:

* `simple` - rooms, souls (no need for levels), skills (no need for levels, commitment). Season is important for some actions.
* `crafting` - rooms, souls, skills (with levels), memories, inventory
* `mystery item` - rooms, souls, skills (with levels), mystery items, memories, inventory
* `room` - rooms, souls, memories, inventory
* `skill` - rooms, skills (with levels and level caps), memories
* `soul` - rooms, souls, skills (commitment), memories (with evolve attribute)

:bulb: tips:
* track **rooms** in either case
* track which **memories** you have in inventory or are available from re-reading and crafting
* track only the best **soul** elements. Single item of each kind is usually enough.
* track your **skills** and levels. Commitments and level caps are required only for few use-cases.
* track **mystery items** only for mastering use-case. No need to track items already mastered.
* track **inventory** additions/removal only for items you _suspect_ might be used in solutions. Or to affect their cost.

Provided 'sample saves' are tracking _everything_. You don't have to follow that.
""")

#######################################################################################################
st.subheader("cost assessment", divider=True)

st.markdown("""
For the purpose of comparing solutions to find cheapest one, every
item needs to be assessted. This is a virtual cost that does not exist
in the game. Solver will calculate it automatically. Here are the rules:
""")

cols = (
     80,    # cost
    800,    # description
)
c = st.container(gap="xxsmall", width=sum(cols))
col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[0]")
col_description.markdown("""
* items that are not consumed by the action - skills, tools, books (re-reading), etc
* items that perish at dawn - memory, weather, assistence
""")

col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[1]")
col_description.markdown("""
* maladied soul - using such soul is free (cost sould be 0), but for technical reasons we use cost 1
* persistent memory
* inventory item - if you have 5+ items of the same kind (eg. there are 23x widow's candles in hush house)
""")

col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[2]")
col_description.markdown("""
* inventory item - if you have 4 items of the same kind
""")

col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[4]")
col_description.markdown("""
* soul element - value 4 was chosen as a middle between cost to recover (2) and value produced (6) when working
* inventory item - if you have 3 items of the same kind
""")

col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[8]")
col_description.markdown("""
* inventory item - if you have 2 items of the same kind
""")

col_cost, col_description = c.columns(cols)
col_cost.markdown("cost :yellow-badge[16]")
col_description.markdown("""
* inventory item - if you have only one such item
* lesson - cost 16 for lesson is arbitrary and represents how valuable lessons are
""")

st.markdown("""
If an action requires a fee to pay, the cost is the number of **pennies** (eg. shilling has cost 12).

The product of simple actions are **available items**. Available item's cost is their production cost.
Eg. 'assistance.blacksmith' can be created with one soul (4) and shilling (12). The cost is 16.

Available item's cost is multiplied by their **inverse probability** (eg. x2 for 50%, x5 for 20% probability).
Most actions produce the same item every time (no cost change). But, for example, beachcombing can produce
'material.sand' with 13% probability, so the original cost (soul 4, skill 0) becomes 30 (`(4+0)*(1/0.13) =~ 30`).

:bulb: tip: adding/removing items from inventory will make them more/less favorable for solutions
""")

#######################################################################################################
st.subheader("features (and gaps)", divider=True)

st.markdown("""
This app DOES support:
* attributes for majority of game items (1081 cards)
* can track mutable cards (soul, skill, mystery item) and their attributes
* inventory and stations for all rooms
* most actions available at stations (including output based on season and probability)
* rooms and their neighbor relations
* two solver types
  * simple for finding cheapest fit for mandatory slots
  * backtrack for finding cheapest solution that also satisfy power aspect requirement
* cost assessment for in-inventory and available items (not in inventory, but producible)
* 'book of hours' version 2025.8.E.6 (no dlc)

The app DOES NOT support:
* loading game state from savegame - that would be super cool and super hard to implement
* show all solutions - solver shows only the cheapest solution even if there may be many possible
* multiple actions - we calculate only single action. Solver does not provide "plan for the whole day".
* tracking tree of wisdom - we track only which skill is committed to which wisdom branch
* mutability of assistance and beast cards - not too important
* all starting setups - it only implements starting setup with 'rector' as an old friend.
  Workaround is to add all 'assistance' cards to inventory to give them equal cost.
* concept of time - no of time of day, nor does it take into account how long the action take
* secret room items - when you find them, add them to inventory manually
* history endings - solutions are easy and do not require help of a solver
* tracking of money, spintria or shoping
* incident, visitors - not relevant and their solution are simple
* dlc content - no actions or items from later versions
""")

#######################################################################################################
st.subheader("source code", divider=True)

st.markdown("""
The source code is published on github, [zarnovican/book_of_hours_solver](https://github.com/zarnovican/book_of_hours_solver) repo.

To run it locally, follow the provided install steps.
""")

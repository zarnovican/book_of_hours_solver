import streamlit as st

from boh.model import room_unlocking
from streamlit_utils import attributes_as_markdown, state_from_streamlit_state


def flip_lock_status(name):
    if name in st.session_state.room:
        st.session_state.room.remove(name)
    else:
        st.session_state.room.append(name)


assert "room" in st.session_state

# str -> ( row, column )    ( 0, 0 ) is upper left corner
room_position = dict(
  atrium                                = (  6, 10 ),
  back_stairs                           = ( 11,  6 ),
  bells                                 = (  1,  8 ),
  boathouse                             = ( 16,  3 ),
  catacombs                             = ( 17,  5 ),
  cell_adepts                           = (  8,  2 ),
  cell_long                             = (  8,  1 ),
  cell_question                         = (  7,  2 ),
  cell_worm_inhabited                   = (  7,  1 ),
  chancel_of_the_abbey_church           = (  6,  8 ),
  chapel_ascite                         = ( 16,  6 ),
  chapel_calicite                       = ( 16,  7 ),
  chapel_malachite                      = ( 16,  5 ),
  chapter_house                         = (  4,  7 ),
  church_tower                          = (  3,  8 ),
  columbic_crypt                        = ( 17,  6 ),
  crucible_tower_governors_office       = (  7,  3 ),
  crucible_tower_governors_quarters     = (  6,  3 ),
  crucible_tower_interview_laboratory   = (  5,  3 ),
  deep_well_descent                     = ( 14,  9 ),
  deeplight_caves                       = ( 18,  3 ),
  duelling_hall                         = (  9,  7 ),
  earl_brians_field                     = ( 12,  4 ),
  earth_cellar                          = ( 12,  5 ),
  entrance_hall                         = ( 10, 12 ),
  examination_room                      = (  7, 10 ),
  fludd_gallery                         = (  7,  8 ),
  foundry                               = ( 12,  9 ),
  gaol_cellar                           = ( 10,  1 ),
  gaol_hall                             = (  9,  2 ),
  gaol_kitchen                          = (  9,  1 ),
  gaol_yard                             = (  9,  3 ),
  glorious_stair                        = (  5, 10 ),
  grand_ascent_first_floor              = (  9, 10 ),
  grand_ascent_ground_floor             = ( 10, 11 ),
  grand_ascent_second_floor             = (  8, 11 ),
  grand_ascent_third_floor              = (  7,  9 ),
  gull_colony                           = ( 14,  3 ),
  gullscry_loggia                       = (  8,  5 ),
  gullscry_tower_eales_room             = (  6,  5 ),
  gullscry_tower_summit                 = (  5,  5 ),
  gullscry_tower_valentines_room        = (  7,  5 ),
  hall_of_division                      = (  7,  7 ),
  hall_of_voices                        = ( 16,  8 ),
  hermit_cell                           = ( 15,  3 ),
  hidden_stair                          = ( 13,  6 ),
  infirmary                             = (  8, 12 ),
  iron_vault                            = ( 18,  6 ),
  ivory_vault                           = ( 18,  8 ),
  keepers_lodge                         = (  9, 16 ),
  kitchen                               = ( 11, 10 ),
  kitchen_garden                        = ( 12,  7 ),
  lesser_bridge                         = (  9,  4 ),
  librarians_quarters                   = (  8,  7 ),
  loading_dock                          = ( 10,  0 ),
  long_tower_solomons_quarters          = (  8, 14 ),
  long_tower_solomons_study             = (  9, 13 ),
  lower_pump_room                       = ( 17,  7 ),
  map_room                              = (  9,  8 ),
  mazarine_room                         = ( 10,  9 ),
  motley_tower_dispensary               = (  5, 12 ),
  motley_tower_illopolys_nook           = (  6, 12 ),
  motley_tower_regensburg_room          = (  4, 10 ),
  narthex                               = ( 15,  6 ),
  nave_of_the_abbey_church              = (  6,  9 ),
  night_gallery                         = ( 10,  5 ),
  oubliette                             = ( 11,  1 ),
  our_lady_beneath                      = ( 15,  5 ),
  pale_chamber                          = (  8,  8 ),
  pantry                                = ( 11,  9 ),
  patients_lounge                       = (  7, 11 ),
  physic_garden                         = (  9, 11 ),
  practic_garden                        = ( 11, 13 ),
  radiant_stair                         = (  5,  8 ),
  reading_room                          = ( 10, 10 ),
  refectory                             = ( 10,  8 ),
  rowenarium                            = ( 16, 10 ),
  sacred_spring                         = ( 15,  7 ),
  scent_garden                          = ( 11, 12 ),
  sea_caves                             = ( 17,  3 ),
  servants_hall                         = ( 11, 11 ),
  servants_quarters_north               = ( 11,  7 ),
  servants_quarters_south               = ( 11,  8 ),
  severn_chamber                        = (  8, 10 ),
  shrine_to_st_tentreto                 = ( 18,  4 ),
  silver_vault                          = ( 16, 11 ),
  smugglers_den                         = ( 15,  4 ),
  solarium                              = (  3,  7 ),
  spire                                 = (  0,  8 ),
  st_brandans_cloister                  = ( 10, 13 ),
  staff_room                            = (  8,  3 ),
  stair_tenebrous                       = ( 11,  5 ),
  stores                                = ( 10,  7 ),
  tower_clock                           = (  2,  8 ),
  upper_pump_room                       = ( 16,  9 ),
  vestibulum_transitus                  = (  9,  6 ),
  violet_chamber                        = (  8,  9 ),
  watchmans_tower_first_floor           = (  9, 14 ),
  watchmans_tower_gatehouse             = ( 10, 14 ),
  watchmans_tower_observatory           = (  8, 15 ),
  well                                  = ( 12,  8 ),
  well_descent                          = ( 13,  9 ),
  westcott_room                         = (  9,  9 ),
  whispering_stair                      = ( 14,  6 ),
  windlit_gallery                       = (  4,  8 ),
  wine_cellar                           = ( 12,  6 ),
)

st.header("unlocked rooms")

c = st.container(gap="xxsmall")

# some rooms span multiple cells, so they are merged
grid = (
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,      4,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,  2,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,  2,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,  2,  2,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,  2,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,  2,1,1,1,  2,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,  2,  2,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,  2,  2,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,  2,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,    3,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,  2,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,    3,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
    c.columns([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], gap="xxsmall"),
)

game_state = state_from_streamlit_state(st.session_state)

# locked rooms neighboring unlocked rooms
locked_neighbors = tuple(sorted(game_state.locked_neighbors()))

for name, (row, column) in room_position.items():
    grid[row][column].button(
        "", help=name, width="stretch",
        on_click=flip_lock_status, args=(name, ),
        icon=":material/lock:" if name in locked_neighbors else None,
        type="primary" if name in st.session_state.room else "secondary",
    )

st.header("neighboring locked rooms")
st.table({
    name: attributes_as_markdown(room_unlocking.requirements_for(name))
    for name in locked_neighbors
}, border="horizontal", width="content")

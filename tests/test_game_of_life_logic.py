from src.game_of_life_logic import determine_next_cell_state
from src.game_of_life_logic import count_live_neighbors

# Variables needed for Issue #2 testing
GRID_WIDTH = 60
GRID_HEIGHT = 60

#-----------------------#
#   ISSUE #1 TESTING    #
#-----------------------#

def test_survival_with_two_neighbors():
    assert determine_next_cell_state(is_alive = True, live_neighbors=2) is True

def test_survival_with_three_neighbors():
    assert determine_next_cell_state(is_alive= True, live_neighbors= 3) is True

def test_underpopulation_kills_cell():
    assert determine_next_cell_state(is_alive= True, live_neighbors=1) is False

def test_overpopulation_kills_cell():
    assert determine_next_cell_state(is_alive= True, live_neighbors=4) is False

def test_reproduction_brings_cell_to_life():
    assert determine_next_cell_state(is_alive=False, live_neighbors=3) is True

def test_dead_cell_with_two_neighbors_remains_dead():
    assert determine_next_cell_state(is_alive=False, live_neighbors=2) is False

#-----------------------#
#   ISSUE #2 TESTING    #
#-----------------------#

def test_cell_in_center_has_zero_neighbors():
    center_test_position = (30, 30)
    live_neighbors_set = set() # Empty set for zero count
    assert count_live_neighbors(center_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 0

def test_cell_in_center_has_eight_neighbors():
    center_test_position = (30, 30)
    live_neighbors_set = {
        (29, 29), (30, 29), (31, 29),
        (29, 30), (31, 30),
        (29, 31), (30, 31), (31, 31)
    }
    assert count_live_neighbors(center_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 8

def test_cell_at_corner_has_max_three_neighbors():
    top_left_corner_test_position = (0, 0)
    live_neighbors_set = {(0, 1), (1, 0), (1, 1)}
    assert count_live_neighbors(top_left_corner_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 3

def test_cell_at_edge_has_max_five_neighbors():
    top_edge_test_position = (30, 0) 
    live_neighbors_set = {(29, 0), (31, 0), (29, 1), (30, 1), (31, 1)}
    assert count_live_neighbors(top_edge_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 5
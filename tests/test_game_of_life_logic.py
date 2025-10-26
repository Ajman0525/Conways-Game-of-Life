from src.game_of_life_logic import (
    determine_next_cell_state, 
    count_live_neighbors
)
from src.main import adjust_grid

# Variables for counting live neighbors test
GRID_WIDTH = 60 
GRID_HEIGHT = 60

#-----------------------#
#    CELL FATE LOGIC    #
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

#------------------------------#
#   DETERMINE LIVE NEIGHBORS   #
#------------------------------#

def test_cell_in_center_has_zero_neighbors():
    center_test_position = (30, 30)
    live_neighbors_set = set() # Empty set for zero count
    assert count_live_neighbors(center_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 0

def test_cell_in_center_has_eight_neighbors():
    center_test_position = (30, 30)
    live_neighbors_set = {
        (29, 29), # Upper-left of the center cell
        (30, 29), # Above 
        (31, 29), # Upper-right 
        (29, 30), # Left side 
        (31, 30), # Right side 
        (29, 31), # Bottom-left
        (30, 31), # Below 
        (31, 31)  # Bottom-Right
    }
    assert count_live_neighbors(center_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 8

def test_cell_at_corner_has_max_three_neighbors():
    top_left_corner_test_position = (0, 0)
    live_neighbors_set = {
        (0, 1), # Below the top corner cell
        (1, 0), # Right 
        (1, 1)  # Bottom-right
    }
    assert count_live_neighbors(top_left_corner_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 3

def test_cell_at_edge_has_max_five_neighbors():
    top_edge_test_position = (30, 0) 
    live_neighbors_set = {
        (29, 0), # Left of the top edge cell
        (31, 0), # Right
        (29, 1), # Bottom-left
        (30, 1), # Below
        (31, 1)  # Bottom-right
    }
    assert count_live_neighbors(top_edge_test_position, live_neighbors_set, GRID_WIDTH, GRID_HEIGHT) == 5

def test_glider_pattern_moves_one_generation():
        # Standard Glider Pattern (Moves Diagonally)
        # Y=0: . X . 
        # Y=1: . . X
        # Y=2: X X X
        GLIDER_START = {
            (1, 0), 
            (2, 1), 
            (0, 2), 
            (1, 2), 
            (2, 2)
        }

        # Expected state after 1 generation:
        # Y=0: . . .
        # Y=1: X . X
        # Y=2: . X X
        # Y=3: . X .
        GLIDER_GENERATION_1 = {
            (0, 1), 
            (2, 1),
            (1, 2), 
            (2, 2),
            (1, 3) 
        }

        next_generation = adjust_grid(GLIDER_START)
        assert next_generation == GLIDER_GENERATION_1

def test_block_pattern_is_stable():
    BLOCK_START = {
        (10, 10), 
        (10, 11), 
        (11, 10), 
        (11, 11)
    }
    expected_generation = BLOCK_START
    next_generation = adjust_grid(BLOCK_START)
    assert next_generation == expected_generation

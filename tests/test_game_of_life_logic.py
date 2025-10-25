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
from src.game_of_life_logic import determine_next_cell_state

#-----------------------#
#   ISSUE #1 TESTING    #
#-----------------------#

# --- Alive cell tests --- #
# Rule: A live cell with two or three live neighbors remains alive in the next generation (SURVIVAL)
def test_survival_with_two_neighbors():
    assert determine_next_cell_state(is_alive = True, live_neighbors=2) is True

def test_survival_with_three_neighbors():
    assert determine_next_cell_state(is_alive= True, live_neighbors= 3) is True

# Rule: A live cell with less than two live neighbors dies in the next generation (UNDERPOPULATION)
def test_underpopulation_kills_cell():
    assert determine_next_cell_state(is_alive= True, live_neighbors=1) is False

# Rule: A live cell with more than three live neighbors dies in the next generation (OVERPOPULATION)
def test_overpopulation_kills_cell():
    assert determine_next_cell_state(is_alive= True, live_neighbors=4) is False

# --- Dead cell tests --- #
# Rule: A dead cell with three live neighbors becomes a live cell (REPRODUCTION)
def test_reproduction_brings_cell_to_life():
    assert determine_next_cell_state(is_alive=False, live_neighbors=3) is True

# Rule: A dead cell with any other count remains dead (DEFAULT)
def test_dead_cell_with_two_neighbors_remains_dead():
    assert determine_next_cell_state(is_alive=False, live_neighbors=2) is False

#-----------------------#
#   ISSUE #2 TESTING    #
#-----------------------#

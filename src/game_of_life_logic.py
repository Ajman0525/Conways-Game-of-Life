WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600 

TILE_SIZE = 20

GRID_WIDTH = WINDOW_WIDTH // TILE_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // TILE_SIZE


def determine_next_cell_state(is_alive: bool, live_neighbors: int) -> bool:
    if is_alive:
        return live_neighbors in [2, 3]
    else:
        return live_neighbors == 3
    
def count_live_neighbors(cell_position: tuple[int, int], live_positions: set[tuple[int, int]], grid_width: int, grid_height: int) -> int:
    '''Counts live neighbors around a cell, doing boundary and liveness checks 
    to eliminate duplication (Criteria 3).'''
    
    current_x, current_y = cell_position
    live_neighbor_count = 0 

    for offset_x in [-1, 0, 1]:
        for offset_y in [-1, 0, 1]:
            
            neighbor_x = current_x + offset_x
            neighbor_y = current_y + offset_y

            # Skips the cell itself, as a cell is not its own neighbor.
            if offset_x == 0 and offset_y == 0:
                continue

            # Skips any neighbor that falls outside the defined grid boundaries.
            if neighbor_x < 0 or neighbor_x >= grid_width:
                continue
            if neighbor_y < 0 or neighbor_y >= grid_height:
                continue

            neighbor_position = (neighbor_x, neighbor_y)

            # Check if the valid neighbor's position is present in the set of all live cells
            if neighbor_position in live_positions:
                live_neighbor_count += 1

    return live_neighbor_count
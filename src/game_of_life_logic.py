def determine_next_cell_state(is_alive: bool, live_neighbors: int) -> bool:
    if is_alive:
        return live_neighbors in [2, 3]
    else:
        return live_neighbors == 3
    
def count_live_neighbors(pos, live_positions):
    return 0

#  def get_neighbors(pos):
#     x, y = pos
#     neighbors = []
#     for dx in [-1, 0, 1]:
#         if x + dx < 0 or x + dx > GRID_WIDTH:
#             continue
#         for dy in [-1, 0, 1]:
#             if y + dy < 0 or y + dy > GRID_HEIGHT:
#                 continue
#             if dx == 0 and dy == 0:
#                 continue

#             neighbors.append((x + dx, y + dy))
    
#     return neighbors


# def adjust_grid(positions):
#     all_neighbors = set() # Neighbors of the original live set of cells
#     new_positions = set() # New set of live cell positions

#     for position in positions:
#         neighbors = get_neighbors(position)
#         all_neighbors.update(neighbors)

#         neighbors = list(filter(lambda x: x in positions, neighbors)) # Anonymous function that acts as a filter to neighboring cells and returns only the live ones

#         if len(neighbors) in [2,3]: # Rule no. 2 (survival)
#             new_positions.add(position)
        
#     for position in all_neighbors:
#         neighbors = get_neighbors(position) 

#         neighbors = list(filter(lambda x: x in positions, neighbors)) # Note: Make a function for this instead to prevent duplication
        
#         if len(neighbors) == 3:
#             new_positions.add(position)
    
#     return new_positions
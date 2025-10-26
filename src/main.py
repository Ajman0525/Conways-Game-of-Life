import pygame
import random

pygame.init()

pygame.display.set_caption("Conway's Game of Life")

BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)
from .game_of_life_logic import(
    determine_next_cell_state,
    count_live_neighbors,
    WINDOW_WIDTH, # Window Size
    WINDOW_HEIGHT, # Window Size
    GRID_WIDTH,
    GRID_HEIGHT,
    TILE_SIZE

)
FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0,GRID_HEIGHT), random.randrange(0,GRID_WIDTH)) for _ in range(num)]) 

def draw_grid(positions):

    for position in positions: # A set containing the positions of the live cells
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) # Note *top_left will unpack the values so that they would be written individually

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WINDOW_WIDTH, row * TILE_SIZE)) # Horizontal Grid Lines
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, WINDOW_HEIGHT)) # Vertical Grid Lines

def adjust_grid(positions):
    # Initializes the set of positions that must be checked for reproduction.
    cells_to_check_for_reproduction = set() 
    
    new_live_positions = set() 

    # 1. CHECK CURRENTLY LIVE CELLS (Survival)
    for cell_position in positions:
        
        live_neighbors_count = count_live_neighbors(
            cell_position, 
            positions, 
            GRID_WIDTH, 
            GRID_HEIGHT
        )
        
        if determine_next_cell_state(is_alive=True, live_neighbors=live_neighbors_count):
            new_live_positions.add(cell_position)
        
        current_x, current_y = cell_position
        for offset_x in [-1, 0, 1]:
            for offset_y in [-1, 0, 1]:
                if offset_x == 0 and offset_y == 0:
                    continue
                cells_to_check_for_reproduction.add((current_x + offset_x, current_y + offset_y))

    # 2. CHECK DEAD NEIGHBORS (Reproduction)
    for position_to_check in cells_to_check_for_reproduction:
        
        # Skips cells that were already handled in the survival check.
        if position_to_check in positions: 
            continue
            
        live_neighbors_count = count_live_neighbors(
            position_to_check, 
            positions, 
            GRID_WIDTH, 
            GRID_HEIGHT
        )
        
        if determine_next_cell_state(is_alive=False, live_neighbors=live_neighbors_count):
            new_live_positions.add(position_to_check)
    
    return new_live_positions

# ---- TO DO: Add a function that takes number of generations as input ---- #
def generation_num():
    pass

def main():
    running = True
    playing = False
    count = 0
    update_frequency = 5 # Calibrate to a higher value for a slower update speed
    
    positions = set() # Contains all the positions of live cells
    while running:
        clock.tick(FPS) # Regulate the fps of the loop

        if playing:
            count += 1

        if count >= update_frequency:
            count = 0
            positions = adjust_grid(positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Terminate the loop once the game exits 
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: # Mark a position when the mouse is pressed 
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions: # Note: constant time complexity
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Pausing or playing the simulation
                    playing = not playing

                if event.key == pygame.K_c: # Resets the screen
                    positions = set()
                    playing = False
                    count = 0

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(10,20) * GRID_WIDTH) # Randomly generate cells
                

        screen.fill(GREY)   # Color of the screen
        draw_grid(positions) # Draw the grids
        pygame.display.update() # Applies the drawing and show it to the screen


    pygame.quit()

if __name__ == "__main__":
    main()
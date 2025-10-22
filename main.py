import pygame
import random

pygame.init()

# ---- Window Title ---- #
pygame.display.set_caption("Conway's Game of Life")

# ---- COLOR VARIABLES ---- #
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)

# ---- WIDTH AND HEIGHT OF THE SCREEN ---- #
WIDTH, HEIGHT = 600, 600 

# ---- SIZE OF EVERY SINGLE TILE ---- #
TILE_SIZE = 10

# ---- NUMBER OF TILES IN THE GRID ---- #
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# ---- FRAMES PER SECOND ---- #
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0,GRID_HEIGHT), random.randrange(0,GRID_WIDTH)) for _ in range(num)]) 

def draw_grid(positions):

    for position in positions: # A set containing the positions of the live cells
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) # Note *top_left will unpack the values so that they would be written individually

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)) # Horizontal Grid Lines
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT)) # Vertical Grid Lines


def adjust_grid(positions):
    all_neighbors = set() # Neighbors of the original live set of cells
    new_positions = set() # New set of live cell positions

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors)) # Anonymous function that acts as a filter to neighboring cells and returns only the live ones

        if len(neighbors) in [2,3]: # Rule no. 2 (survival)
            new_positions.add(position)
        
    for position in all_neighbors:
        neighbors = get_neighbors(position) 

        neighbors = list(filter(lambda x: x in positions, neighbors)) # Note: Make a function for this instead to prevent duplication
        
        if len(neighbors) == 3:
            new_positions.add(position)
    
    return new_positions

def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))
    
    return neighbors

# ---- TO DO: Add a function that takes number of generations as input ---- #
def generation_num():
    pass

def main():
    running = True
    playing = False
    count = 0
    update_frequency = 5
    
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
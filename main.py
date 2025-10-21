import pygame

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
TILE_SIZE = 20

# ---- NUMBER OF TILES IN THE GRID ---- #
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# ---- FRAMES PER SECOND ---- #
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):

    for position in positions: # A set containing the positions of the live cells
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) # Note *top_left will unpack the values so that they would be written individually

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)) # Horizontal Grid Lines
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT)) # Vertical Grid Lines

def main():
    running = True
    
    positions = set() # Contains all the positions of live cells
    while running:
        clock.tick(FPS) # Regulate the fps of the loop

        
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


        screen.fill(GREY)   # Color of the screen
        draw_grid(positions) # Draw the grids
        pygame.display.update() # Applies the drawing and show it to the screen


    pygame.quit()

if __name__ == "__main__":
    main()
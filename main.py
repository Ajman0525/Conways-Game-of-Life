import pygame

pygame.init()

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
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def main():
    running = True
    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREY)   
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
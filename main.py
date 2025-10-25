import pygame
import random

pygame.init()

# ---- Window Title ---- #
pygame.display.set_caption("Conway's Game of Life")

# ---- COLOR VARIABLES ---- #
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

# ---- WIDTH AND HEIGHT OF THE SCREEN ---- #
WIDTH, HEIGHT = 600, 600

# ---- SIZE OF EVERY SINGLE TILE ---- #
TILE_SIZE = 10

# ---- NUMBER OF TILES IN THE GRID ---- #
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# ---- FRAMES PER SECOND ---- #
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ---- Function to generate random live cells ---- #
def gen(num):
    return set(
        [(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)]
    )

# ---- Function to draw the grid and live cells ---- #
def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

# ---- Function to adjust grid per generation ---- #
def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        live_neighbors = [x for x in neighbors if x in positions]
        if len(live_neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        live_neighbors = [x for x in neighbors if x in positions]
        if len(live_neighbors) == 3:
            new_positions.add(position)

    return new_positions

# ---- Function to get the neighbors of a cell ---- #
def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx >= GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy >= GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x + dx, y + dy))
    return neighbors

# ---- MAIN FUNCTION ---- #
def main():
    running = True
    count = 0
    update_frequency = 5

    # Ask user for number of generations
    try:
        num_generations = int(input("Enter number of generations to simulate: "))
    except ValueError:
        print("Invalid input. Using default 50 generations.")
        num_generations = 50

    # Start with random live cells
    positions = gen(random.randrange(10, 20) * GRID_WIDTH)
    print(f"Initial live cells: {len(positions)}")

    while running:
        clock.tick(FPS)
        screen.fill(GREY)

        #  Run simulation for specified generations only
        if count < num_generations:
            positions = adjust_grid(positions)
            count += 1
        else:
            print(f"Simulation ended at generation {count}.")
            running = False  # Stop simulation
            continue

        draw_grid(positions)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

    # Print final simulation summary
    print(f"Final generation reached: {count}")
    print(f"Remaining live cells: {len(positions)}")
    print("Simulation complete!")

if __name__ == "__main__":
    main()

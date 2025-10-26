import pygame
import random

pygame.init()

pygame.display.set_caption("Conway's Game of Life")

BLACK = (0, 0, 0)
GREY = (30, 30, 30)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

from .game_of_life_logic import(
    determine_next_cell_state,
    count_live_neighbors,
    get_cells_to_evaluate,
    WINDOW_WIDTH, # Window Size
    WINDOW_HEIGHT, # Window Size
    GRID_WIDTH,
    GRID_HEIGHT,
    TILE_SIZE
)

FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

clock = pygame.time.Clock()

current_generation = 0

target_generations = None  


def generate_random_cells(count):
    return set([(random.randrange(0,GRID_HEIGHT), random.randrange(0,GRID_WIDTH)) for _ in range(count)]) 

def draw_grid(live_cells):

    for position in live_cells: 
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)

        # Note *top_left will unpack the values as if they would be written individually
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) 

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WINDOW_WIDTH, row * TILE_SIZE)) # Horizontal Grid Lines
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, WINDOW_HEIGHT)) # Vertical Grid Lines

def adjust_grid(positions: set) -> set:
    new_live_positions = set() 

    cells_to_evaluate = get_cells_to_evaluate(positions, GRID_WIDTH, GRID_HEIGHT)

    for cell_position in cells_to_evaluate:
        
        is_alive = cell_position in positions

        live_neighbors_count = count_live_neighbors(
            cell_position, 
            positions, 
            GRID_WIDTH, 
            GRID_HEIGHT
        )
            
        if determine_next_cell_state(is_alive=is_alive, live_neighbors=live_neighbors_count):
            new_live_positions.add(cell_position)
    
    return new_live_positions

def main():
    running = True
    playing = False
    count = 0
    update_frequency = 5 # Calibrate to a higher value for a slower update speed

    positions = set()
    
    global current_generation, target_generations
    current_generation = 0
    target_generations = None  

    try:
        gens = input("Enter number of generations to run (or press Enter for unlimited): ")
        if gens.strip() == "":
            target_generations = None
            print("Running unlimited generations")
        else:
            target_generations = int(gens)
            print(f"Will run for {target_generations} generations")
    except ValueError:
        print("Invalid input. Running unlimited generations")
        target_generations = None

    positions = generate_random_cells(random.randrange(10,20) * GRID_WIDTH)  # Randomly generate some live cells

    while running:
        clock.tick(FPS) 

        if playing:
            count += 1

        if count >= update_frequency:
            count = 0
            positions = adjust_grid(positions)
            current_generation += 1

            if target_generations is not None and current_generation >= target_generations:
                playing = False
                print(f"Reached target of {target_generations} generations.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions: 
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    playing = not playing

                if event.key == pygame.K_c: 
                    positions = set()
                    playing = False
                    count = 0
                    current_generation = 0 
                    target_generations = None 

                if event.key == pygame.K_g:
                    positions = generate_random_cells(random.randrange(10,20) * GRID_WIDTH) 
                    current_generation = 0 


        screen.fill(GREY)   
        draw_grid(positions) 

        font = pygame.font.Font(None, 25)
        gen_text = f"Generation: {current_generation}"
        if target_generations is not None:
            gen_text += f" / {target_generations}"
        text_surface = font.render(gen_text, True, GREEN)
        screen.blit(text_surface, (10, 10))
        
        pygame.display.update() 

    pygame.quit()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            target_generations = int(sys.argv[1])
            print(f"Will run for {target_generations} generations")
        except ValueError:
            print("Usage: python main.py [generations]")
            target_generations = None
    main()

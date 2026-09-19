import pygame
import general_algorithm as gal

ROW = 50
WIDTH = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH,WIDTH))

WHILE = (255,255,255)
BLACK = (000,000,000)

clock = pygame.time.Clock()

grid = gal.create_grid(ROW,WIDTH)

start_pos = None
end_pos = None

start_finding = False

is_running = True
while is_running:

    #Get row col
    row, col = gal.find_clicked_position(pygame.mouse.get_pos(),ROW,WIDTH)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if pygame.mouse.get_pressed()[0]:

            # check if it out of grid
            if len(grid) - 1 < row or len(grid[row]) - 1 < col or row < 0 or col < 0:
                continue

            # draw
            if not start_pos and not grid[row][col].is_wall():
                grid[row][col].set_start()
                start_pos = grid[row][col]
            elif not end_pos and not grid[row][col].is_wall() and not grid[row][col].is_start():
                grid[row][col].set_end()
                end_pos = grid[row][col]
            elif not grid[row][col].is_start() and not grid[row][col].is_end():
                grid[row][col].set_wall()
        
        #set empty
        elif pygame.mouse.get_pressed()[2]:
            if grid[row][col].is_start():
                start_pos = None
            elif grid[row][col].is_end():
                end_pos = None
            grid[row][col].set_empty()

        if event.type == pygame.KEYDOWN:
            #claer all
            if event.key == pygame.K_c:
                for row in grid:
                    for node in row:
                        node.set_empty()
                        start_pos = None
                        end_pos = None
            #start finding
            if event.key == pygame.K_SPACE:
               if start_pos and end_pos:
                gal.Bfs_alogorithm(screen, grid,start_pos,end_pos,ROW,WIDTH)

    screen.fill(WHILE)

    gal.draw_node(screen,grid)
    gal.draw_grid(screen,ROW,WIDTH)

    pygame.display.flip()
    pygame.display.set_caption(f"Pathfinder for Python ({clock.get_fps():.2f})")
    clock.tick(60)

pygame.quit()
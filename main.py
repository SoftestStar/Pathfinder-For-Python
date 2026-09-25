import pygame
import general_algorithm as gal

ROW = 50
WIDTH = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH,WIDTH))

WHILE = (255,255,255)
BLACK = (000,000,000)
RED = (255,000,000)
GREEN = (000,255,000)
BLUE = (000,000,255)
YELLOW = (255,255,000)
PURPLE = (128, 0, 128)

clock = pygame.time.Clock()

grid = gal.create_grid(ROW,WIDTH)

start_pos = None
end_pos = None

pathfinding_mode_dict = {0:"BFS",1:"DFS"}
mode_index = 0

start_finding = False

def click_to_draw(grid,row,col):
    global start_pos, end_pos
    if not start_pos and not grid[row][col].is_wall():
        grid[row][col].set_start()
        start_pos = grid[row][col]
    elif not end_pos and not grid[row][col].is_wall() and not grid[row][col].is_start():
        grid[row][col].set_end()
        end_pos = grid[row][col]
    elif not grid[row][col].is_start() and not grid[row][col].is_end():
        grid[row][col].set_wall()

def click_to_remove(grid,row,col):
    global start_pos, end_pos
    if grid[row][col].is_start():
        start_pos = None
    elif grid[row][col].is_end():
        end_pos = None
    grid[row][col].set_empty()

def claer_grid(event):
    global start_pos, end_pos
    if event.key == pygame.K_c:
        for row in grid:
            for node in row:
                node.set_empty()
                start_pos = None
                end_pos = None

def finding(event):
    if event.key == pygame.K_SPACE:
        if start_pos and end_pos:
            if pathfinding_mode_dict[mode_index] == "BFS":
                gal.Bfs_alogorithm(screen, grid,start_pos,end_pos,ROW,WIDTH,False)
            elif pathfinding_mode_dict[mode_index] == "DFS":
                gal.Dfs_alogorithm(screen, grid,start_pos,end_pos,ROW,WIDTH,False)

def mode_select(event):
    global mode_index
    if event.key == pygame.K_LEFT:
        if mode_index - 1 >= 0:
            mode_index -= 1
        else:
            mode_index = 1
    if event.key == pygame.K_RIGHT:
        if mode_index + 1 <= 1:
            mode_index += 1
        else:
            mode_index = 0

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

            click_to_draw(grid,row,col)
        
        #set empty
        elif pygame.mouse.get_pressed()[2]:

            # check if it out of grid
            if len(grid) - 1 < row or len(grid[row]) - 1 < col or row < 0 or col < 0:
                continue

            click_to_remove(grid,row,col)

        if event.type == pygame.KEYDOWN:
            #claer all
            claer_grid(event)
            #start finding
            finding(event)
            #select
            mode_select(event)

    screen.fill(WHILE)

    gal.draw_node(screen,grid)
    gal.draw_grid(screen,ROW,WIDTH)

    pygame.display.flip()
    pygame.display.set_caption(f"Pathfinder for Python: {pathfinding_mode_dict[mode_index]} ({clock.get_fps():.2f})")
    clock.tick(60)

pygame.quit()
import pygame
import Node
from collections import deque

WHITE = (255,255,255)
BLACK = (000,000,000)
RED = (255,000,000)
GREEN = (000,255,000)
BLUE = (000,000,255)
YELLOW = (255,255,000)
PURPLE = (128, 0, 128)


#Pygame

def update_grid(screen,grid,rows,width):

    screen.fill(WHITE)
    draw_node(screen, grid)
    draw_grid(screen, rows, width)
    pygame.display.flip()

#Finding algorithm

def find_neighbor(grid, node):
    row, col = node.get_position()
    rows, cols = len(grid), len(grid[0])

    neighbors = []

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col].is_empty() or grid[new_row][new_col].is_end() or grid[new_row][new_col].is_currenly_visit():
                if not grid[new_row][new_col].is_end():
                    grid[new_row][new_col].set_currenly_visit()
                neighbors.append(grid[new_row][new_col])
    
    return neighbors

def make_path(path):
    for i in path:
        if not i.is_start() and not i.is_end():
            i.set_path()

# BFS
def Bfs_alogorithm(screen ,grid, start ,end, rows, width, step_by_step = False, delay = 1):

    visited = {start: None}
    queue = deque([start])
    meet_end = False

    start_time = pygame.time.get_ticks()

    while queue and not meet_end:

        end_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

        if end_time - start_time >= delay:
            start_time = end_time

            if not step_by_step:
                for i in queue: # set all neighbor for butter animation
                    find_neighbor(grid, i)
                update_grid(screen,grid,rows,width)

            node = queue.popleft()
            if node == end:
                meet_end = True
            
            for neighbor in find_neighbor(grid, node):
                if step_by_step:
                    update_grid(screen,grid,rows,width)
                if neighbor not in visited:
                    if not neighbor.is_end():
                        neighbor.set_visited()
                    visited[neighbor] = node
                    queue.append(neighbor)
    
    if end not in visited:
        return None

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = visited[node]

    path.reverse()
    make_path(path)

# DFS
def Dfs_alogorithm(screen ,grid, start ,end, rows, width, step_by_step = False, delay = 1):

    visited = {start: None}
    stack = deque([start])
    meet_end = False

    start_time = pygame.time.get_ticks()

    while stack and not meet_end:

        end_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

        if end_time - start_time >= delay:
            start_time = end_time

            if not step_by_step:
                for i in stack: # set all neighbor for butter animation
                    find_neighbor(grid, i)
                update_grid(screen,grid,rows,width)

            node = stack.pop()
            if node == end:
                meet_end = True
            
            for neighbor in find_neighbor(grid, node):
                if step_by_step:
                    update_grid(screen,grid,rows,width)
                if neighbor not in visited:
                    if not neighbor.is_end():
                        neighbor.set_visited()
                    visited[neighbor] = node
                    stack.append(neighbor)
    
    if end not in visited:
        return None

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = visited[node]

    path.reverse()
    make_path(path)

#Grid

def create_grid(rows, width):

    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node.create_node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

def draw_grid(screen, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(screen, (000,000,000), (0, i*gap), (width, i*gap))
    for i in range(rows):
            pygame.draw.line(screen, (000,000,000), (i*gap, 0), (i*gap, width))

def draw_node(screen, grid):
    for row in grid:
        for node in row:
            node.draw(screen)

def find_clicked_position(pos, rows, width):

    gap = width // rows
    x, y = pos

    row = x // gap
    col = y // gap

    return row, col


import pygame
from Node import node

def draw_grid(screen,WIDTH, row, COLOR = (0,0,0)):

    GAP = WIDTH / row 
    
    for i in range(row + 1):
        pygame.draw.line(screen, COLOR, (0, i*GAP), (WIDTH,i*GAP),1)
        pygame.draw.line(screen, COLOR, (i*GAP,0), (i*GAP,WIDTH),1)
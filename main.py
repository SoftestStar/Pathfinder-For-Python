import pygame
import general_algorithm as gal

ROW = 50
WIDTH = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH,WIDTH))

WHILE = (255,255,255)
BLACK = (000,000,000)

clock = pygame.time.Clock()

is_running = True

def mouse_act():
    if pygame.mouse.get_pressed()[0]:
        print(pygame.mouse.get_pos())
    elif pygame.mouse.get_pressed()[2]:
        pass

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill(BLACK)

    gal.draw_grid(screen,WIDTH,ROW,WHILE)

    mouse_act()

    gal.created_grid()

    pygame.display.flip()
    pygame.display.set_caption(f"Pathfinder for Python ({clock.get_fps():.2f})")
    clock.tick(60)

pygame.quit()
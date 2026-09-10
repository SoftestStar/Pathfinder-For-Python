import pygame

SCREEN_SIZE = (200,200)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pathfinder for Python")

clock = pygame.time.Clock()

is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((000,000,000))
    print(clock)
    clock.tick(60)

pygame.quit()
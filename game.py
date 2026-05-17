import pygame

pygame.init()

screen = pygame.display.set_mode((1800, 1600))

running = True

while running:

    # THis is for handling the shutdown :D
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 30))
    pygame.display.update()

pygame.quit()
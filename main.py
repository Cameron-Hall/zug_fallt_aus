import pygame

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((951,700))
clock = pygame.time.Clock()

# loops and stages
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()
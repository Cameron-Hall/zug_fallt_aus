import pygame

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((951,700))
clock = pygame.time.Clock()

# loops and stages
running = True
homepage = True
game = False

# sizes
width = screen.get_width()
height = screen.get_height()

# fonts
font_h1 = pygame.font.SysFont("ocraextended", 100, False, False)
font_h2 = pygame.font.SysFont("ocraextended", 30, False, False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if homepage:
        screen.fill(pygame.Color(200,200,200))

        text = font_h1.render("Zug Fällt Aus", True, "black")
        screen.blit(text, ((width / 2) - (text.get_width() / 2), (height / 2) - (text.get_height() / 2) - height * 0.1))
        text = font_h2.render("Press anywhere to continue", True, "black")
        screen.blit(text, ((width / 2) - (text.get_width() / 2), (height / 2) - (text.get_height() / 2) + height * 0.1))

        if pygame.mouse.get_pressed()[2] or pygame.mouse.get_pressed()[0]:
            homepage = False
            game = True

    pygame.display.flip()

pygame.quit()
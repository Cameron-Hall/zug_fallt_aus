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
H1_SIZE = 100
H2_SIZE = 30
font_h1 = pygame.font.SysFont("ocraextended", H1_SIZE, False, False)
font_h2 = pygame.font.SysFont("ocraextended", H2_SIZE, False, False)

# images and sprites
map = pygame.image.load("zug_fallt_aus/germany-satellite-map.png")

# values
euros = 100000

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

    if game:
        screen.fill(pygame.Color(200,200,200))
        screen.blit(map,(0,0))

        sidebar_rect = pygame.Rect(map.get_width(), 0, width-map.get_width(), height)
        pygame.draw.rect(screen, "black", sidebar_rect, width = 2)

        # money tab
        money = font_h2.render(f"${euros}", True, "black")
        screen.blit(money, ((map.get_width() + ((width-map.get_width()) / 2)) - (money.get_width() / 2), H2_SIZE))
        y_down = H2_SIZE * 3


    pygame.display.flip()

pygame.quit()
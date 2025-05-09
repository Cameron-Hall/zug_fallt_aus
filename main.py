import pygame

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((961,700))
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
H3_SIZE = 16
font_h1 = pygame.font.SysFont("ocraextended", H1_SIZE, False, False)
font_h2 = pygame.font.SysFont("ocraextended", H2_SIZE, False, False)
font_h3 = pygame.font.SysFont("ocraextended", H3_SIZE, False, False)

# images and sprites
map = pygame.image.load("zug_fallt_aus/germany-satellite-map.png")

# values
euros = 100000

def horizontal_labels(labels, x_across, y_down):
    '''Print horizontal labels based on a list of values and an x and y value'''
    rect_list = []
    max_len = (width-map.get_width() + (len(labels) * 2)) / len(labels)
    for label in labels:
        label_text = font_h3.render(label, True, "black")
        text_gap = (max_len - (H3_SIZE * 2) - label_text.get_width()) / 2
        screen.blit(label_text, (map.get_width() + x_across + text_gap, y_down + H3_SIZE - 1.5))

        label_text_rect = pygame.Rect(map.get_width() + x_across - H3_SIZE, y_down, max_len, H3_SIZE * 3)
        pygame.draw.rect(screen, "black", label_text_rect, width = 2)

        rect_list.append(label_text_rect)
        x_across += (max_len-2)
    return rect_list


def button_check(rect):
    if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]-2) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]+1):
        pygame.event.get()
        return True
    

while running:
    for event in pygame.event.get(exclude=pygame.MOUSEBUTTONUP):
        if event.type == pygame.QUIT:
            running = False

    if homepage:
        screen.fill(pygame.Color(200,200,200))

        text = font_h1.render("Zug Fällt Aus", True, "black")
        screen.blit(text, ((width / 2) - (text.get_width() / 2), (height / 2) - (text.get_height() / 2) - height * 0.1))
        text = font_h2.render("Press anywhere to continue", True, "black")
        screen.blit(text, ((width / 2) - (text.get_width() / 2), (height / 2) - (text.get_height() / 2) + height * 0.1))

        rect = pygame.Rect(0, 0, width, height)
        if button_check(rect):
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

        # nav bar buttons
        nav_labels = ["Stations", "Trains", "Lines", "Upgrades"]
        nav_rects = horizontal_labels(nav_labels ,H3_SIZE, y_down)
        y_down += H3_SIZE * 3 - 2

        # nav bar functions
        for rect in nav_rects:
            if button_check(rect):
                if nav_rects.index(rect) == 0:
                    station_menu = True
                    train_menu = False
                    line_menu = False
                    upgrade_menu = False
                elif nav_rects.index(rect) == 1:
                    station_menu = False
                    train_menu = True
                    line_menu = False
                    upgrade_menu = False
                elif nav_rects.index(rect) == 2:
                    station_menu = False
                    train_menu = False
                    line_menu = True
                    upgrade_menu = False
                elif nav_rects.index(rect) == 3:
                    station_menu = False
                    train_menu = False
                    line_menu = False
                    upgrade_menu = True   

    pygame.display.flip()

pygame.quit()
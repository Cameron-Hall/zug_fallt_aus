import pygame

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((961,700))
clock = pygame.time.Clock()

# loops and stages
running = True
homepage = True
game = False

mouse_up_check = False

station_menu = False
train_menu = False
line_menu = False
upgrade_menu = False

station_menu_unowned = False
station_menu_owned = False

train_menu_purchase = False
train_menu_owned = False

# sizes
width = screen.get_width()
height = screen.get_height()

# fonts
H1_SIZE = 100
H2_SIZE = 30
H3_SIZE = 16
H4_SIZE = 13
H5_SIZE = 11
font_h1 = pygame.font.SysFont("ocraextended", H1_SIZE, False, False)
font_h2 = pygame.font.SysFont("ocraextended", H2_SIZE, False, False)
font_h3 = pygame.font.SysFont("ocraextended", H3_SIZE, False, False)
font_h4 = pygame.font.SysFont("ocraextended", H4_SIZE, False, False)
font_h5 = pygame.font.SysFont("ocraextended", H5_SIZE, False, False)

# images and sprites
map = pygame.image.load("zug_fallt_aus/germany-satellite-map.png")

# values
euros = 100000

# lists
stations_unowned = [["Munich",     "MUC", 360, 610, 125000, 50000, 6, ""],
                    ["Nuremberg",  "NRB", 310, 490, 50000,  25000, 3, ""],
                    ["Stuttgart",  "STT", 195, 560, 65000,  30000, 5, ""],
                    ["Frankfurt",  "FRA", 150, 460, 105000, 50000, 6, ""],
                    ["Essen",      "ESS", 70,  320, 100000, 45000, 5, ""],
                    ["Dortmund",   "DOR", 100, 315, 145000, 50000, 5, ""],
                    ["Dusseldorf", "DUS", 60,  345, 120000, 50000, 5, ""],
                    ["Cologne",    "KOL", 65,  370, 150000, 50000, 5, ""],
                    ["Bielefeld",  "BIE", 165, 270, 60000,  25000, 3, ""],
                    ["Hanover",    "HAN", 220, 240, 55000,  15000, 3, ""],
                    ["Bremen",     "BRE", 170, 185, 80000,  40000, 4, ""],
                    ["Hamburg",    "HAM", 230, 145, 120000, 50000, 5, ""]
                    ] 
                  # [name, code, x, y, price, passenger_capacity, train_cap, operates_to]


stations_owned = [["Berlin", "BER", 425, 220, 120000, 50000, 6, ""],
                  ["Dresden", "DRS", 460, 350, 50000, 20000, 3, ""],
                  ["Leipzig", "LPZ", 375, 320, 45000, 20000, 3, ""]] # [name, x, y, profit, text_color, bg_color]

train_types = [] # [make, model, cost, capacity, speed, text_color, bg_color]
owned_trains = [] # [make, model, station_a, station_b]

lines = [["BER", "LPZ", [], 400],
         ["DRS", "LPZ", [], 200],
         ["BER", "DRS", [], 300],
         ] # [start, end, [train_ids], distance]

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

    # checks for phantom clicks (ie. player clicks not on a button, so MOUSEBUTTONUP does not get removed from the event queue)
    if mouse_up_check:
        mouse_up_check = False
        pygame.event.get()
    if pygame.event.peek(pygame.MOUSEBUTTONUP):
        mouse_up_check = True

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
            station_menu = True
            station_menu_unowned = True

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

        # station menu
        if station_menu:
            station_purchase_labels = ["Unowned", "Owned"]
            station_purchase_rects = horizontal_labels(station_purchase_labels, H3_SIZE, y_down)
            y_down += H3_SIZE * 3
            for rect in station_purchase_rects:
                if button_check(rect):
                    if station_purchase_rects.index(rect) == 0:
                        station_menu_unowned = True
                        station_menu_owned = False
                    elif station_purchase_rects.index(rect) == 1:
                        station_menu_unowned = False
                        station_menu_owned = True


        # drawing on map
        # draw lines
        for line in lines:
            for station in stations_owned:
                if station[1] == line[0]:
                    start_loc = station
                if station[1] == line[1]:
                    end_loc = station
            pygame.draw.line(screen, "white", (start_loc[2]+2.5, start_loc[3]+2.5), (end_loc[2]+2.5, end_loc[3]+2.5), width = 3)

        # draw stations
        for station in stations_unowned+stations_owned:
            # on hover
            if pygame.mouse.get_pos()[0] in range(station[2]-5,station[2]+11) and pygame.mouse.get_pos()[1] in range(station[3]-5,station[3]+11):
                station_inner = pygame.Rect(station[2]-2,station[3]-2,9,9)

            # no hover
            else:
                station_inner = pygame.Rect(station[2],station[3],5,5)
            station_outer = pygame.Rect(station[2]-5,station[3]-5,15,15)

            # color based on ownership status
            if station in stations_unowned and station[4] > euros: # unowned, cannot afford
                color = pygame.Color(161, 53, 45)
            elif station in stations_unowned:                      # unowned, can afford
                color = pygame.Color(200,200,200)
            else:                                                  # owned
                color = pygame.Color(11,188,9)

            pygame.draw.rect(screen, "black", station_outer)
            pygame.draw.rect(screen, color, station_inner)


    pygame.display.flip()

pygame.quit()
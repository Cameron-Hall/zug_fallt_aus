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

station_menu_unowned = True
station_menu_owned = False
train_menu_purchase = False
train_menu_owned = True
line_menu_owned = True
line_menu_purchase = False

station_page_unowned = 0
station_page_owned = 0
train_page_purchase = 0
train_page_owned = 0
line_page_owned = 0
line_page_purchase = 0

# images
map = pygame.image.load("zug_fallt_aus/germany-satellite-map.png")

# sizes
width = screen.get_width()
height = screen.get_height()
sidebar_centre = map.get_width()+((width-map.get_width())/2)

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

font_h1.set_bold(True)
font_h2.set_bold(True)
# font_h4.set_bold(True)

# values
euros = 1200000

# lists
stations_unowned = [["Munich",               "MUC", 360, 610, 740000,  50000, 6, ["NRB", "AUG"], "High"],
                    ["Nuremberg",            "NRB", 310, 490, 420000,  25000, 3, ["MUC", "AUG", "ERF", "FRA", "STT"], "Medium"],
                    ["Stuttgart",            "STT", 195, 560, 650000,  30000, 5, ["FRA", "KAR", "AUG", "NRB"], "Medium"],
                    ["Frankfurt",            "FRA", 155, 460, 1000000, 50000, 6, ["ERF", "BIE", "KOL", "KAR", "STT", "NRB"], "Very High"],
                    ["Essen",                "ESS", 70,  320, 800000,  45000, 5, ["DUS", "DOR"], "High"],
                    ["Dortmund",             "DOR", 100, 315, 950000,  50000, 5, ["ESS", "BIE"], "Very High"],
                    ["Dusseldorf",           "DUS", 60,  345, 720000,  50000, 5, ["KOL", "ESS"], "High"],
                    ["Bielefeld",            "BIE", 165, 270, 450000,  20000, 3, ["DOR", "FRA", "HAN", "BRE"], "Low"],
                    ["Hanover",              "HAN", 220, 240, 510000,  25000, 3, ["HAM", "BRE", "BIE", "ERF"], "Low"],
                    ["Bremen",               "BRE", 170, 185, 650000,  40000, 4, ["HAM", "HAN", "BIE"], "Medium"],
                    ["Hamburg",              "HAM", 230, 145, 800000,  50000, 5, ["BER", "BRE", "HAN"], "Medium"],
                    ["Karlsruhe",            "KAR", 150, 545, 300000,  18000, 3, ["FRA", "STT"], "Low"],
                    ["Erfurt",               "ERF", 305, 370, 400000,  40000, 5, ["LPZ", "NRB", "HAN"], "Low"],
                    ["Augsburg",             "AUG", 300, 585, 350000,  25000, 4, ["MUC", "STT", "NRB"], "Low"],

                    ["Berlin",               "BER", 425, 220, 740000,  50000, 6, ["NRB", "AUG"], "High"],
                    ["Leipzig",              "LPZ", 375, 320, 420000,  25000, 3, ["MUC", "AUG", "ERF", "FRA", "STT"], "Medium"],
                    ["Dresden",              "DRS", 460, 350, 650000,  30000, 5, ["FRA", "KAR", "AUG", "NRB"], "Medium"],

                    ["Munster",              "MUN", 115, 275, 600000,  35000, 6, [], "High"],
                    ["Bonn",                 "BON", 75,  390, 680000,  40000, 5, [], "High"],
                    ["Madgeburg",            "MAD", 320, 260, 500000,  25000, 5, [], "Medium"],
                    ["Potsdam",              "POT", 380, 240, 450000,  30000, 5, [], "Medium"],
                    ["Regensburg",           "REG", 385, 525, 380000,  22000, 5, [], "Low"],
                    ["Konstanz",             "KON", 195, 655, 150000,  8000,  3, [], "Low"],
                    ["Freiburg im Breisgau", "FRB", 120, 630, 200000,  7500,  3, [], "Low"],
                    ["Wurzburg",             "WRZ", 230, 475, 240000,  10000, 4, [], "Medium"],
                    ["Mannheim",             "MAN", 150, 495, 520000,  15000, 5, [], "Medium"],
                    ["Kassel",               "KAS", 200, 340, 300000,  18000, 3, [], "Medium"],
                    ["Flensburg",            "FLN", 205, 30,  90000,   5000,  1, [], "Low"],
                    ["Bremerhaven",          "BRM", 160, 135, 350000,  20000, 4, [], "Medium"],
                    ["Aachen",               "AAC", 25,  385, 300000,  18000, 3, [], "Medium"],
                    ["Oldenburg",            "OLD", 125, 180, 400000,  12000, 5, [], "Low"],
                    ["Wuppertal",            "WUP", 85,  345, 900000,  30000, 4, [], "High"],
                    ["Cologne",              "KOL", 65,  370, 850000,  60000, 5, ["DUS", "FRA"], "Very High"]
                    ] 
                  # [name,          code, x,   y,   price, passenger_capacity, train_cap, can_operate_to, demand]


stations_owned = [] 
# [name, code, x, y, additional_costs, passive_daily_profit, train_daily_profit, total_daily_profit, trains_running, train_cap, operates to, can_operate_to, text_color, bg_color]

train_types = [["TTT", "Baron", 50000, "Diesel", 250, 120, None, None],
               ] # [make, model, cost, fuel type, capacity, speed, text_color, bg_color]
owned_trains = [] # [make, model, station_a, station_b]

lines = [] # [start, end, [train_ids], distance]

# functions
def cell_amount_calc(cell_height):
    return round((height - 250) / cell_height)


def button_check(rect):
    if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]-2) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]+1):
        pygame.event.get()
        return True


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


def print_text(words, font, color, x, y):
    text = font.render(str(words), True, color)
    screen.blit(text, (x, y))


def page_numbers(list, page, cell_amount):
    page_num_rects = []
    pages = (len(list) // 11) + 1
    x_across = map.get_width() + ((width - map.get_width()) / 2) - ((pages * 2 - 1) * 15 ) / 2 + 2
    y_down = (height - H5_SIZE*2.65)
    for i in range(pages):
        rect = pygame.Rect(x_across, y_down, 15, 15)
        pygame.draw.rect(screen, pygame.Color(170,170,170), rect)
        page_num_rects.append(rect)

        print_text(str(i+1), font_h5, "black", x_across + 4.0625, y_down+1)
        x_across += 30

    for rect in page_num_rects:
        if button_check(rect):
            page = page_num_rects.index(rect)
    return page


def page_tab(y_down, left_title, right_title, data_1_title, data_1_value, data_2_title, data_2_value, data_3_title = None, data_3_value = None, data_4_title = None, data_4_value = None, data_5_title = None, data_5_value = None, data_6_title = None, data_6_value = None):
    if data_3_title == None:
        h5_mult = 1
    elif data_5_title == None:
        h5_mult = 2
    else:
        h5_mult = 3
    rect = pygame.Rect(map.get_width()+2, y_down, width-map.get_width()-4, H4_SIZE + 8 + (H5_SIZE * h5_mult))
    pygame.draw.rect(screen, pygame.Color(130,130,130), rect, width = 2)
    pygame.draw.line(screen,pygame.Color(130,130,130),(sidebar_centre, y_down + H4_SIZE + 4), (sidebar_centre, y_down + H4_SIZE + 6 + (H5_SIZE * h5_mult)), width = 2)

    print_text(left_title[0], font_h4, left_title[1], map.get_width()+6, y_down + 2)
    print_text(right_title[0], font_h4, right_title[1], width - 6 - (H4_SIZE/1.6)*len(right_title[0]), y_down + 2)

    print_text(data_1_title[0], font_h5, data_1_title[1], map.get_width() + 6, y_down + H4_SIZE + 4)
    print_text(data_1_value[0], font_h5, data_1_value[1], sidebar_centre - 2 - (H5_SIZE/1.6)*len(f"{data_1_value[0]}"), y_down + H4_SIZE + 4)

    print_text(data_2_title[0], font_h5, data_2_title[1], sidebar_centre + 4, y_down + H4_SIZE + 4)
    print_text(data_2_value[0], font_h5, data_2_value[1], width - 6 - (H5_SIZE/1.6)*len(f"{data_2_value[0]}"), y_down + H4_SIZE + 4)

    if data_3_title != None:
        print_text(data_3_title[0], font_h5, data_3_title[1], map.get_width() + 6, y_down + H4_SIZE + H5_SIZE + 4)
        print_text(data_3_value[0], font_h5, data_3_value[1], sidebar_centre - 2 - (H5_SIZE/1.6)*len(f"{data_3_value[0]}"), y_down + H4_SIZE + H5_SIZE + 4)

    if data_4_title != None:
        print_text(data_4_title[0], font_h5, data_4_title[1], sidebar_centre + 4, y_down + H4_SIZE + H5_SIZE + 4)
        print_text(data_4_value[0], font_h5, data_4_value[1], width - 6 - (H5_SIZE/1.6)*len(f"{data_4_value[0]}"), y_down + H4_SIZE + H5_SIZE + 4)

    if data_5_title != None:
        print_text(data_5_title[0], font_h5, data_5_title[1], map.get_width() + 6, y_down + H4_SIZE + H5_SIZE*2 + 4)
        print_text(data_5_value[0], font_h5, data_5_value[1], sidebar_centre - 2 - (H5_SIZE/1.6)*len(f"{data_5_value[0]}"), y_down + H4_SIZE + H5_SIZE*2 + 4)

    if data_6_title != None:
        print_text(data_6_title[0], font_h5, data_6_title[1], sidebar_centre + 4, y_down + H4_SIZE + H5_SIZE*2 + 4)
        print_text(data_6_value[0], font_h5, data_6_value[1], width - 6 - (H5_SIZE/1.6)*len(f"{data_6_value[0]}"), y_down + H4_SIZE + H5_SIZE*2 + 4)

    return h5_mult

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

        menu = font_h1.render("Zug Fällt Aus", True, "black")
        screen.blit(menu,((width/2)-(menu.get_width()/2),(height/2)-(menu.get_height()/2)-height*0.1))
        anywhere = font_h2.render("Press anywhere to continue", True, "black")
        screen.blit(anywhere,((width/2)-(anywhere.get_width()/2),(height/2)-(anywhere.get_height()/2)+height*0.1))
        rect = pygame.Rect(0, 0, width, height)
        
        if button_check(rect):
            homepage = False
            game = True
            station_menu = True

    if game:
        screen.fill(pygame.Color(200,200,200))
        screen.blit(map,(0,0))

        sidebar_rect = pygame.Rect(map.get_width(), 0, width-map.get_width(), height)
        pygame.draw.rect(screen, "black", sidebar_rect, width = 2)

        # money tab
        money = font_h2.render(f"${euros}", True, "black")
        screen.blit(money, ((map.get_width()+((width-map.get_width())/2))-(money.get_width()/2),H2_SIZE))
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
                    line_menu_purchase = False
                    upgrade_menu = False
                elif nav_rects.index(rect) == 1:
                    station_menu = False
                    train_menu = True
                    line_menu = False
                    line_menu_purchase = False
                    upgrade_menu = False
                elif nav_rects.index(rect) == 2:
                    station_menu = False
                    train_menu = False
                    line_menu = True
                    line_menu_purchase = False
                    upgrade_menu = False
                elif nav_rects.index(rect) == 3:
                    station_menu = False
                    train_menu = False
                    line_menu = False
                    line_menu_purchase = False
                    upgrade_menu = True                 

        # station menu
        if station_menu:
            y_down = H2_SIZE * 3 + H3_SIZE * 3 - 2
            station_purchase_rects = horizontal_labels(["Unowned", "Owned"], H3_SIZE, y_down)
            y_down += H3_SIZE * 3
            for rect in station_purchase_rects:
                if button_check(rect):
                    if station_purchase_rects.index(rect) == 0:
                        station_menu_unowned = True
                        station_menu_owned = False
                    elif station_purchase_rects.index(rect) == 1:
                        station_menu_unowned = False
                        station_menu_owned = True
            
            # unowned stations
            if station_menu_unowned:
                purchase_rects = []

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * 3))

                for station in stations_unowned[cell_amount * station_page_unowned:cell_amount * station_page_unowned + cell_amount]:
                    color = pygame.Color(130,130,130) if station[4] > euros else pygame.Color(11,128,9)
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.6)*len("PURCHASE"), y_down + 3, (H4_SIZE/1.6)*len("PURCHASE") + 2, H4_SIZE + 1)
                    pygame.draw.rect(screen, color, rect)
                    purchase_rects.append(rect)

                    color = "red" if station[4] > euros else pygame.Color(11,128,9)
                    h5_mult = page_tab(y_down,
                             [f"{station[0]} - {station[1]}", "black"],
                             ["PURCHASE", "white"],
                             ["Cost", "black"],
                             [station[4], color],
                             ["Train Cap", "black"],
                             [station[6], "black"],
                             ["Passenger Cap", "black"],
                             [station[5], "black"],
                             ["Operates to", "black"],
                             [", ".join(station[7][0:4]), "black"],
                             ["Demand", "black"],
                             [station[8], "black"],
                             ["", "black"],
                             [", ".join(station[7][4:8]), "black"])
                    
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)

                # add page numbers
                station_page_unowned = page_numbers(stations_unowned, station_page_unowned, cell_amount)

                for rect in purchase_rects:
                    if button_check(rect):
                        if euros < stations_unowned[purchase_rects.index(rect)][4]:
                            pass
                        else:
                            euros -= stations_unowned[purchase_rects.index(rect)][4]
                            stations_owned.append(stations_unowned[purchase_rects.index(rect)])
                            stations_unowned.remove(stations_unowned[purchase_rects.index(rect)])

                            # [name, code, x, y, price,            passenger_capacity,   train_cap,          can_operate_to    ,   demand      ,          ,            ,               ,           ,     ]
                            # [name, code, x, y, additional_costs, passive_daily_profit, train_daily_profit, total_daily_profit, trains_running, train_cap, operates to, can_operate_to, text_color, bg_color]
                            #   0      1   2  3   4                      5                     6                 7                      8              9      10            11                   12      13

                            stations_owned[-1][4] = round(stations_owned[-1][4]/125)
                            stations_owned[-1][5] = 0
                            stations_owned[-1][6] = 0
                            can_operate = stations_owned[-1][7]
                            stations_owned[-1][7] = 0
                            stations_owned[-1].append(0)
                            stations_owned[-1].append(0)
                            stations_owned[-1].append(can_operate)
                            stations_owned[-1].append([])

            # owned stations
            if station_menu_owned:
                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * 3))
# [name, code, x, y, additional_costs, daily_profit, all_time_profit, trains_running, train_cap, operates to, can_operate_to, text_color, bg_color]
                for station in stations_owned[cell_amount * station_page_owned:cell_amount * station_page_owned + cell_amount]:
                    h5_mult = page_tab(y_down,
                             [f"{station[0]} - {station[1]}", "black"],
                             ["", "white"],
                             ["Daily Profit", "black"],
                             [station[5], "black"],
                             ["All Time Profit", "black"],
                             [station[6], "black"],
                             ["Train Space", "black"],
                             [f"{station[7]}/{station[8]}", "black"],
                             ["Operates to", "black"],
                             [station[9], "black"],
                             ["Price Markup", "black"],
                             [station[4], "black"],
                             ["", "black"],
                             [station[10], "black"])
                    
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)
                # add page numbers
                station_page_owned = page_numbers(stations_owned, station_page_owned, cell_amount)


        # train menu
        if train_menu:
            text = font_h1.render("train", True, "black")
            screen.blit(text, (width/2,height/2))

        # lines menu
        if line_menu:
            y_down = H2_SIZE * 3 + H3_SIZE * 3 - 2
            line_menu_purchase_rects = horizontal_labels(["Owned", "Purchase New"], H3_SIZE, y_down)
            y_down += H3_SIZE * 3
            for rect in line_menu_purchase_rects:
                if button_check(rect):
                    if line_menu_purchase_rects.index(rect) == 0:
                        line_menu_owned = True
                        line_menu_purchase = False
                    elif line_menu_purchase_rects.index(rect) == 1:
                        line_menu_owned = False
                        line_menu_purchase = True

            # owned lines
            if line_menu_owned:

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * h5_mult))

                for line in lines[cell_amount * line_page_owned:cell_amount * line_page_owned + cell_amount]:
                    # rect for line box
                    h5_mult = page_tab(y_down,
                            [line[0], "black"],
                            [line[1], "black"],
                            ["Trains Running", "black"],
                            [len(line[2]), "black"],
                            ["Line Length", "black"],
                            [f"{line[3]}km", "black"]
                            )

                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)
            
                rect = pygame.Rect(map.get_width()+2, y_down, width-map.get_width()-4, H4_SIZE * 3)
                pygame.draw.rect(screen, pygame.Color(11,128,9), rect)
                pygame.draw.rect(screen, pygame.Color(130,130,130), rect, width = 2)
                print_text("+ Add new line", font_h4, "white", (map.get_width()+((width-map.get_width())/2))-((H5_SIZE/1.6)*len(f"+ Add new line")/2), y_down + H4_SIZE - 2)

                if button_check(rect):
                    line_menu_purchase = True
                    line_menu_owned = False

                # add page numbers
                line_page_owned = page_numbers(lines, line_page_owned, cell_amount)

            # line purchasing
            if line_menu_purchase:
                y_down = H2_SIZE * 3 + H3_SIZE * 6 - 4
                horizontal_labels(["Choose starting station"], H3_SIZE, y_down)
                y_down += H3_SIZE * 3

                line_choose_rects = []

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * h5_mult))

                for station in stations_owned[cell_amount * line_page_purchase:cell_amount * line_page_purchase + cell_amount]:
                    color = pygame.Color(130,130,130) if station[4] > euros else pygame.Color(11,128,9)
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.6)*len("CHOOSE"), y_down + 3, (H4_SIZE/1.6)*len("CHOOSE") + 2, H4_SIZE + 1)
                    pygame.draw.rect(screen, color, rect)
                    line_choose_rects.append(rect)
                    
                    train_space_used = 0

                    for line in lines:
                        if line[0] == station[1] or line[1] == station[1]:
                            train_space_used += len(line[2])

                    color = "red" if station[4] > euros else pygame.Color(11,128,9)
                    h5_mult = page_tab(y_down,
                                [station[0], "black"],
                                ["CHOOSE", "white"],
                                ["Additional Fee", "black"],
                                [station[4], color],
                                ["Train Space", "black"],
                                [station[6]-train_space_used, "black"]
                                )
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)

                # add page numbers
                line_page_purchase = page_numbers(stations_owned, line_page_purchase, cell_amount)

                for rect in line_choose_rects:
                    if button_check(rect):
                        if euros < stations_owned[purchase_rects.index(rect)][4]:
                            pass
                        else:
                            euros -= stations_owned[purchase_rects.index(rect)][4]
                            


        # upgrades menu
        if upgrade_menu:
            text = font_h1.render("upgrade", True, "black")
            screen.blit(text, (width/2,height/2))

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

            if station in stations_unowned and station[4] > euros:
                color = pygame.Color(161, 53, 45)
            elif station in stations_unowned:
                color = pygame.Color(200,200,200)
            else:
                color = "yellow"

            # pygame.Color(11,188,9)

            pygame.draw.rect(screen, "black", station_outer)
            pygame.draw.rect(screen, color, station_inner)

        # hover labels - needs separate loop so they show above the stations on the map
        for station in stations_unowned+stations_owned:
            if pygame.mouse.get_pos()[0] in range(station[2]-5,station[2]+11) and pygame.mouse.get_pos()[1] in range(station[3]-5,station[3]+11):

                if station in stations_unowned and station[4] > euros:
                    bg_color = pygame.Color(161, 53, 45)
                elif station in stations_unowned:
                    bg_color = pygame.Color(170,170,170)
                else:
                    bg_color = "yellow"

                rect = pygame.Rect(station[2] + 3 - ((H5_SIZE/1.6)*len("XXXX"))/2, station[3] - H5_SIZE * 2, ((H5_SIZE/1.6)*len("XXXX")), H5_SIZE+2)
                pygame.draw.rect(screen, bg_color, rect)
                font_h5.set_bold(True)
                print_text(station[1], font_h5, "black", station[2] + 2.5 - ((H5_SIZE/1.6)*len("XXX"))/2, station[3] - H5_SIZE * 2)
                font_h5.set_bold(False)

    pygame.display.flip()

    # print(pygame.mouse.get_pos())
    # print(pygame.event.poll())

pygame.quit()
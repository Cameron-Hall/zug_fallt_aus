import pygame
import math

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((961,700))
clock = pygame.time.Clock()
dt = 0

# loops and stages
running = True
homepage = True
game = False

mouse_up_check = False
flash = 0

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
line_menu_purchase_2 = False

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

# colours
dark_red = 0
black = "black"
yellow = "yellow"
green = 0
dark_grey = pygame.Color(130,130,130)
grey = pygame.Color(170,170,170)

# values
euros = 1200000
COST_PER_KM = 100

# lists
stations_unowned = [
    {"name": "Aachen",      "code": "AAC", "x": 25,  "y": 385, "cost": 250000, "passenger_cap": 15000, "train_cap": 15, "operates_to": ['BON', 'DUS', 'KOL']},
    {"name": "Augsburg",    "code": "AUG", "x": 300, "y": 585, "cost": 600000, "passenger_cap": 40000, "train_cap": 18, "operates_to": ['MUC', 'NRB', 'ULM']},
    {"name": "Berlin",      "code": "BER", "x": 425, "y": 220, "cost": 1200000,"passenger_cap": 100000,"train_cap": 28, "operates_to": ['DRS', 'HAM', 'POT', 'ROS']},
    {"name": "Bielefeld",   "code": "BIE", "x": 165, "y": 270, "cost": 450000, "passenger_cap": 35000, "train_cap": 24, "operates_to": ['BRE', 'DOR', 'HAN', 'KAS', 'MUN', 'OLD']},
    {"name": "Bonn",        "code": "BON", "x": 75,  "y": 390, "cost": 320000, "passenger_cap": 25000, "train_cap": 12, "operates_to": ['AAC', 'FRA', 'KOL']},
    {"name": "Bremerhaven", "code": "BRM", "x": 160, "y": 135, "cost": 400000, "passenger_cap": 30000, "train_cap": 20, "operates_to": ['BRE', 'HAM', 'OLD']},
    {"name": "Bremen",      "code": "BRE", "x": 170, "y": 185, "cost": 150000, "passenger_cap": 9000,  "train_cap": 9,  "operates_to": ['BIE', 'BRM', 'HAM', 'HAN', 'OLD']},
    {"name": "Chemnitz",    "code": "CHM", "x": 400, "y": 365, "cost": 180000, "passenger_cap": 10000, "train_cap": 6,  "operates_to": ['DRS', 'ERF']},
    {"name": "Cologne",     "code": "KOL", "x": 65,  "y": 370, "cost": 600000, "passenger_cap": 52000, "train_cap": 16, "operates_to": ['AAC', 'BON', 'DUS', 'WUP']},
    {"name": "Dortmund",    "code": "DOR", "x": 100, "y": 315, "cost": 700000, "passenger_cap": 55000, "train_cap": 25, "operates_to": ['BIE', 'ESS', 'KAS', 'MUN', 'WUP']},
    {"name": "Dresden",     "code": "DRS", "x": 460, "y": 350, "cost": 750000, "passenger_cap": 60000, "train_cap": 12, "operates_to": ['BER', 'CHM', 'LPZ']},
    {"name": "Dusseldorf",  "code": "DUS", "x": 60,  "y": 345, "cost": 750000, "passenger_cap": 45000, "train_cap": 16, "operates_to": ['AAC', 'ESS', 'KOL', 'WUP']},
    {"name": "Essen",       "code": "ESS", "x": 70,  "y": 320, "cost": 400000, "passenger_cap": 35000, "train_cap": 12, "operates_to": ['DOR', 'DUS', 'WUP']},
    {"name": "Erfurt",      "code": "ERF", "x": 305, "y": 370, "cost": 320000, "passenger_cap": 28000, "train_cap": 24, "operates_to": ['CHM', 'KAS', 'LPZ', 'MAD', 'NRB', 'WRZ']},
    {"name": "Flensburg",   "code": "FLN", "x": 205, "y": 30,  "cost": 90000,  "passenger_cap": 8000,  "train_cap": 3,  "operates_to": ['KIE']},
    {"name": "Freiburg",    "code": "FRB", "x": 120, "y": 630, "cost": 85000,  "passenger_cap": 10000, "train_cap": 3,  "operates_to": ['KAR']},
    {"name": "Frankfurt",   "code": "FRA", "x": 155, "y": 460, "cost": 900000, "passenger_cap": 80000, "train_cap": 30, "operates_to": ['BON', 'KAS', 'MAN', 'SBR', 'WRZ']},
    {"name": "Hamburg",     "code": "HAM", "x": 230, "y": 145, "cost": 850000, "passenger_cap": 70000, "train_cap": 30, "operates_to": ['BRM', 'BRE', 'BER', 'KIE', 'MAD', 'ROS']},
    {"name": "Hannover",    "code": "HAN", "x": 220, "y": 240, "cost": 620000, "passenger_cap": 50000, "train_cap": 20, "operates_to": ['BIE', 'BRE', 'KAS', 'MAD']},
    {"name": "Kassel",      "code": "KAS", "x": 200, "y": 340, "cost": 530000, "passenger_cap": 45000, "train_cap": 30, "operates_to": ['BIE', 'DOR', 'ERF', 'FRA', 'HAN', 'MAD']},
    {"name": "Karlsruhe",   "code": "KAR", "x": 150, "y": 545, "cost": 200000, "passenger_cap": 20000, "train_cap": 12, "operates_to": ['FRB', 'MAN', 'SBR', 'STT']},
    {"name": "Kiel",        "code": "KIE", "x": 240, "y": 80,  "cost": 180000, "passenger_cap": 15000, "train_cap": 9,  "operates_to": ['FLN', 'HAM', 'ROS']},
    {"name": "Konstanz",    "code": "KON", "x": 195, "y": 655, "cost": 85000,  "passenger_cap": 9000,  "train_cap": 6,  "operates_to": ['STT', 'ULM']},
    {"name": "Leipzig",     "code": "LPZ", "x": 375, "y": 320, "cost": 450000, "passenger_cap": 40000, "train_cap": 16, "operates_to": ['DRS', 'ERF', 'MAD', 'POT']},
    {"name": "Magdeburg",   "code": "MAD", "x": 320, "y": 260, "cost": 420000, "passenger_cap": 38000, "train_cap": 30, "operates_to": ['ERF', 'HAM', 'HAN', 'KAS', 'LPZ', 'POT']},
    {"name": "Mannheim",    "code": "MAN", "x": 150, "y": 495, "cost": 300000, "passenger_cap": 28000, "train_cap": 12, "operates_to": ['FRA', 'KAR', 'STT']},
    {"name": "Munster",     "code": "MUN", "x": 115, "y": 275, "cost": 360000, "passenger_cap": 32000, "train_cap": 9,  "operates_to": ['BIE', 'DOR', 'OLD']},
    {"name": "Munich",      "code": "MUC", "x": 360, "y": 610, "cost": 1100000,"passenger_cap": 95000, "train_cap": 15, "operates_to": ['AUG', 'NRB', 'REG']},
    {"name": "Nuremberg",   "code": "NRB", "x": 310, "y": 490, "cost": 510000, "passenger_cap": 44000, "train_cap": 25, "operates_to": ['AUG', 'ERF', 'MUC', 'REG', 'WRZ']},
    {"name": "Oldenburg",   "code": "OLD", "x": 125, "y": 180, "cost": 300000, "passenger_cap": 26000, "train_cap": 16, "operates_to": ['BIE', 'BRM', 'BRE', 'MUN']},
    {"name": "Potsdam",     "code": "POT", "x": 380, "y": 240, "cost": 200000, "passenger_cap": 22000, "train_cap": 9,  "operates_to": ['BER', 'LPZ', 'MAD']},
    {"name": "Regensburg",  "code": "REG", "x": 385, "y": 525, "cost": 180000, "passenger_cap": 17000, "train_cap": 6,  "operates_to": ['MUC', 'NRB']},
    {"name": "Rostock",     "code": "ROS", "x": 340, "y": 85,  "cost": 220000, "passenger_cap": 20000, "train_cap": 9,  "operates_to": ['BER', 'HAM', 'KIE']},
    {"name": "Saarbrucken", "code": "SBR", "x": 75,  "y": 520, "cost": 140000, "passenger_cap": 12000, "train_cap": 6,  "operates_to": ['FRA', 'KAR']},
    {"name": "Stuttgart",   "code": "STT", "x": 195, "y": 560, "cost": 600000, "passenger_cap": 55000, "train_cap": 25, "operates_to": ['KAR', 'KON', 'MAN', 'ULM', 'WRZ']},
    {"name": "Ulm",         "code": "ULM", "x": 245, "y": 585, "cost": 210000, "passenger_cap": 18000, "train_cap": 9,  "operates_to": ['AUG', 'KON', 'STT']},
    {"name": "Wuppertal",   "code": "WUP", "x": 85,  "y": 345, "cost": 250000, "passenger_cap": 24000, "train_cap": 16, "operates_to": ['DOR', 'DUS', 'ESS', 'KOL']},
    {"name": "Wurzburg",    "code": "WRZ", "x": 230, "y": 475, "cost": 300000, "passenger_cap": 27000, "train_cap": 16, "operates_to": ['ERF', 'FRA', 'NRB', 'STT']}
]
                  # [name,          code, x,   y,   price, passenger_capacity, train_cap, can_operate_to, demand]


stations_owned = [] 
# [name, code, x, y, additional_costs, passive_daily_profit, passenger_cap, total_daily_profit, trains_running, train_cap, operates_to, can_operate_to, text_color, bg_color]

train_types = [
    {"make": "", "model": "", "cost": "", "fuel type": ""}


] # [make, model, cost, fuel type, capacity, speed, text_color, bg_color]
owned_trains = [] # [make, model, station_a, station_b]

lines = [] # [start, end, [train_ids], distance]


# functions
def cell_amount_calc(cell_height, other_height):
    return round((height - (227 + other_height)) / cell_height)


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
    pages = (len(list) // cell_amount) + 1
    x_across = map.get_width() + ((width - map.get_width()) / 2) - ((pages * 2 - 1) * 15 ) / 2 + 2
    y_down = (height - H5_SIZE*2.65)
    for i in range(pages):

        if i == page:
            color = "yellow"
            rect = pygame.Rect(x_across-1, y_down-1, 17, 17)
            pygame.draw.rect(screen, "black", rect)
        else:
            color = pygame.Color(170,170,170)

        rect = pygame.Rect(x_across, y_down, 15, 15)
        pygame.draw.rect(screen, color, rect)
        page_num_rects.append(rect)

        font_h5.set_bold(True)
        print_text(str(i+1), font_h5, "black", x_across + 4.0625, y_down+1)
        font_h5.set_bold(False)
        x_across += 30

    for rect in page_num_rects:
        if button_check(rect):
            page = page_num_rects.index(rect)
    return page


def page_tab(y_down, left_title, right_title, data_1_title = None, data_1_value = None, data_2_title = None, data_2_value = None, data_3_title = None, data_3_value = None, data_4_title = None, data_4_value = None, data_5_title = None, data_5_value = None, data_6_title = None, data_6_value = None):
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
    print_text(right_title[0], font_h4, right_title[1], width - 6 - (H4_SIZE/1.58)*len(right_title[0]), y_down + 2)

    if data_1_title != None:
        print_text(data_1_title[0], font_h5, data_1_title[1], map.get_width() + 6, y_down + H4_SIZE + 4)
        print_text(data_1_value[0], font_h5, data_1_value[1], sidebar_centre - 2 - (H5_SIZE/1.58)*len(f"{data_1_value[0]}"), y_down + H4_SIZE + 4)

    if data_2_title != None:
        print_text(data_2_title[0], font_h5, data_2_title[1], sidebar_centre + 4, y_down + H4_SIZE + 4)
        print_text(data_2_value[0], font_h5, data_2_value[1], width - 6 - (H5_SIZE/1.58)*len(f"{data_2_value[0]}"), y_down + H4_SIZE + 4)

    if data_3_title != None:
        print_text(data_3_title[0], font_h5, data_3_title[1], map.get_width() + 6, y_down + H4_SIZE + H5_SIZE + 4)
        print_text(data_3_value[0], font_h5, data_3_value[1], sidebar_centre - 2 - (H5_SIZE/1.58)*len(f"{data_3_value[0]}"), y_down + H4_SIZE + H5_SIZE + 4)

    if data_4_title != None:
        print_text(data_4_title[0], font_h5, data_4_title[1], sidebar_centre + 4, y_down + H4_SIZE + H5_SIZE + 4)
        print_text(data_4_value[0], font_h5, data_4_value[1], width - 6 - (H5_SIZE/1.58)*len(f"{data_4_value[0]}"), y_down + H4_SIZE + H5_SIZE + 4)

    if data_5_title != None:
        print_text(data_5_title[0], font_h5, data_5_title[1], map.get_width() + 6, y_down + H4_SIZE + H5_SIZE*2 + 4)
        print_text(data_5_value[0], font_h5, data_5_value[1], sidebar_centre - 2 - (H5_SIZE/1.58)*len(f"{data_5_value[0]}"), y_down + H4_SIZE + H5_SIZE*2 + 4)

    if data_6_title != None:
        print_text(data_6_title[0], font_h5, data_6_title[1], sidebar_centre + 4, y_down + H4_SIZE + H5_SIZE*2 + 4)
        print_text(data_6_value[0], font_h5, data_6_value[1], width - 6 - (H5_SIZE/1.58)*len(f"{data_6_value[0]}"), y_down + H4_SIZE + H5_SIZE*2 + 4)

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

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * 3), 0)

                for station in stations_unowned[cell_amount * station_page_unowned:cell_amount * station_page_unowned + cell_amount]:
                    color = pygame.Color(130,130,130) if station["cost"] > euros else pygame.Color(11,128,9)
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.58)*len("PURCHASE"), y_down + 3, (H4_SIZE/1.58)*len("PURCHASE") + 2, H4_SIZE + 1)
                    pygame.draw.rect(screen, color, rect)
                    purchase_rects.append(rect)

                    color = "red" if station["cost"] > euros else pygame.Color(11,128,9)
                    h5_mult = page_tab(y_down,
                             [f'{station["name"]} - {station["code"]}', "black"],
                             ["PURCHASE", "white"],
                             ["Cost", "black"],
                             [station["cost"], color],
                             ["Train Cap", "black"],
                             [station["train_cap"], "black"],
                             ["Passenger Cap", "black"],
                             [station["passenger_cap"], "black"],
                             ["Operates to", "black"],
                             [", ".join(station["operates_to"][0:4]), "black"],
                             ["", "black"],
                             ["", "black"],
                             ["", "black"],
                             [", ".join(station["operates_to"][4:8]), "black"])
                    
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)

                # add page numbers
                station_page_unowned = page_numbers(stations_unowned, station_page_unowned, cell_amount)

                for rect in purchase_rects:
                    if button_check(rect):
                        if euros < stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["cost"]:
                            pass
                        else:
                            euros -= stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["cost"]
# [name, code, x, y, additional_costs, passive_daily_profit, passenger_cap, total_daily_profit, trains_running, train_cap, operates_to, can_operate_to, text_color, bg_color]
                            stations_owned.append({"name": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["name"],
                                                   "code": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["code"],
                                                   "x": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["x"],
                                                   "y": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["y"],
                                                   "additional costs": round(stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["cost"]/125),
                                                   "passive daily profit": 0,
                                                   "passenger_cap": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["passenger_cap"],
                                                   "total daily profit": 0,
                                                   "trains running": 0,
                                                   "train_cap": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["train_cap"],
                                                   "runs to": [],
                                                   "operates_to": stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)]["operates_to"]
                                                   })
                            stations_unowned.remove(stations_unowned[station_page_unowned*cell_amount + purchase_rects.index(rect)])

            # owned stations
            if station_menu_owned:
                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * 3), 0)
                for station in stations_owned[cell_amount * station_page_owned:cell_amount * station_page_owned + cell_amount]:
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.58)*len("PROFIT GRAPHS"), y_down + 3, (H4_SIZE/1.58)*len("PROFIT GRAPHS") + 2, H4_SIZE + 1)
                    purchase_rects.append(rect)

                    if len(station["runs to"]+station["operates_to"]) <= 4:
                        extra_line_1 = None
                        extra_line_2 = None
                        extra_line_3 = None
                        extra_line_4 = None
                    else:
                        extra_line_1 = ["", "black"]
                        extra_line_2 = [",".join(station["runs to"][4:8]), "black"]
                        extra_line_3 = ["", "black"]
                        extra_line_4 = [",".join(station["operates_to"][4:8]), "black"]
                        

                    h5_mult = page_tab(y_down,
                             [f'{station["name"]} - {station["code"]}', "black"],
                             ["PROFIT GRAPHS", " black"],
                             ["Train slots in use", "black"],
                             [f'{station["trains running"]}/{station["train_cap"]}', "black"],
                             ["Passenger Cap", "black"],
                             [station["passenger_cap"], "black"],
                             ["Runs to", "black"],
                             [",".join(station["runs to"][0:4]), "black"],
                             ["Can operate to", "black"],
                             [",".join(station["operates_to"][0:4]), "black"],
                             extra_line_1,
                             extra_line_2,
                             extra_line_3,
                             extra_line_4)
                    
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
                        line_menu_purchase_2 = False
                    elif line_menu_purchase_rects.index(rect) == 1:
                        line_menu_owned = False
                        line_menu_purchase = True
                        line_menu_purchase_2 = False

            # owned lines
            if line_menu_owned:

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * h5_mult), 0)

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
                print_text("+ Add new line", font_h4, "white", (map.get_width()+((width-map.get_width())/2))-((H4_SIZE/1.58)*len(f"+ Add new line")/2), y_down + H4_SIZE - 2)

                if button_check(rect):
                    line_menu_purchase = True
                    line_menu_owned = False

                # add page numbers
                line_page_owned = page_numbers(lines, line_page_owned, cell_amount)

            # line purchasing
            if line_menu_purchase:
                y_down = H2_SIZE * 3 + H3_SIZE * 6 - 4
                horizontal_labels(["Choose starting station" if stations_owned else "You don't own any stations!"], H3_SIZE, y_down)
                y_down += H3_SIZE * 3

                line_choose_rects = []

                cell_amount = cell_amount_calc(H4_SIZE + 6 + (H5_SIZE * 1), H3_SIZE*3)

                poss_stations = []
                for station in stations_owned:
                    if station["operates_to"] == []:
                        pass
                    else:
                        poss_stations.append(station)

                for station in poss_stations[cell_amount * line_page_purchase:cell_amount * line_page_purchase + cell_amount]:
                    color = pygame.Color(130,130,130) if station["additional costs"] > euros else pygame.Color(11,128,9)
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.58)*len("CHOOSE"), y_down + 3, (H4_SIZE/1.58)*len("CHOOSE") + 2, H4_SIZE + 1)
                    pygame.draw.rect(screen, color, rect)
                    line_choose_rects.append(rect)
                    
                    train_space_used = 0

                    for line in lines:
                        if line[0] == station["code"] or line[1] == station["code"]:
                            train_space_used += len(line[2])

                    color = "red" if station["additional costs"] > euros else pygame.Color(11,128,9)
                    h5_mult = page_tab(y_down,
                                [station["name"], "black"],
                                ["CHOOSE", "white"],
                                ["Additional Fee", "black"],
                                [station["additional costs"], color],
                                ["Train Space", "black"],
                                [station["train_cap"]-train_space_used, "black"]
                                )
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)

                # add page numbers
                if stations_owned:
                    line_page_purchase = page_numbers(poss_stations, line_page_purchase, cell_amount)

                for rect in line_choose_rects:
                    if button_check(rect):
                        if euros < poss_stations[line_choose_rects.index(rect)]["additional costs"]:
                            pass
                        else:
                            change_in_euros = poss_stations[line_choose_rects.index(rect)]["additional costs"]
                            line_menu_purchase_2 = True
                            line_menu_purchase = False
                            chosen_station = poss_stations[line_choose_rects.index(rect)]
            
            # line purchasing - part 2
            if line_menu_purchase_2:

                line_choose_rects = []

                y_down = H2_SIZE * 3 + H3_SIZE * 6 - 4
                horizontal_labels(["Choose destination station"], H3_SIZE, y_down)
                y_down += H3_SIZE * 3

                poss_stations = []
                for station in stations_owned:
                    if station["code"] in chosen_station["operates_to"]:
                        poss_stations.append(station)

                for station in poss_stations:
                    color = pygame.Color(130,130,130) if station["additional costs"] > euros else pygame.Color(11,128,9)
                    rect = pygame.Rect(width - 7 - (H4_SIZE/1.58)*len("CHOOSE"), y_down + 3, (H4_SIZE/1.58)*len("CHOOSE") + 2, H4_SIZE + 1)
                    pygame.draw.rect(screen, color, rect)

                    line_choose_rects.append(rect)
                    
                    train_space_used = 0

                    for line in lines:
                        if line[0] == station["code"] or line[1] == station["code"]:
                            train_space_used += len(line[2])

                    color = "red" if station["additional costs"] > euros else pygame.Color(11,128,9)
                    h5_mult = page_tab(y_down,
                                [station["name"], "black"],
                                ["CHOOSE", "white"],
                                ["Additional Fee", "black"],
                                [station["additional costs"], color],
                                ["Train Space", "black"],
                                [station["train_cap"]-train_space_used, "black"]
                                )
                    y_down += H4_SIZE + 6 + (H5_SIZE * h5_mult)

                for rect in line_choose_rects:
                    if button_check(rect):
                        if euros < poss_stations[line_choose_rects.index(rect)]['additional costs']:
                            pass
                        else:
                            change_in_euros += poss_stations[line_choose_rects.index(rect)]["additional costs"]
                            chosen_station_2 = poss_stations[line_choose_rects.index(rect)]

                            hypotenuse = round(math.sqrt((max(chosen_station["x"],chosen_station_2["x"]) - min(chosen_station["x"],chosen_station_2["x"]))**2 + (max(chosen_station["y"],chosen_station_2["y"]) - min(chosen_station["y"],chosen_station_2["y"]))**2)/0.9)
                            change_in_euros += hypotenuse * COST_PER_KM

                            if euros < change_in_euros:
                                pass
                            else:
                                euros -= change_in_euros
                                lines.append([chosen_station["code"], chosen_station_2["code"], [], hypotenuse])

                                line_menu_owned = True
                                line_menu_purchase_2 = False

                                stations_owned[stations_owned.index(chosen_station)]["operates_to"].remove(chosen_station_2["code"])
                                stations_owned[stations_owned.index(chosen_station)]["runs to"].append(chosen_station_2["code"])

                                stations_owned[stations_owned.index(chosen_station_2)]["operates_to"].remove(chosen_station["code"])
                                stations_owned[stations_owned.index(chosen_station_2)]["runs to"].append(chosen_station["code"])


        # upgrades menu
        if upgrade_menu:
            text = font_h1.render("upgrade", True, "black")
            screen.blit(text, (width/2,height/2))


        # drawing on map
        # draw lines
        for line in lines:
            for station in stations_owned:
                if station["code"] == line[0]:
                    start_loc = station
                if station["code"] == line[1]:
                    end_loc = station
            pygame.draw.line(screen, "yellow", (start_loc["x"]+2.5, start_loc["y"]+2.5), (end_loc["x"]+2.5, end_loc["y"]+2.5), width = 3)


        # hover lines - needs separate loop so they show BELOW the stations on the map
        for station in stations_unowned+stations_owned:
            if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11):
                for dest in station["operates_to"]:
                    for item in stations_unowned+stations_owned:
                        if dest == item["code"] and flash < 0.5:
                            pygame.draw.line(screen, pygame.Color(170,170,170), (item["x"]+2.5, item["y"]+2.5), (station["x"]+2.5, station["y"]+2.5), width = 3)


        # draw stations
        for station in stations_unowned+stations_owned:
            # on hover
            if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11):
                station_inner = pygame.Rect(station["x"]-2,station["y"]-2,9,9)

            # no hover
            else:
                station_inner = pygame.Rect(station["x"],station["y"],5,5)
            station_outer = pygame.Rect(station["x"]-5,station["y"]-5,15,15)

            if station in stations_unowned and station["cost"] > euros:
                color = pygame.Color(161, 53, 45)
            elif station in stations_unowned:
                color = pygame.Color(200,200,200)
            else:
                color = "yellow"

            # pygame.Color(11,188,9)

            pygame.draw.rect(screen, "black", station_outer)
            pygame.draw.rect(screen, color, station_inner)


        # hover labels - needs separate loop so they show ABOVE the stations on the map
        for station in stations_unowned+stations_owned:
            if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11):

                if station in stations_unowned and station["cost"] > euros:
                    bg_color = pygame.Color(161, 53, 45)
                elif station in stations_unowned:
                    bg_color = pygame.Color(170,170,170)
                else:
                    bg_color = "yellow"

                rect = pygame.Rect(station["x"] + 3 - ((H5_SIZE/1.58)*len("XXXX"))/2, station["y"] - H5_SIZE * 2, ((H5_SIZE/1.58)*len("XXXX")), H5_SIZE+2)
                pygame.draw.rect(screen, bg_color, rect)
                font_h5.set_bold(True)
                print_text(station["code"], font_h5, "black", station["x"] + 2.5 - ((H5_SIZE/1.58)*len("XXX"))/2, station["y"] - H5_SIZE * 2)
                font_h5.set_bold(False)


        # map key
        rect = pygame.Rect(10,10,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,13,9,9)
        pygame.draw.rect(screen, pygame.Color(161, 53, 45), rect)

        rect = pygame.Rect(30,10,(H4_SIZE/1.58 * len("Can't Afford"))+2,15)
        pygame.draw.rect(screen, "black", rect)
        print_text("Can't Afford", font_h4, "white", 31, 10)

        rect = pygame.Rect(10,30,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,33,9,9)
        pygame.draw.rect(screen, pygame.Color(170,170,170), rect)

        rect = pygame.Rect(30,30,(H4_SIZE/1.58 * len("Can Afford"))+2,15)
        pygame.draw.rect(screen, "black", rect)
        print_text("Can Afford", font_h4, "white", 31, 30)

        rect = pygame.Rect(10,50,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,53,9,9)
        pygame.draw.rect(screen, "yellow", rect)

        rect = pygame.Rect(30,50,(H4_SIZE/1.58 * len("Owned"))+2,15)
        pygame.draw.rect(screen, "black", rect)
        print_text("Owned", font_h4, "white", 31, 50)


    pygame.display.flip()

    # print(pygame.mouse.get_pos())
    # print(pygame.event.poll())

    if flash < 1:
        flash += 1 * dt
    else:
        flash -= 1
        
    dt = clock.tick(1000)/1000

pygame.quit()
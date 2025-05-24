import pygame
import math

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0],pygame.display.get_desktop_sizes()[0][1]))
clock = pygame.time.Clock()
dt = 0

# loops and stages
running = True
homepage = True
game = False

mouse_up_check = False
flash = 0

line_purchasing = False

flash_dests = []

# sizes
width = screen.get_width()
height = screen.get_height()

# images
map = pygame.image.load("zug_fallt_aus/north-europe-extended.png")
map = pygame.transform.scale(map, (width, (height * (map.get_width()/width)))) # adjusts map size so the width of the map is the same as the width of the screen

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
stations = [
    {"name": "Aachen",      "code": "AAC", "x": 305, "y": 485, "owned": False, "clicked": False, "cost": 250000, "passenger_cap": 15000, "train_cap": 15, "operates_to": ['BON', 'DUS', 'KOL']},
    {"name": "Augsburg",    "code": "AUG", "x": 580, "y": 685, "owned": False, "clicked": False, "cost": 600000, "passenger_cap": 40000, "train_cap": 18, "operates_to": ['MUC', 'NRB', 'ULM']},
    {"name": "Berlin",      "code": "BER", "x": 705, "y": 320, "owned": False, "clicked": False, "cost": 1200000,"passenger_cap": 100000,"train_cap": 28, "operates_to": ['DRS', 'HAM', 'POT', 'ROS']},
    {"name": "Bielefeld",   "code": "BIE", "x": 445, "y": 370, "owned": False, "clicked": False, "cost": 450000, "passenger_cap": 35000, "train_cap": 24, "operates_to": ['BRE', 'DOR', 'HAN', 'KAS', 'MUN', 'OLD']},
    {"name": "Bonn",        "code": "BON", "x": 355, "y": 490, "owned": False, "clicked": False, "cost": 320000, "passenger_cap": 25000, "train_cap": 12, "operates_to": ['AAC', 'FRA', 'KOL']},
    {"name": "Bremerhaven", "code": "BRM", "x": 440, "y": 235, "owned": False, "clicked": False, "cost": 400000, "passenger_cap": 30000, "train_cap": 20, "operates_to": ['BRE', 'HAM', 'OLD']},
    {"name": "Bremen",      "code": "BRE", "x": 450, "y": 285, "owned": False, "clicked": False, "cost": 150000, "passenger_cap": 9000,  "train_cap": 9,  "operates_to": ['BIE', 'BRM', 'HAM', 'HAN', 'OLD']},
    {"name": "Chemnitz",    "code": "CHM", "x": 680, "y": 465, "owned": False, "clicked": False, "cost": 180000, "passenger_cap": 10000, "train_cap": 6,  "operates_to": ['DRS', 'ERF']},
    {"name": "Cologne",     "code": "KOL", "x": 345, "y": 470, "owned": False, "clicked": False, "cost": 600000, "passenger_cap": 52000, "train_cap": 16, "operates_to": ['AAC', 'BON', 'DUS', 'WUP']},
    {"name": "Dortmund",    "code": "DOR", "x": 380, "y": 415, "owned": False, "clicked": False, "cost": 700000, "passenger_cap": 55000, "train_cap": 25, "operates_to": ['BIE', 'ESS', 'KAS', 'MUN', 'WUP']},
    {"name": "Dresden",     "code": "DRS", "x": 740, "y": 450, "owned": False, "clicked": False, "cost": 750000, "passenger_cap": 60000, "train_cap": 12, "operates_to": ['BER', 'CHM', 'LPZ']},
    {"name": "Dusseldorf",  "code": "DUS", "x": 340, "y": 445, "owned": False, "clicked": False, "cost": 750000, "passenger_cap": 45000, "train_cap": 16, "operates_to": ['AAC', 'ESS', 'KOL', 'WUP']},
    {"name": "Essen",       "code": "ESS", "x": 350, "y": 420, "owned": False, "clicked": False, "cost": 400000, "passenger_cap": 35000, "train_cap": 12, "operates_to": ['DOR', 'DUS', 'WUP']},
    {"name": "Erfurt",      "code": "ERF", "x": 585, "y": 470, "owned": False, "clicked": False, "cost": 320000, "passenger_cap": 28000, "train_cap": 24, "operates_to": ['CHM', 'KAS', 'LPZ', 'MAD', 'NRB', 'WRZ']},
    {"name": "Flensburg",   "code": "FLN", "x": 485, "y": 130, "owned": False, "clicked": False, "cost": 90000,  "passenger_cap": 8000,  "train_cap": 3,  "operates_to": ['KIE']},
    {"name": "Freiburg",    "code": "FRB", "x": 400, "y": 730, "owned": False, "clicked": False, "cost": 85000,  "passenger_cap": 10000, "train_cap": 3,  "operates_to": ['KAR']},
    {"name": "Frankfurt",   "code": "FRA", "x": 435, "y": 560, "owned": False, "clicked": False, "cost": 900000, "passenger_cap": 80000, "train_cap": 30, "operates_to": ['BON', 'KAS', 'MAN', 'SBR', 'WRZ']},
    {"name": "Hamburg",     "code": "HAM", "x": 510, "y": 245, "owned": False, "clicked": False, "cost": 850000, "passenger_cap": 70000, "train_cap": 30, "operates_to": ['BRM', 'BRE', 'BER', 'KIE', 'MAD', 'ROS', 'HAN']},
    {"name": "Hannover",    "code": "HAN", "x": 500, "y": 340, "owned": False, "clicked": False, "cost": 620000, "passenger_cap": 50000, "train_cap": 20, "operates_to": ['BIE', 'BRE', 'KAS', 'MAD', 'HAM']},
    {"name": "Kassel",      "code": "KAS", "x": 480, "y": 440, "owned": False, "clicked": False, "cost": 530000, "passenger_cap": 45000, "train_cap": 30, "operates_to": ['BIE', 'DOR', 'ERF', 'FRA', 'HAN', 'MAD']},
    {"name": "Karlsruhe",   "code": "KAR", "x": 430, "y": 645, "owned": False, "clicked": False, "cost": 200000, "passenger_cap": 20000, "train_cap": 12, "operates_to": ['FRB', 'MAN', 'SBR', 'STT']},
    {"name": "Kiel",        "code": "KIE", "x": 520, "y": 180, "owned": False, "clicked": False, "cost": 180000, "passenger_cap": 15000, "train_cap": 9,  "operates_to": ['FLN', 'HAM', 'ROS']},
    {"name": "Konstanz",    "code": "KON", "x": 475, "y": 755, "owned": False, "clicked": False, "cost": 85000,  "passenger_cap": 9000,  "train_cap": 6,  "operates_to": ['STT', 'ULM']},
    {"name": "Leipzig",     "code": "LPZ", "x": 655, "y": 420, "owned": False, "clicked": False, "cost": 450000, "passenger_cap": 40000, "train_cap": 16, "operates_to": ['DRS', 'ERF', 'MAD', 'POT']},
    {"name": "Magdeburg",   "code": "MAD", "x": 600, "y": 360, "owned": False, "clicked": False, "cost": 420000, "passenger_cap": 38000, "train_cap": 30, "operates_to": ['ERF', 'HAM', 'HAN', 'KAS', 'LPZ', 'POT']},
    {"name": "Mannheim",    "code": "MAN", "x": 430, "y": 595, "owned": False, "clicked": False, "cost": 300000, "passenger_cap": 28000, "train_cap": 12, "operates_to": ['FRA', 'KAR', 'STT']},
    {"name": "Munster",     "code": "MUN", "x": 395, "y": 375, "owned": False, "clicked": False, "cost": 360000, "passenger_cap": 32000, "train_cap": 9,  "operates_to": ['BIE', 'DOR', 'OLD']},
    {"name": "Munich",      "code": "MUC", "x": 640, "y": 710, "owned": False, "clicked": False, "cost": 1100000,"passenger_cap": 95000, "train_cap": 15, "operates_to": ['AUG', 'NRB', 'REG']},
    {"name": "Nuremberg",   "code": "NRB", "x": 590, "y": 590, "owned": False, "clicked": False, "cost": 510000, "passenger_cap": 44000, "train_cap": 25, "operates_to": ['AUG', 'ERF', 'MUC', 'REG', 'WRZ']},
    {"name": "Oldenburg",   "code": "OLD", "x": 405, "y": 280, "owned": False, "clicked": False, "cost": 300000, "passenger_cap": 26000, "train_cap": 16, "operates_to": ['BIE', 'BRM', 'BRE', 'MUN']},
    {"name": "Potsdam",     "code": "POT", "x": 660, "y": 340, "owned": False, "clicked": False, "cost": 200000, "passenger_cap": 22000, "train_cap": 9,  "operates_to": ['BER', 'LPZ', 'MAD']},
    {"name": "Regensburg",  "code": "REG", "x": 665, "y": 625, "owned": False, "clicked": False, "cost": 180000, "passenger_cap": 17000, "train_cap": 6,  "operates_to": ['MUC', 'NRB']},
    {"name": "Rostock",     "code": "ROS", "x": 620, "y": 185, "owned": False, "clicked": False, "cost": 220000, "passenger_cap": 20000, "train_cap": 9,  "operates_to": ['BER', 'HAM', 'KIE']},
    {"name": "Saarbrucken", "code": "SBR", "x": 355, "y": 620, "owned": False, "clicked": False, "cost": 140000, "passenger_cap": 12000, "train_cap": 6,  "operates_to": ['FRA', 'KAR']},
    {"name": "Stuttgart",   "code": "STT", "x": 475, "y": 660, "owned": False, "clicked": False, "cost": 600000, "passenger_cap": 55000, "train_cap": 25, "operates_to": ['KAR', 'KON', 'MAN', 'ULM', 'WRZ']},
    {"name": "Ulm",         "code": "ULM", "x": 525, "y": 685, "owned": False, "clicked": False, "cost": 210000, "passenger_cap": 18000, "train_cap": 9,  "operates_to": ['AUG', 'KON', 'STT']},
    {"name": "Wuppertal",   "code": "WUP", "x": 365, "y": 445, "owned": False, "clicked": False, "cost": 250000, "passenger_cap": 24000, "train_cap": 16, "operates_to": ['DOR', 'DUS', 'ESS', 'KOL']},
    {"name": "Wurzburg",    "code": "WRZ", "x": 510, "y": 575, "owned": False, "clicked": False, "cost": 300000, "passenger_cap": 27000, "train_cap": 16, "operates_to": ['ERF', 'FRA', 'NRB', 'STT']}
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
def button_check(rect):
    if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]-2) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]+1):
        pygame.event.get()
        return True


def print_text(words, font, color, x, y):
    text = font.render(str(words), True, color)
    screen.blit(text, (x, y))


def game_init():
    # draws map - map has already been adjusted to fill screen size
    screen.fill("black")
    screen.blit(map,(0,0))

    # close window button
    rect = pygame.Rect(width - 50, 10, 40, 40)
    pygame.draw.rect(screen, "red", rect)
    text = font_h2.render("X", True, "white")
    screen.blit(text, (width-41, 14))
    if button_check(rect):
        return False
    else:
        return True


def draw_lines(lines, stations):
    for line in lines:
        for station in stations:
            if station == line["start"]:
                start_loc = station
            if station == line["end"]:
                end_loc = station
        pygame.draw.line(screen, "black", (start_loc["x"]+2.5, start_loc["y"]+2.5), (end_loc["x"]+2.5, end_loc["y"]+2.5), width = 3)


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

    if game:
        running = game_init()
        
        # drawing on map
        # line flashes - lowest layer
        for station in stations:
            if line_purchasing and station["owned"] and station["clicked"]:
                start_loc = station

                for dest in station["operates_to"]:

                    for item in stations:
                        if dest == item["code"]:
                            end_loc = item

                    if flash < 0.5:
                        pygame.draw.line(screen, pygame.Color(160,160,160), (start_loc["x"]+2.5, start_loc["y"]+2.5), (end_loc["x"]+2.5, end_loc["y"]+2.5), width = 3)
            
                    rect = pygame.Rect(end_loc["x"]-5, end_loc["y"]-5, 15, 15)

                    if button_check(rect) and end_loc["owned"]:
                        lines.append({"start": start_loc,
                                      "end": end_loc,
                                      "trains": []}) 
                        line_purchasing = False

                    if button_check(rect) and not end_loc["owned"]:
                        for station in stations:
                            station["clicked"] = False
                        end_loc["clicked"] = True
                        line_purchasing = False




        # draw lines
        draw_lines(lines, stations)
        
        # draw stations
        for station in stations:
            # on hover
            if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11):
                station_inner = pygame.Rect(station["x"]-2,station["y"]-2,9,9)

            # no hover
            else:
                station_inner = pygame.Rect(station["x"]-1,station["y"]-1,7,7)
            station_outer = pygame.Rect(station["x"]-5,station["y"]-5,15,15)

            if not station["owned"] and station["cost"] > euros:
                color = pygame.Color(161, 53, 45)
            elif not station["owned"]:
                color = "white"
            else:
                color = "yellow"

            # pygame.Color(11,188,9)

            pygame.draw.rect(screen, "black", station_outer)
            pygame.draw.rect(screen, color, station_inner)


        # hover labels - will show when mouse is hovering over station icon on map
        # makes hover labels not show if currently clicked into the menu for another station
        hover = True
        for station in stations:
            if station["clicked"]:
                hover = False
            else:
                pass
        
        # if hovering allowed, show hover labels
        if hover:
            # detecting mouse pos relative to each station
            for station in stations:
                if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11):

                    # determining backing colour based on cost and players money - adds a clearer visualisation of what the player can do with station
                    if station in stations and station["cost"] > euros:
                        bg_color = pygame.Color(161, 53, 45)
                    elif station in stations:
                        bg_color = pygame.Color(210,210,210)
                    else:
                        bg_color = "yellow"

                    rect = pygame.Rect(station["x"] - 12, station["y"] - 27, 29, 17)
                    pygame.draw.rect(screen, bg_color, rect)
                    # font_h5.set_bold(True)
                    print_text(station["code"], font_h4, "black", station["x"] - 12 + (29 - (H4_SIZE/1.58)*len("XXX"))/2, station["y"] - 26)
                    font_h5.set_bold(False)

        
        # show station labels on click
        for station in stations:

            # rect checking for each station - finds which station was clicked
            rect = pygame.Rect(station["x"]-5, station["y"]-5, 15, 15)
            if button_check(rect):
                for clicked in stations:       # makes every other stations  
                    clicked["clicked"] = False # 'clicked' status False, then sets 
                station["clicked"] = True      # the correct stations status to True

            # station labels
            if station["clicked"]: 
                if station["y"] - (H5_SIZE * 5 + 30) < 20:
                    box = pygame.Vector2(station["x"] - 60, station["y"] + ((H5_SIZE * 5 + 10)-H5_SIZE * 5) + 5) # used V2 then rect
                    rect = pygame.Rect(box.x, box.y, 125, H5_SIZE * 5)                                           # for ease in communication
                else:
                    box = pygame.Vector2(station["x"] - 60, station["y"] - (H5_SIZE * 5 + 10))
                    rect = pygame.Rect(box.x, box.y, 125, H5_SIZE * 5)
                pygame.draw.rect(screen, pygame.Color(210,210,210), rect)

                # printing name details in top corners of box
                print_text(f"{station['name']}", font_h4, "black", box.x+4, box.y+2)
                font_h4.set_bold(True)
                text = font_h4.render(station['code'], True, "black")
                screen.blit(text, (box.x+rect[2]-text.get_width()-4, box.y+2))
                font_h4.set_bold(False)

                # shows purchase button for if the station is NOT owned
                if not station["owned"]:
                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+6, 117, H5_SIZE*5-(H4_SIZE+6)-4)
                    pygame.draw.rect(screen, pygame.Color(39, 143, 31), rect)

                    # printing purchase details on station
                    text = font_h5.render("PURCHASE", True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, rect[1]+2))
                    text = font_h4.render(str(station["cost"]), True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, rect[1]+4+H5_SIZE))

                    # checks for if user is clicking the purchase button or not
                    if button_check(rect):
                        station["owned"] = True
                        # add money changes etc here
                
                # shows two buttons if station is owned - purchasing a line, levelling up the station
                if station["owned"]:
                    # changing color based on whether line can be purchased or not
                    color = pygame.Color(150,150,150)
                    for dest in station["operates_to"]:
                        for item in stations:
                            if dest == item["code"] and item["owned"]:
                                color = pygame.Color(39, 143, 31)
                                # line_purchase = True
                    
                    # rect for the add line button
                    line_rect = pygame.Rect(box.x+4, box.y+H4_SIZE+6, 57, H5_SIZE*5-(H4_SIZE+6)-4)
                    pygame.draw.rect(screen, color, line_rect)
                    text = font_h4.render("ADD", True, "white")
                    screen.blit(text, ((line_rect[0]+line_rect[2]/2) - text.get_width()/2, (line_rect[1]+line_rect[3]/3) - text.get_height()/2))
                    text = font_h4.render("LINE", True, "white")
                    screen.blit(text, ((line_rect[0]+line_rect[2]/2) - text.get_width()/2, (line_rect[1]+line_rect[3]/1.5) - text.get_height()/2))

                    # rect for the level up button
                    level_rect = pygame.Rect(box.x+64, box.y+H4_SIZE+6, 57, H5_SIZE*5-(H4_SIZE+6)-4)
                    pygame.draw.rect(screen, pygame.Color(39, 143, 31), level_rect)
                    text = font_h4.render("LEVEL", True, "white")
                    screen.blit(text, ((level_rect[0]+level_rect[2]/2) - text.get_width()/2, (level_rect[1]+level_rect[3]/3) - text.get_height()/2))
                    text = font_h4.render("UP", True, "white")
                    screen.blit(text, ((level_rect[0]+level_rect[2]/2) - text.get_width()/2, (level_rect[1]+level_rect[3]/1.5) - text.get_height()/2))

                    if button_check(line_rect) and color == pygame.Color(39, 143, 31):
                        line_purchasing = True  

        # removing large station labels when clicked elsewhere
        if button_check(pygame.Rect(0,0,width,height)):
            for station in stations:
                station["clicked"] = False
            line_purchasing = False

        # map key
        # can't afford key
        rect = pygame.Rect(10,10,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,13,9,9)
        pygame.draw.rect(screen, pygame.Color(186, 24, 24), rect)
        print_text("Can't Afford", font_h4, "black", 31, 10)

        # can afford key
        rect = pygame.Rect(10,30,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,33,9,9)
        pygame.draw.rect(screen, pygame.Color(170,170,170), rect)
        print_text("Can Afford", font_h4, "black", 31, 30)

        # owned key
        rect = pygame.Rect(10,50,15,15)
        pygame.draw.rect(screen, "black", rect)
        rect = pygame.Rect(13,53,9,9)
        pygame.draw.rect(screen, "yellow", rect)
        print_text("Owned", font_h4, "black", 31, 50)


    pygame.display.flip()

    # print(pygame.mouse.get_pos())
    # print(pygame.event.poll())

    # for flashing/pulsing items such as lines in purchase phase
    if flash < 1:
        flash += 1 * dt
    else:
        flash -= 1
    
    # dt is time between frames, makes flashing smoother.
    dt = clock.tick(1000)/1000

pygame.quit()
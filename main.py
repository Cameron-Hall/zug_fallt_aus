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
map = pygame.image.load("zug_fallt_aus/north-europe-map.png")
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
    {"name": "Amsterdam",        "code": "AMS", "x": 200,  "y": 275, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 36, "operates_to": [], "runs_to": []},
    {"name": "Berlin",           "code": "BER", "x": 790,  "y": 250, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 30, "operates_to": [], "runs_to": []},
    {"name": "Prague",           "code": "PRA", "x": 860,  "y": 500, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Brussels",         "code": "BRU", "x": 160,  "y": 420, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Warsaw",           "code": "WSW", "x": 1320, "y": 280, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Brno",             "code": "BRN", "x": 1005, "y": 590, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Gdansk",           "code": "GDA", "x": 1130, "y": 65,  "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Lodz",             "code": "LOD", "x": 1225, "y": 335, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Krakow",           "code": "KRA", "x": 1240, "y": 495, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Rotterdam",        "code": "ROT", "x": 160,  "y": 320, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "The Hague",        "code": "HAG", "x": 150,  "y": 300, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Antwerp",          "code": "ANT", "x": 160,  "y": 380, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Ostrava",          "code": "OST", "x": 1110, "y": 525, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Munich",           "code": "MUC", "x": 650,  "y": 695, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Frankfurt",        "code": "FRA", "x": 445,  "y": 495, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Hamburg",          "code": "HAM", "x": 530,  "y": 155, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Luxembourg",       "code": "LUX", "x": 270,  "y": 540, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Leipzig",          "code": "LPZ", "x": 705,  "y": 370, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Koln",             "code": "KOL", "x": 330,  "y": 415, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Stuttgart",        "code": "STT", "x": 480,  "y": 620, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Dusseldorf",       "code": "DUS", "x": 320,  "y": 385, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Nuremberg",        "code": "NRB", "x": 620,  "y": 580, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Bydgoszcz",        "code": "BYD", "x": 1100, "y": 200, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Poznan",           "code": "POZ", "x": 1030, "y": 270, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Wroclaw",          "code": "WRO", "x": 1015, "y": 410, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Ghent",            "code": "GHE", "x": 105,  "y": 400, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Katowice",         "code": "KAT", "x": 1155, "y": 480, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Szczecin",         "code": "SZZ", "x": 850,  "y": 160, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Lublin",           "code": "LUB", "x": 1405, "y": 405, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Charleroi",        "code": "CHA", "x": 170,  "y": 465, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Dortmund",         "code": "DOR", "x": 365,  "y": 360, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Utrecht",          "code": "UTR", "x": 210,  "y": 300, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Eindhoven",        "code": "EIN", "x": 225,  "y": 355, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Groningen",        "code": "GRO", "x": 305,  "y": 180, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Essen",            "code": "ESS", "x": 335,  "y": 365, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Hanover",          "code": "HAN", "x": 520,  "y": 265, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Bremen",           "code": "BRE", "x": 460,  "y": 190, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Munster",          "code": "MUN", "x": 385,  "y": 310, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Bielefeld",        "code": "BIE", "x": 435,  "y": 300, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Liege",            "code": "LIE", "x": 230,  "y": 440, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Aachen",           "code": "AAC", "x": 275,  "y": 425, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Erfurt",           "code": "ERF", "x": 615,  "y": 400, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Dresden",          "code": "DRE", "x": 815,  "y": 400, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Magdeburg",        "code": "MAG", "x": 660,  "y": 300, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Kiel",             "code": "KIE", "x": 550,  "y": 70,  "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Flensburg",        "code": "FLN", "x": 500,  "y": 25,  "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Freiburg",         "code": "FRB", "x": 385,  "y": 715, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Namur",            "code": "NAM", "x": 190,  "y": 460, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Kortrijk",         "code": "KJK", "x": 75,   "y": 420, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Bruges",           "code": "BRG", "x": 70,   "y": 380, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Apeldoorn",        "code": "APL", "x": 260,  "y": 275, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Zwolle",           "code": "ZWL", "x": 270,  "y": 245, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Nijmegen",         "code": "NIJ", "x": 250,  "y": 320, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Czestochowa",      "code": "CZE", "x": 1160, "y": 425, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Bialystok",        "code": "BIA", "x": 1440, "y": 200, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Elblag",           "code": "ELB", "x": 1185, "y": 85,  "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Rzeszow",          "code": "RZS", "x": 1370, "y": 505, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Pilsen",           "code": "PIL", "x": 780,  "y": 530, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "Pardubice",        "code": "PAR", "x": 945,  "y": 505, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []},
    {"name": "",         "code": "", "x": 0, "y": 0, "shown": True, "owned": False, "clicked": False, "cost": 0, "passenger_cap": 0, "train_cap": 0, "operates_to": [], "runs_to": []}

    ]

                  # [name,          code, x,   y,   price, passenger_capacity, train_cap, can_operate_to, demand]

for station in stations:
    print(f'Code - {station["code"]}, X - {station["x"]}, Y - {station["y"]}')



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


def draw_station(station, color=None, flash=1):
    if (pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11)) or flash < 0.5:
        station_inner = pygame.Rect(station["x"]-2,station["y"]-2,9,9)

    # no hover
    else:
        station_inner = pygame.Rect(station["x"]-1,station["y"]-1,7,7)
    station_outer = pygame.Rect(station["x"]-5,station["y"]-5,15,15)

    if color != None:
        pass
    else:
        if not station["owned"] and station["cost"] > euros:
            color = pygame.Color(217, 49, 30)
        elif not station["owned"]:
            color = "white"
        else:
            color = "yellow"

    # pygame.Color(11,188,9)

    pygame.draw.rect(screen, "black", station_outer)
    pygame.draw.rect(screen, color, station_inner)



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
        screen.fill(pygame.Color(210,210,210))

        menu = font_h1.render("Zug Fallt Aus", True, "black")
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
                end_loc = start_loc
                for dest in station["operates_to"]:

                    for item in stations:
                        if item["owned"]:
                            if dest == item["code"]:
                                end_loc = item

                    if flash < 0.5:
                        pygame.draw.line(screen, pygame.Color(160,160,160), (start_loc["x"]+2.5, start_loc["y"]+2.5), (end_loc["x"]+2.5, end_loc["y"]+2.5), width = 3)
            
                    rect = pygame.Rect(end_loc["x"]-5, end_loc["y"]-5, 15, 15)

                    if button_check(rect) and end_loc["owned"]:
                        lines.append({"start": start_loc,
                                      "end": end_loc,
                                      "trains": []}) 
                        start_loc["operates_to"].remove(end_loc["code"])
                        end_loc["operates_to"].remove(start_loc["code"])

                        start_loc["runs_to"].append(end_loc["code"])
                        end_loc["runs_to"].append(start_loc["code"])

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
            if station["shown"]:
                draw_station(station)

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
                if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11) and station["shown"]:

                    # determining backing colour based on cost and players money - adds a clearer visualisation of what the player can do with station
                    if station in stations and station["cost"] > euros:
                        bg_color = pygame.Color(217, 49, 30)
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
                draw_station(station, "green")
                BOX_WIDTH = 125
                BOX_HEIGHT = H5_SIZE * 5
                # box down
                if station["y"] - (H5_SIZE * 5 + 30) < 20:
                    box = pygame.Vector2(station["x"] - 60, station["y"] + ((H5_SIZE * 5 + 10)-H5_SIZE * 5) + 5) # used V2 then rect
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 
                # box up
                else:
                    box = pygame.Vector2(station["x"] - 60, station["y"] - (H5_SIZE * 5 + 10))
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 

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

                        for dest in station["operates_to"]:
                            for item in stations:
                                if dest == item["code"]:
                                    item["shown"] = True
                        # add money changes etc here
                
                # shows two buttons if station is owned - purchasing a line, levelling up the station
                if station["owned"]:
                    line_available = False
                    # changing color based on whether line can be purchased or not
                    if station["operates_to"] != []:
                        for dest in station["operates_to"]:
                            for item in stations:
                                if dest == item["code"]:
                                    if item["owned"]:
                                        line_available = True
                    
                    color = pygame.Color(39, 143, 31) if line_available else pygame.Color(150,150,150)

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

    	# line clicking
        rect = pygame.Rect(pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10, 20,20)
        for line in lines:
            for line in lines:
                for station in stations:
                    if station == line["start"]:
                        start_loc = station
                    if station == line["end"]:
                        end_loc = station
            if pygame.Rect.clipline(rect, first_coordinate=(start_loc["x"]+2.5, start_loc["y"]+2.5), second_coordinate=(end_loc["x"]+2.5, end_loc["y"]+2.5)) and pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP):
                pygame.draw.rect(screen, "green", rect)

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
        pygame.draw.rect(screen, pygame.Color(217, 49, 30), rect)
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

        text = font_h5.render(str(pygame.mouse.get_pos()), True, "black")
        screen.blit(text, (pygame.mouse.get_pos()[0]+4, pygame.mouse.get_pos()[1]+4))


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
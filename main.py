import math
import pygame

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
extra = 0

    # tutorial things
money_clicked = False
tutorial_final = False
name_select = False
congratulations = False

username = ""

daily_euros = 0

line_purchasing = False
line_build = False
train_purchase = False

start_loc = None
end_loc = None

seconds_since_date_update = 0
day = 1
month = 1
year = 1980

menu_page = 'Lines'

flash_lines = []
income_statements = ["","","","","","","","",""]

zoom_level = 0


# start and end of day
start = 7
end = 21
trains_running = False

# sizes
width = screen.get_width()
height = screen.get_height()
ROWS = 4
ROW_HEIGHT = 60
SPACING = 8

# images
map = pygame.image.load("zug_fallt_aus/assets/north-europe-map.png")
map = pygame.transform.scale(map, (width-300, (height * (map.get_width()/(width+300))))) # adjusts map size so the width of the map is the same as the width of the screen
lock = pygame.image.load("zug_fallt_aus/assets/lock.png")
lock = pygame.transform.scale(lock, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))

# train icons
red_hill = pygame.image.load("zug_fallt_aus/assets/train_icons/red-hill.png")
red_hill = pygame.transform.scale(red_hill, (ROW_HEIGHT, ROW_HEIGHT))
great_northern = pygame.image.load("zug_fallt_aus/assets/train_icons/great-northern.png")
great_northern = pygame.transform.scale(great_northern, (ROW_HEIGHT, ROW_HEIGHT))
guangdong_star = pygame.image.load("zug_fallt_aus/assets/train_icons/guangdong-star.png")
guangdong_star = pygame.transform.scale(guangdong_star, (ROW_HEIGHT, ROW_HEIGHT))
west_network = pygame.image.load("zug_fallt_aus/assets/train_icons/west-network.png")
west_network = pygame.transform.scale(west_network, (ROW_HEIGHT, ROW_HEIGHT))
railspark_bulb = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-bulb.png")
railspark_bulb = pygame.transform.scale(railspark_bulb, (ROW_HEIGHT, ROW_HEIGHT))
railspark_ember = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-ember.png")
railspark_ember = pygame.transform.scale(railspark_ember, (ROW_HEIGHT, ROW_HEIGHT))
railspark_torrent = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-torrent.png")
railspark_torrent = pygame.transform.scale(railspark_torrent, (ROW_HEIGHT, ROW_HEIGHT))
railspark_mystic = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-mystic.png")
railspark_mystic = pygame.transform.scale(railspark_mystic, (ROW_HEIGHT, ROW_HEIGHT))
erlington_works = pygame.image.load("zug_fallt_aus/assets/train_icons/erlington-works.png")
erlington_works = pygame.transform.scale(erlington_works, (ROW_HEIGHT, ROW_HEIGHT))
erlington_works_2 = pygame.image.load("zug_fallt_aus/assets/train_icons/erlington-works-purple.png")
erlington_works_2 = pygame.transform.scale(erlington_works_2, (ROW_HEIGHT, ROW_HEIGHT))
north_star_green = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-green.png")
north_star_green = pygame.transform.scale(north_star_green, (ROW_HEIGHT, ROW_HEIGHT))
north_star_purple = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-purple.png")
north_star_purple = pygame.transform.scale(north_star_purple, (ROW_HEIGHT, ROW_HEIGHT))
north_star_red = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-red.png")
north_star_red = pygame.transform.scale(north_star_red, (ROW_HEIGHT, ROW_HEIGHT))
north_star_yellow = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-yellow.png")
north_star_yellow = pygame.transform.scale(north_star_yellow, (ROW_HEIGHT, ROW_HEIGHT))
express_orange = pygame.image.load("zug_fallt_aus/assets/train_icons/express-orange.png")
express_orange = pygame.transform.scale(express_orange, (ROW_HEIGHT, ROW_HEIGHT))
express_blue = pygame.image.load("zug_fallt_aus/assets/train_icons/express-blue.png")
express_blue = pygame.transform.scale(express_blue, (ROW_HEIGHT, ROW_HEIGHT))
express_green = pygame.image.load("zug_fallt_aus/assets/train_icons/express-green.png")
express_green = pygame.transform.scale(express_green, (ROW_HEIGHT, ROW_HEIGHT))
express_red = pygame.image.load("zug_fallt_aus/assets/train_icons/express-red.png")
express_red = pygame.transform.scale(express_red, (ROW_HEIGHT, ROW_HEIGHT))
thompson_lines_blue = pygame.image.load("zug_fallt_aus/assets/train_icons/thompson-locomotives-blue.png")
thompson_lines_blue = pygame.transform.scale(thompson_lines_blue, (ROW_HEIGHT, ROW_HEIGHT))
thompson_lines_red = pygame.image.load("zug_fallt_aus/assets/train_icons/thompson-locomotives-red.png")
thompson_lines_red = pygame.transform.scale(thompson_lines_red, (ROW_HEIGHT, ROW_HEIGHT))
royal_bronze = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-bronze.png")
royal_bronze = pygame.transform.scale(royal_bronze, (ROW_HEIGHT, ROW_HEIGHT))
royal_silver = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-silver.png")
royal_silver = pygame.transform.scale(royal_silver, (ROW_HEIGHT, ROW_HEIGHT))
royal_gold = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-gold.png")
royal_gold = pygame.transform.scale(royal_gold, (ROW_HEIGHT, ROW_HEIGHT))
royal_diamond = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-diamond.png")
royal_diamond = pygame.transform.scale(royal_diamond, (ROW_HEIGHT, ROW_HEIGHT))
peng_enterprises = pygame.image.load("zug_fallt_aus/assets/train_icons/peng-enterprises.png")
peng_enterprises = pygame.transform.scale(peng_enterprises, (ROW_HEIGHT, ROW_HEIGHT))
yangtze_monos = pygame.image.load("zug_fallt_aus/assets/train_icons/yangtze-monos.png")
yangtze_monos = pygame.transform.scale(yangtze_monos, (ROW_HEIGHT, ROW_HEIGHT))
wang_li = pygame.image.load("zug_fallt_aus/assets/train_icons/wang-li.png")
wang_li = pygame.transform.scale(wang_li, (ROW_HEIGHT, ROW_HEIGHT))
southern_star = pygame.image.load("zug_fallt_aus/assets/train_icons/southern-star.png")
southern_star = pygame.transform.scale(southern_star, (ROW_HEIGHT, ROW_HEIGHT))
eastern_power = pygame.image.load("zug_fallt_aus/assets/train_icons/eastern-power.png")
eastern_power = pygame.transform.scale(eastern_power, (ROW_HEIGHT, ROW_HEIGHT))
blue_hill = pygame.image.load("zug_fallt_aus/assets/train_icons/blue-hill.png")
blue_hill = pygame.transform.scale(blue_hill, (ROW_HEIGHT, ROW_HEIGHT))
hermann_orange = pygame.image.load("zug_fallt_aus/assets/train_icons/hermann-trainworks.png")
hermann_orange = pygame.transform.scale(hermann_orange, (ROW_HEIGHT, ROW_HEIGHT))
hermann_green = pygame.image.load("zug_fallt_aus/assets/train_icons/hermann-trainworks-2.png")
hermann_green = pygame.transform.scale(hermann_green, (ROW_HEIGHT, ROW_HEIGHT))
    
# fonts
H1_SIZE = 100
H2_SIZE = 38
H3_SIZE = 22
H4_SIZE = 17
H5_SIZE = 11
font_h1 = pygame.font.SysFont("ticketing", H1_SIZE, False, False)
font_h2_standard = pygame.font.SysFont("ticketing", H2_SIZE, False, False)
font_h2_diff = pygame.font.SysFont("bahnschrift", H2_SIZE, False, False)
font_h3 = pygame.font.SysFont("ticketing", H3_SIZE, False, False)
font_h4 = pygame.font.SysFont("ticketing", H4_SIZE, False, False)
font_h5 = pygame.font.SysFont("ticketing", H5_SIZE, False, False)

# print(pygame.font.get_fonts())

# font_h1.set_bold(True)
# font_h2.set_bold(True)
# font_h4.set_bold(True)

# colours
dark_red = 0
black = "black"
yellow = "yellow"
green = 0
dark_grey = pygame.Color(130,130,130)
grey = pygame.Color(170,170,170)
COLOR = pygame.Color(61, 72, 138)

# values
euros = 500000000
COST_PER_KM = 100

# date calc things
months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31, }

# lists
stations = [
    {'name': 'Amsterdam', 'code': 'AMS', 'x': 161, 'y': 221, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3410000, 'passenger_cap': 47000, 'operates_to': ['HAG', 'ROT', 'UTR', 'ARN', 'APL', 'ZWL'], 'runs_to': []},
    {'name': 'Berlin', 'code': 'BER', 'x': 636, 'y': 201, 'shown': False, 'owned': False, 'clicked': False, 'cost': 10000000, 'passenger_cap': 188000, 'operates_to': ['ROS', 'SZZ', 'POZ', 'MAG', 'LPZ', 'DRE'], 'runs_to': []},
    {'name': 'Prague', 'code': 'PRA', 'x': 692, 'y': 402, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4470000, 'passenger_cap': 66000, 'operates_to': ['PLS', 'DRE', 'PAR', 'LIB', 'BRN'], 'runs_to': []},
    {'name': 'Brussels', 'code': 'BRU', 'x': 129, 'y': 338, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4080000, 'passenger_cap': 59000, 'operates_to': ['GHE', 'CHA', 'NAM', 'LIE', 'ANT'], 'runs_to': []},
    {'name': 'Warsaw', 'code': 'WSW', 'x': 1062, 'y': 225, 'shown': False, 'owned': False, 'clicked': False, 'cost': 5830000, 'passenger_cap': 93000, 'operates_to': ['PLK', 'LOD', 'SID', 'BIA', 'OLZ'], 'runs_to': []},
    {'name': 'Brno', 'code': 'BRN', 'x': 809, 'y': 475, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1630000, 'passenger_cap': 19000, 'operates_to': ['PRA', 'PAR', 'OLO', 'ZLI'], 'runs_to': []},
    {'name': 'Gdansk', 'code': 'GDA', 'x': 909, 'y': 52, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1950000, 'passenger_cap': 24000, 'operates_to': ['ELB', 'GRD', 'SLP'], 'runs_to': []},
    {'name': 'Lodz', 'code': 'LOD', 'x': 986, 'y': 270, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2610000, 'passenger_cap': 34000, 'operates_to': ['PLK', 'TOR', 'POZ', 'WSW', 'LUB', 'KIL', 'CZE'], 'runs_to': []},
    {'name': 'Krakow', 'code': 'KRA', 'x': 998, 'y': 398, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3010000, 'passenger_cap': 40000, 'operates_to': ['TAR', 'KIL', 'CZE', 'KAT'], 'runs_to': []},
    {'name': 'Rotterdam', 'code': 'ROT', 'x': 129, 'y': 258, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2590000, 'passenger_cap': 33000, 'operates_to': ['HAG', 'UTR', 'AMS', 'ANT', 'EIN'], 'runs_to': []},
    {'name': 'The Hague', 'code': 'HAG', 'x': 121, 'y': 241, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2260000, 'passenger_cap': 28000, 'operates_to': ['ROT', 'AMS'], 'runs_to': []},
    {'name': 'Antwerp', 'code': 'ANT', 'x': 129, 'y': 306, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2150000, 'passenger_cap': 26000, 'operates_to': ['GHE', 'BRG', 'BRU', 'ROT', 'EIN'], 'runs_to': []},
    {'name': 'Ostrava', 'code': 'OST', 'x': 893, 'y': 422, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1270000, 'passenger_cap': 14000, 'operates_to': ['OLO', 'ZLI', 'WRO', 'KAT'], 'runs_to': []},
    {'name': 'Munich', 'code': 'MUC', 'x': 523, 'y': 559, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4910000, 'passenger_cap': 74000, 'operates_to': ['KON', 'AUG', 'ING', 'REG'], 'runs_to': []},
    {'name': 'Frankfurt', 'code': 'FRA', 'x': 362, 'y': 398, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2900000, 'passenger_cap': 38000, 'operates_to': ['WIE', 'MAN', 'WRZ', 'MAR', 'SIE'], 'runs_to': []},
    {'name': 'Hamburg', 'code': 'HAM', 'x': 428, 'y': 124, 'shown': False, 'owned': False, 'clicked': False, 'cost': 5810000, 'passenger_cap': 93000, 'operates_to': ['KIE', 'LBK', 'SCH', 'BRE', 'HAN'], 'runs_to': []},
    {'name': 'Luxembourg', 'code': 'LUX', 'x': 217, 'y': 433, 'shown': False, 'owned': False, 'clicked': False, 'cost': 530000, 'passenger_cap': 6000, 'operates_to': ['NAM', 'LIE', 'TRI', 'SAA'], 'runs_to': []},
    {'name': 'Leipzig', 'code': 'LPZ', 'x': 567, 'y': 297, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2390000, 'passenger_cap': 30000, 'operates_to': ['ERF', 'CHM', 'DRE', 'BER', 'MAG'], 'runs_to': []},
    {'name': 'Koln', 'code': 'KOL', 'x': 266, 'y': 329, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3820000, 'passenger_cap': 54000, 'operates_to': ['WUP', 'DUS', 'AAC', 'BON', 'SIE'], 'runs_to': []},
    {'name': 'Stuttgart', 'code': 'STT', 'x': 386, 'y': 498, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2500000, 'passenger_cap': 32000, 'operates_to': ['KAR', 'KON', 'ULM', 'WRZ'], 'runs_to': []},
    {'name': 'Dusseldorf', 'code': 'DUS', 'x': 262, 'y': 309, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2450000, 'passenger_cap': 31000, 'operates_to': ['DUI', 'ESS', 'WUP', 'KOL', 'AAC'], 'runs_to': []},
    {'name': 'Nuremberg', 'code': 'NRB', 'x': 500, 'y': 464, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2110000, 'passenger_cap': 26000, 'operates_to': ['WRZ', 'AUG', 'ING', 'REG', 'PLS'], 'runs_to': []},
    {'name': 'Bydgoszcz', 'code': 'BYD', 'x': 885, 'y': 161, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1490000, 'passenger_cap': 17000, 'operates_to': ['PIL', 'POZ', 'GRD', 'TOR'], 'runs_to': []},
    {'name': 'Poznan', 'code': 'POZ', 'x': 828, 'y': 217, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2210000, 'passenger_cap': 27000, 'operates_to': ['BER', 'LEZ', 'PIL', 'BYD', 'LOD'], 'runs_to': []},
    {'name': 'Wroclaw', 'code': 'WRO', 'x': 816, 'y': 329, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2620000, 'passenger_cap': 34000, 'operates_to': ['LEG', 'GLO', 'LEZ', 'PAR', 'OST', 'KAT', 'CZE'], 'runs_to': []},
    {'name': 'Ghent', 'code': 'GHE', 'x': 84, 'y': 321, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1170000, 'passenger_cap': 13000, 'operates_to': ['BRG', 'KJK', 'ANT', 'BRU'], 'runs_to': []},
    {'name': 'Katowice', 'code': 'KAT', 'x': 930, 'y': 386, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1290000, 'passenger_cap': 15000, 'operates_to': ['WRO', 'CZE', 'KRA', 'OST'], 'runs_to': []},
    {'name': 'Szczecin', 'code': 'SZZ', 'x': 684, 'y': 128, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1690000, 'passenger_cap': 20000, 'operates_to': ['ROS', 'BER', 'KSZ', 'PIL'], 'runs_to': []},
    {'name': 'Lublin', 'code': 'LUB', 'x': 1130, 'y': 324, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1470000, 'passenger_cap': 17000, 'operates_to': ['LOD', 'SID', 'KIL', 'RZS'], 'runs_to': []},
    {'name': 'Charleroi', 'code': 'CHA', 'x': 137, 'y': 372, 'shown': False, 'owned': False, 'clicked': False, 'cost': 900000, 'passenger_cap': 10000, 'operates_to': ['NAM', 'BRU', 'KJK'], 'runs_to': []},
    {'name': 'Dortmund', 'code': 'DOR', 'x': 294, 'y': 281, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2350000, 'passenger_cap': 29000, 'operates_to': ['ESS', 'MUN', 'WUP'], 'runs_to': []},
    {'name': 'Utrecht', 'code': 'UTR', 'x': 170, 'y': 241, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1580000, 'passenger_cap': 18000, 'operates_to': ['AMS', 'ROT', 'NIJ', 'ARN', 'EIN'], 'runs_to': []},
    {'name': 'Eindhoven', 'code': 'EIN', 'x': 182, 'y': 286, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1080000, 'passenger_cap': 12000, 'operates_to': ['MAA', 'ANT', 'ROT', 'UTR', 'NIJ'], 'runs_to': []},
    {'name': 'Groningen', 'code': 'GRO', 'x': 246, 'y': 144, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1040000, 'passenger_cap': 12000, 'operates_to': ['ZWL', 'OLD'], 'runs_to': []},
    {'name': 'Essen', 'code': 'ESS', 'x': 271, 'y': 286, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2330000, 'passenger_cap': 29000, 'operates_to': ['ENS', 'DUI', 'DOR', 'DUS', 'WUP'], 'runs_to': []},
    {'name': 'Hanover', 'code': 'HAN', 'x': 419, 'y': 213, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2180000, 'passenger_cap': 27000, 'operates_to': ['HAM', 'BRS', 'BRE', 'BIE', 'KAS'], 'runs_to': []},
    {'name': 'Bremen', 'code': 'BRE', 'x': 371, 'y': 153, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2290000, 'passenger_cap': 28000, 'operates_to': ['OLD', 'BIE', 'HAM', 'HAN'], 'runs_to': []},
    {'name': 'Munster', 'code': 'MUN', 'x': 311, 'y': 250, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1380000, 'passenger_cap': 16000, 'operates_to': ['OSN', 'ENS', 'BIE', 'DOR'], 'runs_to': []},
    {'name': 'Bielefeld', 'code': 'BIE', 'x': 351, 'y': 241, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1450000, 'passenger_cap': 17000, 'operates_to': ['OSN', 'MUN', 'HAN', 'BRE', 'KAS'], 'runs_to': []},
    {'name': 'Liege', 'code': 'LIE', 'x': 185, 'y': 354, 'shown': False, 'owned': False, 'clicked': False, 'cost': 880000, 'passenger_cap': 10000, 'operates_to': ['MAA', 'AAC', 'LUX', 'NAM', 'BRU', 'ANT'], 'runs_to': []},
    {'name': 'Aachen', 'code': 'AAC', 'x': 225, 'y': 343, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1110000, 'passenger_cap': 12000, 'operates_to': ['MAA', 'LIE', 'DUS', 'KOL', 'BON'], 'runs_to': []},
    {'name': 'Erfurt', 'code': 'ERF', 'x': 495, 'y': 323, 'shown': True, 'owned': False, 'clicked': False, 'cost': 950000, 'passenger_cap': 11000, 'operates_to': ['BRS', 'KAS', 'MAG', 'LPZ', 'CHM', 'WRZ'], 'runs_to': []},
    {'name': 'Dresden', 'code': 'DRE', 'x': 656, 'y': 323, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2240000, 'passenger_cap': 28000, 'operates_to': ['CHM', 'LPZ', 'LIB', 'PRA', 'BER'], 'runs_to': []},
    {'name': 'Magdeburg', 'code': 'MAG', 'x': 532, 'y': 241, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1060000, 'passenger_cap': 12000, 'operates_to': ['BRS', 'ERF', 'BER', 'LPZ'], 'runs_to': []},
    {'name': 'Kiel', 'code': 'KIE', 'x': 444, 'y': 56, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1100000, 'passenger_cap': 12000, 'operates_to': ['FLN', 'LBK', 'HAM'], 'runs_to': []},
    {'name': 'Flensburg', 'code': 'FLN', 'x': 404, 'y': 20, 'shown': False, 'owned': False, 'clicked': False, 'cost': 290000, 'passenger_cap': 4000, 'operates_to': ['KIE'], 'runs_to': []},
    {'name': 'Freiburg', 'code': 'FRB', 'x': 311, 'y': 576, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1030000, 'passenger_cap': 12000, 'operates_to': ['KON', 'KAR'], 'runs_to': []},
    {'name': 'Namur', 'code': 'NAM', 'x': 161, 'y': 371, 'shown': False, 'owned': False, 'clicked': False, 'cost': 430000, 'passenger_cap': 6000, 'operates_to': ['CHA', 'BRU', 'LIE', 'LUX'], 'runs_to': []},
    {'name': 'Kortrijk', 'code': 'KJK', 'x': 60, 'y': 338, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['BRG', 'GHE', 'CHA'], 'runs_to': []},
    {'name': 'Bruges', 'code': 'BRG', 'x': 56, 'y': 306, 'shown': False, 'owned': False, 'clicked': False, 'cost': 470000, 'passenger_cap': 6000, 'operates_to': ['ANT', 'GHE', 'KJK'], 'runs_to': []},
    {'name': 'Apeldoorn', 'code': 'APL', 'x': 209, 'y': 213, 'shown': False, 'owned': False, 'clicked': False, 'cost': 720000, 'passenger_cap': 8000, 'operates_to': ['ZWL', 'ARN', 'ENS', 'AMS'], 'runs_to': []},
    {'name': 'Zwolle', 'code': 'ZWL', 'x': 217, 'y': 189, 'shown': False, 'owned': False, 'clicked': False, 'cost': 540000, 'passenger_cap': 7000, 'operates_to': ['GRO', 'ENS', 'APL', 'AMS'], 'runs_to': []},
    {'name': 'Nijmegen', 'code': 'NIJ', 'x': 201, 'y': 258, 'shown': False, 'owned': False, 'clicked': False, 'cost': 790000, 'passenger_cap': 9000, 'operates_to': ['ARN', 'UTR', 'EIN', 'DUI'], 'runs_to': []},
    {'name': 'Czestochowa', 'code': 'CZE', 'x': 934, 'y': 343, 'shown': False, 'owned': False, 'clicked': False, 'cost': 980000, 'passenger_cap': 11000, 'operates_to': ['WRO', 'KAT', 'KRA', 'KIL', 'LOD'], 'runs_to': []},
    {'name': 'Bialystok', 'code': 'BIA', 'x': 1161, 'y': 161, 'shown': True, 'owned': False, 'clicked': False, 'cost': 1310000, 'passenger_cap': 15000, 'operates_to': ['OLZ', 'WSW', 'SID'], 'runs_to': []},
    {'name': 'Elblag', 'code': 'ELB', 'x': 953, 'y': 68, 'shown': False, 'owned': False, 'clicked': False, 'cost': 480000, 'passenger_cap': 6000, 'operates_to': ['GDA', 'OLZ'], 'runs_to': []},
    {'name': 'Rzeszow', 'code': 'RZS', 'x': 1104, 'y': 404, 'shown': False, 'owned': False, 'clicked': False, 'cost': 870000, 'passenger_cap': 10000, 'operates_to': ['TAR', 'KIL', 'LUB'], 'runs_to': []},
    {'name': 'Pilsen', 'code': 'PLS', 'x': 627, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 770000, 'passenger_cap': 9000, 'operates_to': ['NRB', 'REG', 'CHM', 'PRA'], 'runs_to': []},
    {'name': 'Pardubice', 'code': 'PAR', 'x': 761, 'y': 404, 'shown': False, 'owned': False, 'clicked': False, 'cost': 300000, 'passenger_cap': 5000, 'operates_to': ['LIB', 'PRA', 'OLO', 'BRN', 'WRO'], 'runs_to': []},
    {'name': 'Wurzburg', 'code': 'WRZ', 'x': 439, 'y': 429, 'shown': False, 'owned': False, 'clicked': False, 'cost': 530000, 'passenger_cap': 6000, 'operates_to': ['FRA', 'MAN', 'NRB', 'STT', 'ULM', 'ERF'], 'runs_to': []},
    {'name': 'Mannheim', 'code': 'MAN', 'x': 345, 'y': 445, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1350000, 'passenger_cap': 15000, 'operates_to': ['SAA', 'KAR', 'WIE', 'FRA', 'WRZ'], 'runs_to': []},
    {'name': 'Kassel', 'code': 'KAS', 'x': 414, 'y': 293, 'shown': False, 'owned': False, 'clicked': False, 'cost': 900000, 'passenger_cap': 10000, 'operates_to': ['BIE', 'HAN', 'BRS', 'ERF', 'MAR'], 'runs_to': []},
    {'name': 'Chemnitz', 'code': 'CHM', 'x': 590, 'y': 334, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1100000, 'passenger_cap': 12000, 'operates_to': ['LPZ', 'DRE', 'PLS', 'ERF'], 'runs_to': []},
    {'name': 'Oldenburg', 'code': 'OLD', 'x': 332, 'y': 144, 'shown': False, 'owned': False, 'clicked': False, 'cost': 750000, 'passenger_cap': 9000, 'operates_to': ['GRO', 'BRE', 'OSN'], 'runs_to': []},
    {'name': 'Rostock', 'code': 'ROS', 'x': 536, 'y': 76, 'shown': False, 'owned': False, 'clicked': False, 'cost': 930000, 'passenger_cap': 10000, 'operates_to': ['LBK', 'SCH', 'BER', 'SZZ'], 'runs_to': []},
    {'name': 'Lubeck', 'code': 'LBK', 'x': 461, 'y': 89, 'shown': False, 'owned': False, 'clicked': False, 'cost': 960000, 'passenger_cap': 11000, 'operates_to': ['KIE', 'HAM', 'SCH', 'ROS'], 'runs_to': []},
    {'name': 'Slupsk', 'code': 'SLP', 'x': 825, 'y': 40, 'shown': False, 'owned': False, 'clicked': False, 'cost': 310000, 'passenger_cap': 5000, 'operates_to': ['KSZ', 'GDA'], 'runs_to': []},
    {'name': 'Koszalin', 'code': 'KSZ', 'x': 786, 'y': 64, 'shown': False, 'owned': False, 'clicked': False, 'cost': 410000, 'passenger_cap': 5000, 'operates_to': ['SLP', 'SZZ', 'PIL'], 'runs_to': []},
    {'name': 'Olsztyn', 'code': 'OLZ', 'x': 1014, 'y': 105, 'shown': False, 'owned': False, 'clicked': False, 'cost': 760000, 'passenger_cap': 9000, 'operates_to': ['ELB', 'BIA', 'GRB', 'WSW'], 'runs_to': []},
    {'name': 'Kielce', 'code': 'KIL', 'x': 1022, 'y': 343, 'shown': False, 'owned': False, 'clicked': False, 'cost': 860000, 'passenger_cap': 10000, 'operates_to': ['LOD', 'CZE', 'KRA', 'RZS', 'LUB'], 'runs_to': []},
    {'name': 'Plock', 'code': 'PLK', 'x': 994, 'y': 208, 'shown': False, 'owned': False, 'clicked': False, 'cost': 480000, 'passenger_cap': 6000, 'operates_to': ['TOR', 'LOD', 'WSW'], 'runs_to': []},
    {'name': 'Braunschweig', 'code': 'BRS', 'x': 462, 'y': 221, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1090000, 'passenger_cap': 12000, 'operates_to': ['HAN', 'KAS', 'ERF', 'MAG'], 'runs_to': []},
    {'name': 'Ulm', 'code': 'ULM', 'x': 431, 'y': 519, 'shown': False, 'owned': False, 'clicked': False, 'cost': 520000, 'passenger_cap': 6000, 'operates_to': ['STT', 'KON', 'AUG', 'WRZ'], 'runs_to': []},
    {'name': 'Konstanz', 'code': 'KON', 'x': 382, 'y': 591, 'shown': False, 'owned': False, 'clicked': False, 'cost': 270000, 'passenger_cap': 4000, 'operates_to': ['FRB', 'MUC', 'STT', 'ULM'], 'runs_to': []},
    {'name': 'Augsburg', 'code': 'AUG', 'x': 470, 'y': 523, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1320000, 'passenger_cap': 15000, 'operates_to': ['NRB', 'ING', 'MUC', 'ULM'], 'runs_to': []},
    {'name': 'Regensburg', 'code': 'REG', 'x': 551, 'y': 491, 'shown': False, 'owned': False, 'clicked': False, 'cost': 660000, 'passenger_cap': 8000, 'operates_to': ['PLS', 'NRB', 'ING', 'MUC'], 'runs_to': []},
    {'name': 'Ingolstadt', 'code': 'ING', 'x': 510, 'y': 512, 'shown': False, 'owned': False, 'clicked': False, 'cost': 590000, 'passenger_cap': 7000, 'operates_to': ['NRB', 'REG', 'AUG', 'MUC'], 'runs_to': []},
    {'name': 'Koblenz', 'code': 'KOB', 'x': 297, 'y': 378, 'shown': False, 'owned': False, 'clicked': False, 'cost': 450000, 'passenger_cap': 6000, 'operates_to': ['BON', 'WIE', 'TRI', 'SIE'], 'runs_to': []},
    {'name': 'Olomouc', 'code': 'OLO', 'x': 845, 'y': 439, 'shown': False, 'owned': False, 'clicked': False, 'cost': 370000, 'passenger_cap': 5000, 'operates_to': ['PAR', 'BRN', 'ZLI', 'OST'], 'runs_to': []},
    {'name': 'Zlin', 'code': 'ZLI', 'x': 861, 'y': 470, 'shown': False, 'owned': False, 'clicked': False, 'cost': 180000, 'passenger_cap': 4000, 'operates_to': ['OLO', 'OST', 'BRN'], 'runs_to': []},
    {'name': 'Pila', 'code': 'PIL', 'x': 813, 'y': 153, 'shown': False, 'owned': False, 'clicked': False, 'cost': 180000, 'passenger_cap': 4000, 'operates_to': ['SZZ', 'KSZ', 'BYD', 'POZ'], 'runs_to': []},
    {'name': 'Glogow', 'code': 'GLO', 'x': 764, 'y': 282, 'shown': False, 'owned': False, 'clicked': False, 'cost': 120000, 'passenger_cap': 3000, 'operates_to': ['LEZ', 'LEG', 'WRO'], 'runs_to': []},
    {'name': 'Karlsruhe', 'code': 'KAR', 'x': 337, 'y': 487, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1370000, 'passenger_cap': 16000, 'operates_to': ['SAA', 'MAN', 'STT', 'FRB'], 'runs_to': []},
    {'name': 'Saarbrucken', 'code': 'SAA', 'x': 257, 'y': 462, 'shown': False, 'owned': False, 'clicked': False, 'cost': 790000, 'passenger_cap': 9000, 'operates_to': ['LUX', 'TRI', 'MAN', 'KAR'], 'runs_to': []},
    {'name': 'Trier', 'code': 'TRI', 'x': 244, 'y': 417, 'shown': False, 'owned': False, 'clicked': False, 'cost': 430000, 'passenger_cap': 6000, 'operates_to': ['LUX', 'SAA', 'KOB'], 'runs_to': []},
    {'name': 'Wiesbaden', 'code': 'WIE', 'x': 332, 'y': 398, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1230000, 'passenger_cap': 14000, 'operates_to': ['FRA', 'KOB', 'MAN'], 'runs_to': []},
    {'name': 'Bonn', 'code': 'BON', 'x': 274, 'y': 354, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1430000, 'passenger_cap': 16000, 'operates_to': ['KOB', 'AAC', 'KOL', 'SIE'], 'runs_to': []},
    {'name': 'Wuppertal', 'code': 'WUP', 'x': 290, 'y': 314, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1530000, 'passenger_cap': 18000, 'operates_to': ['DOR', 'ESS', 'DUS', 'KOL', 'SIE'], 'runs_to': []},
    {'name': 'Duisburg', 'code': 'DUI', 'x': 241, 'y': 282, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2040000, 'passenger_cap': 25000, 'operates_to': ['ESS', 'DUS', 'NIJ', 'EIN'], 'runs_to': []},
    {'name': 'Marburg', 'code': 'MAR', 'x': 377, 'y': 341, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['KAS', 'SIE', 'FRA'], 'runs_to': []},
    {'name': 'Schwerin', 'code': 'SCH', 'x': 510, 'y': 113, 'shown': False, 'owned': False, 'clicked': False, 'cost': 340000, 'passenger_cap': 5000, 'operates_to': ['ROS', 'LBK', 'HAM'], 'runs_to': []},
    {'name': 'Torun', 'code': 'TOR', 'x': 909, 'y': 173, 'shown': False, 'owned': False, 'clicked': False, 'cost': 880000, 'passenger_cap': 10000, 'operates_to': ['BYD', 'GBD', 'PLK', 'LOD'], 'runs_to': []},
    {'name': 'Leszno', 'code': 'LEZ', 'x': 786, 'y': 262, 'shown': False, 'owned': False, 'clicked': False, 'cost': 50000, 'passenger_cap': 3000, 'operates_to': ['GLO', 'WRO', 'POZ'], 'runs_to': []},
    {'name': 'Siegen', 'code': 'SIE', 'x': 326, 'y': 339, 'shown': False, 'owned': False, 'clicked': False, 'cost': 380000, 'passenger_cap': 5000, 'operates_to': ['WUP', 'KOL', 'MAR', 'FRA', 'BON', 'KOB'], 'runs_to': []},
    {'name': 'Liberec', 'code': 'LIB', 'x': 723, 'y': 343, 'shown': False, 'owned': False, 'clicked': False, 'cost': 390000, 'passenger_cap': 5000, 'operates_to': ['DRE', 'PRA', 'PAR', 'LEG'], 'runs_to': []},
    {'name': 'Legnica', 'code': 'LEG', 'x': 764, 'y': 318, 'shown': False, 'owned': False, 'clicked': False, 'cost': 360000, 'passenger_cap': 5000, 'operates_to': ['GLO', 'WRO', 'LIB'], 'runs_to': []},
    {'name': 'Grudziadz', 'code': 'GRD', 'x': 916, 'y': 133, 'shown': False, 'owned': False, 'clicked': False, 'cost': 330000, 'passenger_cap': 5000, 'operates_to': ['GDA', 'OLZ', 'BYD', 'TOR'], 'runs_to': []},
    {'name': 'Siedlce', 'code': 'SID', 'x': 1127, 'y': 229, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['WSW', 'BIA', 'LUB'], 'runs_to': []},
    {'name': 'Tarnow', 'code': 'TAR', 'x': 1051, 'y': 408, 'shown': False, 'owned': False, 'clicked': False, 'cost': 420000, 'passenger_cap': 5000, 'operates_to': ['KRA', 'RZS'], 'runs_to': []},
    {'name': 'Arnhem', 'code': 'ARN', 'x': 201, 'y': 233, 'shown': False, 'owned': False, 'clicked': False, 'cost': 720000, 'passenger_cap': 8000, 'operates_to': ['UTR', 'NIJ', 'ENS', 'ZWL', 'AMS'], 'runs_to': []},
    {'name': 'Maastricht', 'code': 'MAA', 'x': 201, 'y': 329, 'shown': False, 'owned': False, 'clicked': False, 'cost': 490000, 'passenger_cap': 6000, 'operates_to': ['AAC', 'LIE', 'EIN'], 'runs_to': []},
    {'name': 'Osnabruck', 'code': 'OSN', 'x': 326, 'y': 217, 'shown': False, 'owned': False, 'clicked': False, 'cost': 750000, 'passenger_cap': 8000, 'operates_to': ['OLD', 'BIE', 'MUN', 'ENS'], 'runs_to': []},
    {'name': 'Enschede', 'code': 'ENS', 'x': 258, 'y': 213, 'shown': False, 'owned': False, 'clicked': False, 'cost': 690000, 'passenger_cap': 8000, 'operates_to': ['ZWL', 'APL', 'ARN', 'OSN', 'MUN', 'ESS'], 'runs_to': []}
]

trains = [
{'make': 'Express', 'model': 'DT-4', 'icon': express_red, 'shown': False, 'unlocked': False, 'cost': 300000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 100, 'profit_per_person_per_km': 0.025, 'desc': 'The most basic train of the lot. Small yet reliable for transporting your first passengers, or for serving new connections.', 'level': 0},
{'make': 'Express', 'model': 'DT-5A', 'icon': express_orange, 'shown': False, 'unlocked': False, 'cost': 340000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 100, 'profit_per_person_per_km': 0.025, 'level': 0},
{'make': 'Express', 'model': 'DT-5B', 'icon': express_green, 'shown': False, 'unlocked': False, 'cost': 350000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 110, 'profit_per_person_per_km': 0.028, 'level': 0},
{'make': 'Express', 'model': 'DT-6', 'icon': express_blue, 'shown': False, 'unlocked': False, 'cost': 400000, 'train_type': 'Diesel', 'capacity': 300, 'speed': 112, 'profit_per_person_per_km': 0.03, 'level': 0},
{'make': 'RailSpark', 'model': 'Ember', 'icon': railspark_ember, 'shown': False, 'unlocked': False, 'cost': 650000, 'train_type': 'Diesel', 'capacity': 400, 'speed': 105, 'profit_per_person_per_km': 0.025, 'level': 0},
{'make': 'RailSpark', 'model': 'Torrent', 'icon': railspark_torrent, 'shown': False, 'unlocked': False, 'cost': 600000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 160, 'profit_per_person_per_km': 0.04, 'level': 0},
{'make': 'RailSpark', 'model': 'Bulb', 'icon': railspark_bulb, 'shown': False, 'unlocked': False, 'cost': 200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 140, 'profit_per_person_per_km': 0.05, 'level': 0},
{'make': 'RailSpark', 'model': 'Mystic', 'icon': railspark_mystic, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 375, 'speed': 180, 'profit_per_person_per_km': 0.06, 'level': 0},
{'make': 'North Star', 'model': 'Ursa', 'icon': north_star_green, 'shown': False, 'unlocked': False, 'cost': 500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 80, 'profit_per_person_per_km': 0.02, 'level': 0},
{'make': 'North Star', 'model': 'Maris', 'icon': north_star_red, 'shown': False, 'unlocked': False, 'cost': 320000, 'train_type': 'Electric', 'capacity': 200, 'speed': 120, 'profit_per_person_per_km': 0.03, 'level': 0},
{'make': 'North Star', 'model': 'Polaris', 'icon': north_star_purple, 'shown': False, 'unlocked': False, 'cost': 1600000, 'train_type': 'Electric', 'capacity': 400, 'speed': 134, 'profit_per_person_per_km': 0.045, 'level': 0},
{'make': 'North Star', 'model': 'Polaris-2', 'icon': north_star_yellow, 'shown': False, 'unlocked': False, 'cost': 2150000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.045, 'level': 0},
{'make': 'Thompson Lines', 'model': 'AC-76', 'icon': thompson_lines_red, 'shown': False, 'unlocked': False, 'cost': 150000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 110, 'profit_per_person_per_km': 0.02, 'level': 0},
{'make': 'Thompson Lines', 'model': 'AC-77', 'icon': thompson_lines_blue, 'shown': False, 'unlocked': False, 'cost': 160000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 120, 'profit_per_person_per_km': 0.02, 'level': 0},
{'make': 'Erlington Works', 'model': 'Jubilee-A', 'icon': erlington_works, 'shown': False, 'unlocked': False, 'cost': 900000, 'train_type': 'Electric', 'capacity': 50, 'speed': 50, 'profit_per_person_per_km': 1.0, 'level': 0},
{'make': 'Erlington Works', 'model': 'Jubilee-B', 'icon': erlington_works_2, 'shown': False, 'unlocked': False, 'cost': 1100000, 'train_type': 'Electric', 'capacity': 75, 'speed': 75, 'profit_per_person_per_km': 0.5, 'level': 0},
{'make': 'Royal', 'model': 'Bronze', 'icon': royal_bronze, 'shown': False, 'unlocked': False, 'cost': 3620000, 'train_type': 'Electric', 'capacity': 200, 'speed': 150, 'profit_per_person_per_km': 0.2, 'level': 0},
{'make': 'Royal', 'model': 'Silver', 'icon': royal_silver, 'shown': False, 'unlocked': False, 'cost': 4200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 170, 'profit_per_person_per_km': 0.5, 'level': 0},
{'make': 'Royal', 'model': 'Gold', 'icon': royal_gold, 'shown': False, 'unlocked': False, 'cost': 5000000, 'train_type': 'Electric', 'capacity': 50, 'speed': 185, 'profit_per_person_per_km': 1.0, 'level': 0},
{'make': 'Royal', 'model': 'Diamond', 'icon': royal_diamond, 'shown': False, 'unlocked': False, 'cost': 9900000, 'train_type': 'MagLev', 'capacity': 20, 'speed': 200, 'profit_per_person_per_km': 4.0, 'level': 0},
{'make': 'Mr Peng Enterprises', 'model': 'Peng-01', 'icon': peng_enterprises, 'shown': False, 'unlocked': False, 'cost': 43000000, 'train_type': 'Electric', 'capacity': 500, 'speed': 200, 'profit_per_person_per_km': 0.055, 'level': 0},
{'make': 'Guangdong Star', 'model': 'Star of China', 'icon': guangdong_star, 'shown': False, 'unlocked': False, 'cost': 850000000, 'train_type': 'MagLev', 'capacity': 800, 'speed': 250, 'profit_per_person_per_km': 0.6, 'level': 0},
{'make': 'Wang Li', 'model': 'Wang-01', 'icon': wang_li, 'shown': False, 'unlocked': False, 'cost': 18000000, 'train_type': 'Diesel', 'capacity': 1200, 'speed': 150, 'profit_per_person_per_km': 0.02, 'level': 0},
{'make': 'Yangtze Monos', 'model': 'Current', 'icon': yangtze_monos, 'shown': False, 'unlocked': False, 'cost': 11500000, 'train_type': 'Monorail', 'capacity': 100, 'speed': 120, 'profit_per_person_per_km': 0.2, 'level': 0},
{'make': 'West Network', 'model': 'Bullet', 'icon': west_network, 'shown': False, 'unlocked': False, 'cost': 600000000, 'train_type': 'MagLev', 'capacity': 600, 'speed': 300, 'profit_per_person_per_km': 0.4, 'level': 0},
{'make': 'Great Northern', 'model': 'Piercer', 'icon': great_northern, 'shown': False, 'unlocked': False, 'cost': 12250000, 'train_type': 'Electric', 'capacity': 300, 'speed': 180, 'profit_per_person_per_km': 0.05, 'level': 0},
{'make': 'Southern Star', 'model': 'Solo', 'icon': southern_star, 'shown': False, 'unlocked': False, 'cost': 24000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 200, 'profit_per_person_per_km': 0.2, 'level': 0},
{'make': 'Eastern Power', 'model': 'Taurus', 'icon': eastern_power, 'shown': False, 'unlocked': False, 'cost': 9000000, 'train_type': 'Diesel', 'capacity': 900, 'speed': 100, 'profit_per_person_per_km': 0.04, 'level': 0},
{'make': 'Red Hill', 'model': 'Baron', 'icon': red_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.03, 'level': 0},
{'make': 'Blue Hill', 'model': 'Ocean', 'icon': blue_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.03, 'level': 0},
{'make': 'Hermann Monorails', 'model': 'HM-11W', 'icon': hermann_green, 'shown': False, 'unlocked': False, 'cost': 11000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 140, 'profit_per_person_per_km': 0.2, 'level': 0},
{'make': 'Hermann Monorails', 'model': 'HM-12W', 'icon': hermann_orange, 'shown': False, 'unlocked': False, 'cost': 12000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 150, 'profit_per_person_per_km': 0.2, 'level': 0},
]

owned_trains = []

lines = [
    # Reds
    {"class": "Red", "name": "Red-1", "color": pygame.Color(255, 102, 102),  "shown": True, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-2", "color": pygame.Color(255, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-3", "color": pygame.Color(204, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-4", "color": pygame.Color(153, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Oranges
    {"class": "Orange", "name": "Orange-1", "color": pygame.Color(255, 200, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-2", "color": pygame.Color(255, 150, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-3", "color": pygame.Color(255, 100, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-4", "color": pygame.Color(255, 50, 0),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Yellows
    {"class": "Yellow", "name": "Yellow-1", "color": pygame.Color(255, 255, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-2", "color": pygame.Color(210, 210, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-3", "color": pygame.Color(150, 150, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-4", "color": pygame.Color(70, 70, 0),   "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Greens
    {"class": "Green", "name": "Green-1", "color": pygame.Color(0, 255, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-2", "color": pygame.Color(0, 190, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-3", "color": pygame.Color(0, 120, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-4", "color": pygame.Color(0, 70, 0),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Light Blues
    {"class": "Light Blue", "name": "Blue-L1", "color": pygame.Color(80, 225, 225), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L2", "color": pygame.Color(0, 190, 190),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L3", "color": pygame.Color(0, 140, 140),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L4", "color": pygame.Color(0, 70, 70),    "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Blues
    {"class": "Blue", "name": "Blue-D1", "color": pygame.Color(80, 80, 255), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D2", "color": pygame.Color(0, 0, 255),   "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D3", "color": pygame.Color(0, 0, 110),   "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D4", "color": pygame.Color(0, 0, 40),    "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Purples
    {"class": "Purple", "name": "Purple-1", "color": pygame.Color(150, 75, 150), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-2", "color": pygame.Color(160, 0, 160),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-3", "color": pygame.Color(110, 0, 110),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-4", "color": pygame.Color(50, 0, 50),    "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Pinks
    {"class": "Gray", "name": "Gray-1", "color": pygame.Color(180, 180, 180), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-2", "color": pygame.Color(130, 130, 130), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-3", "color": pygame.Color(80, 80, 80),    "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-4", "color": pygame.Color(50, 50, 50),    "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Browns
    {"class": "Brown", "name": "Brown-1", "color": pygame.Color(181, 101, 29), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-2", "color": pygame.Color(160, 82, 45),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-3", "color": pygame.Color(139, 69, 19),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-4", "color": pygame.Color(101, 67, 33),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0}

]

upgrades = []

# classes
class Train:
    def __init__(self, model, line, cap, ppkm, speed):
        self.model = model
        self.line = line
        self.cap = cap
        self.ppkm = ppkm
        self.speed = speed
        self.last_hr = 0
        self.last_min = 0
        self.next_hr = 0
        self.next_min = 0
        self.trip_hr = 0
        self.trip_min = 0


# functions
def button_check(rect):
    if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]-2) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]+1):
        pygame.event.get()
        return True
  
 
def print_text(words, font, color, x, y):
    text = font.render(str(words), True, color)
    screen.blit(text, (x, y))


def draw_lines(lines, stations):
    for line in lines:
        if line["stations"] != [] and item["finished"]:
            for code in range(len(line["stations"])-1):
                for station in stations:
                    if station["code"] == line["stations"][code]:
                        start_loc = station
                    if station["code"] == line["stations"][code+1]:
                        end_loc = station

                pygame.draw.line(screen, line["color"], (start_loc["x"]+2.5, start_loc["y"]+2.5), (end_loc["x"]+2.5, end_loc["y"]+2.5), width = 5)
        

def draw_station(station, color=None, flash=1):
    if (pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+10) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+10)) or flash < 0.5:
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


def tips(tip_line_1, tip_line_2, tip_line_3, font_1, font_2, font_3):
    rect = pygame.Rect(350,800,520, height-800)
    pygame.draw.rect(screen, pygame.Color(210,210,210), rect)
    text = font_1.render(tip_line_1, True, "black")
    screen.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]/4-text.get_height()/2))
    text = font_2.render(tip_line_2, True, "black")
    screen.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]/2-text.get_height()/2))
    text = font_3.render(tip_line_3, True, "black")
    screen.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]*3/4-text.get_height()/2))


def name_change(username):
    name_chosen = False
    for event in pygame.event.get(exclude=pygame.MOUSEBUTTONUP):
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_BACKSPACE]:
                username = username[:-1]
            elif key[pygame.K_RETURN]:
                name_chosen = True
            elif event.unicode:
                username += event.unicode

    return [username, name_chosen]


def e_euros(euros):
    if euros >= 100000000000:
        e_number = str(euros).count("0")
    else:
        e_number = None

    if e_number is not None:
        return f'€{str(euros)[0]}.{str(euros)[1:4]}e{e_number}'
    else:
        return f"€{'{:,}'.format(euros)}"


# clock functions
def circle_point(center, radius, theta):
    """Calculates the location of a point of a circle given the circle's
    center and radius as well as the point's angle from the xx' axis"""

    return (center[0] + radius * math.cos(theta),
            center[1] + radius * math.sin(theta))

def line_at_angle(screen, center, radius, theta, color, width):
    """Draws a line from a center towards an angle. The angle is given in
    radians."""
    point = circle_point(center, radius, theta)
    pygame.draw.line(screen, color, center, point, width)

def get_angle(unit, total):
    """Calculates the angle, in radians, corresponding to a portion of the clock
    counting using the given units up to a given total and starting from 12
    o'clock and moving clock-wise."""
    return 2 * math.pi * unit / total - math.pi / 2


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
        screen.fill(pygame.Color(61, 72, 138))

        text = font_h1.render("Zug Fallt Aus", True, "white")
        screen.blit(text,((width/2)-(text.get_width()/2),(height/2)-(text.get_height()/2)-height*0.1))
        anywhere = font_h2_standard.render("Click anywhere to continue", True, "white")
        screen.blit(anywhere,((width/2)-(anywhere.get_width()/2),(height/2)-(anywhere.get_height()/2)+height*0.1))
        rect = pygame.Rect(0, 0, width, height)
        
        if button_check(rect):
            homepage = False
            game = True

    if game:
        # draws map - map has already been adjusted to fill screen size
        screen.fill(pygame.Color(254, 254, 233))
        screen.blit(map,(0,0))

        # tips
        tips("","","",font_h5,font_h5,font_h5)

        # bottom bar
        rect = pygame.Rect(0, height-200, width, 200)
        pygame.draw.rect(screen, COLOR, rect)

        # left side menus
        # money
        rect = pygame.Rect(0, height - 200, 450, 200)
        pygame.draw.rect(screen, pygame.Color(210,210,210), rect)

        if euros >= 100000000000:
            e_number = str(euros).count("0")
        else:
            e_number = None

        if e_number is not None:
            euros_print = f'{str(euros)[0]}.{str(euros)[1:4]}e{e_number}'
        else:
            euros_print = '{:,}'.format(euros)
        

        rect = pygame.Rect(0, height - 200, 450, 60)
        pygame.draw.rect(screen, "black", rect)
        text = font_h2_diff.render(e_euros(euros), True, "yellow")
        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/2)-(text.get_height()/2)+2))

        # clock
        # background
        rect = pygame.Rect(0, height - 140, 140, 140)
        pygame.draw.rect(screen, pygame.Color(128, 50, 1), rect)
        # clock face
        pygame.draw.circle(screen, "black", (70, height-70), 61)
        pygame.draw.circle(screen, "white", (70, height-70), 58)
        # clock hands
        now = pygame.Vector2(math.floor(seconds_since_date_update), math.floor((seconds_since_date_update%1)*60))
        hour_theta = get_angle(now.x+1.0*now.y/60, 12)
        # minute_theta = get_angle(now.y, 60)
        line_at_angle(screen, (70, height-70), 58*0.7, hour_theta, "black", 5)
        # line_at_angle(screen, (70, height-70), 58*0.9, minute_theta, "black", 3)
        pygame.draw.circle(screen, "black", (70, height-70), 5) 
        # service running markers
        FROM_EDGE = 14
        rect = pygame.Rect(FROM_EDGE, (height-140)+FROM_EDGE, 140-FROM_EDGE*2, 140-FROM_EDGE*2)
        pygame.draw.arc(screen, "green", rect, get_angle(18-12, 12), get_angle(18-7,12), width = 3)
        FROM_EDGE = 20
        rect = pygame.Rect(FROM_EDGE, (height-140)+FROM_EDGE, 140-FROM_EDGE*2, 140-FROM_EDGE*2)
        pygame.draw.arc(screen, "green", rect, get_angle(18-21, 12), get_angle(18-12,12), width = 3)
        # draw markings
        for hour in range(0, 12):
            theta = get_angle(hour, 12)
            p1 = circle_point((70, height-70), 58 - 5, theta)
            p2 = circle_point((70, height-70), 58, theta)
            pygame.draw.line(screen, "black", p1, p2, 3)

        hour = now.x
        minute = now.y

        # date info
        text = font_h4.render(list(months.keys())[month-1], True, "black")
        screen.blit(text, (30, height-70-text.get_height()/2))
        text = font_h4.render(str(day), True, "black")
        screen.blit(text, (110-text.get_width(), height-70-text.get_height()/2))
        text = font_h4.render(str(year), True, "black")
        screen.blit(text, (70-text.get_width()/2, height-50-text.get_height()/2))

        # income box
        rect = pygame.Rect(140, height-140, 310, 140)
        pygame.draw.rect(screen, pygame.Color(232, 170, 0), rect)
        rect = pygame.Rect(145, height-135, 300, 130)
        pygame.draw.rect(screen, "black", rect)
        x_across = 145
        y_down = height-135
        for statement in range(1,8):
            text = font_h4.render(income_statements[-statement], True, "yellow")
            screen.blit(text, (x_across+2, y_down+2))
            y_down += H4_SIZE+1

           
        # right side menus
        # mini menu labels
        title_rects = []
        titles = ["Lines", "Trains", "Upgrades"]
        y_down = 20
        TAB_HEIGHT = 110
        for title in titles:
            if menu_page == title:
                color = pygame.Color(61, 72, 138)
                extra_add = 10
            else:
                color = pygame.Color(88, 103, 199)
                extra_add = 0

            text = font_h3.render(title, True, "white")
            text = pygame.transform.rotate(text, 90)
            rect = pygame.Rect(map.get_width()-20-extra_add, y_down, 40+extra_add, TAB_HEIGHT)
            pygame.draw.rect(screen, color, rect, border_top_left_radius=16, border_bottom_left_radius=16)
            screen.blit(text, (map.get_width()-10-extra_add, y_down+(TAB_HEIGHT/2)-(text.get_height()/2)))
            title_rects.append(rect)
            y_down += TAB_HEIGHT + 10

        rect = pygame.Rect(map.get_width()+18, 0, width-map.get_width()-18, height)
        pygame.draw.rect(screen, COLOR, rect)

        for rect in title_rects:
            if button_check(rect):
                menu_page = titles[title_rects.index(rect)] 
                extra = 0

        x_across = width - 280
        y_down = 52-SPACING

        # line page
        if menu_page == "Lines":
            line_rects = []
            for line in range(len(lines)):
                color = lines[line]["color"]
                
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-4, ROW_HEIGHT-4)
                pygame.draw.rect(screen, pygame.Color(min(255, color.r+50), min(255, color.g+50), min(255, color.b+50)), rect)
                rect = pygame.Rect(x_across+SPACING+4, y_down+SPACING+4, ROW_HEIGHT-4, ROW_HEIGHT-4)
                pygame.draw.rect(screen, color//pygame.Color(2,2,2), rect)
                rect = pygame.Rect(x_across+SPACING+4, y_down+SPACING+4, ROW_HEIGHT-8, ROW_HEIGHT-8)
                pygame.draw.rect(screen, color, rect)

                rect = pygame.Rect(x_across, y_down, ROW_HEIGHT, ROW_HEIGHT)
                line_rects.append(rect)

                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING
                
            for rect in line_rects:
                if not train_purchase:
                    if button_check(rect):
                        for item in trains+lines+upgrades:
                            item["shown"] = False
                        lines[line_rects.index(rect)]["shown"] = True

        if menu_page == "Trains":
            train_rects = []
            for train in range(len(trains)):
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-8, ROW_HEIGHT-8)
                screen.blit(trains[train]["icon"], (x_across+SPACING, y_down+SPACING))

                train_rects.append(rect)

                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING
                
            for rect in train_rects:
                if button_check(rect):
                    for item in trains+lines+upgrades:
                        item["shown"] = False
                    trains[train_rects.index(rect)]["shown"] = True

        if menu_page == "Upgrades":
            pass

        # popup answers
        for item in trains+lines+upgrades:
            if item["shown"]:
                x_across = width - 500
                y_down = height - 200
                rect = pygame.Rect(x_across, y_down, 500, 200)
                pygame.draw.rect(screen, pygame.Color(210,210,210), rect)

                if item in lines:
                    rect = pygame.Rect(x_across, y_down, 500, H3_SIZE+SPACING*2)
                    pygame.draw.rect(screen, item["color"], rect)
                    text = font_h3.render(f'{item["name"]} Line', True, "black" if item["name"] == "Yellow-1" else "white")
                    screen.blit(text, (x_across+250-text.get_width()/2, y_down+SPACING))

                    y_down += H3_SIZE+SPACING*2

                    # line unowned
                    if not item["owned"]:
                        # purchase button
                        rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*2))
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Purchase", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/5)-(text.get_height()/2)))
                        text = font_h3.render("Line", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*3/5)-(text.get_height()/2)))

                        if button_check(rect):
                            item["owned"] = True

                    # line owned
                    else:
                        # line owned, not built
                        if not item["stations"]:
                            rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*3)/2)
                            pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                            text = font_h3.render("Build", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                            text = font_h3.render("Line", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                            
                            if button_check(rect):
                                line_build = True
                                item["finished"] = False
                        
                        # line owned, built
                        else:
                            rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*3)/2)
                            pygame.draw.rect(screen, pygame.Color(255, 153, 43), rect)
                            text = font_h3.render("Destroy", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                            text = font_h3.render("Line", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))

                            if button_check(rect):
                                item["stations"] = []

                        y_down += (height-y_down-SPACING*3)/2+SPACING*2

                        # line owned, upgrade
                        rect = pygame.Rect(x_across+350, y_down, 150-SPACING, (height-y_down-SPACING))
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Upgrade", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                        text = font_h3.render("Line", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))

                        if button_check(rect):
                            pass

                        # building line
                        if line_build:
                            y_down = height - 200 + (H3_SIZE+SPACING*2)
                            rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*3)/2)
                            pygame.draw.rect(screen, "red", rect)
                            text = font_h3.render("Building", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                            text = font_h3.render("in progress", True, "white")
                            screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                            
                            for station in stations:
                                key = pygame.key.get_pressed()
                                rect = pygame.Rect(station["x"]-5, station["y"]-5, 15, 15)
                                if item["stations"] == [] and button_check(rect) and item["owned"] and station["owned"]:
                                    item["stations"].append(station["code"])
                                    pygame.draw.rect(screen, "red", rect)
                                elif button_check(rect) and item["stations"][-1] in station["operates_to"] and len(item["stations"]) < 10 and station["code"] not in item["stations"] and station["owned"]:
                                    item["stations"].append(station["code"])
                                    pygame.draw.rect(screen, "red", rect)
                                elif key[pygame.K_RETURN]:
                                    item["finished"] = True
                                    line_build = False
                                elif key[pygame.K_ESCAPE]:
                                    item["stations"] = []
                                    line_build = False
                                else:
                                    pass
                                flash_lines = []
                                if item["stations"] != [] and not item["finished"]:
                                    for station in stations:
                                        if item["stations"][-1] == station["code"]:
                                            for dest in station["operates_to"]:
                                                flash_lines.append({"stations": [station["code"], dest], "color": pygame.Color(160,160,160)})
                            
                            tips("Current Line Path", ", ".join(item["stations"]) if len(item["stations"]) > 0 else "None", "Press enter to finish building line, or escape to cancel build", font_h4, font_h3, font_h4)

                    # other line details
                    y_down = (height - 200) + H3_SIZE+SPACING*2

                    text = font_h4.render(f"Line Route:", True, "black")
                    screen.blit(text, (x_across+8, y_down+8))
                    text = font_h4.render(f"{','.join(item['stations'])}", True, "black")
                    screen.blit(text, (x_across+8, y_down+8+H4_SIZE))

                if item in trains:
                    rect = pygame.Rect(x_across, y_down, 500, H3_SIZE+SPACING*2)
                    pygame.draw.rect(screen, pygame.Color(255, 50,50), rect)
                    text = font_h3.render(f'{item["make"]} - {item["model"]}', True, "white")
                    screen.blit(text, (x_across+250-text.get_width()/2, y_down+SPACING))

                    y_down += H3_SIZE+SPACING*2

                    # train not unlocked
                    if not item["unlocked"]:
                        # purchase button
                        rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*2))
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Unlock", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/5)-(text.get_height()/2)))
                        text = font_h3.render(e_euros(item["cost"]*10), True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*3/5)-(text.get_height()/2)))

                        if button_check(rect):
                            if item["cost"]*10 > euros:
                                pass
                            else:
                                euros -= item["cost"]*10
                                item["unlocked"] = True
                                item["level"] = 1

                    # train owned
                    else:
                        # train owned, purchase
                        rect = pygame.Rect(x_across+350, y_down+SPACING, 150-SPACING, (height-y_down-SPACING*3)/2)
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Purchase", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                        text = font_h3.render("Train", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))

                        if button_check(rect):
                            train_purchase = True
                        if train_purchase:
                            menu_page = "Lines"
                            tips("Choose which line you'd like this train to run on.", f'This train requires a {item["train_type"]} line.', "", font_h3, font_h3, font_h3)
                            for rect in line_rects:
                                if button_check(rect) and lines[line_rects.index(rect)]["owned"]:
                                    lines[line_rects.index(rect)]["trains"].append(item["model"])

                                    # create Train with Train class
                                    owned_trains.append(Train(item["model"], lines[line_rects.index(rect)]["name"], item["capacity"], item["profit_per_person_per_km"], item["speed"]))

                                    menu_page = "Trains"
                                    train_purchase = False

                        y_down += (height-y_down-SPACING*3)/2+SPACING*2

                        upgrade_cost = round(item["cost"]**(1+item["level"]*0.1), -4)

                        # train owned, upgrade
                        rect = pygame.Rect(x_across+350, y_down, 150-SPACING, (height-y_down-SPACING))
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Upgrade", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)))
                        text = font_h3.render(str('{:,}'.format(upgrade_cost)[:-2]), True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))

                        if button_check(rect):
                            if upgrade_cost > euros:
                                pass
                            else:
                                euros -= upgrade_cost
                                item["level"] += 1

                                # determine upgrade stat changes here
                                # train capacity
                                if item["model"] in ["DT-4", "DT-5A", "DT-5B", "DT-6", "Ember", "Torrent", "Mystic", "Maris", "Polaris", "Polaris-2", "AC-76", "AC-77", "Piercer", "Baron", "Ocean", "HM-11W", "HM-12W"]:
                                    item["capacity"] += 50 if item["capacity"] < 600 else 100
                                elif item["model"] in ["Bulb", "Current", "Solo", "Bronze"]:
                                    item["capacity"] += 25 if item["capacity"] < 300 else 50
                                elif item["model"] in ["Ursa", "Peng-01", "Star of China", "Wang-01", 'Bullet', "Taurus"]:
                                    item["capacity"] += 100 if item["capacity"] < 1000 else 200
                                elif item["model"] in ["Jubilee-A", "Jubilee-B", "Silver", "Gold"]:
                                    item["capacity"] += 10
                                elif item["model"] in ["Diamond"]:
                                    item["capacity"] += 2

                                # train speed
                                if item ["model"] in ["Solo"]:
                                    item["speed"] += 0
                                elif item["model"] in ["HM-11W", "HM-12W"]:
                                    item["speed"] += 2
                                elif item["model"] in ["Bronze", "Silver", "Gold", "Diamond"]:
                                    item["speed"] += 5
                                elif item["model"] in ["DT-4", "DT-5A", "DT-5B"]:
                                    item["speed"] += 5 if item["speed"] < 140 else 2
                                elif item["model"] in ["Ember", "Jubilee-A", "Jubilee-B"]:
                                    item["speed"] += 5 if item["speed"] < 160 else 2
                                elif item["model"] in ["DT-6", "Bulb"]:
                                    item["speed"] += 6 if item["speed"] < 160 else 2
                                elif item["model"] in ["Ursa", "Maris", "Torrent", "Mystic"]:
                                    item["speed"] += 10 if item["speed"] < 200 else 5
                                elif item["model"] in ["Current"]:
                                    item["speed"] += 10 if item["speed"] < 200 else 0
                                elif item["model"] in ["Polaris", "Polaris-2", "Wang-01"]:
                                    item["speed"] += 12
                                elif item["model"] in ["Baron", "Ocean"]:
                                    item["speed"] += 15 if item["speed"] < 200 else 10
                                elif item["model"] in ["Star of China", "Peng-01"]:
                                    item["speed"] += 20
                                elif item["model"] in ["Bullet", "Piercer"]:
                                    item["speed"] += 20 if item["speed"] < 320 else 10
                                elif item["model"] in ["AC-76", "AC-77", "Taurus"]:
                                    if item["speed"] < 150:
                                        item["speed"] += 10
                                    elif item["speed"] < 230:
                                        item["speed"] += 20
                                    elif item["speed"] >= 230:
                                        item["speed"] += 30

                                # train profit

                    y_down = height - 200
                    y_down += H3_SIZE+SPACING*2
                    text = font_h4.render(f"Top Speed: {item['speed']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+8))
                    text = font_h4.render(f"Capacity: {item['capacity']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+10+H4_SIZE))
                    text = font_h4.render(f"Earnings: {item['profit_per_person_per_km']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+12+H4_SIZE*2))
                    text = font_h4.render(f"Line Type: {item['train_type']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+14+H4_SIZE*3))



                    pygame.draw.line(screen, "black", (x_across+175, y_down+8), (x_across+175, y_down+100), width=8)



                    # level graph
                    reset_to_0 = False
                    if item["level"] == 0:
                        item["level"] = 1
                        reset_to_0 = True
                    rect = pygame.Rect(x_across+15, height-40, 320, 32)
                    pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect, border_radius = 20)
                    rect = pygame.Rect(x_across+15+(item["level"]-1)*32 +16, height-40, (10-(item["level"]))*32+16, 32)
                    pygame.draw.rect(screen, "red", rect, border_top_right_radius = 20, border_bottom_right_radius = 20)
                    pygame.draw.circle(screen, pygame.Color(252, 219, 3), (x_across+15+(item["level"]-1)*32 +16, height-8-(16)), 16)
                    font_h3.set_bold(True)
                    if reset_to_0:
                        item["level"] = 0
                    text = font_h3.render(str(item["level"]), True, "black")
                    if reset_to_0:
                        item["level"] = 1
                    screen.blit(text, (x_across+15+(item["level"]-1)*32 +16 -text.get_width()/2, height-8-(16)-text.get_height()/2))
                    if reset_to_0:
                        item["level"] = 0
                    font_h3.set_bold(False)
                        
                    






                        





                if item in upgrades:
                    pass

        # close game
        font_h2_diff.set_bold(True)
        rect = pygame.Rect(width - 42, 10, 32, 32)
        pygame.draw.rect(screen, "red", rect)
        text = font_h2_diff.render("X", True, "white")
        screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]/2)-text.get_height()/2+2))
        if button_check(rect):
            running = False
        font_h2_diff.set_bold(False)

        # money
        # passive from stations
        for station in stations:
            pass

        # from trains on lines
        for line in lines:
            if line["owned"] and line["stations"] != [] and line["finished"]:
                euros_per_trip = 0
                distance = 0
                for station in range(len(line["stations"])-1):
                    for code in stations:
                        if code["code"] == line["stations"][station]:
                            start_loc = code
                        if code["code"] == line["stations"][station+1]:
                            end_loc = code
                        if start_loc == None or end_loc == None:
                            pass
                        else:
                            distance += round(math.sqrt((start_loc["x"] - end_loc["x"])**2 + (start_loc["y"] - end_loc["y"])**2))

                for train in owned_trains:
                    if train.line == line["name"]:
                        euros_per_trip = train.cap * train.ppkm * distance
                        trip_time = distance / train.speed
                        train.trip_hr = trip_time // 60
                        train.trip_min = trip_time % 60
                        if hour == start and minute >= 0:
                            trains_running = True
                            train.last_hr = start
                            train.last_min = 0
                        if hour == end:
                            trains_running = False

                        if trains_running:
                            train.next_hr = train.last_hr + train.trip_hr
                            train.next_min = train.last_min + train.trip_min
                            if train.next_min >= 60:
                                train.next_min -= 60
                                train.next_hr += 1
                            if train.next_hr >= end:
                                pass
                            else:
                                if hour == train.next_hr and minute in range(int(train.next_min)-10, int(train.next_min+15)) or hour == train.next_hr+1 and minute <= 10 and train.next_min > 50:
                                    euros += euros_per_trip
                                    train.last_hr = train.next_hr
                                    train.last_min = train.next_min
                                    income_statements.append(f'{list(months.keys())[month-1]} {round(day)}{" " if round(day)<10 else ""} {0 if round(train.next_hr)<10 else ""}{round(train.next_hr)}:{0 if round(train.next_min)<10 else ""}{round(train.next_min)} | {line["name"]:<8} | ${round(euros_per_trip)}')                           
            
        # drawing on map
        # draw lines
        if flash > 0.5:
            draw_lines(flash_lines+lines, stations)
        else:
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
                if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+10) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+10) and station["shown"]:

                    # determining backing colour based on cost and players money - adds a clearer visualisation of what the player can do with station
                    if station in stations and not station["owned"] and station["cost"] > euros:
                        bg_color = pygame.Color(217, 49, 30)
                    elif station in stations and not station["owned"]:
                        bg_color = pygame.Color(210,210,210)
                    else:
                        bg_color = "yellow"

                    rect = pygame.Rect(station["x"] - 12, station["y"] - 30, 29, H4_SIZE+4)
                    pygame.draw.rect(screen, bg_color, rect)
                    text = font_h4.render(station["code"], True, "black")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2+1, rect[1]+(rect[3]/2)-text.get_height()/2))

        # show station labels on click
        for station in stations:

            # station labels
            if station["clicked"] and not line_build: 
                draw_station(station, pygame.Color(54, 153, 43))
                BOX_WIDTH = font_h4.render("XXXXXXXXXXXX  XXX", True, "black").get_width()
                BOX_HEIGHT = H4_SIZE * 3 + 12
                # box down
                if station["y"] - (H5_SIZE * 5 + 30) < 20:
                    box = pygame.Vector2(station["x"] - 65, station["y"] + ((H5_SIZE * 5 + 15)-H5_SIZE * 5) + 5) # used V2 then rect
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 
                # box up
                else:
                    box = pygame.Vector2(station["x"] - 65, station["y"] - (H5_SIZE * 5 + 15))
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

                    if euros > station["cost"]:
                        color = pygame.Color(39, 143, 31)
                        words_1 = "PURCHASE"
                        words_2 = str(station["cost"])
                    else:
                        color = "red"
                        words_1 = "CAN'T AFFORD"
                        words_2 = str(station["cost"])

                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+4, BOX_WIDTH-8, (H4_SIZE*3+12)-(H4_SIZE+4)-4)
                    pygame.draw.rect(screen, color, rect)
                    # printing purchase details on station
                    text = font_h4.render(words_1, True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)-1))
                    text = font_h4.render(words_2, True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)+2))

                    # checks for if user is clicking the purchase button or not
                    if button_check(rect):
                        if euros > station["cost"]:
                            station["owned"] = True
                            euros -= station["cost"]
                            for dest in station["operates_to"]:
                                for item in stations:
                                    if dest == item["code"]:
                                        item["shown"] = True
                            

                        # add money changes etc here
                
                # shows 'owned' button if station is owned - may change
                if station["owned"]:
                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+4, BOX_WIDTH-8, (H4_SIZE*3+12)-(H4_SIZE+4)-4)
                    pygame.draw.rect(screen, pygame.Color(160, 160, 160), rect)

                    font_h4.set_bold(True)
                    text = font_h4.render("OWNED", True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, (rect[1]+rect[3]/2) - text.get_height()/2))
                    font_h4.set_bold(False)

            # rect checking for each station - finds which station was clicked
            rect = pygame.Rect(station["x"]-5, station["y"]-5, 15, 15)
            if button_check(rect):
                for clicked in stations:       # makes every other stations  
                    clicked["clicked"] = False # 'clicked' status False, then sets 
                station["clicked"] = True      # the correct stations status to True

        # removing large station labels when clicked elsewhere
        if button_check(pygame.Rect(0,0,width,height)):
            for station in stations:
                station["clicked"] = False

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

        text = font_h5.render(f'{round(hour)}:{round(minute)}', True, "black")
        screen.blit(text, (pygame.mouse.get_pos()[0]+10, pygame.mouse.get_pos()[1]+5))

    pygame.display.flip()

    # for flashing/pulsing items such as lines in purchase phase
    if flash < 1:
        flash += 1.1 * dt
    else:
        flash -= 1

    flash = 0


    # dt is time between frames, makes flashing smoother.
    dt = clock.tick(1000)/1000

    # date
    seconds_since_date_update += dt*6 
    if seconds_since_date_update >= 24:
        seconds_since_date_update = 0
        day += 1
        if months[list(months.keys())[month-1]] < day:
            month += 1
            day = 1
        if month > 12:
            year += 1
            month = 1


pygame.quit()
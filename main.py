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

# sizes
width = screen.get_width()
height = screen.get_height()
ROWS = 4
ROW_HEIGHT = 45
SPACING = 6

# images
map = pygame.image.load("zug_fallt_aus/assets/north-europe-map.png")
map = pygame.transform.scale(map, (width, (height * (map.get_width()/width)))) # adjusts map size so the width of the map is the same as the width of the screen
lock = pygame.image.load("zug_fallt_aus/assets/lock.png")
lock = pygame.transform.scale(lock, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))

# train icons
red_hill = pygame.image.load("zug_fallt_aus/assets/train_icons/red-hill.png")
red_hill = pygame.transform.scale(red_hill, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
great_northern = pygame.image.load("zug_fallt_aus/assets/train_icons/great-northern.png")
great_northern = pygame.transform.scale(great_northern, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
guangdong_star = pygame.image.load("zug_fallt_aus/assets/train_icons/guangdong-star.png")
guangdong_star = pygame.transform.scale(guangdong_star, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
west_network = pygame.image.load("zug_fallt_aus/assets/train_icons/west-network.png")
west_network = pygame.transform.scale(west_network, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
railspark_bulb = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-bulb.png")
railspark_bulb = pygame.transform.scale(railspark_bulb, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
railspark_ember = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-ember.png")
railspark_ember = pygame.transform.scale(railspark_ember, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
railspark_torrent = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-torrent.png")
railspark_torrent = pygame.transform.scale(railspark_torrent, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
railspark_mystic = pygame.image.load("zug_fallt_aus/assets/train_icons/railspark-mystic.png")
railspark_mystic = pygame.transform.scale(railspark_mystic, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
erlington_works = pygame.image.load("zug_fallt_aus/assets/train_icons/erlington-works.png")
erlington_works = pygame.transform.scale(erlington_works, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
erlington_works_2 = pygame.image.load("zug_fallt_aus/assets/train_icons/erlington-works-purple.png")
erlington_works_2 = pygame.transform.scale(erlington_works_2, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
north_star_green = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-green.png")
north_star_green = pygame.transform.scale(north_star_green, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
north_star_purple = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-purple.png")
north_star_purple = pygame.transform.scale(north_star_purple, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
north_star_red = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-red.png")
north_star_red = pygame.transform.scale(north_star_red, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
north_star_yellow = pygame.image.load("zug_fallt_aus/assets/train_icons/north-star-yellow.png")
north_star_yellow = pygame.transform.scale(north_star_yellow, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
express_orange = pygame.image.load("zug_fallt_aus/assets/train_icons/express-orange.png")
express_orange = pygame.transform.scale(express_orange, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
express_blue = pygame.image.load("zug_fallt_aus/assets/train_icons/express-blue.png")
express_blue = pygame.transform.scale(express_blue, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
express_green = pygame.image.load("zug_fallt_aus/assets/train_icons/express-green.png")
express_green = pygame.transform.scale(express_green, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
express_red = pygame.image.load("zug_fallt_aus/assets/train_icons/express-red.png")
express_red = pygame.transform.scale(express_red, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
thompson_lines_blue = pygame.image.load("zug_fallt_aus/assets/train_icons/thompson-locomotives-blue.png")
thompson_lines_blue = pygame.transform.scale(thompson_lines_blue, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
thompson_lines_red = pygame.image.load("zug_fallt_aus/assets/train_icons/thompson-locomotives-red.png")
thompson_lines_red = pygame.transform.scale(thompson_lines_red, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
royal_bronze = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-bronze.png")
royal_bronze = pygame.transform.scale(royal_bronze, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
royal_silver = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-silver.png")
royal_silver = pygame.transform.scale(royal_silver, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
royal_gold = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-gold.png")
royal_gold = pygame.transform.scale(royal_gold, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
royal_diamond = pygame.image.load("zug_fallt_aus/assets/train_icons/royal-diamond.png")
royal_diamond = pygame.transform.scale(royal_diamond, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
peng_enterprises = pygame.image.load("zug_fallt_aus/assets/train_icons/peng-enterprises.png")
peng_enterprises = pygame.transform.scale(peng_enterprises, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
yangtze_monos = pygame.image.load("zug_fallt_aus/assets/train_icons/yangtze-monos.png")
yangtze_monos = pygame.transform.scale(yangtze_monos, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
wang_li = pygame.image.load("zug_fallt_aus/assets/train_icons/wang-li.png")
wang_li = pygame.transform.scale(wang_li, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
southern_star = pygame.image.load("zug_fallt_aus/assets/train_icons/southern-star.png")
southern_star = pygame.transform.scale(southern_star, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
eastern_power = pygame.image.load("zug_fallt_aus/assets/train_icons/eastern-power.png")
eastern_power = pygame.transform.scale(eastern_power, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
blue_hill = pygame.image.load("zug_fallt_aus/assets/train_icons/blue-hill.png")
blue_hill = pygame.transform.scale(blue_hill, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
hermann_orange = pygame.image.load("zug_fallt_aus/assets/train_icons/hermann-trainworks.png")
hermann_orange = pygame.transform.scale(hermann_orange, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
hermann_green = pygame.image.load("zug_fallt_aus/assets/train_icons/hermann-trainworks-2.png")
hermann_green = pygame.transform.scale(hermann_green, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))
    
    
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

# values
euros = 5000000
COST_PER_KM = 100

# date calc things
months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31, }

# lists
stations = [
    {'name': 'Amsterdam', 'code': 'AMS', 'x': 200, 'y': 275, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3410000, 'passenger_cap': 47000, 'operates_to': ['HAG', 'ROT', 'UTR', 'ARN', 'APL', 'ZWL'], 'runs_to': []},
    {'name': 'Berlin', 'code': 'BER', 'x': 790, 'y': 250, 'shown': False, 'owned': False, 'clicked': False, 'cost': 10000000, 'passenger_cap': 188000, 'operates_to': ['ROS', 'SZZ', 'POZ', 'MAG', 'LPZ', 'DRE'], 'runs_to': []},
    {'name': 'Prague', 'code': 'PRA', 'x': 860, 'y': 500, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4470000, 'passenger_cap': 66000, 'operates_to': ['PLS', 'DRE', 'PAR', 'LIB', 'BRN'], 'runs_to': []},
    {'name': 'Brussels', 'code': 'BRU', 'x': 160, 'y': 420, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4080000, 'passenger_cap': 59000, 'operates_to': ['GHE', 'CHA', 'NAM', 'LIE', 'ANT'], 'runs_to': []},
    {'name': 'Warsaw', 'code': 'WSW', 'x': 1320, 'y': 280, 'shown': False, 'owned': False, 'clicked': False, 'cost': 5830000, 'passenger_cap': 93000, 'operates_to': ['PLK', 'LOD', 'SID', 'BIA', 'OLZ'], 'runs_to': []},
    {'name': 'Brno', 'code': 'BRN', 'x': 1005, 'y': 590, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1630000, 'passenger_cap': 19000, 'operates_to': ['PRA', 'PAR', 'OLO', 'ZLI'], 'runs_to': []},
    {'name': 'Gdansk', 'code': 'GDA', 'x': 1130, 'y': 65, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1950000, 'passenger_cap': 24000, 'operates_to': ['ELB', 'GRD', 'SLP'], 'runs_to': []},
    {'name': 'Lodz', 'code': 'LOD', 'x': 1225, 'y': 335, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2610000, 'passenger_cap': 34000, 'operates_to': ['PLK', 'TOR', 'POZ', 'WSW', 'LUB', 'KIL', 'CZE'], 'runs_to': []},
    {'name': 'Krakow', 'code': 'KRA', 'x': 1240, 'y': 495, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3010000, 'passenger_cap': 40000, 'operates_to': ['TAR', 'KIL', 'CZE', 'KAT'], 'runs_to': []},
    {'name': 'Rotterdam', 'code': 'ROT', 'x': 160, 'y': 320, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2590000, 'passenger_cap': 33000, 'operates_to': ['HAG', 'UTR', 'AMS', 'ANT', 'EIN'], 'runs_to': []},
    {'name': 'The Hague', 'code': 'HAG', 'x': 150, 'y': 300, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2260000, 'passenger_cap': 28000, 'operates_to': ['ROT', 'AMS'], 'runs_to': []},
    {'name': 'Antwerp', 'code': 'ANT', 'x': 160, 'y': 380, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2150000, 'passenger_cap': 26000, 'operates_to': ['GHE', 'BRG', 'BRU', 'ROT', 'EIN'], 'runs_to': []},
    {'name': 'Ostrava', 'code': 'OST', 'x': 1110, 'y': 525, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1270000, 'passenger_cap': 14000, 'operates_to': ['OLO', 'ZLI', 'WRO', 'KAT'], 'runs_to': []},
    {'name': 'Munich', 'code': 'MUC', 'x': 650, 'y': 695, 'shown': False, 'owned': False, 'clicked': False, 'cost': 4910000, 'passenger_cap': 74000, 'operates_to': ['KON', 'AUG', 'ING', 'REG'], 'runs_to': []},
    {'name': 'Frankfurt', 'code': 'FRA', 'x': 450, 'y': 495, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2900000, 'passenger_cap': 38000, 'operates_to': ['WIE', 'MAN', 'WRZ', 'MAR', 'SIE'], 'runs_to': []},
    {'name': 'Hamburg', 'code': 'HAM', 'x': 530, 'y': 155, 'shown': False, 'owned': False, 'clicked': False, 'cost': 5810000, 'passenger_cap': 93000, 'operates_to': ['KIE', 'LBK', 'SCH', 'BRE', 'HAN'], 'runs_to': []},
    {'name': 'Luxembourg', 'code': 'LUX', 'x': 270, 'y': 540, 'shown': False, 'owned': False, 'clicked': False, 'cost': 530000, 'passenger_cap': 6000, 'operates_to': ['NAM', 'LIE', 'TRI', 'SAA'], 'runs_to': []},
    {'name': 'Leipzig', 'code': 'LPZ', 'x': 705, 'y': 370, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2390000, 'passenger_cap': 30000, 'operates_to': ['ERF', 'CHM', 'DRE', 'BER', 'MAG'], 'runs_to': []},
    {'name': 'Koln', 'code': 'KOL', 'x': 330, 'y': 410, 'shown': False, 'owned': False, 'clicked': False, 'cost': 3820000, 'passenger_cap': 54000, 'operates_to': ['WUP', 'DUS', 'AAC', 'BON', 'SIE'], 'runs_to': []},
    {'name': 'Stuttgart', 'code': 'STT', 'x': 480, 'y': 620, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2500000, 'passenger_cap': 32000, 'operates_to': ['KAR', 'KON', 'ULM', 'WRZ'], 'runs_to': []},
    {'name': 'Dusseldorf', 'code': 'DUS', 'x': 325, 'y': 385, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2450000, 'passenger_cap': 31000, 'operates_to': ['DUI', 'ESS', 'WUP', 'KOL', 'AAC'], 'runs_to': []},
    {'name': 'Nuremberg', 'code': 'NRB', 'x': 620, 'y': 580, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2110000, 'passenger_cap': 26000, 'operates_to': ['WRZ', 'AUG', 'ING', 'REG', 'PLS'], 'runs_to': []},
    {'name': 'Bydgoszcz', 'code': 'BYD', 'x': 1100, 'y': 200, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1490000, 'passenger_cap': 17000, 'operates_to': ['PIL', 'POZ', 'GRD', 'TOR'], 'runs_to': []},
    {'name': 'Poznan', 'code': 'POZ', 'x': 1030, 'y': 270, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2210000, 'passenger_cap': 27000, 'operates_to': ['BER', 'LEZ', 'PIL', 'BYD', 'LOD'], 'runs_to': []},
    {'name': 'Wroclaw', 'code': 'WRO', 'x': 1015, 'y': 410, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2620000, 'passenger_cap': 34000, 'operates_to': ['LEG', 'GLO', 'LEZ', 'PAR', 'OST', 'KAT', 'CZE'], 'runs_to': []},
    {'name': 'Ghent', 'code': 'GHE', 'x': 105, 'y': 400, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1170000, 'passenger_cap': 13000, 'operates_to': ['BRG', 'KJK', 'ANT', 'BRU'], 'runs_to': []},
    {'name': 'Katowice', 'code': 'KAT', 'x': 1155, 'y': 480, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1290000, 'passenger_cap': 15000, 'operates_to': ['WRO', 'CZE', 'KRA', 'OST'], 'runs_to': []},
    {'name': 'Szczecin', 'code': 'SZZ', 'x': 850, 'y': 160, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1690000, 'passenger_cap': 20000, 'operates_to': ['ROS', 'BER', 'KSZ', 'PIL'], 'runs_to': []},
    {'name': 'Lublin', 'code': 'LUB', 'x': 1405, 'y': 405, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1470000, 'passenger_cap': 17000, 'operates_to': ['LOD', 'SID', 'KIL', 'RZS'], 'runs_to': []},
    {'name': 'Charleroi', 'code': 'CHA', 'x': 170, 'y': 465, 'shown': False, 'owned': False, 'clicked': False, 'cost': 900000, 'passenger_cap': 10000, 'operates_to': ['NAM', 'BRU', 'KJK'], 'runs_to': []},
    {'name': 'Dortmund', 'code': 'DOR', 'x': 365, 'y': 350, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2350000, 'passenger_cap': 29000, 'operates_to': ['ESS', 'MUN', 'WUP'], 'runs_to': []},
    {'name': 'Utrecht', 'code': 'UTR', 'x': 210, 'y': 300, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1580000, 'passenger_cap': 18000, 'operates_to': ['AMS', 'ROT', 'NIJ', 'ARN', 'EIN'], 'runs_to': []},
    {'name': 'Eindhoven', 'code': 'EIN', 'x': 225, 'y': 355, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1080000, 'passenger_cap': 12000, 'operates_to': ['MAA', 'ANT', 'ROT', 'UTR', 'NIJ'], 'runs_to': []},
    {'name': 'Groningen', 'code': 'GRO', 'x': 305, 'y': 180, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1040000, 'passenger_cap': 12000, 'operates_to': ['ZWL', 'OLD'], 'runs_to': []},
    {'name': 'Essen', 'code': 'ESS', 'x': 335, 'y': 355, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2330000, 'passenger_cap': 29000, 'operates_to': ['ENS', 'DUI', 'DOR', 'DUS', 'WUP'], 'runs_to': []},
    {'name': 'Hanover', 'code': 'HAN', 'x': 520, 'y': 265, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2180000, 'passenger_cap': 27000, 'operates_to': ['HAM', 'BRS', 'BRE', 'BIE', 'KAS'], 'runs_to': []},
    {'name': 'Bremen', 'code': 'BRE', 'x': 460, 'y': 190, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2290000, 'passenger_cap': 28000, 'operates_to': ['OLD', 'BIE', 'HAM', 'HAN'], 'runs_to': []},
    {'name': 'Munster', 'code': 'MUN', 'x': 385, 'y': 310, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1380000, 'passenger_cap': 16000, 'operates_to': ['OSN', 'ENS', 'BIE', 'DOR'], 'runs_to': []},
    {'name': 'Bielefeld', 'code': 'BIE', 'x': 435, 'y': 300, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1450000, 'passenger_cap': 17000, 'operates_to': ['OSN', 'MUN', 'HAN', 'BRE', 'KAS'], 'runs_to': []},
    {'name': 'Liege', 'code': 'LIE', 'x': 230, 'y': 440, 'shown': False, 'owned': False, 'clicked': False, 'cost': 880000, 'passenger_cap': 10000, 'operates_to': ['MAA', 'AAC', 'LUX', 'NAM', 'BRU', 'ANT'], 'runs_to': []},
    {'name': 'Aachen', 'code': 'AAC', 'x': 280, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1110000, 'passenger_cap': 12000, 'operates_to': ['MAA', 'LIE', 'DUS', 'KOL', 'BON'], 'runs_to': []},
    {'name': 'Erfurt', 'code': 'ERF', 'x': 615, 'y': 400, 'shown': True, 'owned': False, 'clicked': False, 'cost': 950000, 'passenger_cap': 11000, 'operates_to': ['BRS', 'KAS', 'MAG', 'LPZ', 'CHM', 'WRZ'], 'runs_to': []},
    {'name': 'Dresden', 'code': 'DRE', 'x': 815, 'y': 400, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2240000, 'passenger_cap': 28000, 'operates_to': ['CHM', 'LPZ', 'LIB', 'PRA', 'BER'], 'runs_to': []},
    {'name': 'Magdeburg', 'code': 'MAG', 'x': 660, 'y': 300, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1060000, 'passenger_cap': 12000, 'operates_to': ['BRS', 'ERF', 'BER', 'LPZ'], 'runs_to': []},
    {'name': 'Kiel', 'code': 'KIE', 'x': 550, 'y': 70, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1100000, 'passenger_cap': 12000, 'operates_to': ['FLN', 'LBK', 'HAM'], 'runs_to': []},
    {'name': 'Flensburg', 'code': 'FLN', 'x': 500, 'y': 25, 'shown': False, 'owned': False, 'clicked': False, 'cost': 290000, 'passenger_cap': 4000, 'operates_to': ['KIE'], 'runs_to': []},
    {'name': 'Freiburg', 'code': 'FRB', 'x': 385, 'y': 715, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1030000, 'passenger_cap': 12000, 'operates_to': ['KON', 'KAR'], 'runs_to': []},
    {'name': 'Namur', 'code': 'NAM', 'x': 200, 'y': 460, 'shown': False, 'owned': False, 'clicked': False, 'cost': 430000, 'passenger_cap': 6000, 'operates_to': ['CHA', 'BRU', 'LIE', 'LUX'], 'runs_to': []},
    {'name': 'Kortrijk', 'code': 'KJK', 'x': 75, 'y': 420, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['BRG', 'GHE', 'CHA'], 'runs_to': []},
    {'name': 'Bruges', 'code': 'BRG', 'x': 70, 'y': 380, 'shown': False, 'owned': False, 'clicked': False, 'cost': 470000, 'passenger_cap': 6000, 'operates_to': ['ANT', 'GHE', 'KJK'], 'runs_to': []},
    {'name': 'Apeldoorn', 'code': 'APL', 'x': 260, 'y': 265, 'shown': False, 'owned': False, 'clicked': False, 'cost': 720000, 'passenger_cap': 8000, 'operates_to': ['ZWL', 'ARN', 'ENS', 'AMS'], 'runs_to': []},
    {'name': 'Zwolle', 'code': 'ZWL', 'x': 270, 'y': 235, 'shown': False, 'owned': False, 'clicked': False, 'cost': 540000, 'passenger_cap': 7000, 'operates_to': ['GRO', 'ENS', 'APL', 'AMS'], 'runs_to': []},
    {'name': 'Nijmegen', 'code': 'NIJ', 'x': 250, 'y': 320, 'shown': False, 'owned': False, 'clicked': False, 'cost': 790000, 'passenger_cap': 9000, 'operates_to': ['ARN', 'UTR', 'EIN', 'DUI'], 'runs_to': []},
    {'name': 'Czestochowa', 'code': 'CZE', 'x': 1160, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 980000, 'passenger_cap': 11000, 'operates_to': ['WRO', 'KAT', 'KRA', 'KIL', 'LOD'], 'runs_to': []},
    {'name': 'Bialystok', 'code': 'BIA', 'x': 1440, 'y': 200, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1310000, 'passenger_cap': 15000, 'operates_to': ['OLZ', 'WSW', 'SID'], 'runs_to': []},
    {'name': 'Elblag', 'code': 'ELB', 'x': 1185, 'y': 85, 'shown': False, 'owned': False, 'clicked': False, 'cost': 480000, 'passenger_cap': 6000, 'operates_to': ['GDA', 'OLZ'], 'runs_to': []},
    {'name': 'Rzeszow', 'code': 'RZS', 'x': 1370, 'y': 505, 'shown': False, 'owned': False, 'clicked': False, 'cost': 870000, 'passenger_cap': 10000, 'operates_to': ['TAR', 'KIL', 'LUB'], 'runs_to': []},
    {'name': 'Pilsen', 'code': 'PLS', 'x': 780, 'y': 530, 'shown': False, 'owned': False, 'clicked': False, 'cost': 770000, 'passenger_cap': 9000, 'operates_to': ['NRB', 'REG', 'CHM', 'PRA'], 'runs_to': []},
    {'name': 'Pardubice', 'code': 'PAR', 'x': 945, 'y': 505, 'shown': False, 'owned': False, 'clicked': False, 'cost': 300000, 'passenger_cap': 5000, 'operates_to': ['LIB', 'PRA', 'OLO', 'BRN', 'WRO'], 'runs_to': []},
    {'name': 'Wurzburg', 'code': 'WRZ', 'x': 545, 'y': 535, 'shown': False, 'owned': False, 'clicked': False, 'cost': 530000, 'passenger_cap': 6000, 'operates_to': ['FRA', 'MAN', 'NRB', 'STT', 'ULM', 'ERF'], 'runs_to': []},
    {'name': 'Mannheim', 'code': 'MAN', 'x': 430, 'y': 555, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1350000, 'passenger_cap': 15000, 'operates_to': ['SAA', 'KAR', 'WIE', 'FRA', 'WRZ'], 'runs_to': []},
    {'name': 'Kassel', 'code': 'KAS', 'x': 515, 'y': 365, 'shown': False, 'owned': False, 'clicked': False, 'cost': 900000, 'passenger_cap': 10000, 'operates_to': ['BIE', 'HAN', 'BRS', 'ERF', 'MAR'], 'runs_to': []},
    {'name': 'Chemnitz', 'code': 'CHM', 'x': 735, 'y': 415, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1100000, 'passenger_cap': 12000, 'operates_to': ['LPZ', 'DRE', 'PLS', 'ERF'], 'runs_to': []},
    {'name': 'Oldenburg', 'code': 'OLD', 'x': 415, 'y': 180, 'shown': False, 'owned': False, 'clicked': False, 'cost': 750000, 'passenger_cap': 9000, 'operates_to': ['GRO', 'BRE', 'OSN'], 'runs_to': []},
    {'name': 'Rostock', 'code': 'ROS', 'x': 680, 'y': 95, 'shown': False, 'owned': False, 'clicked': False, 'cost': 930000, 'passenger_cap': 10000, 'operates_to': ['LBK', 'SCH', 'BER', 'SZZ'], 'runs_to': []},
    {'name': 'Lubeck', 'code': 'LBK', 'x': 585, 'y': 110, 'shown': False, 'owned': False, 'clicked': False, 'cost': 960000, 'passenger_cap': 11000, 'operates_to': ['KIE', 'HAM', 'SCH', 'ROS'], 'runs_to': []},
    {'name': 'Slupsk', 'code': 'SLP', 'x': 1025, 'y': 50, 'shown': False, 'owned': False, 'clicked': False, 'cost': 310000, 'passenger_cap': 5000, 'operates_to': ['KSZ', 'GDA'], 'runs_to': []},
    {'name': 'Koszalin', 'code': 'KSZ', 'x': 975, 'y': 80, 'shown': False, 'owned': False, 'clicked': False, 'cost': 410000, 'passenger_cap': 5000, 'operates_to': ['SLP', 'SZZ', 'PIL'], 'runs_to': []},
    {'name': 'Olsztyn', 'code': 'OLZ', 'x': 1260, 'y': 130, 'shown': False, 'owned': False, 'clicked': False, 'cost': 760000, 'passenger_cap': 9000, 'operates_to': ['ELB', 'BIA', 'GRB', 'WSW'], 'runs_to': []},
    {'name': 'Kielce', 'code': 'KIL', 'x': 1270, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 860000, 'passenger_cap': 10000, 'operates_to': ['LOD', 'CZE', 'KRA', 'RZS', 'LUB'], 'runs_to': []},
    {'name': 'Plock', 'code': 'PLK', 'x': 1235, 'y': 260, 'shown': False, 'owned': False, 'clicked': False, 'cost': 480000, 'passenger_cap': 6000, 'operates_to': ['TOR', 'LOD', 'WSW'], 'runs_to': []},
    {'name': 'Braunschweig', 'code': 'BRS', 'x': 575, 'y': 275, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1090000, 'passenger_cap': 12000, 'operates_to': ['HAN', 'KAS', 'ERF', 'MAG'], 'runs_to': []},
    {'name': 'Ulm', 'code': 'ULM', 'x': 535, 'y': 645, 'shown': False, 'owned': False, 'clicked': False, 'cost': 520000, 'passenger_cap': 6000, 'operates_to': ['STT', 'KON', 'AUG', 'WRZ'], 'runs_to': []},
    {'name': 'Konstanz', 'code': 'KON', 'x': 475, 'y': 735, 'shown': False, 'owned': False, 'clicked': False, 'cost': 270000, 'passenger_cap': 4000, 'operates_to': ['FRB', 'MUC', 'STT', 'ULM'], 'runs_to': []},
    {'name': 'Augsburg', 'code': 'AUG', 'x': 585, 'y': 650, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1320000, 'passenger_cap': 15000, 'operates_to': ['NRB', 'ING', 'MUC', 'ULM'], 'runs_to': []},
    {'name': 'Regensburg', 'code': 'REG', 'x': 685, 'y': 610, 'shown': False, 'owned': False, 'clicked': False, 'cost': 660000, 'passenger_cap': 8000, 'operates_to': ['PIL', 'NRB', 'ING', 'MUC'], 'runs_to': []},
    {'name': 'Ingolstadt', 'code': 'ING', 'x': 635, 'y': 635, 'shown': False, 'owned': False, 'clicked': False, 'cost': 590000, 'passenger_cap': 7000, 'operates_to': ['NRB', 'REG', 'AUG', 'MUC'], 'runs_to': []},
    {'name': 'Koblenz', 'code': 'KOB', 'x': 370, 'y': 470, 'shown': False, 'owned': False, 'clicked': False, 'cost': 450000, 'passenger_cap': 6000, 'operates_to': ['BON', 'WIE', 'TRI', 'SIE'], 'runs_to': []},
    {'name': 'Olomouc', 'code': 'OLO', 'x': 1050, 'y': 545, 'shown': False, 'owned': False, 'clicked': False, 'cost': 370000, 'passenger_cap': 5000, 'operates_to': ['PAR', 'BRN', 'ZLI', 'OST'], 'runs_to': []},
    {'name': 'Zlin', 'code': 'ZLI', 'x': 1070, 'y': 585, 'shown': False, 'owned': False, 'clicked': False, 'cost': 180000, 'passenger_cap': 4000, 'operates_to': ['OLO', 'OST', 'BRN'], 'runs_to': []},
    {'name': 'Pila', 'code': 'PIL', 'x': 1010, 'y': 190, 'shown': False, 'owned': False, 'clicked': False, 'cost': 180000, 'passenger_cap': 4000, 'operates_to': ['SZZ', 'KSZ', 'BYD', 'POZ'], 'runs_to': []},
    {'name': 'Glogow', 'code': 'GLO', 'x': 950, 'y': 350, 'shown': False, 'owned': False, 'clicked': False, 'cost': 120000, 'passenger_cap': 3000, 'operates_to': ['LEZ', 'LEG', 'WRO'], 'runs_to': []},
    {'name': 'Karlsruhe', 'code': 'KAR', 'x': 420, 'y': 605, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1370000, 'passenger_cap': 16000, 'operates_to': ['SAA', 'MAN', 'STT', 'FRB'], 'runs_to': []},
    {'name': 'Saarbrucken', 'code': 'SAA', 'x': 320, 'y': 575, 'shown': False, 'owned': False, 'clicked': False, 'cost': 790000, 'passenger_cap': 9000, 'operates_to': ['LUX', 'TRI', 'MAN', 'KAR'], 'runs_to': []},
    {'name': 'Trier', 'code': 'TRI', 'x': 305, 'y': 520, 'shown': False, 'owned': False, 'clicked': False, 'cost': 430000, 'passenger_cap': 6000, 'operates_to': ['LUX', 'SAA', 'KOB'], 'runs_to': []},
    {'name': 'Wiesbaden', 'code': 'WIE', 'x': 415, 'y': 495, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1230000, 'passenger_cap': 14000, 'operates_to': ['FRA', 'KOB', 'MAN'], 'runs_to': []},
    {'name': 'Bonn', 'code': 'BON', 'x': 340, 'y': 440, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1430000, 'passenger_cap': 16000, 'operates_to': ['KOB', 'AAC', 'KOL', 'SIE'], 'runs_to': []},
    {'name': 'Wuppertal', 'code': 'WUP', 'x': 360, 'y': 390, 'shown': False, 'owned': False, 'clicked': False, 'cost': 1530000, 'passenger_cap': 18000, 'operates_to': ['DOR', 'ESS', 'DUS', 'KOL', 'SIE'], 'runs_to': []},
    {'name': 'Duisburg', 'code': 'DUI', 'x': 300, 'y': 350, 'shown': False, 'owned': False, 'clicked': False, 'cost': 2040000, 'passenger_cap': 25000, 'operates_to': ['ESS', 'DUS', 'NIJ', 'EIN'], 'runs_to': []},
    {'name': 'Marburg', 'code': 'MAR', 'x': 470, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['KAS', 'SIE', 'FRA'], 'runs_to': []},
    {'name': 'Schwerin', 'code': 'SCH', 'x': 635, 'y': 140, 'shown': False, 'owned': False, 'clicked': False, 'cost': 340000, 'passenger_cap': 5000, 'operates_to': ['ROS', 'LBK', 'HAM'], 'runs_to': []},
    {'name': 'Torun', 'code': 'TOR', 'x': 1130, 'y': 215, 'shown': False, 'owned': False, 'clicked': False, 'cost': 880000, 'passenger_cap': 10000, 'operates_to': ['BYD', 'GBD', 'PLK', 'LOD'], 'runs_to': []},
    {'name': 'Leszno', 'code': 'LEZ', 'x': 975, 'y': 325, 'shown': False, 'owned': False, 'clicked': False, 'cost': 50000, 'passenger_cap': 3000, 'operates_to': ['GLO', 'WRO', 'POZ'], 'runs_to': []},
    {'name': 'Siegen', 'code': 'SIE', 'x': 405, 'y': 420, 'shown': False, 'owned': False, 'clicked': False, 'cost': 380000, 'passenger_cap': 5000, 'operates_to': ['WUP', 'KOL', 'MAR', 'FRA', 'BON', 'KOB'], 'runs_to': []},
    {'name': 'Liberec', 'code': 'LIB', 'x': 890, 'y': 425, 'shown': False, 'owned': False, 'clicked': False, 'cost': 390000, 'passenger_cap': 5000, 'operates_to': ['DRE', 'PRA', 'PAR', 'LEG'], 'runs_to': []},
    {'name': 'Legnica', 'code': 'LEG', 'x': 950, 'y': 395, 'shown': False, 'owned': False, 'clicked': False, 'cost': 360000, 'passenger_cap': 5000, 'operates_to': ['GLO', 'WRO', 'LIB'], 'runs_to': []},
    {'name': 'Grudziadz', 'code': 'GRD', 'x': 1140, 'y': 165, 'shown': False, 'owned': False, 'clicked': False, 'cost': 330000, 'passenger_cap': 5000, 'operates_to': ['GDA', 'OLZ', 'BYD', 'TOR'], 'runs_to': []},
    {'name': 'Siedlce', 'code': 'SID', 'x': 1400, 'y': 285, 'shown': False, 'owned': False, 'clicked': False, 'cost': 200000, 'passenger_cap': 4000, 'operates_to': ['WSW', 'BIA', 'LUB'], 'runs_to': []},
    {'name': 'Tarnow', 'code': 'TAR', 'x': 1305, 'y': 510, 'shown': False, 'owned': False, 'clicked': False, 'cost': 420000, 'passenger_cap': 5000, 'operates_to': ['KRA', 'RZS'], 'runs_to': []},
    {'name': 'Arnhem', 'code': 'ARN', 'x': 250, 'y': 290, 'shown': False, 'owned': False, 'clicked': False, 'cost': 720000, 'passenger_cap': 8000, 'operates_to': ['UTR', 'NIJ', 'ENS', 'ZWL', 'AMS'], 'runs_to': []},
    {'name': 'Maastricht', 'code': 'MAA', 'x': 250, 'y': 410, 'shown': False, 'owned': False, 'clicked': False, 'cost': 490000, 'passenger_cap': 6000, 'operates_to': ['AAC', 'LIE', 'EIN'], 'runs_to': []},
    {'name': 'Osnabruck', 'code': 'OSN', 'x': 405, 'y': 270, 'shown': False, 'owned': False, 'clicked': False, 'cost': 750000, 'passenger_cap': 8000, 'operates_to': ['OLD', 'BIE', 'MUN', 'ENS'], 'runs_to': []},
    {'name': 'Enschede', 'code': 'ENS', 'x': 320, 'y': 265, 'shown': False, 'owned': False, 'clicked': False, 'cost': 690000, 'passenger_cap': 8000, 'operates_to': ['ZWL', 'APL', 'ARN', 'OSN', 'MUN', 'ESS'], 'runs_to': []},
]

trains = [
    {'make': 'Express', 'model': 'DT-4', 'icon': express_red, 'shown': False, 'unlocked': False, 'cost': 300000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 100, 'profit_per_person_per_km': 0.025, 'desc': 'The most basic train of the lot. Small yet reliable for transporting your first passengers, or for serving new connections.'},
{'make': 'Express', 'model': 'DT-5A', 'icon': express_orange, 'shown': False, 'unlocked': False, 'cost': 340000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 100, 'profit_per_person_per_km': 0.025},
{'make': 'Express', 'model': 'DT-5B', 'icon': express_green, 'shown': False, 'unlocked': False, 'cost': 350000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 110, 'profit_per_person_per_km': 0.028},
{'make': 'Express', 'model': 'DT-6', 'icon': express_blue, 'shown': False, 'unlocked': False, 'cost': 400000, 'train_type': 'Diesel', 'capacity': 300, 'speed': 112, 'profit_per_person_per_km': 0.03},
{'make': 'RailSpark', 'model': 'Ember', 'icon': railspark_ember, 'shown': False, 'unlocked': False, 'cost': 650000, 'train_type': 'Diesel', 'capacity': 400, 'speed': 105, 'profit_per_person_per_km': 0.025},
{'make': 'RailSpark', 'model': 'Torrent', 'icon': railspark_torrent, 'shown': False, 'unlocked': False, 'cost': 600000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 160, 'profit_per_person_per_km': 0.04},
{'make': 'RailSpark', 'model': 'Bulb', 'icon': railspark_bulb, 'shown': False, 'unlocked': False, 'cost': 200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 140, 'profit_per_person_per_km': 0.05},
{'make': 'RailSpark', 'model': 'Mystic', 'icon': railspark_mystic, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 375, 'speed': 180, 'profit_per_person_per_km': 0.06},
{'make': 'North Star', 'model': 'Ursa', 'icon': north_star_green, 'shown': False, 'unlocked': False, 'cost': 500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 80, 'profit_per_person_per_km': 0.02},
{'make': 'North Star', 'model': 'Maris', 'icon': north_star_purple, 'shown': False, 'unlocked': False, 'cost': 320000, 'train_type': 'Electric', 'capacity': 200, 'speed': 120, 'profit_per_person_per_km': 0.03},
{'make': 'North Star', 'model': 'Polaris', 'icon': north_star_red, 'shown': False, 'unlocked': False, 'cost': 1600000, 'train_type': 'Electric', 'capacity': 400, 'speed': 134, 'profit_per_person_per_km': 0.045},
{'make': 'North Star', 'model': 'Polaris-2', 'icon': north_star_yellow, 'shown': False, 'unlocked': False, 'cost': 2150000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.045},
{'make': 'Thompson Lines', 'model': 'AC-76', 'icon': thompson_lines_red, 'shown': False, 'unlocked': False, 'cost': 150000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 110, 'profit_per_person_per_km': 0.02},
{'make': 'Thompson Lines', 'model': 'AC-77', 'icon': thompson_lines_blue, 'shown': False, 'unlocked': False, 'cost': 160000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 120, 'profit_per_person_per_km': 0.02},
{'make': 'Erlington Works', 'model': 'Jubilee-A', 'icon': erlington_works, 'shown': False, 'unlocked': False, 'cost': 900000, 'train_type': 'Electric', 'capacity': 50, 'speed': 50, 'profit_per_person_per_km': 1.0},
{'make': 'Erlington Works', 'model': 'Jubilee-B', 'icon': erlington_works_2, 'shown': False, 'unlocked': False, 'cost': 1100000, 'train_type': 'Electric', 'capacity': 75, 'speed': 75, 'profit_per_person_per_km': 0.5},
{'make': 'Royal', 'model': 'Bronze', 'icon': royal_bronze, 'shown': False, 'unlocked': False, 'cost': 3620000, 'train_type': 'Electric', 'capacity': 200, 'speed': 150, 'profit_per_person_per_km': 0.2},
{'make': 'Royal', 'model': 'Silver', 'icon': royal_silver, 'shown': False, 'unlocked': False, 'cost': 4200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 170, 'profit_per_person_per_km': 0.5},
{'make': 'Royal', 'model': 'Gold', 'icon': royal_gold, 'shown': False, 'unlocked': False, 'cost': 5000000, 'train_type': 'Electric', 'capacity': 50, 'speed': 185, 'profit_per_person_per_km': 1.0},
{'make': 'Royal', 'model': 'Diamond', 'icon': royal_diamond, 'shown': False, 'unlocked': False, 'cost': 9900000, 'train_type': 'MagLev', 'capacity': 20, 'speed': 200, 'profit_per_person_per_km': 4.0},
{'make': 'Mr Peng Enterprises', 'model': 'Peng-01', 'icon': peng_enterprises, 'shown': False, 'unlocked': False, 'cost': 43000000, 'train_type': 'Electric', 'capacity': 500, 'speed': 200, 'profit_per_person_per_km': 0.055},
{'make': 'Guangdong Star', 'model': 'Star of China', 'icon': guangdong_star, 'shown': False, 'unlocked': False, 'cost': 0, 'train_type': 'MagLev', 'capacity': 0, 'speed': 0, 'profit_per_person_per_km': 0},
{'make': 'Wang Li', 'model': 'Wang-01', 'icon': wang_li, 'shown': False, 'unlocked': False, 'cost': 18000000, 'train_type': 'Diesel', 'capacity': 1200, 'speed': 150, 'profit_per_person_per_km': 0.02},
{'make': 'Yangtze Monos', 'model': 'Current', 'icon': yangtze_monos, 'shown': False, 'unlocked': False, 'cost': 11500000, 'train_type': 'Monorail', 'capacity': 100, 'speed': 120, 'profit_per_person_per_km': 0.2},
{'make': 'West Network', 'model': 'Bullet', 'icon': west_network, 'shown': False, 'unlocked': False, 'cost': 600000000, 'train_type': 'MagLev', 'capacity': 600, 'speed': 300, 'profit_per_person_per_km': 0.4},
{'make': 'Great Northern', 'model': 'Piercer', 'icon': great_northern, 'shown': False, 'unlocked': False, 'cost': 12250000, 'train_type': 'Electric', 'capacity': 300, 'speed': 180, 'profit_per_person_per_km': 0.05},
{'make': 'Southern Star', 'model': 'Solo', 'icon': southern_star, 'shown': False, 'unlocked': False, 'cost': 24000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 200, 'profit_per_person_per_km': 0.2},
{'make': 'Eastern Power', 'model': 'Taurus', 'icon': eastern_power, 'shown': False, 'unlocked': False, 'cost': 9000000, 'train_type': 'Diesel', 'capacity': 900, 'speed': 100, 'profit_per_person_per_km': 0.04},
{'make': 'Red Hill', 'model': 'Baron', 'icon': red_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.03},
{'make': 'Blue Hill', 'model': 'Ocean', 'icon': blue_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'profit_per_person_per_km': 0.03},
{'make': 'Hermann Monorails', 'model': 'HM-11W', 'icon': hermann_orange, 'shown': False, 'unlocked': False, 'cost': 11000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 140, 'profit_per_person_per_km': 0.2},
{'make': 'Hermann Monorails', 'model': 'HM-12W', 'icon': hermann_green, 'shown': False, 'unlocked': False, 'cost': 12000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 150, 'profit_per_person_per_km': 0.2},
]

owned_trains = []

lines = [
    # Reds
    {"class": "Red", "name": "Light Red", "color":  pygame.Color(255, 102, 102), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red", "color":        pygame.Color(255, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Dark Red 1", "color": pygame.Color(204, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Dark Red 2", "color": pygame.Color(153, 0, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Yellows
    {"class": "Yellow", "name": "Light Yellow",  "color":  pygame.Color(255, 255, 153), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow",        "color":        pygame.Color(255, 255, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Dark Yellow 1", "color": pygame.Color(204, 204, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Dark Yellow 2", "color": pygame.Color(153, 153, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Greens
    {"class": "Green", "name": "Green", "color": pygame.Color(0, 255, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Dark Green 1", "color": pygame.Color(0, 204, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Dark Green 2", "color": pygame.Color(0, 153, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Dark Green 3", "color": pygame.Color(0, 102, 0), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Light Blues
    {"class": "Light Blue", "name": "Light Light Blue", "color":  pygame.Color(153, 255, 255), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Light Blue", "color":        pygame.Color(0, 255, 255), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Dark Light Blue 1", "color": pygame.Color(0, 204, 204), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Dark Light Blue 2", "color": pygame.Color(0, 153, 153), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Blues
    {"class": "Blue", "name": "Light Blue", "color":    pygame.Color(80, 80, 255), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue", "color":          pygame.Color(0, 0, 255), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Darker Blue 1", "color": pygame.Color(0, 0, 110), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Darker Blue 2", "color": pygame.Color(0, 0, 40), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Purples
    {"class": "Purple", "name": "Dark Purple 1", "color":    pygame.Color(204, 0, 204), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Dark Purple 2", "color":    pygame.Color(179, 0, 179), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple", "color":           pygame.Color(153, 0, 153), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Very Dark Purple", "color": pygame.Color(102, 0, 102), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Pinks
    {"class": "Pink", "name": "Light Pink", "color":        pygame.Color(255, 192, 203), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Pink", "name": "Hot Pink", "color":          pygame.Color(255, 105, 180), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Pink", "name": "Deep Pink", "color":         pygame.Color(255, 20, 147),  "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Pink", "name": "Medium Violet Red", "color": pygame.Color(199, 21, 133), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},

    # Browns
    {"class": "Brown", "name": "Light Brown", "color":  pygame.Color(181, 101, 29), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Medium Brown", "color": pygame.Color(160, 82, 45), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown", "color":        pygame.Color(139, 69, 19), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Dark Brown", "color":   pygame.Color(101, 67, 33), "shown": False, "owned": False, "finished": True, "stations": [], "trains": [], "money_earned": 0}
]

upgrades = []


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
    key = pygame.key.get_pressed()
    for event in pygame.event.get(exclude=pygame.MOUSEBUTTONUP):
        if event.type == pygame.KEYDOWN:
            if key[pygame.K_BACKSPACE]:
                username = username[:-1]
            elif key[pygame.K_RETURN]:
                name_chosen = True
            elif event.unicode:
                username += event.unicode

    return [username, name_chosen]

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
        # draws map - map has already been adjusted to fill screen size
        screen.fill("black")
        screen.blit(map,(0,0))

        # left side menus
        # money          
        box_top = height - 240
        rect = pygame.Rect(25, box_top, 300, H2_SIZE * 2)
        pygame.draw.rect(screen, "black", rect)
        text = font_h2.render(f"€{round(euros)}", True, pygame.Color(232, 170, 0))
        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/2)-(text.get_height()/2)))
        box_top += H2_SIZE * 2

        if button_check(rect):
            money_clicked = True

        # clock
        # background
        rect = pygame.Rect(25, box_top, 120, 120)
        pygame.draw.rect(screen, pygame.Color(128, 50, 1), rect)
        # face
        pygame.draw.circle(screen, "white", (85, box_top+60), 46)

        # date
        rect = pygame.Rect(25, box_top + 120, 120, 60)
        pygame.draw.rect(screen, "pink", rect)

        font_h3.set_bold(True)
        text = font_h3.render(f'{day} {list(months.keys())[month-1]}', True, "black")
        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/4)-(text.get_height()/2)+5))
        text = font_h3.render(f'{year}', True, "black")
        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*3/4)-(text.get_height()/2)-5))
        font_h3.set_bold(False)

        # graph
        rect = pygame.Rect(145, box_top, 180, 180)
        pygame.draw.rect(screen, pygame.Color(232, 170, 0), rect)

        rect = pygame.Rect(150, box_top+5, 170, 170)
        pygame.draw.rect(screen, "black", rect)

        # tips
        tips("","","",font_h5,font_h5,font_h5)

        tutorial = True
        owned = 0
        for station in stations:
            if station["owned"]:
                owned += 1
        if owned == 0:
            tips("", "Click on the station in the centre of the map", "", font_h3, font_h3, font_h3)
            for station in stations:
                if station["shown"]:
                    pygame.draw.circle(screen, "yellow", (station["x"]+2.5,station["y"]+2.5), 15)
            clicked = False
            for station in stations:
                if station["clicked"]:
                    clicked = True
            if clicked:
                tips("", "Click 'PURCHASE' to buy the station", "", font_h3, font_h3, font_h3)
        elif owned in range(1,3):
            tips("Look in the bottom left corner", "That area shows the date, and how much money you have", "Click on your money to view how it's been changing", font_h3, font_h4, font_h4)
            if money_clicked:
                tips("Now, purchase two more stations on the map", "More stations will appear based on the ones you have purchased", "", font_h3, font_h4, font_h4)
        elif owned == 3:
            tips("You can click anywhere on the screen to clear the", "little station menus", "", font_h3, font_h3, font_h4)
            clicked = False
            for station in stations:
                if station["clicked"]:
                    clicked = True
            if not clicked:
                tips("Now, look at the menu in the bottom right corner", "Make sure you're on the 'Line' menu,", "then click on a colour of line you like.", font_h3, font_h4, font_h4)
                for line in lines:
                    if line["shown"]:
                        tips("", "Click 'Purchase Line'", "", font_h4, font_h3, font_h4)
                    if line["owned"]:
                        tips("", "Click 'Build Line'", "", font_h4, font_h3, font_h4)
                    if line_build and line["stations"] == []:
                        tips("Click on your three purchased stations to connect them with a line.", "Look at the flashing lines to see which of your stations can link", "together. Once done, press enter to finish building the line", font_h5, font_h5, font_h5)
            line_owned = False
            for line in lines:
                if line["finished"] and line["stations"] != []:
                    line_owned = True
            if line_owned:
                tips("", "Next, click on the 'Trains' menu", "", font_h4, font_h3, font_h4)
                if menu_page == "Trains":
                    tips("", "Select one of the trains and click 'Unlock'", "", font_h4, font_h3, font_h4)
                    for train in trains:
                        if train["unlocked"] and train["shown"]:
                            tips("", "Click 'Purchase Train'", "", font_h4, font_h3, font_h4)
                if train_purchase:
                    tips("In the side menu, click the icon for the line", "that you purchased earlier. This adds your selected", "train to that line.", font_h4,font_h4,font_h4)
                    tutorial_final = True
        if tutorial_final and not train_purchase:
            tips("You will now see your money increase every day, depending", "on the statistics of the train you purchased.", "Click anywhere to continue", font_h4, font_h4, font_h5)
            rect = pygame.Rect(0,0,width,height)
            if button_check(rect):
                name_select = True
                tutorial_final = False
        if name_select:
            tips("Congratulations, you have completed the tutorial.", "Please choose a name for your train company", username, font_h4, font_h4, font_h3)       
            returned = name_change(username)
            username = returned[0]
            if returned[1]:
                name_select = False
                congratulations = True
        if congratulations:
            tips("", f"Welcome to [insert game name], {username}", "", font_h4, font_h3, font_h4)
            tutorial = False

                            
        # right side menus
        # top selection
        x_across = width - 25 - (32 / ROWS) * ROW_HEIGHT - SPACING
        y_down = height - (ROWS-32 % 32 / ROWS) * ROW_HEIGHT - SPACING - H2_SIZE
        MENU_WIDTH = (32 / ROWS) * ROW_HEIGHT + SPACING*2

        # mini menu titles
        title_rects = []
        titles = ['Lines', 'Trains', 'Upgrades']
        for title in titles:
            if menu_page == title:
                color = pygame.Color(210,210,210)
            else:
                color = pygame.Color(160,160,160)


            rect = pygame.Rect(x_across, y_down, MENU_WIDTH/3, H2_SIZE)
            pygame.draw.rect(screen, color, rect)
            text = font_h3.render(title, True, "black")
            screen.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]/2-text.get_height()/2-2))
            pygame.draw.line(screen, "black", (x_across+1,y_down), (x_across+1,y_down+H2_SIZE), width=4)
            x_across += MENU_WIDTH/3
            title_rects.append(rect)

        x_across = width - 25 - (32 / ROWS) * ROW_HEIGHT - SPACING
        y_down = height - (ROWS-32 % 32 / ROWS) * ROW_HEIGHT - SPACING - H2_SIZE - 2
        rect = pygame.Rect(x_across, y_down, MENU_WIDTH, H2_SIZE)
        pygame.draw.rect(screen, 'black', rect, width=4)

        for rect in title_rects:
            if button_check(rect):
                menu_page = titles[title_rects.index(rect)]

        x_shift = 0

        if menu_page == "Lines":
            # lines
            x_across = width - 25 - (len(lines) / ROWS) * ROW_HEIGHT
            y_down = height - (ROWS-(len(lines) % (len(lines) / ROWS))) * ROW_HEIGHT - SPACING
            rect = pygame.Rect(x_across-SPACING, y_down-SPACING, (len(lines) / ROWS) * ROW_HEIGHT + SPACING*2, (ROWS-(len(lines) % (len(lines) / ROWS))) * ROW_HEIGHT + SPACING*2)
            pygame.draw.rect(screen, pygame.Color(210,210,210), rect)
            line_rects = []
            for line in range(len(lines)):
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2)
                pygame.draw.rect(screen, lines[line]["color"], rect)
                line_rects.append(rect)

                if not lines[line]["owned"]:
                    screen.blit(lock, (x_across+SPACING, y_down+SPACING))

                y_down += ROW_HEIGHT
                x_shift += 1
                if x_shift == ROWS:
                    y_down = height - (ROWS-(len(lines) % (len(lines) / ROWS))) * ROW_HEIGHT - SPACING
                    x_across += ROW_HEIGHT
                    x_shift = 0
                
            for rect in line_rects:
                if not train_purchase:
                    if button_check(rect):
                        for item in trains+lines+upgrades:
                            item["shown"] = False
                        lines[line_rects.index(rect)]["shown"] = True

        if menu_page == "Trains":
            # lines
            x_across = width - 25 - (len(trains) / ROWS) * ROW_HEIGHT
            y_down = height - (ROWS-(len(trains) % (len(trains) / ROWS))) * ROW_HEIGHT - SPACING
            rect = pygame.Rect(x_across-SPACING, y_down-SPACING, (len(lines) / ROWS) * ROW_HEIGHT + SPACING*2, (ROWS-(len(trains) % (len(trains) / ROWS))) * ROW_HEIGHT + SPACING*2)
            pygame.draw.rect(screen, pygame.Color(210,210,210), rect)
            train_rects = []
            for train in range(len(trains)):
                screen.blit(trains[train]['icon'], (x_across+SPACING, y_down+SPACING))
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2)
                train_rects.append(rect)

                if not trains[train]["unlocked"]:
                    screen.blit(lock, (x_across+SPACING, y_down+SPACING))

                y_down += ROW_HEIGHT
                x_shift += 1
                if x_shift == ROWS:
                    y_down = height - (ROWS-(len(trains) % (len(trains) / ROWS))) * ROW_HEIGHT - SPACING
                    x_across += ROW_HEIGHT
                    x_shift = 0
                
            for rect in train_rects:
                if button_check(rect):
                    for item in trains+lines+upgrades:
                        item["shown"] = False
                    trains[train_rects.index(rect)]["shown"] = True

        if menu_page == "Upgrades":
            pass

        x_across = width - 25 - (32 / ROWS) * ROW_HEIGHT - SPACING
        y_down = height - (ROWS-(32 % (32 / ROWS))) * ROW_HEIGHT - SPACING*2
        pygame.draw.line(screen, "black", (x_across+1, y_down), (x_across+1, height), width=4)
        pygame.draw.line(screen, "black", (width-22, y_down), (width-22, height), width=4)

        # popup answers
        for item in trains+lines+upgrades:
            if item["shown"]:
                x_across = width - 25 - (32 / ROWS) * ROW_HEIGHT - SPACING - 250
                y_down = height - (ROWS-(32 % (32 / ROWS))) * ROW_HEIGHT - SPACING*2
                rect = pygame.Rect(x_across, y_down, 254, height-y_down + 4)
                pygame.draw.rect(screen, pygame.Color(210,210,210), rect)
                pygame.draw.rect(screen, "black", rect, width=4)

                if item in lines:
                    y_down += 6

                    text = font_h3.render(f'{item["name"]} Line', True, "black")
                    screen.blit(text, (x_across+8, y_down))
                    rect = pygame.Rect(x_across+213, y_down+2, 29, 29)
                    pygame.draw.rect(screen, item["color"], rect)
                    y_down += H3_SIZE

                    text = font_h4.render(f'{item["class"]} class line', True, "black")
                    screen.blit(text, (x_across+8, y_down))
                    y_down += H4_SIZE + 6

                    pygame.draw.line(screen, pygame.Color(160,160,160), (x_across+4, y_down),(x_across+249, y_down), width = 4)
                    pygame.draw.line(screen, pygame.Color(160,160,160), (x_across+127, y_down), (x_across+127, height - 55), width = 4)
                    y_down += 4

                    text = font_h5.render("Trains Running", True, "black")
                    screen.blit(text, (x_across + 8, y_down))
                    text = font_h5.render(str(len(item["trains"])), True, "black")
                    screen.blit(text, (x_across + 123 - text.get_width(), y_down ))
                    text = font_h5.render("Value Y", True, "black")
                    screen.blit(text, (x_across + 133, y_down))
                    text = font_h5.render(str(0), True, "black")
                    screen.blit(text, (x_across + 246 - text.get_width(), y_down))
                    y_down += H5_SIZE + 2

                    text = font_h5.render("Value Z", True, "black")
                    screen.blit(text, (x_across + 8, y_down))
                    text = font_h5.render("0", True, "black")
                    screen.blit(text, (x_across + 123 - text.get_width(), y_down ))
                    text = font_h5.render("Money Earnt", True, "black")
                    screen.blit(text, (x_across + 133, y_down))
                    text = font_h5.render(f'€{item["money_earned"]}', True, "black")
                    screen.blit(text, (x_across + 246 - text.get_width(), y_down))

                    if not item["owned"]:
                        font_h4.set_bold(True)
                        rect = pygame.Rect(x_across+10, height - 50, 115, 44)
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h4.render("Purchase", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/3)-(text.get_height()/2)))
                        text = font_h4.render("Line", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                    else:
                        font_h4.set_bold(True)
                        rect = pygame.Rect(x_across+10, height - 50, 115, 44)
                        pygame.draw.rect(screen, pygame.Color(160, 160, 160), rect)
                        text = font_h4.render("OWNED", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/2)-(text.get_height()/2)))

                    if button_check(rect):
                        lines[lines.index(item)]["owned"] = True

                    rect = pygame.Rect(x_across+129, height - 50, 115, 44)
                    pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                    text = font_h4.render("Build", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/3)-(text.get_height()/2)))
                    text = font_h4.render("Line", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                    font_h4.set_bold(False)

                    if button_check(rect):
                        line_build = True
                        item["finished"] = False
                    if line_build:
                        pygame.draw.rect(screen, "black", rect)
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
                        
                        if not tutorial:
                            tips("Current Line Path", ", ".join(item["stations"]) if len(item["stations"]) > 0 else "None", "Press enter to finish building line, or escape to cancel build", font_h4, font_h3, font_h4)

                if item in trains:
                    y_down += 6

                    text = font_h3.render(item["make"], True, "black")
                    screen.blit(text, (x_across+8, y_down))
                    screen.blit(item["icon"], (x_across+248-item["icon"].get_width(), y_down))
                    y_down += H3_SIZE

                    text = font_h4.render(item["model"], True, "black")
                    screen.blit(text, (x_across+8, y_down))
                    y_down += H4_SIZE + 6

                    pygame.draw.line(screen, pygame.Color(160,160,160), (x_across+4, y_down),(x_across+249, y_down), width = 4)
                    pygame.draw.line(screen, pygame.Color(160,160,160), (x_across+127, y_down), (x_across+127, height - 55), width = 4)
                    y_down += 4

                    text = font_h5.render("Capacity", True, "black")
                    screen.blit(text, (x_across + 8, y_down))
                    text = font_h5.render(str(item["capacity"]), True, "black")
                    screen.blit(text, (x_across + 123 - text.get_width(), y_down ))
                    text = font_h5.render("Type", True, "black")
                    screen.blit(text, (x_across + 133, y_down))
                    text = font_h5.render(item["train_type"], True, "black")
                    screen.blit(text, (x_across + 246 - text.get_width(), y_down))
                    y_down += H5_SIZE + 2

                    text = font_h5.render("Top Speed", True, "black")
                    screen.blit(text, (x_across + 8, y_down))
                    text = font_h5.render(f'{item["speed"]}km/h', True, "black")
                    screen.blit(text, (x_across + 123 - text.get_width(), y_down ))
                    text = font_h5.render("Profit PP", True, "black")
                    screen.blit(text, (x_across + 133, y_down))
                    text = font_h5.render(f'€{item["profit_per_person_per_km"]}', True, "black")
                    screen.blit(text, (x_across + 246 - text.get_width(), y_down))

                    # for char in item["desc"]:
                    # desc writing - 34 char per horizontal

                    if not item["unlocked"]:
                        font_h3.set_bold(True)
                        rect = pygame.Rect(x_across+10, height - 50, 234, 44)
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h3.render("Unlock", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/2)-(text.get_height()/2)-2))
                        font_h3.set_bold(False)

                        if button_check(rect):
                            item["unlocked"] = True

                    else:
                        font_h4.set_bold(True)
                        rect = pygame.Rect(x_across+10, height - 50, 115, 44)
                        pygame.draw.rect(screen, pygame.Color(54, 153, 43), rect)
                        text = font_h4.render("Purchase", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/3)-(text.get_height()/2)))
                        text = font_h4.render("Train", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                        
                        if button_check(rect):
                            train_purchase = True
                        if train_purchase:
                            menu_page = "Lines"
                            if not tutorial:
                                tips("Choose which line you'd like this train to run on.", f'This train requires a {item["train_type"]} line.', "", font_h3, font_h3)
                            for rect in line_rects:
                                if button_check(rect) and lines[line_rects.index(rect)]["owned"]:
                                    lines[line_rects.index(rect)]["trains"].append(item["model"])
                                    menu_page = "Trains"
                                    train_purchase = False


                        rect = pygame.Rect(x_across+129, height - 50, 115, 44)
                        pygame.draw.rect(screen, "red", rect)
                        text = font_h4.render("Upgrade", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/3)-(text.get_height()/2)))
                        text = font_h4.render("Train", True, "white")
                        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)))
                        font_h4.set_bold(False)

                        if button_check(rect):
                            text = font_h1.render("DOESNT WORK YET", True, "black")
                            screen.blit(text, (50, 200))

                    

                if item in upgrades:
                    pass


        # close game
        rect = pygame.Rect(width - 50, 10, 40, 40)
        pygame.draw.rect(screen, "red", rect)
        text = font_h2.render("X", True, "white")
        screen.blit(text, (width-41, 14))
        if button_check(rect):
            running = False


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
                for train in line["trains"]:
                    for model in trains:
                        if model["model"] == train:
                            train = model
                    euros_per_trip = train["capacity"] * train["profit_per_person_per_km"] * distance
                    daily_euros += (24 / (distance / train["speed"])) * euros_per_trip
        
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
                if pygame.mouse.get_pos()[0] in range(station["x"]-5,station["x"]+11) and pygame.mouse.get_pos()[1] in range(station["y"]-5,station["y"]+11) and station["shown"]:

                    # determining backing colour based on cost and players money - adds a clearer visualisation of what the player can do with station
                    if station in stations and not station["owned"] and station["cost"] > euros:
                        bg_color = pygame.Color(217, 49, 30)
                    elif station in stations and not station["owned"]:
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

            # station labels
            if station["clicked"] and not line_build: 
                draw_station(station, pygame.Color(54, 153, 43))
                BOX_WIDTH = 135
                BOX_HEIGHT = H5_SIZE * 5
                # box down
                if station["y"] - (H5_SIZE * 5 + 30) < 20:
                    box = pygame.Vector2(station["x"] - 65, station["y"] + ((H5_SIZE * 5 + 10)-H5_SIZE * 5) + 5) # used V2 then rect
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 
                # box up
                else:
                    box = pygame.Vector2(station["x"] - 65, station["y"] - (H5_SIZE * 5 + 10))
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

                    font_h4.set_bold(True)
                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+6, BOX_WIDTH-8, H5_SIZE*5-(H4_SIZE+6)-4)
                    pygame.draw.rect(screen, color, rect)
                    # printing purchase details on station
                    text = font_h4.render(words_1, True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, rect[1]+2))
                    text = font_h4.render(words_2, True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, rect[1]+4+H5_SIZE))
                    font_h4.set_bold(False)

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
                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+6, BOX_WIDTH-8, H5_SIZE*5-(H4_SIZE+6)-4)
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

        text = font_h5.render(str(pygame.mouse.get_pos()), True, "black")
        screen.blit(text, (pygame.mouse.get_pos()[0]+4, pygame.mouse.get_pos()[1]+4))


    pygame.display.flip()

    # for flashing/pulsing items such as lines in purchase phase
    if flash < 1:
        flash += 1.1 * dt
    else:
        flash -= 1
    
    # dt is time between frames, makes flashing smoother.
    dt = clock.tick(1000)/1000

    seconds_since_date_update += dt
    if seconds_since_date_update >= 2:
        seconds_since_date_update = 0
        day += 1
        euros += daily_euros
        if months[list(months.keys())[month-1]] < day:
            month += 1
            day = 1
        if month > 12:
            year += 1
            month = 1
    daily_euros = 0


pygame.quit()
import math
import pygame
import numpy as np
from scipy.spatial import Delaunay
import random

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
loop = True

# sizes
width = screen.get_width()
height = screen.get_height()
ROWS = 4
ROW_HEIGHT = 60
SPACING = 8

# images
# map = pygame.image.load("zug_fallt_aus/assets/north-europe-map.png")
# init_map_w = map.get_width()
# init_map_h = map.get_height()
# map = pygame.transform.scale(map, (width-300, (height * (map.get_width()/(width+300))))) # adjusts map size so the width of the map is the same as the width of the screen
lock = pygame.image.load("zug_fallt_aus/assets/lock.png")
lock = pygame.transform.scale(lock, (ROW_HEIGHT-SPACING*2, ROW_HEIGHT-SPACING*2))

speed = 60

scale_level = 0

# map = pygame.image.load("zug_fallt_aus/assets/train_icons/red-hill.png")
map_loc = pygame.Vector2(0,0)

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
trains = [
{'make': 'Express', 'model': 'DT-4', 'icon': express_red, 'shown': False, 'unlocked': False, 'cost': 300000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 100, 'ppppkm': 0.025, 'desc': 'The most basic train of the lot. Small yet reliable for transporting your first passengers, or for serving new connections.', 'level': 0},
{'make': 'Express', 'model': 'DT-5A', 'icon': express_orange, 'shown': False, 'unlocked': False, 'cost': 340000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 100, 'ppppkm': 0.025, 'level': 0},
{'make': 'Express', 'model': 'DT-5B', 'icon': express_green, 'shown': False, 'unlocked': False, 'cost': 350000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 110, 'ppppkm': 0.028, 'level': 0},
{'make': 'Express', 'model': 'DT-6', 'icon': express_blue, 'shown': False, 'unlocked': False, 'cost': 400000, 'train_type': 'Diesel', 'capacity': 300, 'speed': 112, 'ppppkm': 0.03, 'level': 0},
{'make': 'RailSpark', 'model': 'Ember', 'icon': railspark_ember, 'shown': False, 'unlocked': False, 'cost': 650000, 'train_type': 'Diesel', 'capacity': 400, 'speed': 105, 'ppppkm': 0.025, 'level': 0},
{'make': 'RailSpark', 'model': 'Torrent', 'icon': railspark_torrent, 'shown': False, 'unlocked': False, 'cost': 600000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 160, 'ppppkm': 0.04, 'level': 0},
{'make': 'RailSpark', 'model': 'Bulb', 'icon': railspark_bulb, 'shown': False, 'unlocked': False, 'cost': 200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 140, 'ppppkm': 0.05, 'level': 0},
{'make': 'RailSpark', 'model': 'Mystic', 'icon': railspark_mystic, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 375, 'speed': 180, 'ppppkm': 0.06, 'level': 0},
{'make': 'North Star', 'model': 'Ursa', 'icon': north_star_green, 'shown': False, 'unlocked': False, 'cost': 500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 80, 'ppppkm': 0.02, 'level': 0},
{'make': 'North Star', 'model': 'Maris', 'icon': north_star_red, 'shown': False, 'unlocked': False, 'cost': 320000, 'train_type': 'Electric', 'capacity': 200, 'speed': 120, 'ppppkm': 0.03, 'level': 0},
{'make': 'North Star', 'model': 'Polaris', 'icon': north_star_purple, 'shown': False, 'unlocked': False, 'cost': 1600000, 'train_type': 'Electric', 'capacity': 400, 'speed': 134, 'ppppkm': 0.045, 'level': 0},
{'make': 'North Star', 'model': 'Polaris-2', 'icon': north_star_yellow, 'shown': False, 'unlocked': False, 'cost': 2150000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'ppppkm': 0.045, 'level': 0},
{'make': 'Thompson Lines', 'model': 'AC-76', 'icon': thompson_lines_red, 'shown': False, 'unlocked': False, 'cost': 150000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 110, 'ppppkm': 0.02, 'level': 0},
{'make': 'Thompson Lines', 'model': 'AC-77', 'icon': thompson_lines_blue, 'shown': False, 'unlocked': False, 'cost': 160000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 120, 'ppppkm': 0.02, 'level': 0},
{'make': 'Erlington Works', 'model': 'Jubilee-A', 'icon': erlington_works, 'shown': False, 'unlocked': False, 'cost': 900000, 'train_type': 'Electric', 'capacity': 50, 'speed': 50, 'ppppkm': 1.0, 'level': 0},
{'make': 'Erlington Works', 'model': 'Jubilee-B', 'icon': erlington_works_2, 'shown': False, 'unlocked': False, 'cost': 1100000, 'train_type': 'Electric', 'capacity': 75, 'speed': 75, 'ppppkm': 0.5, 'level': 0},
{'make': 'Royal', 'model': 'Bronze', 'icon': royal_bronze, 'shown': False, 'unlocked': False, 'cost': 3620000, 'train_type': 'Electric', 'capacity': 200, 'speed': 150, 'ppppkm': 0.2, 'level': 0},
{'make': 'Royal', 'model': 'Silver', 'icon': royal_silver, 'shown': False, 'unlocked': False, 'cost': 4200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 170, 'ppppkm': 0.5, 'level': 0},
{'make': 'Royal', 'model': 'Gold', 'icon': royal_gold, 'shown': False, 'unlocked': False, 'cost': 5000000, 'train_type': 'Electric', 'capacity': 50, 'speed': 185, 'ppppkm': 1.0, 'level': 0},
{'make': 'Royal', 'model': 'Diamond', 'icon': royal_diamond, 'shown': False, 'unlocked': False, 'cost': 9900000, 'train_type': 'MagLev', 'capacity': 20, 'speed': 200, 'ppppkm': 4.0, 'level': 0},
{'make': 'Mr Peng Enterprises', 'model': 'Peng-01', 'icon': peng_enterprises, 'shown': False, 'unlocked': False, 'cost': 43000000, 'train_type': 'Electric', 'capacity': 500, 'speed': 200, 'ppppkm': 0.055, 'level': 0},
{'make': 'Guangdong Star', 'model': 'Star of China', 'icon': guangdong_star, 'shown': False, 'unlocked': False, 'cost': 850000000, 'train_type': 'MagLev', 'capacity': 800, 'speed': 250, 'ppppkm': 0.6, 'level': 0},
{'make': 'Wang Li', 'model': 'Wang-01', 'icon': wang_li, 'shown': False, 'unlocked': False, 'cost': 18000000, 'train_type': 'Diesel', 'capacity': 1200, 'speed': 150, 'ppppkm': 0.02, 'level': 0},
{'make': 'Yangtze Monos', 'model': 'Current', 'icon': yangtze_monos, 'shown': False, 'unlocked': False, 'cost': 11500000, 'train_type': 'Monorail', 'capacity': 100, 'speed': 120, 'ppppkm': 0.2, 'level': 0},
{'make': 'West Network', 'model': 'Bullet', 'icon': west_network, 'shown': False, 'unlocked': False, 'cost': 600000000, 'train_type': 'MagLev', 'capacity': 600, 'speed': 300, 'ppppkm': 0.4, 'level': 0},
{'make': 'Great Northern', 'model': 'Piercer', 'icon': great_northern, 'shown': False, 'unlocked': False, 'cost': 12250000, 'train_type': 'Electric', 'capacity': 300, 'speed': 180, 'ppppkm': 0.05, 'level': 0},
{'make': 'Southern Star', 'model': 'Solo', 'icon': southern_star, 'shown': False, 'unlocked': False, 'cost': 24000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 200, 'ppppkm': 0.2, 'level': 0},
{'make': 'Eastern Power', 'model': 'Taurus', 'icon': eastern_power, 'shown': False, 'unlocked': False, 'cost': 9000000, 'train_type': 'Diesel', 'capacity': 900, 'speed': 100, 'ppppkm': 0.04, 'level': 0},
{'make': 'Red Hill', 'model': 'Baron', 'icon': red_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 150, 'ppppkm': 0.03, 'level': 0},
{'make': 'Blue Hill', 'model': 'Ocean', 'icon': blue_hill, 'shown': False, 'unlocked': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'ppppkm': 0.03, 'level': 0},
{'make': 'Hermann Monorails', 'model': 'HM-11W', 'icon': hermann_green, 'shown': False, 'unlocked': False, 'cost': 11000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 140, 'ppppkm': 0.2, 'level': 0},
{'make': 'Hermann Monorails', 'model': 'HM-12W', 'icon': hermann_orange, 'shown': False, 'unlocked': False, 'cost': 12000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 150, 'ppppkm': 0.2, 'level': 0},
]
owned_trains = []
lines = [
    # Reds
    {"class": "Red", "name": "Red-1", "color": pygame.Color(255, 102, 102),  "shown": True, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-2", "color": pygame.Color(255, 0, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-3", "color": pygame.Color(204, 0, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Red", "name": "Red-4", "color": pygame.Color(153, 0, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Oranges
    {"class": "Orange", "name": "Orange-1", "color": pygame.Color(255, 200, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-2", "color": pygame.Color(255, 150, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-3", "color": pygame.Color(255, 100, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Orange", "name": "Orange-4", "color": pygame.Color(255, 50, 0),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Yellows
    {"class": "Yellow", "name": "Yellow-1", "color": pygame.Color(255, 255, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-2", "color": pygame.Color(210, 210, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-3", "color": pygame.Color(150, 150, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Yellow", "name": "Yellow-4", "color": pygame.Color(70, 70, 0),   "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Greens
    {"class": "Green", "name": "Green-1", "color": pygame.Color(0, 255, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-2", "color": pygame.Color(0, 190, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-3", "color": pygame.Color(0, 120, 0), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Green", "name": "Green-4", "color": pygame.Color(0, 70, 0),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Light Blues
    {"class": "Light Blue", "name": "Blue-L1", "color": pygame.Color(80, 225, 225), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L2", "color": pygame.Color(0, 190, 190),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L3", "color": pygame.Color(0, 140, 140),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Light Blue", "name": "Blue-L4", "color": pygame.Color(0, 70, 70),    "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Blues
    {"class": "Blue", "name": "Blue-D1", "color": pygame.Color(80, 80, 255), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D2", "color": pygame.Color(0, 0, 255),   "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D3", "color": pygame.Color(0, 0, 110),   "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Blue", "name": "Blue-D4", "color": pygame.Color(0, 0, 40),    "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Purples
    {"class": "Purple", "name": "Purple-1", "color": pygame.Color(150, 75, 150), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-2", "color": pygame.Color(160, 0, 160),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-3", "color": pygame.Color(110, 0, 110),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Purple", "name": "Purple-4", "color": pygame.Color(50, 0, 50),    "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Pinks
    {"class": "Gray", "name": "Gray-1", "color": pygame.Color(180, 180, 180), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-2", "color": pygame.Color(130, 130, 130), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-3", "color": pygame.Color(80, 80, 80),    "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Gray", "name": "Gray-4", "color": pygame.Color(50, 50, 50),    "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},

    # Browns
    {"class": "Brown", "name": "Brown-1", "color": pygame.Color(181, 101, 29), "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-2", "color": pygame.Color(160, 82, 45),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-3", "color": pygame.Color(139, 69, 19),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0},
    {"class": "Brown", "name": "Brown-4", "color": pygame.Color(101, 67, 33),  "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "money_earned": 0}

]
upgrades = []
# place names
first_names = [
    "Ash", "Bath", "Bay", "Beaver", "Bed", "Bell", "Berry", "Black", "Bloom", "Blue",
    "Brad", "Brent", "Bridge", "Brook", "Cam", "Cedar", "Charl", "Chest", "Clear",
    "Clifton", "Coal", "Clover", "Col", "Cran", "Crow", "Daven", "Day",
    "Deer", "Dover", "Down", "Dun", "East", "Edge", "Elm", "Elk", "Fair", "Farm",
    "Fayette", "Fern", "Fish", "Flat", "Fort", "Fountain", "Fox", "Frank", "Freder",
    "Glen", "Gold", "Green", "Ham", "Han", "Hart", "Hazel", "Hemp", "Hen",
    "High", "Hill", "Hol", "Hope", "Hun", "Iron", "John",
    "Jones", "Ken", "King", "Lake", "Lan", "Laurel", "Law", "Leb", "Lex", "Lime",
    "Lin", "Little", "Liver", "Long", "Lynn", "Man", "Maple", "Mar", "Mart", "May",
    "Mid", "Mill", "Mon", "Mount",  "New", "North", "Oak",
    "Oce", "Olive", "Ox", "Park", "Peach", "Pine", "Plain", "Port",
    "Pow", "Pres", "Prince", "Rain", "Red", "River", "Rock", "Rose", "Rox", "Rush",
    "Ruther", "Saint", "Salt", "Sand", "Scot", "Shel", "Silver",
    "Smith", "Snow", "South", "Spring", "Stan", "Stock", "Sun", "Syl",
    "Tall", "Three", "Tim", "Twin", "Valley", "Vern", "Wake",
    "Wash", "Water", "West", "White", "Willow", "Win", "Wood", "York",
]
last_names = [
    "ville", "ton", "ham", "field", "bury", "ford", "land", "wood", "port", "dale",
    "ridge", "side", "hill", "town", "view", "grove", "creek", "spring", "falls", "lake",
    "bay", "point", "beach", "bend", "summit", "peak", "cross", "fort", "cove", "brook",
    "plains", "groves", "heights", "moor", "hurst", "worth", "combe", "fell", "leigh", "well",
    "gate", "head", "stone", "wick", "holt", "burn", "thorpe", "fleet", "march", "den", "cumbe"
]

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

class Tile:
    def __init__(self, img, top, right, bottom, left):
        self.img = img
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

class City:
    def __init__(self, name, code, loc, cost, passengers, operates_to):
        self.name = name
        self.code = code
        self.loc = loc
        self.shown = True
        self.clicked = False
        self.owned = False
        self.cost = cost
        self.passengers = passengers
        self.operates_to = operates_to


# functions
def button_check(rect):
    if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]-2) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]+1):
        pygame.event.get()
        return True
  
 
def print_text(words, font, color, x, y):
    text = font.render(str(words), True, color)
    screen.blit(text, (x, y))


def draw_lines(lines, cities):
    for line in lines:
        if line["cities"] != [] and item["finished"]:
            for code in range(len(line["cities"])-1):
                for city in cities:
                    if city.code == line["cities"][code]:
                        start_loc = city
                    if city.code == line["cities"][code+1]:
                        end_loc = city

                pygame.draw.line(screen, line["color"], (start_loc.loc.x+2.5, start_loc.loc.y+2.5), (end_loc.loc.x+2.5, end_loc.loc.y+2.5), width = 5)
        

def draw_city(city, color=None, flash=1):
    if (pygame.mouse.get_pos()[0] in range(round(city.loc.x)-5, round(city.loc.x)+10) and pygame.mouse.get_pos()[1] in range(round(city.loc.y)-5,round(city.loc.y)+10)) or flash < 0.5:
        city_inner = pygame.Rect(city.loc.x-2,city.loc.y-2,9,9)

    # no hover
    else:
        city_inner = pygame.Rect(city.loc.x-1,city.loc.y-1,7,7)
    city_outer = pygame.Rect(city.loc.x-5,city.loc.y-5,15,15)

    if color != None:
        pass
    else:
        if not city.owned and city.cost > euros:
            color = pygame.Color(217, 49, 30)
        elif not city.owned:
            color = "white"
        else:
            color = "yellow"

    # pygame.Color(11,188,9)

    pygame.draw.rect(screen, "black", city_outer)
    pygame.draw.rect(screen, color, city_inner)


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


def triangle_overlaps_other_rects(tri_pts, rects):
    for i in range(3):
        p1 = tri_pts[i]
        p2 = tri_pts[(i + 1) % 3]
        for rect_info in rects:
            cx, cy = rect_info["center"]
            # Skip if this rect belongs to an endpoint
            if (p1 == (cx, cy)) or (p2 == (cx, cy)):
                continue
            if rect_info["rect"].clipline(p1, p2):
                return True
    return False

tiles = []
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_1.png"), "green", "green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_2.png"), "desert", "desert", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_3.png"), "desert", "green-desert", "green", "green-desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_4.png"), "green", "desert-green", "desert", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_5.png"), "desert-green", "green", "desert-green", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_6.png"), "green-desert", "desert", "green-desert", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_7.png"), "desert", "desert", "green-desert", "green-desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_8.png"), "green", "green", "desert-green", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_9.png"), "green", "desert-green", "green-desert", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_10.png"), "desert", "green-desert", "desert-green", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_11.png"), "desert-green", "desert-green", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_12.png"), "green-desert", "green-desert", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_13.png"), "desert-green", "green", "green", "green-desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_14.png"), "green-desert", "desert", "desert", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_15.png"), "green", "desert", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_16.png"), "green-desert", "desert", "desert", "green-desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_17.png"), "desert-green", "green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_18.png"), "desert-green", "green", "green", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_19.png"), "desert", "desert", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_20.png"), "green", "green", "green", "green-desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_21.png"), "desert", "desert", "desert", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_22.png"), "green-desert", "desert", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_23.png"), "desert-green", "green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_24.png"), "green", "green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_25.png"), "green", "desert-green", "green-desert", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_26.png"), "green", "desert-green", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_27.png"), "green", "green", "desert", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_28.png"), "desert-green", "green", "green", "desert"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_29.png"), "green", "desert", "desert", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_30.png"), "green", "desert", "green-desert", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_31.png"), "green-desert", "green-desert", "desert-green", "desert-green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_32.png"), "green", "green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_33.png"), "green", "desert-green", "green", "green"))
tiles.append(Tile(pygame.image.load("zug_fallt_aus/assets/procedural_tiles/tile_34.png"), "green", "desert", "desert", "desert-green"))

for tile in tiles[0:1]:
    greens = 0
    if tile.top == "green":
        greens += 1
    elif tile.top in ["desert-green", "green-desert"]:
        greens += 0.4

    if tile.left == "green":
        greens += 1
    elif tile.left in ["desert-green", "green-desert"]:
        greens += 0.4

    if tile.right == "green":
        greens += 1
    elif tile.right in ["desert-green", "green-desert"]:
        greens += 0.4

    if tile.bottom == "green":
        greens += 1
    elif tile.bottom in ["desert-green", "green-desert"]:
        greens += 0.4

    if greens >= 2:
        tiles.append(tile)
    if greens >= 3:
        tiles.append(tile)
    if greens == 4:
        tiles.append(tile)

# generating tile map based on specified sizes 
TILE_SIZE = 100

tile_order = []

# for i in range(0, (width//TILE_SIZE)):
#     tile_order.append(tiles[0])

for slot in range(((width//TILE_SIZE))*(height//TILE_SIZE)):
    good = False
    while True:
        tile = random.choice(tiles)
        while True:
            if slot == 0:
                tile_order.append(tile)
                good = True
                break
                
            elif tile.left == tile_order[-1].right and (slot < ((width//TILE_SIZE)) or tile_order[-(width//TILE_SIZE)].bottom == tile.top):
                tile_order.append(tile)
                good = True
                break
            else:
                break
        if good:
            break

# generating city points based on specified amounts
num_points = 50
points = np.random.rand(num_points, 2)
points *= [width-350, height-250]  # Scale to screen size    
points += [25, 25]

# creating cities
cities_base = []
valid_points = []
deletions = 0
for index, point in enumerate(points):
    first_name = random.choice(first_names)
    first_names.remove(first_name)
    city_name = str(first_name+random.choice(last_names))
    city_loc = pygame.Vector2(point[0], point[1])
    good = True
    for item in cities_base:
        if item["loc"].x-70 <= city_loc.x <= item["loc"].x+70 and item["loc"].y-70 <= city_loc.y <= item["loc"].y+70:
            good = False
            deletions += 1
    if good:
        cities_base.append({"name":city_name, "loc":city_loc})
        valid_points.append([city_loc.x, city_loc.y])

# triangle linkage map
valid_points = np.array(valid_points)
tri = Delaunay(valid_points)    

int_points = [tuple(map(int, p)) for p in valid_points]

# exclusion rects
RECT_SIZE = 65 
half = RECT_SIZE // 2
exclude_rects = [
    {
        "rect": pygame.Rect(x - half, y - half, RECT_SIZE, RECT_SIZE),
        "center": (x, y)
    }
    for x, y in int_points
]

num_cities = len(int_points)
connections = [set() for _ in range(num_cities)]

for simplex in tri.simplices:
    tri_pts = [int_points[i] for i in simplex]

    if triangle_overlaps_other_rects(tri_pts, exclude_rects):
        continue

    i0, i1, i2 = simplex

    connections[i0].update([i1, i2])
    connections[i1].update([i0, i2])
    connections[i2].update([i0, i1])

cities = []
for city in cities_base:
    runs_to = []
    for i, conn in enumerate(connections):
        if city["name"] == cities_base[i]["name"]:
            conns = len(conn)
            runs_to = [int(x) for x in conn]
            for i, x in enumerate(runs_to):
                runs_to[i] = cities_base[x]["name"][0:3].upper()

    cost = round(random.choice(range(10000, 20000))*(random.choice(range(8, 50))), -4)
    
    cities.append(City(city["name"], city["name"][0:3].upper(), city["loc"], cost, round(cost/50*conns), runs_to))


    


while running:
# int(round((495 * map.get_width())/init_map_w)+map_loc.x)

    for event in pygame.event.get(exclude= [pygame.MOUSEBUTTONUP]):
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

        x_across = 0
        y_down = 0
        for slot in range(((width//TILE_SIZE))*(height//TILE_SIZE)):
            screen.blit(tile_order[slot].img, (x_across, y_down))
            x_across += TILE_SIZE

            if x_across >= ((width//TILE_SIZE))*TILE_SIZE:
                x_across = 0
                y_down += TILE_SIZE

        for simplex in tri.simplices:
            tri_pts = [int_points[i] for i in simplex]
            if not triangle_overlaps_other_rects(tri_pts, exclude_rects):
                pygame.draw.polygon(screen, "black", tri_pts, 1)

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
            rect = pygame.Rect((width-300)-20-extra_add, y_down, 40+extra_add, TAB_HEIGHT)
            pygame.draw.rect(screen, color, rect, border_top_left_radius=16, border_bottom_left_radius=16)
            screen.blit(text, ((width-300)-10-extra_add, y_down+(TAB_HEIGHT/2)-(text.get_height()/2)))
            title_rects.append(rect)
            y_down += TAB_HEIGHT + 10

        rect = pygame.Rect((width-300)+18, 0, width-(width-300)-18, height)
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
                        if not item["cities"]:
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
                                item["cities"] = []

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
                            
                            for city in cities:
                                key = pygame.key.get_pressed()
                                rect = pygame.Rect(city.loc.x-5, city.loc.y-5, 15, 15)
                                if item["cities"] == [] and button_check(rect) and item["owned"] and city.owned:
                                    item["cities"].append(city.code)
                                    pygame.draw.rect(screen, "red", rect)
                                elif button_check(rect) and item["cities"][-1] in city.operates_to and len(item["cities"]) < 10 and city.code not in item["cities"] and city.owned:
                                    item["cities"].append(city.code)
                                    pygame.draw.rect(screen, "red", rect)
                                elif key[pygame.K_RETURN]:
                                    item["finished"] = True
                                    line_build = False
                                elif key[pygame.K_ESCAPE]:
                                    item["cities"] = []
                                    line_build = False
                                else:
                                    pass
                                flash_lines = []
                                if item["cities"] != [] and not item["finished"]:
                                    for city in cities:
                                        if item["cities"][-1] == city.code:
                                            for dest in city.operates_to:
                                                flash_lines.append({"cities": [city.code, dest], "color": pygame.Color(160,160,160)})
                            
                            tips("Current Line Path", ", ".join(item["cities"]) if len(item["cities"]) > 0 else "None", "Press enter to finish building line, or escape to cancel build", font_h4, font_h3, font_h4)

                    # other line details
                    y_down = (height - 200) + H3_SIZE+SPACING*2

                    text = font_h4.render(f"Line Route:", True, "black")
                    screen.blit(text, (x_across+8, y_down+8))
                    text = font_h4.render(f"{','.join(item['cities'])}", True, "black")
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
                                    owned_trains.append(Train(item["model"], lines[line_rects.index(rect)]["name"], item["capacity"], item["ppppkm"], item["speed"]))

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

                                item["capacity"] = round(item["capacity"], 3)

                                # train speed
                                if item["model"] in ["Solo"]:
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

                                item["speed"] = round(item["speed"], 3)

                                # train profit
                                if item["model"] in ["Diamond"]:
                                    item["ppppkm"] += 0.2
                                elif item["model"] in ["Gold"]:
                                    item["ppppkm"] += 0.2 if item["ppppkm"] < 2 else 0.05
                                elif item["model"] in ["Jubilee-A", "Jubilee-B", "Silver"]:
                                    item["ppppkm"] += 0.1 if item["ppppkm"] < 1.5 else 0.05
                                elif item["model"] in ["Star of China", "Bronze"]:
                                    item["ppppkm"] += 0.05
                                elif item["model"] in ["Bullet", "Current", "Solo"]:
                                    item["ppppkm"] += 0.02
                                elif item["model"] in ["HM-11W", "HM-12W"]:
                                    item["ppppkm"] += 0.015
                                elif item["model"] in ["Mystic", "Bulb", "Peng-01", "Piercer"]:
                                    item["ppppkm"] += 0.01 if item["ppppkm"] < 0.1 else 0.005
                                elif item["model"] in ["Taurus", "Baron", "Ocean", "Ember", "Torrent", "Maris", "Polaris", "Polaris-2"]:
                                    item["ppppkm"] += 0.008 if item["ppppkm"] < 0.06 else 0.005
                                elif item["model"] in ["DT-4", "DT-5A", "DT-5B", "DT-6", "Ursa", "AC-76", "AC-77", "Wang-01"]:
                                    item["ppppkm"] += 0.005

                                item["ppppkm"] = round(item["ppppkm"], 3)
                                
                                

                    y_down = height - 200
                    y_down += H3_SIZE+SPACING*2
                    text = font_h4.render(f"Top Speed: {item['speed']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+8))
                    text = font_h4.render(f"Capacity: {item['capacity']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+10+H4_SIZE))
                    text = font_h4.render(f"Earnings: {item['ppppkm']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+12+H4_SIZE*2))
                    text = font_h4.render(f"Line Type: {item['train_type']}", True, "black")
                    screen.blit(text, (x_across+8, y_down+14+H4_SIZE*3))

                    pygame.draw.line(screen, "black", (x_across+175, y_down+8), (x_across+175, y_down+100), width=6)


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
        # passive from cities
        for city in cities:
            pass

        # from trains on lines
        for line in lines:
            if line["owned"] and line["cities"] != [] and line["finished"]:
                euros_per_trip = 0
                distance = 0
                for city in range(len(line["cities"])-1):
                    for code in cities:
                        if code.code == line["cities"][city]:
                            start_loc = code
                        if code.code == line["cities"][city+1]:
                            end_loc = code
                        if start_loc == None or end_loc == None:
                            pass
                        else:
                            distance += round(math.sqrt((start_loc.loc.x - end_loc.loc.x)**2 + (start_loc.loc.y - end_loc.loc.y)**2))

                for train in owned_trains:
                    if train.line == line["name"]:
                        euros_per_trip = train.cap * train.ppkm * distance
                        trip_time = distance / train.speed
                        train.trip_hr = trip_time // 60
                        train.trip_min = trip_time % 60
                        if hour == start and minute >= 0 and loop:
                            trains_running = True
                            train.last_hr = start
                            train.last_min = 0
                            loop = False
                        if hour == end:
                            trains_running = False
                            loop = True

                        if trains_running:
                            train.next_hr = train.last_hr + train.trip_hr
                            train.next_min = train.last_min + train.trip_min
                            if train.next_min >= 60:
                                train.next_min -= 60
                                train.next_hr += 1
                            if train.next_hr >= end:
                                pass
                            else:
                                if hour == train.next_hr and minute >= train.next_min or hour == train.next_hr+1 and minute <= 10 and train.next_min > 50:
                                    euros += euros_per_trip
                                    train.last_hr = train.next_hr
                                    train.last_min = train.next_min
                                    income_statements.append(f'{list(months.keys())[month-1]} {round(day)}{" " if round(day)<10 else ""} {0 if round(train.next_hr)<10 else ""}{round(train.next_hr)}:{0 if round(train.next_min)<10 else ""}{round(train.next_min)} | {line["name"]:<8} | ${round(euros_per_trip)}')                           
            
        # drawing on map
        # draw lines
        if flash > 0.5:
            draw_lines(flash_lines+lines, cities)
        else:
            draw_lines(lines, cities)
        
        # draw cities
        for city in cities:
            if city.shown:
                draw_city(city)

        # hover labels - will show when mouse is hovering over city icon on map
        # makes hover labels not show if currently clicked into the menu for another city
        hover = True
        for city in cities:
            if city.clicked:
                hover = False
            else:
                pass
        
        # if hovering allowed, show hover labels
        if hover:
            # detecting mouse pos relative to each city
            for city in cities:
                if pygame.mouse.get_pos()[0] in range(round(city.loc.x)-5,round(city.loc.x)+10) and pygame.mouse.get_pos()[1] in range(round(city.loc.y)-5, round(city.loc.y)+10) and city.shown:

                    # determining backing colour based on cost and players money - adds a clearer visualisation of what the player can do with city
                    if city in cities and not city.owned and city.cost > euros:
                        text_color = pygame.Color(255, 49, 0)
                    elif city in cities and not city.owned:
                        text_color = "white"
                    else:
                        text_color = "yellow"

                    rect = pygame.Rect(city.loc.x - 18, city.loc.y - 38, 41, H4_SIZE+12)
                    pygame.draw.rect(screen, COLOR, rect, border_radius = 13)
                    font_h4.set_bold(True)
                    text = font_h4.render(city.code, True, text_color)
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2+1, rect[1]+(rect[3]/2)-text.get_height()/2))
                    font_h4.set_bold(False)

        # show city labels on click
        for city in cities:

            # city labels
            if city.clicked and not line_build and city.shown: 
                draw_city(city, pygame.Color(54, 153, 43))
                BOX_WIDTH = font_h4.render("XXXXXXXXXXXX  XXX", True, "black").get_width()
                BOX_HEIGHT = H4_SIZE * 3 + 12
                # box down
                if city.loc.y - (H5_SIZE * 5 + 30) < 20:
                    box = pygame.Vector2(city.loc.x - 65, city.loc.y + ((H5_SIZE * 5 + 15)-H5_SIZE * 5) + 5) # used V2 then rect
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 
                # box up
                else:
                    box = pygame.Vector2(city.loc.x - 65, city.loc.y - (H5_SIZE * 5 + 15))
                    rect = pygame.Rect(box.x, box.y, BOX_WIDTH, BOX_HEIGHT) 

                pygame.draw.rect(screen, pygame.Color(210,210,210), rect)

                # printing name details in top corners of box
                print_text(f"{city.name}", font_h4, "black", box.x+4, box.y+2)
                font_h4.set_bold(True)
                text = font_h4.render(city.code, True, "black")
                screen.blit(text, (box.x+rect[2]-text.get_width()-4, box.y+2))
                font_h4.set_bold(False)

                # shows purchase button for if the city is NOT owned
                if not city.owned:

                    if euros > city.cost:
                        color = pygame.Color(39, 143, 31)
                        words_1 = "PURCHASE"
                        words_2 = str(city.cost)
                    else:
                        color = "red"
                        words_1 = "CAN'T AFFORD"
                        words_2 = str(city.cost)

                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+4, BOX_WIDTH-8, (H4_SIZE*3+12)-(H4_SIZE+4)-4)
                    pygame.draw.rect(screen, color, rect)
                    # printing purchase details on city
                    text = font_h4.render(words_1, True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/3)-(text.get_height()/2)-1))
                    text = font_h4.render(words_2, True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*2/3)-(text.get_height()/2)+2))

                    # checks for if user is clicking the purchase button or not
                    if button_check(rect):
                        if euros > city.cost:
                            city.owned = True
                            euros -= city.cost
                            for dest in city.operates_to:
                                for item in cities:
                                    if dest == item.code:
                                        item.shown = True
                            

                        # add money changes etc here
                
                # shows 'owned' button if city is owned - may change
                if city.owned:
                    rect = pygame.Rect(box.x+4, box.y+H4_SIZE+4, BOX_WIDTH-8, (H4_SIZE*3+12)-(H4_SIZE+4)-4)
                    pygame.draw.rect(screen, pygame.Color(160, 160, 160), rect)

                    font_h4.set_bold(True)
                    text = font_h4.render("OWNED", True, "white")
                    screen.blit(text, ((rect[0]+rect[2]/2) - text.get_width()/2, (rect[1]+rect[3]/2) - text.get_height()/2))
                    font_h4.set_bold(False)

            # rect checking for each city - finds which city was clicked
            rect = pygame.Rect(city.loc.x-5, city.loc.y-5, 15, 15)
            if button_check(rect):
                for clicked in cities:       # makes every other cities  
                    clicked.clicked = False # 'clicked' status False, then sets 
                city.clicked = True      # the correct cities status to True

        # removing large city labels when clicked elsewhere
        if button_check(pygame.Rect(0,0,width,height)):
            for city in cities:
                city.clicked = False

        # # map key
        # # can't afford key
        # rect = pygame.Rect(10,10,15,15)
        # pygame.draw.rect(screen, "black", rect)
        # rect = pygame.Rect(13,13,9,9)
        # pygame.draw.rect(screen, pygame.Color(217, 49, 30), rect)
        # print_text("Can't Afford", font_h4, "black", 31, 10)

        # # can afford key
        # rect = pygame.Rect(10,30,15,15)
        # pygame.draw.rect(screen, "black", rect)
        # rect = pygame.Rect(13,33,9,9)
        # pygame.draw.rect(screen, pygame.Color(170,170,170), rect)
        # print_text("Can Afford", font_h4, "black", 31, 30)

        # # owned key
        # rect = pygame.Rect(10,50,15,15)
        # pygame.draw.rect(screen, "black", rect)
        # rect = pygame.Rect(13,53,9,9)
        # pygame.draw.rect(screen, "yellow", rect)
        # print_text("Owned", font_h4, "black", 31, 50)

        text = font_h5.render(f'{pygame.mouse.get_pos()[0]}, {pygame.mouse.get_pos()[1]}', True, "black")
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
    seconds_since_date_update += dt 
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
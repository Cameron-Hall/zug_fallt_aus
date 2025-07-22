import math
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import numpy as np
from scipy.spatial import Delaunay
import random
import os

# pygame initialisation
pygame.init()
screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0],pygame.display.get_desktop_sizes()[0][1]))
trans_surface = pygame.Surface((screen.get_width(),screen.get_height()), pygame.SRCALPHA)
clock = pygame.time.Clock()
dt = 0

# loops and stages
running = True
homepage = True
game = False

mouse_up_check = False
flash = 0
extra = 0
hover = True

hover_time = 0

    # tutorial things
money_clicked = False
tutorial_final = False
name_select = False
congratulations = False

username = ""

daily_euros = 0

income_box_shown = False

line_purchasing = False
line_build = None
train_purchase = False

start_loc = None
end_loc = None

seconds_since_date_update = 0
day = 1
month = 1
year = 1

r = 100
g = 100
b = 100

info_draw = False
type_change = False

menu_page = 'Lines'

# tabs
line_tab = "owned"
train_tab = "stored"
upgrade_tab = None

fake_lines = []
new_line = [{"shown": False}]
income_statements = ["","","","","","","","",""]

zoom_level = 0


# upgrade variables
full_day = False

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
lock = pygame.transform.scale(lock, (16, 16))
track_outline = pygame.image.load("zug_fallt_aus/assets/track_outline.png")
track_outline = pygame.transform.scale(track_outline, (width-700, height-400))

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
euros = 10000000
COST_PER_KM = 100

# date calc things
months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31, }

# lists
trains = [
{'make': 'Express', 'model': 'DT-4', 'icon': express_red, 'shown': False, 'owned': False, 'cost': 300000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 100, 'ppppkm': 0.025, 'level': 0, "stored": 0, 'desc': 'The most basic train of the lot. Small yet reliable for transporting your first passengers, or for serving new connections.'},
{'make': 'Express', 'model': 'DT-5A', 'icon': express_orange, 'shown': False, 'owned': False, 'cost': 340000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 100, 'ppppkm': 0.025, 'level': 0, "stored": 0},
{'make': 'Express', 'model': 'DT-5B', 'icon': express_green, 'shown': False, 'owned': False, 'cost': 350000, 'train_type': 'Diesel', 'capacity': 250, 'speed': 110, 'ppppkm': 0.028, 'level': 0, "stored": 0},
{'make': 'Express', 'model': 'DT-6', 'icon': express_blue, 'shown': False, 'owned': False, 'cost': 400000, 'train_type': 'Diesel', 'capacity': 300, 'speed': 112, 'ppppkm': 0.03, 'level': 0, "stored": 0},
{'make': 'RailSpark', 'model': 'Ember', 'icon': railspark_ember, 'shown': False, 'owned': False, 'cost': 650000, 'train_type': 'Diesel', 'capacity': 400, 'speed': 105, 'ppppkm': 0.025, 'level': 0, "stored": 0},
{'make': 'RailSpark', 'model': 'Torrent', 'icon': railspark_torrent, 'shown': False, 'owned': False, 'cost': 600000, 'train_type': 'Diesel', 'capacity': 200, 'speed': 160, 'ppppkm': 0.04, 'level': 0, "stored": 0},
{'make': 'RailSpark', 'model': 'Bulb', 'icon': railspark_bulb, 'shown': False, 'owned': False, 'cost': 200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 140, 'ppppkm': 0.05, 'level': 0, "stored": 0},
{'make': 'RailSpark', 'model': 'Mystic', 'icon': railspark_mystic, 'shown': False, 'owned': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 375, 'speed': 180, 'ppppkm': 0.06, 'level': 0, "stored": 0},
{'make': 'North Star', 'model': 'Ursa', 'icon': north_star_green, 'shown': False, 'owned': False, 'cost': 500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 80, 'ppppkm': 0.02, 'level': 0, "stored": 0},
{'make': 'North Star', 'model': 'Maris', 'icon': north_star_red, 'shown': False, 'owned': False, 'cost': 320000, 'train_type': 'Electric', 'capacity': 200, 'speed': 120, 'ppppkm': 0.03, 'level': 0, "stored": 0},
{'make': 'North Star', 'model': 'Polaris', 'icon': north_star_purple, 'shown': False, 'owned': False, 'cost': 1600000, 'train_type': 'Electric', 'capacity': 400, 'speed': 134, 'ppppkm': 0.045, 'level': 0, "stored": 0},
{'make': 'North Star', 'model': 'Polaris-2', 'icon': north_star_yellow, 'shown': False, 'owned': False, 'cost': 2150000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'ppppkm': 0.045, 'level': 0, "stored": 0},
{'make': 'Thompson Lines', 'model': 'AC-76', 'icon': thompson_lines_red, 'shown': False, 'owned': False, 'cost': 150000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 110, 'ppppkm': 0.02, 'level': 0, "stored": 0},
{'make': 'Thompson Lines', 'model': 'AC-77', 'icon': thompson_lines_blue, 'shown': False, 'owned': False, 'cost': 160000, 'train_type': 'Diesel', 'capacity': 150, 'speed': 120, 'ppppkm': 0.02, 'level': 0, "stored": 0},
{'make': 'Erlington Works', 'model': 'Jubilee-A', 'icon': erlington_works, 'shown': False, 'owned': False, 'cost': 900000, 'train_type': 'Electric', 'capacity': 50, 'speed': 50, 'ppppkm': 1.0, 'level': 0, "stored": 0},
{'make': 'Erlington Works', 'model': 'Jubilee-B', 'icon': erlington_works_2, 'shown': False, 'owned': False, 'cost': 1100000, 'train_type': 'Electric', 'capacity': 75, 'speed': 75, 'ppppkm': 0.5, 'level': 0, "stored": 0},
{'make': 'Royal', 'model': 'Bronze', 'icon': royal_bronze, 'shown': False, 'owned': False, 'cost': 3620000, 'train_type': 'Electric', 'capacity': 200, 'speed': 150, 'ppppkm': 0.2, 'level': 0, "stored": 0},
{'make': 'Royal', 'model': 'Silver', 'icon': royal_silver, 'shown': False, 'owned': False, 'cost': 4200000, 'train_type': 'Electric', 'capacity': 100, 'speed': 170, 'ppppkm': 0.5, 'level': 0, "stored": 0},
{'make': 'Royal', 'model': 'Gold', 'icon': royal_gold, 'shown': False, 'owned': False, 'cost': 5000000, 'train_type': 'Electric', 'capacity': 50, 'speed': 185, 'ppppkm': 1.0, 'level': 0, "stored": 0},
{'make': 'Royal', 'model': 'Diamond', 'icon': royal_diamond, 'shown': False, 'owned': False, 'cost': 9900000, 'train_type': 'MagLev', 'capacity': 20, 'speed': 200, 'ppppkm': 4.0, 'level': 0, "stored": 0},
{'make': 'Mr Peng Enterprises', 'model': 'Peng-01', 'icon': peng_enterprises, 'shown': False, 'owned': False, 'cost': 43000000, 'train_type': 'Electric', 'capacity': 500, 'speed': 200, 'ppppkm': 0.055, 'level': 0, "stored": 0},
{'make': 'Guangdong Star', 'model': 'Star of China', 'icon': guangdong_star, 'shown': False, 'owned': False, 'cost': 850000000, 'train_type': 'MagLev', 'capacity': 800, 'speed': 250, 'ppppkm': 0.6, 'level': 0, "stored": 0},
{'make': 'Wang Li', 'model': 'Wang-01', 'icon': wang_li, 'shown': False, 'owned': False, 'cost': 18000000, 'train_type': 'Diesel', 'capacity': 1200, 'speed': 150, 'ppppkm': 0.02, 'level': 0, "stored": 0},
{'make': 'Yangtze Monos', 'model': 'Current', 'icon': yangtze_monos, 'shown': False, 'owned': False, 'cost': 11500000, 'train_type': 'Monorail', 'capacity': 100, 'speed': 120, 'ppppkm': 0.2, 'level': 0, "stored": 0},
{'make': 'West Network', 'model': 'Bullet', 'icon': west_network, 'shown': False, 'owned': False, 'cost': 600000000, 'train_type': 'MagLev', 'capacity': 600, 'speed': 300, 'ppppkm': 0.4, 'level': 0, "stored": 0},
{'make': 'Great Northern', 'model': 'Piercer', 'icon': great_northern, 'shown': False, 'owned': False, 'cost': 12250000, 'train_type': 'Electric', 'capacity': 300, 'speed': 180, 'ppppkm': 0.05, 'level': 0, "stored": 0},
{'make': 'Southern Star', 'model': 'Solo', 'icon': southern_star, 'shown': False, 'owned': False, 'cost': 24000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 200, 'ppppkm': 0.2, 'level': 0, "stored": 0},
{'make': 'Eastern Power', 'model': 'Taurus', 'icon': eastern_power, 'shown': False, 'owned': False, 'cost': 9000000, 'train_type': 'Diesel', 'capacity': 900, 'speed': 100, 'ppppkm': 0.04, 'level': 0, "stored": 0},
{'make': 'Red Hill', 'model': 'Baron', 'icon': red_hill, 'shown': False, 'owned': False, 'cost': 2500000, 'train_type': 'Diesel', 'capacity': 500, 'speed': 150, 'ppppkm': 0.03, 'level': 0, "stored": 0},
{'make': 'Blue Hill', 'model': 'Ocean', 'icon': blue_hill, 'shown': False, 'owned': False, 'cost': 2500000, 'train_type': 'Electric', 'capacity': 500, 'speed': 150, 'ppppkm': 0.03, 'level': 0, "stored": 0},
{'make': 'Hermann Monorails', 'model': 'HM-11W', 'icon': hermann_green, 'shown': False, 'owned': False, 'cost': 11000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 140, 'ppppkm': 0.2, 'level': 0, "stored": 0},
{'make': 'Hermann Monorails', 'model': 'HM-12W', 'icon': hermann_orange, 'shown': False, 'owned': False, 'cost': 12000000, 'train_type': 'Monorail', 'capacity': 200, 'speed': 150, 'ppppkm': 0.2, 'level': 0, "stored": 0},
]
owned_trains = []
lines = [
    # Reds
    {"class": "Red", "name": "Red-1", "color": pygame.Color(255, 102, 102), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Red", "name": "Red-2", "color": pygame.Color(255, 0, 0),     "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Red", "name": "Red-3", "color": pygame.Color(204, 0, 0),     "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Red", "name": "Red-4", "color": pygame.Color(153, 0, 0),     "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Oranges
    # {"class": "Orange", "name": "Orange-1", "color": pygame.Color(255, 200, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Orange", "name": "Orange-2", "color": pygame.Color(255, 150, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Orange", "name": "Orange-3", "color": pygame.Color(255, 100, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Orange", "name": "Orange-4", "color": pygame.Color(255, 50, 0),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Yellows
    # {"class": "Yellow", "name": "Yellow-1", "color": pygame.Color(255, 255, 0), "type": "Electric", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Yellow", "name": "Yellow-2", "color": pygame.Color(210, 210, 0), "type": "Electric", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Yellow", "name": "Yellow-3", "color": pygame.Color(150, 150, 0), "type": "Electric", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Yellow", "name": "Yellow-4", "color": pygame.Color(70, 70, 0),   "type": "Electric", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Greens
    # {"class": "Green", "name": "Green-1", "color": pygame.Color(0, 255, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Green", "name": "Green-2", "color": pygame.Color(0, 190, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Green", "name": "Green-3", "color": pygame.Color(0, 120, 0), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Green", "name": "Green-4", "color": pygame.Color(0, 70, 0),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Light Blues
    # {"class": "Light Blue", "name": "Blue-L1", "color": pygame.Color(80, 225, 225), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Light Blue", "name": "Blue-L2", "color": pygame.Color(0, 190, 190),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Light Blue", "name": "Blue-L3", "color": pygame.Color(0, 140, 140),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Light Blue", "name": "Blue-L4", "color": pygame.Color(0, 70, 70),    "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Blues
    # {"class": "Blue", "name": "Blue-D1", "color": pygame.Color(80, 80, 255), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Blue", "name": "Blue-D2", "color": pygame.Color(0, 0, 255),   "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Blue", "name": "Blue-D3", "color": pygame.Color(0, 0, 110),   "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Blue", "name": "Blue-D4", "color": pygame.Color(0, 0, 40),    "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Purples
    # {"class": "Purple", "name": "Purple-1", "color": pygame.Color(150, 75, 150), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Purple", "name": "Purple-2", "color": pygame.Color(160, 0, 160),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Purple", "name": "Purple-3", "color": pygame.Color(110, 0, 110),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Purple", "name": "Purple-4", "color": pygame.Color(50, 0, 50),    "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},

    # # Browns
    # {"class": "Brown", "name": "Brown-1", "color": pygame.Color(181, 101, 29), "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Brown", "name": "Brown-2", "color": pygame.Color(160, 82, 45),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Brown", "name": "Brown-3", "color": pygame.Color(139, 69, 19),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0},
    # {"class": "Brown", "name": "Brown-4", "color": pygame.Color(101, 67, 33),  "type": "Standard", "shown": False, "owned": False, "finished": True, "cities": [], "trains": [], "speed": 100, "level": 1, "cost": 100000, "money_earned": 0}

]
upgrades = [
    {"name": "Night Owl 1",     "cost": 1000000,  "predecessor": [],                              "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will run for an extra hour each night, meaning your trains will finish running at 10pm."},
    {"name": "Night Owl 2",     "cost": 2000000,  "predecessor": ["Night Owl 1"],                 "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will run for an extra hour each night, meaning your trains will finish running at 11pm."},
    {"name": "Night Owl 3",     "cost": 3000000,  "predecessor": ["Night Owl 2"],                 "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will run for an extra hour each night, meaning your trains will finish running at midnight."},
    {"name": "Night Owl 4",     "cost": 4000000,  "predecessor": ["Night Owl 3"],                 "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will run for an extra hour each night, meaning your trains will finish running at 1am."},
    {"name": "Early Bird 1",    "cost": 1000000,  "predecessor": [],                              "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will start running one hour earlier each day, meaning your trains will start running at 6am."},
    {"name": "Early Bird 2",    "cost": 2000000,  "predecessor": ["Early Bird 1"],                "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will start running one hour earlier each day, meaning your trains will start running at 5am."},
    {"name": "Early Bird 3",    "cost": 3000000,  "predecessor": ["Early Bird 2"],                "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will start running one hour earlier each day, meaning your trains will start running at 4am."},
    {"name": "Early Bird 4",    "cost": 4000000,  "predecessor": ["Early Bird 3"],                "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service will start running one hour earlier each day, meaning your trains will start running at 3am."},
    {"name": "Round the Clock", "cost": 10000000, "predecessor": ["Night Owl 4", "Early Bird 4"], "icon": red_hill, "owned": False, "shown": False, "effect": "Your train service now runs around the clock, meaning your trains never stop!"},

]
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
    def __init__(self, img, top, right, bottom, left, rotation=0):
        self.img = img
        self.top = top        # Read left → right
        self.right = right    # Read bottom → top
        self.bottom = bottom  # Read left → right
        self.left = left      # Read bottom → top
        self.rotation = rotation

    def rotate(self):
        # 90° clockwise rotation
        new_top = self.left                # left → top (same direction)
        new_right = self._reverse(self.top)    # top → right (reverse)
        new_bottom = self.right            # right → bottom (same direction)
        new_left = self._reverse(self.bottom)  # bottom → left (reverse)

        self.top = new_top
        self.right = new_right
        self.bottom = new_bottom
        self.left = new_left

        # Rotate image clockwise
        try:
            self.img = pygame.transform.rotate(self.img, -90)
        except:
            pass

        self.rotation = (self.rotation + 90) % 360

    def _reverse(self, s):
        return s[::-1]

    def __repr__(self):
        return f"Tile(rot={self.rotation}, top={self.top}, right={self.right}, bottom={self.bottom}, left={self.left})"

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
    if rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.event.peek(eventtype=pygame.MOUSEBUTTONUP) and rect.collidepoint(pygame.mouse.get_pos()):  
        #pygame.mouse.get_pos()[0] in range(rect[0],rect[0]+rect[2]) and pygame.mouse.get_pos()[1] in range(rect[1],rect[1]+rect[3]):
            pygame.event.get()
            return True
  
 
def print_text(words, font, color, x, y):
    text = font.render(str(words), True, color)
    screen.blit(text, (x, y))


def draw_lines(lines, cities):
    for line in lines:
        if line["cities"] != []:
            for code in range(len(line["cities"])-1):
                for city in cities:
                    if city.code == line["cities"][code]:
                        start_loc = city
                    if city.code == line["cities"][code+1]:
                        end_loc = city

                pygame.draw.line(screen, line["color"], (start_loc.loc.x+2.5, start_loc.loc.y+2.5), (end_loc.loc.x+2.5, end_loc.loc.y+2.5), width = 5)

                if line["type"] == "Electric":
                    spacing = 10
                    offset = 4
                    x1, y1 = (start_loc.loc.x+2, start_loc.loc.y+2)
                    x2, y2 = (end_loc.loc.x+2, end_loc.loc.y+2)

                    # Direction vector from A to B
                    dx = x2 - x1
                    dy = y2 - y1
                    length = math.hypot(dx, dy)
                    dir_x = dx / length
                    dir_y = dy / length

                    # Perpendicular vector (rotated 90 degrees)
                    perp_x = -dir_y
                    perp_y = dir_x

                    num_dots = int(length // spacing)
                    points = []

                    for i in range(num_dots + 1):
                        t = i * spacing
                        base_x = x1 + dir_x * t
                        base_y = y1 + dir_y * t

                        # Alternate offset direction
                        sign = -1 if i % 2 == 0 else 1
                        dot_x = base_x + sign * perp_x * offset
                        dot_y = base_y + sign * perp_y * offset

                        points.append((dot_x, dot_y))
                        # pygame.draw.circle(screen, yellow, (int(dot_x), int(dot_y)), 5)

                    # Draw connecting line
                    if len(points) > 1:
                        pygame.draw.lines(screen, yellow, False, points, 2)

def draw_city(city, color, flash=1):
    if (pygame.mouse.get_pos()[0] in range(round(city.loc.x)-5, round(city.loc.x)+10) and pygame.mouse.get_pos()[1] in range(round(city.loc.y)-5,round(city.loc.y)+10)) and hover:
        city_inner = pygame.Rect(city.loc.x-2,city.loc.y-2,9,9)

    # no hover
    else:
        city_inner = pygame.Rect(city.loc.x-1,city.loc.y-1,7,7)
    city_outer = pygame.Rect(city.loc.x-5,city.loc.y-5,15,15)

    if color != None:
        color = color
    elif not city.owned and city.cost > euros:
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
        return f"€{('{:,}'.format(euros))}"


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


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def triangle_overlaps_other_rects(tri_pts, rects):
    for i in range(3):
        p1 = tri_pts[i]
        p2 = tri_pts[(i + 1) % 3]
        for rect_info in rects:
            cx, cy = rect_info["center"]

            # Skip if this rect belongs to an endpoint
            if (p1 == (cx, cy)) or (p2 == (cx, cy)):
                continue

            # Skip if rect is within 100px of either point
            # if distance((cx, cy), p1) < 100 or distance((cx, cy), p2) < 100:
            #     continue

            # Check for line collision with rect
            if rect_info["rect"].clipline(p1, p2):
                return True
    return False


def process_tile(file_path, number, code_parts):
    # print(f"Processing {file_path}")
    # print(f"Tile number: {number}")
    # print(f"Code parts: {code_parts}")

    # Load the original image
    original_img = pygame.image.load(file_path)

    # Create 4 rotated versions
    img = original_img
    top, right, bottom, left = code_parts[0], code_parts[1], code_parts[2], code_parts[3]

    for i in range(4):
        # Append a tile copy with current rotation
        tiles.append(Tile(img.copy(), top, right, bottom, left, rotation=(i * 90)))

        # Rotate image for next version
        img = pygame.transform.rotate(img, -90)

        # Rotate edge codes
        top, right, bottom, left = (
            left,                           # left → top (same)
            Tile._reverse(None, top),       # top → right (reverse)
            right,                          # right → bottom (same)
            Tile._reverse(None, bottom)     # bottom → left (reverse)
        )


def is_mouse_over_circle(circle_center, radius):
    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - circle_center[0]
    dy = mouse_pos[1] - circle_center[1]
    distance_squared = dx * dx + dy * dy
    return distance_squared <= radius * radius



tiles = []

# The folder containing your tile files
folder = "zug_fallt_aus/assets/procedural_tiles"

for filename in os.listdir(folder):
    if filename.startswith("tile_"):
        name_without_ext = os.path.splitext(filename)[0]
        try:
            _, rest = name_without_ext.split("tile_", 1)
            underscore_index = rest.find("_")
            if underscore_index == -1:
                print(f"Skipping {filename}: missing underscore after number")
                continue

            number_part = rest[:underscore_index]
            code_part = rest[underscore_index + 1:]
            code_elements = code_part.split("-")

            if len(code_elements) == 4:
                full_path = os.path.join(folder, filename)
                process_tile(full_path, number_part, code_elements)
            else:
                print(f"Skipping {filename}: code does not have 4 elements")
        except Exception as e:
            print(f"Skipping {filename}: {e}")

# generating tile map based on specified sizes 
TILE_SIZE = 100

# Placement loop - NO ROTATION
tile_order = []

tiles_per_row = width // TILE_SIZE
tiles_per_column = (height // TILE_SIZE) + 1
total_tiles = tiles_per_row * tiles_per_column

for slot in range(total_tiles):
    row = slot // tiles_per_row
    col = slot % tiles_per_row

    while True:
        tile = random.choice(tiles)  # Pick already rotated tile
        placed = False

        # Check left
        left_ok = True
        if col > 0:
            left_tile = tile_order[slot - 1]
            left_ok = (tile.left == left_tile.right)

        # Check above
        top_ok = True
        if row > 0:
            top_tile = tile_order[slot - tiles_per_row]
            top_ok = (tile.top == top_tile.bottom)

        if left_ok and top_ok:
            tile_order.append(tile)
            placed = True
            # print(f"{slot}:{row}/{col} {tile.top}-{tile.right}-{tile.bottom}-{tile.left} rot={tile.rotation}")
            break  # Go to next slot

    # Next slot

# generating city points based on specified amounts
num_points = len(first_names)
points = np.random.rand(num_points, 2)
points *= [width-430, height-100]  # Scale to screen size    
points += [80, 50]

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
RECT_SIZE = 50 
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
    events = pygame.event.get()
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
        screen.fill(COLOR)

        text = font_h1.render("game", True, "white")
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
        for slot in range(((width//TILE_SIZE))*((height//TILE_SIZE)+1)):
            screen.blit(tile_order[slot].img, (x_across, y_down))
            x_across += TILE_SIZE

            if x_across >= ((width//TILE_SIZE))*TILE_SIZE:
                x_across = 0
                y_down += TILE_SIZE

        # for simplex in tri.simplices:
        #     tri_pts = [int_points[i] for i in simplex]
        #     if not triangle_overlaps_other_rects(tri_pts, exclude_rects):
        #         pygame.draw.polygon(screen, "black", tri_pts, 1)

         # drawing on map
        # draw lines
        if flash < 0.5:
            draw_lines(fake_lines, cities)

        draw_lines(lines, cities)
        # draw cities
        for city in cities:
            draw = False
            if line_build != None:
                for line in lines:
                    if line_build == line:
                        if city.code in line["cities"]:
                            draw_city(city, line["color"])
                            draw = True
                    else:
                        pass
                if not draw:
                    draw_city(city, None)
            elif city.shown:
                draw_city(city, None)

        # hover labels - will show when mouse is hovering over city icon on map
        # makes hover labels not show if currently clicked into the menu for another city
        hover = True
        for city in cities:
            if city.clicked:
                hover = False
            else:
                pass
        
        for item in trains+lines+upgrades+new_line:
            if item["shown"]:
                hover = False
        
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
           
        # popup answers
        for item in trains+lines+upgrades+new_line:
            if item["shown"]:
                hover = False
                rect = (0, 0, width, height)
                pygame.draw.rect(trans_surface, (0,0,0,190), rect)
                screen.blit(trans_surface, (0,0))
                screen.blit(track_outline, (200,120))
                
                popup = pygame.Surface((round(track_outline.get_width()-(track_outline.get_width()/7)), round(track_outline.get_height()-(track_outline.get_height()/4.28))), pygame.SRCALPHA)
                popup_loc = pygame.Vector2(200 + round(track_outline.get_width()/14), 120 + round(track_outline.get_height()/8.57))

                rect = pygame.Rect(popup.get_width()-H2_SIZE-2, 2, H2_SIZE, H2_SIZE)
                pygame.draw.rect(popup, (255, 0, 0, 180), rect)
                font_h2_diff.set_bold(True)
                text = font_h2_diff.render("X", True, "white")
                font_h2_diff.set_bold(False)
                popup.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]/2-text.get_height()/2+2))
                # pygame.draw.rect(screen, (255, 0, 0, 180), pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3]))
                if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                    item["shown"] = False

                if item in lines:   
                    text = font_h2_standard.render(f'{item["name"]} Line', True, item["color"])
                    rect = pygame.Rect((x_across+popup.get_width()/2-text.get_width()/2)-5, 0, text.get_width()+10, H2_SIZE+4) 
                    pygame.draw.rect(popup, (255,255,255,90), rect, border_radius = 10)
                    popup.blit(text, (x_across+popup.get_width()/2-text.get_width()/2, 2))

                    # line unowned
                    if not item["owned"]:
                        # purchase button
                        rect = pygame.Rect(10, popup.get_height()-60, popup.get_width()-20, 50)
                        pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                        text = font_h3.render("Purchase Line", True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                            item["owned"] = True

                    # line owned
                    else:
                        # line owned, not built
                        if not item["cities"]:
                            rect = pygame.Rect(10, popup.get_height()-60, (popup.get_width()-20)/2-5, 50)
                            pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                            text = font_h3.render("Build Line", True, "white")
                            popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))
                            
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                line_build = item
                                item["finished"] = False
                                item["shown"] = False
                        
                        # line owned, built
                        else:
                            rect = pygame.Rect(10, popup.get_height()-60, (popup.get_width()-20)/2-5, 50)
                            pygame.draw.rect(popup, (255, 40, 43, 180), rect, border_radius=20)
                            text = font_h3.render("Destroy Line", True, "white")
                            popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["cities"] = []
                                for train in item["trains"]:
                                    for tren in trains:
                                        if train == tren["model"]:
                                            tren["stored"] += 1
                                item["trains"] = []

                        # line owned, upgrade
                        upgrade_cost = round(item["cost"]**(1+item["level"]*0.08), -4)
                        rect = pygame.Rect((popup.get_width()-20)/2+15, popup.get_height()-60, (popup.get_width()-20)/2, 50)
                        pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                        text = font_h3.render(f"Upgrade {e_euros(upgrade_cost)}", True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                            if upgrade_cost > euros:
                                pass
                            else:
                                euros -= upgrade_cost
                                item["level"] += 1
                            
                                item["speed"] += 10


                    # other line details
                    text = font_h3.render(f"Line Route:", True, "white")
                    popup.blit(text, (50, 50))
                    text = font_h3.render(f"{','.join(item['cities'])}" if item["cities"] != [] else "Not built", True, "white")
                    popup.blit(text, (50, 50+H3_SIZE))

                    text = font_h3.render(f"Line Top Speed: {item['speed']}", True, "white")
                    popup.blit(text, (50, 50+H3_SIZE*2))
                    text = font_h3.render(f"Level: {item['level']}", True, "white")
                    popup.blit(text, (50, 50+H3_SIZE*3))

                    line_colors = {"Standard": (136, 0, 21), "Electric": (236, 255, 17), "MagLev": (16, 12, 115), "Monorail": (0, 162, 232)}

                    text = font_h3.render(f"Line Type", True, "white")
                    popup.blit(text, (popup.get_width() - 100 - text.get_width()/2, 50))
                    pygame.draw.circle(popup, line_colors[f'{item["type"]}'], (popup.get_width()-100, 150), 70)
                    if item["type"][0] != "M":
                        font_h1.set_bold(True)
                    color = "black" if item["type"] == "Electric" else "white"
                    text = font_h1.render(item["type"][0].lower(), True, color)
                    popup.blit(text, (popup.get_width()-100-text.get_width()/2, 150-text.get_height()/2+2))
                    font_h1.set_bold(False)

                    rect = pygame.Rect(popup.get_width()-170, 230, 140, H3_SIZE*2)
                    if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                        type_change = True

                    if item["owned"]:
                        color = (54, 43, 153, 180)
                    else:
                        color = (160, 160, 160, 180)
                        type_change = False

                    pygame.draw.rect(popup, color, rect, border_radius=20)
                    text = font_h3.render("Change Type", True, "white")
                    popup.blit(text, (rect[0]+rect[2]/2-text.get_width()/2, rect[1]+rect[3]/2-text.get_height()/2))

                    if type_change:
                        bg_rect = pygame.Rect(popup.get_width()-170, 80, 140, 140)
                        pygame.draw.rect(popup, "black", bg_rect)

                        if item["type"] == "Standard":
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+6, bg_rect[2]-12, bg_rect[3]-12)
                            pygame.draw.rect(popup, line_colors["Electric"], rect)
                            text = font_h4.render("Electric", True, "black")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "Electric"
                                type_change = False

                        elif item["type"] == "Electric":
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+6, bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["MagLev"], rect)
                            text = font_h4.render("MagLev", True, "white")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "MagLev"
                                type_change = False
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+12+(bg_rect[3]/2-9), bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["Monorail"], rect)
                            text = font_h4.render("Monorail", True, "white")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "Monorail"
                                type_change = False

                        elif item["type"] == "MagLev":
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+6, bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["Electric"], rect)
                            text = font_h4.render("Electric", True, "black")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "Electric"
                                type_change = False
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+12+(bg_rect[3]/2-9), bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["Monorail"], rect)
                            text = font_h4.render("Monorail", True, "white")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "Monorail"
                                type_change = False

                        elif item["type"] == "Monorail":
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+6, bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["Electric"], rect)
                            text = font_h4.render("Electric", True, "black")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "Electric"
                                type_change = False
                            rect = pygame.Rect(bg_rect[0]+6, bg_rect[1]+12+(bg_rect[3]/2-9), bg_rect[2]-12, bg_rect[3]/2-9)
                            pygame.draw.rect(popup, line_colors["MagLev"], rect)
                            text = font_h4.render("MagLev", True, "white")
                            popup.blit(text, (rect[0]+2, rect[1]+2))
                            if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                                item["type"] = "MagLev"
                                type_change = False

                if item in trains:
                    text = font_h2_standard.render(f'{item["make"]} - {item["model"]}', True, "black")
                    rect = pygame.Rect((x_across+popup.get_width()/2-text.get_width()/2)-5, 0, text.get_width()+10, H2_SIZE+4) 
                    pygame.draw.rect(popup, (255,255,255,90), rect, border_radius = 10)
                    popup.blit(text, (x_across+popup.get_width()/2-text.get_width()/2, 2))

                    # train not owned
                    if not item["owned"]:
                        # purchase button
                        rect = pygame.Rect(10, popup.get_height()-60, popup.get_width()-20, 50)
                        pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                        text = font_h3.render(f"Unlock - {e_euros(item['cost']*10)}", True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                            if item["cost"]*10 > euros:
                                pass
                            else:
                                euros -= item["cost"]*10
                                item["owned"] = True
                                item["level"] = 1                            

                    # train owned
                    else:
                        # train owned, purchase
                        if euros < item["cost"]:
                            color = "red"
                            words = f'Purchase - {e_euros(item["cost"])}'
                        elif train_purchase:
                            color = (160,160,160,180)
                            words = "Choose Line"
                        elif item["stored"] > 0:
                            color = (54, 153, 43, 180)
                            words = f'Purchase - FREE'
                        else:
                            color = (54, 153, 43, 180)
                            words = f'Purchase - {e_euros(item["cost"])}'
                        rect = pygame.Rect(10, popup.get_height()-60, (popup.get_width()-20)/2-5, 50)
                        pygame.draw.rect(popup, color, rect, border_radius=20)
                        text = font_h3.render(words, True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                            train_purchase = True
                        if train_purchase:
                            menu_page = "Lines"
                            for rect in line_rects:
                                if button_check(rect) and lines[line_rects.index(rect)]["owned"] and item["cost"] <= euros:
                                    if item["stored"] > 0:
                                        item["stored"] -= 1
                                    else:
                                        euros -= item["cost"]
                                    lines[line_rects.index(rect)]["trains"].append(item["model"])

                                    # create Train with Train class
                                    owned_trains.append(Train(item["model"], lines[line_rects.index(rect)]["name"], item["capacity"], item["ppppkm"], item["speed"]))

                                    menu_page = "Trains"
                                    train_purchase = False

                        upgrade_cost = round(item["cost"]**(1+item["level"]*0.1), -4)

                        # train owned, upgrade
                        rect = pygame.Rect((popup.get_width()-20)/2+15, popup.get_height()-60, (popup.get_width()-20)/2, 50)
                        pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                        text = font_h3.render(f"Upgrade {e_euros(upgrade_cost)}", True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
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
                                
                    text = font_h3.render(f"Top Speed: {item['speed']}", True, "white")
                    popup.blit(text, (8, H2_SIZE+8))
                    text = font_h3.render(f"Capacity: {item['capacity']}", True, "white")
                    popup.blit(text, (8, H2_SIZE+10+H3_SIZE))
                    text = font_h3.render(f"Earnings: {item['ppppkm']}", True, "white")
                    popup.blit(text, (8, H2_SIZE+12+H3_SIZE*2))
                    text = font_h3.render(f"Line Type: {item['train_type']}", True, "white")
                    popup.blit(text, (8, H2_SIZE+14+H3_SIZE*3))

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
                    text = font_h2_standard.render(f'{item["name"]}', True, "black")
                    rect = pygame.Rect((x_across+popup.get_width()/2-text.get_width()/2)-5, 0, text.get_width()+10, H2_SIZE+4) 
                    pygame.draw.rect(popup, (255,255,255,90), rect, border_radius = 10)
                    popup.blit(text, (x_across+popup.get_width()/2-text.get_width()/2, 2))

                    if not item["owned"]:
                        rect = pygame.Rect(10, popup.get_height()-60, popup.get_width()-20, 50)
                        pygame.draw.rect(popup, (54, 153, 43, 180), rect, border_radius=20)
                        text = font_h3.render("Purchase Upgrade", True, "white")
                        popup.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]*1/2)-(text.get_height()/2)))

                        if button_check(pygame.Rect(rect[0]+popup_loc.x, rect[1]+popup_loc.y, rect[2], rect[3])):
                            item["owned"] = True

                            if item["name"] in ["Night Owl 1", "Night Owl 2", "Night Owl 3", "Night Owl 4"]:
                                end += 1
                                if end == 24:
                                    end = 0
                            elif item["name"] in ["Early Bird 1", "Early Bird 2", "Early Bird 3", "Early Bird 4"]:
                                start -= 1
                            elif item["name"] in ["Round the Clock"]:
                                full_day = True

                if item in new_line:
                    for item in trains+lines+upgrades:
                        item["shown"] = False

                    text = font_h2_standard.render("Choose Line Color", True, "white")
                    popup.blit(text, (popup.get_width()/2-text.get_width()/2, 15))
                    
                    y_down = 60+H2_SIZE
                    sliders = []
                    for color, name in zip([r,g,b], ["red", "green", "blue"]):
                        x_across = 30
                        text = font_h3.render(f"{name.title()} Value", True, "white")
                        popup.blit(text, (x_across+20, y_down-5))
                        rect = pygame.Rect(x_across, y_down+H3_SIZE, popup.get_width()*2/3, 30)
                        if name == "red":
                            colour = (color, 0, 0)
                            color_end = (255, 0, 0)
                        elif name == "green":
                            colour = (0, color, 0)
                            color_end = (0, 255, 0)
                        elif name == "blue":
                            colour = (0, 0, color)
                            color_end = (0, 0, 255)                        

                        color_start = (0, 0, 0)
                        for x in range(round(popup.get_width()*2/3)):
                            ratio = x / (popup.get_width()*2/3)
                            r_l = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
                            g_l = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
                            b_l = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
                            pygame.draw.line(popup, (r_l, g_l, b_l), (x_across, y_down+H3_SIZE), (x_across, y_down+30+H3_SIZE))
                            x_across = x + 30

                        x_across = 30

                        sliders.append(Slider(screen, x_across, y_down+H3_SIZE, popup.get_width()*2/3, 30, min=0, max=255, step=1))

                        rect = pygame.Rect(x_across+((color/255)*(popup.get_width()*2/3))-1, y_down+H3_SIZE-2, 2, 34)
                        pygame.draw.rect(popup, "white", rect)

                        rect = pygame.Rect(rect[0]-10, rect[1], rect[2]+20, rect[3])

                        if pygame.event.peek(pygame.MOUSEBUTTONDOWN):
                            dx, dy = pygame.mouse.get_rel()
                            if dx > 0 and color < 255-dx:
                                color += dx
                            elif dx < 0 and color > 0+(dx*-1):
                                color -= dx
                        
                        pygame.draw.circle(popup, "black", (x_across-15, y_down+H3_SIZE+15), 10)
                        if is_mouse_over_circle((popup_loc.x+x_across-15, popup_loc.y+y_down+H3_SIZE+15), 10) and color > 1:
                            color -= 2
                        text = font_h3.render("-", True, "white")
                        popup.blit(text, (x_across-15-text.get_width()/2+1, y_down+H3_SIZE+15-text.get_height()/2-1))

                        pygame.draw.circle(popup, "black", (x_across+(popup.get_width()*2/3)+15, y_down+H3_SIZE+15), 10)
                        if is_mouse_over_circle((popup_loc.x+x_across+(popup.get_width()*2/3)+15, popup_loc.y+y_down+H3_SIZE+15), 10) and color < 254:
                            color += 2
                        text = font_h3.render("+", True, "white")
                        popup.blit(text, (x_across+(popup.get_width()*2/3)+15-text.get_width()/2+1, y_down+H3_SIZE+15-text.get_height()/2-1))

                        color = sliders[-1].getValue()

                        if name == "red":
                            r = color
                        if name == "green":
                            g = color
                        if name == "blue":
                            b = color

                        y_down += 90

                    rect = pygame.Rect(popup.get_width()-160, popup.get_height()/2-125+30, 150, 250)
                    pygame.draw.rect(popup, (r,g,b), rect, border_radius = 20)

                screen.blit(popup, (200+track_outline.get_width()/14,120+track_outline.get_height()/8.57))

        # building line
        fake_lines = []
        if line_build != None:
            item = lines[lines.index(line_build)]
            
            rect = pygame.Rect(0, 0, width-282, 40)
            pygame.draw.rect(screen, item["color"], rect)
            color = "black" if item["color"] in ["Yellow-1", "Yellow-2", "Blue-L1", "Red-1"] else "white"
            text = font_h3.render(f'Building {item["name"].upper()} Line - {", ".join(item["cities"])}', True, color)
            screen.blit(text, ((rect[3]-text.get_height())/2, (rect[3]/2)-(text.get_height()/2)))

            text = font_h3.render("Cancel Build", True, "white")
            rect = pygame.Rect(width-282-57-text.get_width()-20, 3, text.get_width()+24, 34)
            pygame.draw.rect(screen, "white", rect, border_radius = 20)
            cancel_rect = pygame.Rect(width-282-55-text.get_width()-20, 5, text.get_width()+20, 30)
            pygame.draw.rect(screen, "red", cancel_rect, border_radius = 20)
            screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]/2)-text.get_height()/2))
            t_w = text.get_width()

            text = font_h3.render("Finish Build", True, "white")
            rect = pygame.Rect(width-282-57-t_w-20-10-text.get_width()-20, 3, text.get_width()+24, 34)
            pygame.draw.rect(screen, "white", rect, border_radius = 20)
            enter_rect = pygame.Rect(width-282-55-t_w-20-10-text.get_width()-20, 5, text.get_width()+20, 30)
            pygame.draw.rect(screen, (53, 143, 34), enter_rect, border_radius = 20)
            screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]/2)-text.get_height()/2))

            if len(item["cities"]) > 0:
                for loc in [item["cities"][0], item["cities"][-1]]:
                    for city in cities:
                        if city.code == loc:
                            loc = city
                    for dest in loc.operates_to:
                        for city in cities:
                            if city.code == dest:
                                if city.owned:
                                    fake_lines.append({"cities": [dest, loc.code], "color": (150,150,150), "type": "Standard"})
            
            for city in cities:
                key = pygame.key.get_pressed()
                rect = pygame.Rect(city.loc.x-5, city.loc.y-5, 15, 15)
                if item["cities"] == [] and button_check(rect) and item["owned"] and city.owned:
                    item["cities"].append(city.code)
                elif button_check(rect) and item["cities"][-1] in city.operates_to and len(item["cities"]) < 10 and city.code not in item["cities"] and city.owned:
                    item["cities"].append(city.code)
                elif key[pygame.K_RETURN] or button_check(enter_rect):
                    item["finished"] = True
                    line_build = None
                    item["shown"] = True
                elif key[pygame.K_ESCAPE] or button_check(cancel_rect):
                    item["cities"] = []
                    line_build = None
                    item["shown"] = True
                else:
                    pass
                flash_lines = []
                if item["cities"] != [] and not item["finished"]:
                    for city in cities:
                        if item["cities"][-1] == city.code:
                            for dest in city.operates_to:
                                flash_lines.append({"cities": [city.code, dest], "color": pygame.Color(160,160,160)})      

            if line_build != None:
                lines[lines.index(line_build)] = item 

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
                
                if lines[line]["shown"]:
                    rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT, ROW_HEIGHT)
                    pygame.draw.rect(screen, "white", rect, border_radius=8)
                pygame.draw.polygon(screen, color, [(x_across+SPACING+4,                y_down+SPACING+ROW_HEIGHT*4/5), 
                                                    (x_across+SPACING+ROW_HEIGHT*4/5,   y_down+SPACING+4),
                                                    (x_across+SPACING+ROW_HEIGHT-4,     y_down+SPACING+ROW_HEIGHT*1/5),
                                                    (x_across+SPACING+ROW_HEIGHT*1/5,   y_down+SPACING+ROW_HEIGHT-4)])

                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT, ROW_HEIGHT)
                line_rects.append(rect)

                if line_tab == "owned":
                    if lines[line]["owned"] and len(lines[line]["cities"]) > 0 and lines[line]["finished"]:
                        pygame.draw.circle(screen, (39, 143, 31), (x_across+ROW_HEIGHT-5, y_down+ROW_HEIGHT-5), 10)
                        pygame.draw.line(screen, "white", (x_across+ROW_HEIGHT-11, y_down+ROW_HEIGHT-5), (x_across+ROW_HEIGHT-7 ,y_down+ROW_HEIGHT), width=2)
                        pygame.draw.line(screen, "white", (x_across+ROW_HEIGHT-2, y_down+ROW_HEIGHT-11), (x_across+ROW_HEIGHT-7 ,y_down+ROW_HEIGHT), width=2)
                    elif lines[line]["owned"]:
                        pygame.draw.circle(screen, (255, 255, 0), (x_across+ROW_HEIGHT-5, y_down+ROW_HEIGHT-5), 10)
                        pygame.draw.line(screen, "black", (x_across+ROW_HEIGHT-11, y_down+ROW_HEIGHT-5), (x_across+ROW_HEIGHT-7 ,y_down+ROW_HEIGHT), width=2)
                        pygame.draw.line(screen, "black", (x_across+ROW_HEIGHT-2, y_down+ROW_HEIGHT-11), (x_across+ROW_HEIGHT-7 ,y_down+ROW_HEIGHT), width=2)
                    else:
                        pygame.draw.circle(screen, (150,150,150), (x_across+ROW_HEIGHT-5, y_down+ROW_HEIGHT-5), 10)
                        text = font_h4.render("X", True, "white")
                        screen.blit(lock, (x_across+ROW_HEIGHT-5-lock.get_width()/2, y_down+ROW_HEIGHT-5-lock.get_height()/2-1))
                
                elif line_tab == "type":
                    if lines[line]["type"] == "Standard":
                        color = (136, 0, 21)
                    elif lines[line]["type"] == "Electric":
                        color = (196, 255, 34)
                    elif lines[line]["type"] == "MagLev":
                        color = (22, 4, 122)
                    elif lines[line]["type"] == "Monorail":
                        color = (0, 162, 232)

                    if lines[line]["owned"]:
                        pygame.draw.circle(screen, color, (x_across+ROW_HEIGHT-5, y_down+ROW_HEIGHT-5), 10)
                        color = "black" if lines[line]["type"] == "Electric" else "white"
                        text = font_h1.render(lines[line]["type"][0], True, color)
                        if lines[line]["type"][0] == "M":
                            text= pygame.transform.scale(text, (14, 14))
                        else:
                            text= pygame.transform.scale(text, (10, 14))
                        screen.blit(text, (x_across+ROW_HEIGHT-5-text.get_width()/2, y_down+ROW_HEIGHT-5-text.get_height()/2))

                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING

            rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT, ROW_HEIGHT)
            pygame.draw.rect(screen, "green", rect, border_radius=8)
            text = font_h1.render("+", True, "white")
            screen.blit(text, ((rect[0]+rect[2]/2)-text.get_width()/2+4, (rect[1]+rect[3]/2)-text.get_height()/2-1))
            if button_check(rect):
                new_line[0]["shown"] = True

            for i in range(0, 32-len(lines)):
                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING
              
            for rect in line_rects:
                if not train_purchase:
                    if button_check(rect):
                        for item in trains+lines+upgrades+new_line:
                            item["shown"] = False
                        lines[line_rects.index(rect)]["shown"] = True

            # mini info line_tab selection
            for tab in ["owned", "type"]:
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING+2, 20, ROW_HEIGHT-2)
                pygame.draw.rect(screen, (54, 153, 43), rect)
                font_h4.set_bold(True)
                text = font_h4.render("O", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/5)-text.get_height()/2))
                text = font_h4.render("N", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*3/5)-text.get_height()/2))
                font_h4.set_bold(False)

                rect = pygame.Rect(x_across+SPACING+(120-SPACING-SPACING/2), y_down+SPACING+2, 20, ROW_HEIGHT-2)
                pygame.draw.rect(screen, "red", rect)
                font_h4.set_bold(True)
                text = font_h4.render("O", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*1/4)-text.get_height()/2))
                text = font_h4.render("F", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/4)-text.get_height()/2))
                text = font_h4.render("F", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*3/4)-text.get_height()/2))
                font_h4.set_bold(False)

                if line_tab == tab:
                    rect = pygame.Rect(x_across+SPACING+20, y_down+SPACING+2, 120-SPACING-SPACING/2, ROW_HEIGHT-2)
                else:
                    rect = pygame.Rect(x_across+SPACING, y_down+SPACING+2, 120-SPACING-SPACING/2, ROW_HEIGHT-2) 

                pygame.draw.rect(screen, (150,150,150), rect)

                if button_check(rect):
                    line_tab = None if line_tab == tab else tab

                if tab == "owned":
                    text = font_h4.render("Owned", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*1/3)-text.get_height()/2+1))
                    text = font_h4.render("Status", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/3)-text.get_height()/2+1))
                elif tab == "type":
                    text = font_h4.render("Line", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]*2/5)-text.get_width()/2, rect[1]+(rect[3]*1/3)-text.get_height()/2+1))
                    text = font_h4.render("Type", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]*2/5)-text.get_width()/2, rect[1]+(rect[3]*2/3)-text.get_height()/2+1))
                    rect = pygame.Rect(rect[0]+75, y_down+29, 20, 20)
                    pygame.draw.rect(screen, "yellow", rect)
                    font_h4.set_bold(True)
                    text = font_h4.render("!", True, "black")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]/2)-text.get_height()/2))
                    font_h4.set_bold(False)
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        hover_time += 3 * dt
                        info_draw = True
                    else:
                        if hover_time < 0:
                            pass
                        else:
                            hover_time -= 3 * dt
                        info_draw = False
                    
                    if hover_time >= 1 and info_draw:
                        hover_time = 2
                        info_draw = True
                    else:
                        info_draw = False

                

                x_across += SPACING/2+140 - SPACING

        if menu_page == "Trains":
            train_rects = []
            for train in range(len(trains)):
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-8, ROW_HEIGHT-8)
                screen.blit(trains[train]["icon"], (x_across+SPACING, y_down+SPACING))

                train_rects.append(rect)

                if train_tab == "stored":
                    if trains[train]['stored'] > 0:
                        pygame.draw.circle(screen, "white", (x_across+ROW_HEIGHT, y_down+ROW_HEIGHT), 10)
                        text = font_h4.render(str(trains[train]["stored"]), True, "black")
                        screen.blit(text, (x_across+ROW_HEIGHT-text.get_width()/2, y_down+ROW_HEIGHT-text.get_height()/2))

                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING
                
            for rect in train_rects:
                if button_check(rect):
                    for item in trains+lines+upgrades+new_line:
                        item["shown"] = False
                    trains[train_rects.index(rect)]["shown"] = True

            # train tab
            for tab in ["stored"]:
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING+2, 20, ROW_HEIGHT-2)
                pygame.draw.rect(screen, (54, 153, 43), rect)
                font_h4.set_bold(True)
                text = font_h4.render("O", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/5)-text.get_height()/2))
                text = font_h4.render("N", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*3/5)-text.get_height()/2))
                font_h4.set_bold(False)

                rect = pygame.Rect(x_across+SPACING+(120-SPACING-SPACING/2), y_down+SPACING+2, 20, ROW_HEIGHT-2)
                pygame.draw.rect(screen, "red", rect)
                font_h4.set_bold(True)
                text = font_h4.render("O", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*1/4)-text.get_height()/2))
                text = font_h4.render("F", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/4)-text.get_height()/2))
                text = font_h4.render("F", True, "white")
                screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*3/4)-text.get_height()/2))
                font_h4.set_bold(False)

                if train_tab == tab:
                    rect = pygame.Rect(x_across+SPACING+20, y_down+SPACING+2, 120-SPACING-SPACING/2, ROW_HEIGHT-2)
                else:
                    rect = pygame.Rect(x_across+SPACING, y_down+SPACING+2, 120-SPACING-SPACING/2, ROW_HEIGHT-2) 

                pygame.draw.rect(screen, (150,150,150), rect)

                if button_check(rect):
                    train_tab = None if train_tab == tab else tab

                if tab == "stored":
                    text = font_h4.render("Amount", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*1/3)-text.get_height()/2+1))
                    text = font_h4.render("Stored", True, "white")
                    screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]*2/3)-text.get_height()/2+1))

        if menu_page == "Upgrades":
            upgrade_rects = []
            valid_upgrades = []

            for upgrade in upgrades:
                if not upgrade["owned"]:
                    if not upgrade["predecessor"]:
                        valid_upgrades.append(upgrade)
                        continue

                    valid = True
                    for predecessor_name in upgrade["predecessor"]:
                        # Find the predecessor upgrade with the matching name
                        matched = next((item for item in upgrades if item["name"] == predecessor_name), None)
                        if not matched or not matched["owned"]:
                            valid = False
                            break

                    if valid:
                        valid_upgrades.append(upgrade)                

            for upgrade in range(len(valid_upgrades)):
                rect = pygame.Rect(x_across+SPACING, y_down+SPACING, ROW_HEIGHT-8, ROW_HEIGHT-8)
                screen.blit(upgrades[upgrade]["icon"], (x_across+SPACING, y_down+SPACING))

                upgrade_rects.append(rect)

                if x_across == width - 76:
                    x_across = width - 280
                    y_down += ROW_HEIGHT+SPACING
                else:
                    x_across += ROW_HEIGHT+SPACING
                
            for rect in upgrade_rects:
                if button_check(rect):
                    for item in trains+lines+upgrades+new_line:
                        item["shown"] = False
                    upgrades[upgrade_rects.index(rect)]["shown"] = True

        # close game
        font_h2_diff.set_bold(True)
        rect = pygame.Rect(width - 42, 10, 32, 32)
        pygame.draw.rect(screen, "red", rect)
        text = font_h2_diff.render("X", True, "white")
        screen.blit(text, (rect[0]+(rect[2]/2)-text.get_width()/2, rect[1]+(rect[3]/2)-text.get_height()/2+2))
        if button_check(rect):
            running = False
        font_h2_diff.set_bold(False)

        # bottom menus
        EDGE = width-282
        # money
        if euros >= 100000000000:
            e_number = str(euros).count("0")
        else:
            e_number = None

        if e_number is not None:
            euros_print = f'{str(euros)[0]}.{str(euros)[1:4]}e{e_number}'
        else:
            euros_print = '{:,}'.format(euros)
        
        rect = pygame.Rect(EDGE, height - 200, width-EDGE, 60)
        pygame.draw.rect(screen, "black", rect)
        text = font_h2_diff.render(e_euros(euros), True, "yellow")
        screen.blit(text, (rect[0]+(rect[2]/2)-(text.get_width()/2), rect[1]+(rect[3]/2)-(text.get_height()/2)+2))

        # clock
        # background
        rect = pygame.Rect(EDGE, height - 140, width-EDGE, 140)
        pygame.draw.rect(screen, pygame.Color(128, 50, 1), rect)
        # clock face
        pygame.draw.circle(screen, "black", (EDGE+(width-EDGE)/2, height-70), 61)
        pygame.draw.circle(screen, "white", (EDGE+(width-EDGE)/2, height-70), 58)
        # clock hands
        now = pygame.Vector2(math.floor(seconds_since_date_update), math.floor((seconds_since_date_update%1)*60))
        hour_theta = get_angle(now.x+1.0*now.y/60, 12)
        # minute_theta = get_angle(now.y, 60)
        line_at_angle(screen, (EDGE+(width-EDGE)/2, height-70), 58*0.7, hour_theta, "black", 5)
        # line_at_angle(screen, (EDGE+(width-EDGE)/2, height-70), 58*0.9, minute_theta, "black", 3)
        pygame.draw.circle(screen, "black", (EDGE+(width-EDGE)/2, height-70), 5) 
        # service running markers
        FROM_EDGE = EDGE+14
        rect = pygame.Rect(FROM_EDGE, (height-140)+FROM_EDGE, 140-FROM_EDGE*2, 140-FROM_EDGE*2)
        pygame.draw.arc(screen, "green", rect, get_angle(18-12, 12), get_angle(18-7,12), width = 3)
        FROM_EDGE = EDGE+20
        rect = pygame.Rect(FROM_EDGE, (height-140)+FROM_EDGE, 140-FROM_EDGE*2, 140-FROM_EDGE*2)
        pygame.draw.arc(screen, "green", rect, get_angle(18-21, 12), get_angle(18-12,12), width = 3)
        # draw markings
        for hour in range(0, 12):
            theta = get_angle(hour, 12)
            p1 = circle_point((EDGE+(width-EDGE)/2, height-70), 58 - 5, theta)
            p2 = circle_point((EDGE+(width-EDGE)/2, height-70), 58, theta)
            pygame.draw.line(screen, "black", p1, p2, 3)

        hour = now.x
        minute = now.y

        # date info
        text = font_h4.render(list(months.keys())[month-1], True, "black")
        screen.blit(text, (EDGE+((width-EDGE)/2)-40, height-70-text.get_height()/2))
        text = font_h4.render(str(day), True, "black")
        screen.blit(text, (EDGE+((width-EDGE)/2)+40-text.get_width(), height-70-text.get_height()/2))
        text = font_h4.render(f"Year {year}", True, "black")
        screen.blit(text, (EDGE+(width-EDGE)/2-text.get_width()/2, height-50-text.get_height()/2))

        # income box
        if income_box_shown:
            rect = pygame.Rect(EDGE-310, height-140, 310, 140)
            pygame.draw.rect(screen, pygame.Color(232, 170, 0), rect)
            rect = pygame.Rect(EDGE-305, height-135, 300, 130)
            pygame.draw.rect(screen, "black", rect)
            x_across = EDGE-305
            y_down = height-135
            for statement in range(1,8):
                text = font_h4.render(income_statements[-statement], True, "yellow")
                screen.blit(text, (x_across+2, y_down+2))
                y_down += H4_SIZE+1

        y_down = height-125
        TAB_HEIGHT = 110
        text = font_h3.render("Income", True, "white")
        text = pygame.transform.rotate(text, 90)
        rect = pygame.Rect((width-610 if income_box_shown else width-300)-20, y_down, 38, TAB_HEIGHT)
        pygame.draw.rect(screen, pygame.Color(232, 170, 0), rect, border_top_left_radius=16, border_bottom_left_radius=16)
        screen.blit(text, ((width-610 if income_box_shown else width-300)-10, y_down+(TAB_HEIGHT/2)-(text.get_height()/2)))

        if button_check(rect):
            if income_box_shown:
                income_box_shown = False
            else:
                income_box_shown = True

        if info_draw:
            x_across = width-282
            y_down = height-200
            rect = pygame.Rect(x_across, y_down, 282, 200)
            pygame.draw.rect(screen, (150,150,150), rect)
            x_across += 85
            y_down += 30
            for color, line_class in zip([(136, 0, 21), (236, 255, 17), (16, 12, 115), (0, 162, 232)], ["Standard", "Electric", "MagLev", "Monorail"]):
                pygame.draw.circle(screen, "black", (x_across, y_down), 22)
                pygame.draw.circle(screen, color, (x_across, y_down), 20)
                text = font_h3.render(str(line_class), True, "black")
                screen.blit(text, (x_across+40, y_down - text.get_height()/2))

                y_down += 46

        for city in cities:
            # rect checking for each city - finds which city was clicked, limits on occasions
            if not line_build:
                rect = pygame.Rect(city.loc.x-5, city.loc.y-5, 15, 15)
                if button_check(rect):
                    for clicked in cities:       # makes every other cities  
                        clicked.clicked = False  # 'clicked' status False, then sets 
                    city.clicked = True          # the correct cities status to True
            else:
                city.clicked = False

        # removing large city labels when clicked elsewhere
        if button_check(pygame.Rect(0,0,width,height)):
            for city in cities:
                city.clicked = False

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
                        speed = min(line["speed"], train.speed)
                        trip_time = distance / speed
                        train.trip_hr = trip_time // 60
                        train.trip_min = trip_time % 60
                        if full_day:
                            trains_running = True
                        else:
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

        # hotkeys
        key = pygame.key.get_pressed()
        
        if key[pygame.K_l]:
            menu_page = "Lines"
        elif key[pygame.K_t]:
            menu_page = "Trains"
        elif key[pygame.K_u]:
            menu_page = "Upgrades"
       
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

        # text = font_h5.render(f'{pygame.mouse.get_pos()[0]}, {pygame.mouse.get_pos()[1]}', True, "black")
        # screen.blit(text, (pygame.mouse.get_pos()[0]+10, pygame.mouse.get_pos()[1]+5))

    pygame_widgets.update(events)
    pygame.display.flip()

    # for flashing/pulsing items such as lines in purchase phase
    if flash < 1:
        flash += 0.001
    else:
        flash -= 1

    


    # dt is time between frames, makes flashing smoother.
    dt = clock.tick(120)/1000

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
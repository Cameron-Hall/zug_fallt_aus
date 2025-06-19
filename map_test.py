import pygame
import random
import math
import numpy as np
from scipy.spatial import Delaunay

pygame.init()
screen = pygame.display.set_mode((1400,800))
running = True

width = screen.get_width()
height = screen.get_height()

font = pygame.font.SysFont("ticketing", 20)

class Tile:
    def __init__(self, img, top, right, bottom, left):
        self.img = img
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left



first_names = [
    "Ash", "Bath", "Bay", "Beaver", "Bed", "Bell", "Berry", "Black", "Bloom", "Blue",
    "Brad", "Brent", "Bridge", "Brook", "Brown", "Cam", "Cedar", "Charl", "Chest", "Clear",
    "Clifton", "Clinton", "Coal", "Clover", "Col", "Cran", "Crow", "Cumber", "Daven", "Day",
    "Deer", "Dover", "Down", "Dun", "East", "Edge", "Elm", "Elk", "Fair", "Farm",
    "Fayette", "Fern", "Fish", "Flat", "Forest", "Fort", "Fountain", "Fox", "Frank", "Freder",
    "Glen", "Gold", "Green", "Greer", "Ham", "Han", "Hart", "Hazel", "Hemp", "Hen",
    "High", "Hill", "Hol", "Hope", "Hun", "Iron", "Jackson", "Jam", "Jeff", "John",
    "Jones", "Ken", "King", "Lake", "Lan", "Laurel", "Law", "Leb", "Lex", "Lime",
    "Lin", "Little", "Liver", "Long", "Lynn", "Man", "Maple", "Mar", "Mart", "May",
    "Mid", "Mill", "Milton", "Mon", "Mont", "Mount", "Moun", "New", "North", "Oak",
    "Oce", "Olive", "Orchard", "Ox", "Park", "Peach", "Pine", "Plain", "Pleasant", "Port",
    "Pow", "Pres", "Prince", "Rain", "Red", "River", "Rock", "Rose", "Rox", "Rush",
    "Ruther", "Saint", "Salem", "Salt", "San", "Sand", "Sandy", "Scot", "Shel", "Silver",
    "Smith", "Snow", "South", "Spring", "Stan", "Star", "Stone", "Sun", "Syl",
    "Tall", "Temple", "Thor", "Three", "Tim", "Twin", "Union", "Valley", "Vern", "Wake",
    "Wash", "Water", "West", "White", "Wild", "Willow", "Win", "Wood", "York",
]

last_names = [
    "ville", "ton", "ham", "field", "bury", "ford", "land", "wood", "port", "dale",
    "ridge", "side", "hill", "town", "view", "grove", "creek", "spring", "falls", "lake",
    "bay", "point", "beach", "bend", "summit", "peak", "cross", "fort", "cove", "brook",
    "plains", "groves", "heights", "moor", "hurst", "worth", "combe", "fell", "leigh", "well",
    "gate", "head", "stone", "wick", "holt", "burn", "thorpe", "fleet", "march", "den", "cumbe"
]

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

for tile in tiles:
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
    
TILE_SIZE = 100

tile_order = []
for slot in range((width//TILE_SIZE)*(height//TILE_SIZE)):
    good = False
    while True:
        tile = random.choice(tiles)
        while True:
            if slot == 0:
                tile_order.append(tile)
                good = True
                break
                
            elif tile.left == tile_order[-1].right and (slot < (width//TILE_SIZE) or tile_order[-width//TILE_SIZE].bottom == tile.top):
                tile_order.append(tile)
                good = True
                break
            else:
                break
        if good:
            break

num_points = 50
points = np.random.rand(num_points, 2)
points *= [width, height]  # Scale to screen size    

cities = []
valid_points = []
deletions = 0
for index, point in enumerate(points):
    city_name = str(random.choice(first_names)+random.choice(last_names))
    city_loc = pygame.Vector2(point[0], point[1])
    good = True
    for item in cities:
        if item["loc"].x-70 <= city_loc.x <= item["loc"].x+70 and item["loc"].y-70 <= city_loc.y <= item["loc"].y+70:
            good = False
            deletions += 1
    if good:
        cities.append({"name":city_name, "loc":city_loc})
        valid_points.append([city_loc.x, city_loc.y])

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x_across = 0
    y_down = 0
    for slot in range((width//TILE_SIZE)*(height//TILE_SIZE)):
        screen.blit(tile_order[slot].img, (x_across, y_down))
        x_across += TILE_SIZE

        if x_across == width:
            x_across = 0
            y_down += TILE_SIZE
        
    for city in cities:
        if screen.get_at((int(city["loc"].x), int(city["loc"].y))) == pygame.Color(63, 72, 204):
            cities.remove(city)
            
        pygame.draw.circle(screen, "red", city["loc"], 10)
        text = font.render(city["name"], True, 'black')
        screen.blit(text, city["loc"])

    for simplex in tri.simplices:
        tri_pts = [int_points[i] for i in simplex]
        if not triangle_overlaps_other_rects(tri_pts, exclude_rects):
            pygame.draw.polygon(screen, (220, 220, 220), tri_pts, 1)

    pygame.display.flip()

pygame.quit()
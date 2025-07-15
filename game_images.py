import pygame

pygame.init()

ROW_HEIGHT = 60

class Icons:
    def __init__(self):
        pass

def icon_create(ROW_HEIGHT):
    ICONS = Icons()
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
    ICONS.red_hill = red_hill
    ICONS.great_northern = great_northern
    ICONS.guangdong_star = guangdong_star
    ICONS.west_network = west_network
    ICONS.railspark_bulb = railspark_bulb
    ICONS.railspark_ember = railspark_ember
    ICONS.railspark_torrent = railspark_torrent
    ICONS.railspark_mystic = railspark_mystic
    ICONS.erlington_works = erlington_works
    ICONS.erlington_works_2 = erlington_works_2
    ICONS.north_star_green = north_star_green
    ICONS.north_star_purple = north_star_purple
    ICONS.north_star_red = north_star_red
    ICONS.north_star_yellow = north_star_yellow
    ICONS.express_orange = express_orange
    ICONS.express_blue = express_blue
    ICONS.express_green = express_green
    ICONS.express_red = express_red
    ICONS.thompson_lines_blue = thompson_lines_blue
    ICONS.thompson_lines_red = thompson_lines_red
    ICONS.royal_bronze = royal_bronze
    ICONS.royal_silver = royal_silver
    ICONS.royal_gold = royal_gold
    ICONS.royal_diamond = royal_diamond
    ICONS.peng_enterprises = peng_enterprises
    ICONS.yangtze_monos = yangtze_monos
    ICONS.wang_li = wang_li
    ICONS.southern_star = southern_star
    ICONS.eastern_power = eastern_power
    ICONS.blue_hill = blue_hill
    ICONS.hermann_orange = hermann_orange
    ICONS.hermann_green = hermann_green

    return ICONS

pygame.quit()
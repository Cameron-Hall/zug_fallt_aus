import pygame
import numpy as np
from scipy.spatial import Delaunay

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangular Network (Delaunay)")
clock = pygame.time.Clock()

# Generate random 2D points
num_points = 50
points = np.random.rand(num_points, 2)
points *= [WIDTH, HEIGHT]  # Scale to screen size
tri = Delaunay(points)

# Colors
BG_COLOR = (30, 30, 30)
POINT_COLOR = (255, 80, 80)
LINE_COLOR = (100, 200, 255)

# Convert points to integer tuples for Pygame
int_points = [tuple(map(int, p)) for p in points]

running = True
while running:
    screen.fill(BG_COLOR)

    # Draw triangles
    for simplex in tri.simplices:
        pts = [int_points[i] for i in simplex]
        pygame.draw.polygon(screen, LINE_COLOR, pts, width=1)

    # # Draw points
    # for i, (x, y) in enumerate(int_points):
    #     pygame.draw.circle(screen, POINT_COLOR, (x, y), 4)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
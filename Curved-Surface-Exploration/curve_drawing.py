import pygame
import numpy as np

pygame.init()

WIDTH = HEIGHT = 1000 # must be equal to avoid scaling issues
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BACKGROUND_COLOR = WHITE
LINE_COLOR = BLACK
CURVE_COLOR = BLUE

LINE_SPACING= 50
LINE_WIDTH=2
CURVE_WIDTH = 5

# font = pygame.font.SysFont(None, 35)
# img = font.render('f(x)', True, BLUE)

pygame.display.set_caption("Curved Surface")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Curved Surface")
clock = pygame.time.Clock()

def f(x):
    return x + WIDTH - 2*np.sqrt(x*WIDTH)


def convert_ranges(value, value_min, value_max, new_min, new_max):
    return (((value - value_min) * (new_max - new_min)) / (value_max - value_min)) + new_min

def cartesian_to_pygame(x, y):
    return (x, HEIGHT-y)


def box_screen():
    box_coords = [[(0, 0), (0, HEIGHT)], [(0, HEIGHT), (WIDTH, HEIGHT)], [(WIDTH, HEIGHT), (WIDTH, 0)], [(WIDTH, 0), (0, 0)]]
    for line in box_coords:
        pygame.draw.line(WIN, LINE_COLOR, line[0], line[1], LINE_WIDTH)

def scale(points, min_x, max_x, min_y, max_y):
    output = {}
    new_x=0
    new_y=0
    for x, y in points.items():
        new_x = convert_ranges(x, min_x, max_x, 0, WIDTH)
        new_y = convert_ranges(y, min_y, max_y, 0, HEIGHT)
        output[new_x] = new_y
    return output

def get_func_points(f, a_start, b_end, increment):
    points = {x:f(x) for x in np.arange(a_start, b_end, increment)}
    return points


def graph_points(points):
    min_x = min(points.keys())
    max_x = max(points.keys())
    min_y = min(points.values())
    max_y = max(points.values())

    points = scale(points, min_x, max_x, min_y, max_y)

    scaled_points = dict(map(cartesian_to_pygame, points.keys(), points.values()))
    x_list = list(scaled_points.keys())
    y_list = list(scaled_points.values())

    for index in range(len(x_list)):
        # pygame.draw.circle(WIN, BLUE, (x_list[index], y_list[index]), 1)
        if index > 0:
            pygame.draw.line(WIN, CURVE_COLOR, (x_list[index-1], y_list[index-1]), (x_list[index], y_list[index]), CURVE_WIDTH)



points = get_func_points(f, 0.03, WIDTH, 0.1)

def draw_curve():
    for x in range(0, HEIGHT, LINE_SPACING):
        l_start = (0, x)
        l_end = (x, HEIGHT)
        pygame.draw.line(WIN, LINE_COLOR, (l_start), (l_end), LINE_WIDTH)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    WIN.fill(BACKGROUND_COLOR)
    draw_curve()
    box_screen()
    # graph_points(points)
    # WIN.blit(img, (20, 20))
    pygame.display.flip()
    # pygame.image.save(WIN, 'bla.png')
    # running=False
pygame.quit()

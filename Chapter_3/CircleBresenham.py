import pygame
from math import sqrt

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
done = False
white = pygame.Color(255, 255, 255)
click_count = 0
points = []


def circle_points(x, y, center):
    screen.set_at((x + center[0], y + center[1]), white)
    screen.set_at((y + center[0], x + center[1]), white)
    screen.set_at((y + center[0], -x + center[1]), white)
    screen.set_at((x + center[0], -y + center[1]), white)
    screen.set_at((-x + center[0], -y + center[1]), white)
    screen.set_at((-y + center[0], -x + center[1]), white)
    screen.set_at((-y + center[0], x + center[1]), white)
    screen.set_at((-x + center[0], y + center[1]), white)


def plot_circle(radius, center):
    x = 0
    y = radius
    d = 5/4.0 - radius
    circle_points(x, y, center)
    while y > x:
        if d < 0:  # select E
            d = d + 2 * x + 3
            x += 1
        else:  # select SE
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1
        circle_points(x, y, center)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
            click_count += 1
            if click_count > 1:
                x1, y1 = points[0]
                x2, y2 = points[1]
                radius = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Calculates the distance of a vector
                plot_circle(int(radius), (points[0][0], points[0][1]))
                click_count = 0
                points.clear()

    pygame.display.update()

pygame.quit()

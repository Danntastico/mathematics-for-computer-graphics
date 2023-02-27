import math
import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
pygame.display.set_caption('Naive Circle')
done = False
white = pygame.Color(255, 255, 255)
click_count = 0
points = []


def plot_circle_naive(_radius, center):
    for x in range(-_radius, _radius):
        y = math.sqrt(math.pow(_radius, 2) - math.pow(x, 2))
        screen.set_at((int(x + center[0]), int(y + center[1])), white)
        y = -math.sqrt(math.pow(_radius, 2) - math.pow(x, 2))
        screen.set_at((int(x + center[0]), int(y + center[1])), white)


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
                radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Calculates the distance of a vector
                plot_circle_naive(int(radius), points[0])
                click_count = 0
                points.clear()
    pygame.display.update()
pygame.quit()

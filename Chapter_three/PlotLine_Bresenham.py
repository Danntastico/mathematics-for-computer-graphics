import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
click_counter = 0
points = []

def bresenham_plot_points(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1
    sy = 1

    if x1 < x0:
        sx = -1

    if y1 < y0:
        sy = -1

    err = dx + dy
    while True:
        screen.set_at((x0, y0), green)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
            click_counter += 1
            if click_counter > 1:
                bresenham_plot_points(points[0], points[1])
                click_counter = 0
                points.clear()

    pygame.display.update()

pygame.display.quit()


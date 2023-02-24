import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

click_counter = 0
points = []


def plot_points_naive(v0, v1):
    if v0[0] > v1[0]:
        temp = v1
        v1 = v0
        v0 = temp

    x0, y0 = v0
    x1, y1 = v1
    if x1 - x0 == 0:
        return
    m = (y1 - y0) / (x1 - x0)
    c = y0 - (m * x0)

    for x in range(x0, x1):
        y = (m * x) + c
        screen.set_at((int(x), int(y)), white)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())
            click_counter += 1
            if click_counter > 1:
                plot_points_naive(points[0], points[1])
                click_counter = 0
                points.clear()

    pygame.display.update()

pygame.quit()

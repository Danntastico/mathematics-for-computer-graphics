import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)


def to_pygame_coordinates(_screen, x, y):
    return x, _screen.get_height() - y


def to_cartesian_coordinates(_screen, x, y):
    new_width = _screen.get_width() / 2
    new_height = _screen.get_height() / 2
    return new_width + x, new_height + y


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    position = to_cartesian_coordinates(screen, 0, 0)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10), 1)
    pygame.draw.circle(screen, white, (position[0], position[1]), 100, 1)
    screen.set_at(to_pygame_coordinates(screen, 100, 100), white)
    screen.set_at(to_pygame_coordinates(screen, 200, 200), white)
    pygame.display.update()

pygame.quit()

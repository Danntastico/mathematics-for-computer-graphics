import pygame

pygame.init()

screen_width = 1000
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)


def to_pygame_coordinates(_screen, x, y):
    return x, _screen.get_height() - y


def set_star(_screen, _white, x, y):
    position = to_pygame_coordinates(_screen, x, y)
    pygame.draw.rect(_screen, _white, (position[0], position[1], 5, 5), 2)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    set_star(screen, white, 100, 100)
    set_star(screen, white, 260, 220)
    set_star(screen, white, 270, 120)
    set_star(screen, white, 780, 100)
    set_star(screen, white, 750, 200)
    set_star(screen, white, 640, 250)
    set_star(screen, white, 640, 330)
    set_star(screen, white, 780, 400)
    set_star(screen, white, 820, 360)

    pygame.display.update()


pygame.quit()

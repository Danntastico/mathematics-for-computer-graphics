import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
times_clicked = 0

for y in range(800):
    for x in range(1000):
        pixelColor = pygame.Color(int(x / screen_width * 255), int(y / screen_height * 255), 255)
        screen.set_at((x, y), pixelColor)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            times_clicked += 1
            if times_clicked > 1:
                pygame.draw.line(screen, white, point1, point2, 1)
                times_clicked = 0

    pygame.display.update()

pygame.quit()

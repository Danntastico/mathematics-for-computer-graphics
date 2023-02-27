import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

click_counter = 0
vertex_arr = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            vertex_arr.append(pygame.mouse.get_pos())
            click_counter += 1
            if click_counter == 3:
                pygame.draw.polygon(screen, white, (vertex_arr[0], vertex_arr[1], vertex_arr[2]))
                click_counter = 0
                vertex_arr.clear()

    pygame.display.update()

pygame.quit()

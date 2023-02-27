import pygame
pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
done = False
white = pygame.Color(255, 255, 255)
pygame.font.init()
# font = pygame.font.SysFont('Comic Sans MS', 65, False, True)
font = pygame.font.Font('./fonts/Huglove.ttf', 120)
font2 = pygame.font.Font('./fonts/Zagora.ttf', 100)

text = font.render('Hi there!', False, white)
text2 = font2.render('Yeah!', False, white)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (10, 10))
    screen.blit(text2, (0, 75))
    pygame.display.update()

pygame.quit()

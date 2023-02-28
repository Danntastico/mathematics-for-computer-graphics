import pygame
from pygame.locals import *
from OpenGL.GL import *
from Cube import *
from OpenGL.GLU import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

done = False
white = pygame.Color(255, 255, 255)
camera_aspect_ratio = screen_width / screen_height
gluPerspective(60, camera_aspect_ratio, 0.1, 100)
# glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0, 0, -3)
cube = Cube()
rotate_cube = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rotate_cube = not rotate_cube
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw()
    if rotate_cube:
        glRotatef(0.01, 0, 0.5, 0)
    pygame.display.flip()

pygame.quit()

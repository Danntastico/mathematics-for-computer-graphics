import pygame
from pygame.locals import *
from OpenGL.GL import *
from Cube import *
from OpenGL.GLU import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python, Lights Practice')

done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
camera_aspect_ratio = screen_width / screen_height
gluPerspective(60, camera_aspect_ratio, 0.1, 100)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0, 0, -3)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 0, 1))

print(GL_MAX_LIGHTS)
cube = Cube(GL_POLYGON, '../Materials/Plastic_SpaceBlanketFolds_512_albedo.tiff')
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
        glRotatef(0.1, 0.1, 0.1, 0)
    pygame.display.flip()

pygame.quit()

from OpenGL.GL import *
import pygame


class Mesh3D:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)
                         ]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        self.texture = pygame.image.load()
        self.texID = 0

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_POLYGON)
            glVertex3fv(
                self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t +
                                                     1]])
            glVertex3fv(self.vertices[self.triangles[t +
                                                     2]])
            glEnd()

    def init_texture(self):
        self.texID = glGenTextures(1)
        texture_data = pygame.image.tostring(self.texture, "RGB", False)
        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_MIN_FILTER,
                        GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, texture_data)

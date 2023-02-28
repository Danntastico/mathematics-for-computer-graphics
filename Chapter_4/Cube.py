from Chapter_4.Mesh3D import *


class Cube(Mesh3D):
    def __init__(self):
        self.vertices = [
            (-0.5, -0.5, 0.5),
            (0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5)
        ]
        self.triangles = [
            0, 2, 3,
            0, 3, 1,

            0, 2, 4,
            4, 6, 0,

            0, 6, 7,
            0, 7, 1,

            1, 3, 5,
            1, 5, 7,

            2, 3, 5,
            2, 5, 4,

            6, 4, 5,
            6, 5, 7,
        ]

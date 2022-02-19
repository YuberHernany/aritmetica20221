import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/yuber/Documentos/1UdeA/geo_vec_lin/Intensivo/proyecto_lineal3d")
from general import show_segments

class Polygon:
    def __init__(self, init_points, end_points):
        """init_points and end_points are ndarrays 2d with shape (n, 2)"""
        self.init_points = init_points
        self.end_points = end_points
    def __str__(self):
        return str(self.init_points) + str(self.end_points)
    def showPolygon(self, **kwargs):
        ax = plt.gca()
        show_segments(self.init_points, self.end_points, **kwargs)
    def applyMatrix(self, matrix):
        new_init_points = self.init_points @ matrix
        new_end_points = self.end_points @ matrix
        return Polygon(new_init_points, new_end_points)
    def traslatedByVector(self, vector):
        traslated_init_points = self.init_points + vector
        traslated_end_points = self.end_points + vector
        return Polygon(traslated_init_points, traslated_end_points)



e1, e2 = np.eye(2)[0].reshape(1,2), np.eye(2)[1].reshape(1,2)
origin = np.zeros_like(e1)
init_cuadrado = np.vstack([origin, origin, e1+e2, e1+e2])
end_cuadrado = np.vstack([e1, e2, e1, e2])
cuadrado = Polygon(init_cuadrado, end_cuadrado)


def show_squares(array_translators):
    """array_translators is ndarray shape=(-1, 2), each row is a vector
    that is used for traslating square"""
    for vector in array_translators:
        cuadrado.traslatedByVector(vector).showPolygon(color='black')
        ax.set_aspect('equal')


array_trans = np.array([e1, 2*e1, 3*e1]).reshape(-1, 2)

fig, ax = plt.subplots()
cuadrado.showPolygon(color='black')
show_squares(array_trans)
plt.show()

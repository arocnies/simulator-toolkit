from .visual import Visual
from ..entity import Entity
import matplotlib.pyplot as plt
import numpy as np


class Sphere(Visual):
    def __init__(self, radius: float):
        self.radius = radius
        self.artist = None

    def draw(self, entity: Entity, fig: plt.Figure, ax: plt.Axes) -> None:
        if not self.artist:
            u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
            x = self.radius * np.cos(u) * np.sin(v)
            y = self.radius * np.sin(u) * np.sin(v)
            z = self.radius * np.cos(v)
            self.artist = ax.plot_surface(x, y, z, color='blue', cmap=plt.cm.YlGnBu_r)
        else:
            # no update to surface data
            pass

from .visual import Visual
from ..entity import Entity
import matplotlib.pyplot as plt


class Point(Visual):
    def __init__(self, size: int = 50, color: str = 'red'):
        self.size = size
        self.color = color
        self.artist = None

    def draw(self, entity: Entity, fig: plt.Figure, ax: plt.Axes) -> None:
        if not self.artist:
            self.artist = ax.scatter(
                entity.position[0],
                entity.position[1],
                entity.position[2],
                color=self.color,
                s=self.size,
                label=entity.name
            )
        else:
            self.artist._offsets3d = ([entity.position[0]], [entity.position[1]], [entity.position[2]])

from .visual import Visual
from ..entity import Entity
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


class EntityVector(Visual):
    def __init__(
            self, attr: str,
            v_func: Callable[[Entity], np.ndarray] = None,
            color: str = 'orange',
            scale: float = 1.0
    ):
        self.attr = attr
        self.v_func = v_func
        self.color = color
        self.scale = scale
        self.artist = None

    def draw(self, entity: Entity, fig: plt.Figure, ax: plt.Axes) -> None:
        v = None
        if not self.v_func is None:
            v = self.v_func(entity)
        else:
            v = getattr(entity, self.attr)
        pos = entity.position
        length = np.linalg.norm(v) * self.scale
        if self.artist is None:
            self.artist = ax.plot(
                [pos[0], pos[0] + v[0] * length],
                [pos[1], pos[1] + v[1] * length],
                [pos[2], pos[2] + v[2] * length],
                color=self.color,
                linewidth=2,
                label=f"{entity.name}_{self.attr}"
            )[0]
        else:
            self.artist.set_data_3d(
                [pos[0], pos[0] + v[0] * length],
                [pos[1], pos[1] + v[1] * length],
                [pos[2], pos[2] + v[2] * length]
            )

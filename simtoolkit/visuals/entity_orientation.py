from .visual import Visual
from ..entity import Entity
from .entity_vector import EntityVector
import matplotlib.pyplot as plt
import quaternion


class EntityOrientation(Visual):
    def __init__(self, scale: float = 1000):
        self.scale = scale
        self.artist = None
        self.x_visual = EntityVector(
            "x",
            v_func=lambda e: quaternion.as_rotation_matrix(e.orientation)[:, 0],
            color='red',
            scale=scale
        )
        self.y_visual = EntityVector(
            "y",
            v_func=lambda e: quaternion.as_rotation_matrix(e.orientation)[:, 1],
            color='green',
            scale=scale
        )
        self.z_visual = EntityVector(
            "z",
            v_func=lambda e: quaternion.as_rotation_matrix(e.orientation)[:, 2],
            color='blue',
            scale=scale
        )

    def draw(self, entity: Entity, fig: plt.Figure, ax: plt.Axes) -> None:
        self.x_visual.draw(entity=entity, fig=fig, ax=ax)
        self.y_visual.draw(entity=entity, fig=fig, ax=ax)
        self.z_visual.draw(entity=entity, fig=fig, ax=ax)

from typing import List
from .entity import Entity
from .visuals import Point
import matplotlib.pyplot as plt
import numpy as np


class Simulation:
    def __init__(self):
        self.entities: List[Entity] = []
        self.figure = None
        self.ax = None

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def remove_entity(self, entity: Entity) -> None:
        self.entities.remove(entity)

    def _init_figure(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        self.figure = fig
        self.ax = ax

    def update(self, t: float, dt: float) -> None:
        for i in range(0, int(t), int(dt)):
            for entity in self.entities:
                for model in entity.models:
                    model.update(entity, dt)

    def entity(
            self,
            name: str,
            position=None,
            velocity=None,
            orientation=None,
            angular_velocity=None,
            visuals=None,
            models=None
    ) -> Entity:
        if position is None:
            position = [0, 0, 0]
        if velocity is None:
            velocity = [0, 0, 0]
        if orientation is None:
            orientation = [1, 0, 0, 0]  # default orientation (no rotation)
        if angular_velocity is None:
            angular_velocity = [0, 0, 0]
        if models is None:
            models = []
        if visuals is None:
            visuals = [Point()]
        entity = Entity(
            name=name,
            position=position,
            velocity=velocity,
            orientation=orientation,
            angular_velocity=angular_velocity,
            visuals=visuals,
            models=models
        )
        self.entities.append(entity)
        return entity

    def animate(self, frame: int, t: float, dt: float) -> None:
        self.update(t, dt)
        self.show()

    def show(self):
        if self.figure is None:
            self._init_figure()

        # Render all entity visuals
        for entity in self.entities:
            for visual in entity.visuals:
                visual.draw(entity, self.figure, self.ax)

        # Add legend and title
        self.ax.legend()
        self.ax.set_title('Simulation')
        self.ax.set_xlabel('X (km)')
        self.ax.set_ylabel('Y (km)')
        self.ax.set_zlabel('Z (km)')

        self._scale_view_to_limits()

        # Show the plot
        plt.show()

    def _scale_view_to_limits(self):
        # Set the axes limits based on the positions of the entities
        min_x = min(entity.position[0] for entity in self.entities)
        max_x = max(entity.position[0] for entity in self.entities)
        min_y = min(entity.position[1] for entity in self.entities)
        max_y = max(entity.position[1] for entity in self.entities)
        min_z = min(entity.position[2] for entity in self.entities)
        max_z = max(entity.position[2] for entity in self.entities)
        if min_x != max_x:
            self.ax.set_xlim(min_x, max_x)
        if min_y != max_y:
            self.ax.set_ylim(min_y, max_y)
        if min_z != max_z:
            self.ax.set_zlim(min_z, max_z)
        # Set the axis settings
        set_axes_equal(self.ax)


def set_axes_equal(ax):
    """
    From https://stackoverflow.com/a/31364297/2832996
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
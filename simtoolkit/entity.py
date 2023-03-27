import numpy as np
import quaternion


class Entity:
    """
    Entity represents an object in 6DOF space.
    """

    def __init__(
            self,
            name: str,
            position=None,
            velocity=None,
            orientation=None,
            angular_velocity=None,
            visuals=None,
            models=None
    ):
        if models is None:
            models = []
        if visuals is None:
            visuals = []
        if angular_velocity is None:
            angular_velocity = [0, 0, 0]
        if velocity is None:
            velocity = [0, 0, 0]
        if position is None:
            position = [0, 0, 0]
        if orientation is None:
            orientation = [1, 0, 0, 0]  # default orientation (no rotation)
        self.name = name
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.orientation = np.quaternion(*orientation)
        self.angular_velocity = np.array(angular_velocity)
        self.visuals = visuals
        self.models = models

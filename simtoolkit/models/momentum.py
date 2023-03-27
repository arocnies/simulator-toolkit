from .model import Model
from ..entity import Entity
import quaternion


class Momentum(Model):
    def update(self, entity: Entity, dt: int):
        entity.position += dt * entity.velocity
        rotation_quaternion = quaternion.from_rotation_vector(entity.angular_velocity * dt)
        entity.orientation = (rotation_quaternion * entity.orientation)

import numpy as np
from .simulation import Simulation
import matplotlib.animation as animation
from IPython.display import HTML


def video(simulation: Simulation, t: int, dt: int):
    anim = animation.FuncAnimation(
        simulation.figure,
        simulation.animate,
        frames=t,  # This is our `t`, how many frames to create
        interval=50,  # Sets the animation frame step
        fargs=[dt, dt],  # This is our step to update
        # blit=True,  # blit=True re-draws only the parts that have changed.
        repeat=False
    )
    return HTML(anim.to_html5_video())


class WGS84:
    spin_rate = 7.2921150e-5  # radians per second
    gravitation_constant = 6.67430e-11  # m^3/(kg*s^2)
    radius = 6378.137  # kilometers

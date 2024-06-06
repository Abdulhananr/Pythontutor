from math import cos, sin, pi

def kinematics(x_func, y_func, t, dt=1E-6):
    """
    Calculate the kinematic properties (position, velocity, acceleration) of a particle.
    
    Parameters:
    x_func (function): Function representing the x-coordinate as a function of time.
    y_func (function): Function representing the y-coordinate as a function of time.
    t (float): Time at which to evaluate the kinematic properties.
    dt (float): Time step used in numerical differentiation (default is 1E-6).
    
    Returns:
    tuple: A tuple containing the position, velocity, and acceleration vectors at time t.
    """
    # Calculate velocity using central difference method
    vx = (x_func(t + dt) - x_func(t - dt)) / (2 * dt)
    vy = (y_func(t + dt) - y_func(t - dt)) / (2 * dt)
    velocity = (vx, vy)
    
    # Calculate acceleration using central difference method
    ax = (x_func(t + dt) - 2 * x_func(t) + x_func(t - dt)) / (dt ** 2)
    ay = (y_func(t + dt) - 2 * y_func(t) + y_func(t - dt)) / (dt ** 2)
    acceleration = (ax, ay)
    
    # Calculate position
    position = (x_func(t), y_func(t))
    
    return position, velocity, acceleration

t = 1
R = 1
w = 2 * pi
x_func = lambda t: R * w * cos(w * t)
y_func = lambda t: R * sin(w * t)

print(kinematics(x_func, y_func, t, dt=1E-5))

"""
Sample run:
python kinematics.py
((6.283185307179586, -2.4492935982947064e-16), (0.0, 6.283185303064565), (-248.05022036389343, 8.88164867172969e-06))
"""

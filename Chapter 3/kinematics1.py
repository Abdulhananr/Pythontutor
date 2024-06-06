from math import exp

def kinematics(x_func, t, dt=1E-6):
    """
    Calculate the kinematic properties (position, velocity, acceleration) of a particle.
    
    Parameters:
    x_func (function): Function representing the position as a function of time.
    t (float): Time at which to evaluate the kinematic properties.
    dt (float): Time step used in numerical differentiation (default is 1E-6).
    
    Returns:
    tuple: A tuple containing the position, velocity, and acceleration at time t.
    """
    # Calculate velocity using central difference method
    v = (x_func(t + dt) - x_func(t - dt)) / (2 * dt)
    
    # Calculate acceleration using central difference method
    a = (x_func(t + dt) - 2 * x_func(t) + x_func(t - dt)) / (dt ** 2)
    
    # Calculate position
    x = x_func(t)
    
    return x, v, a

x_func = lambda t: exp(-(t - 4) ** 2)

print(kinematics(x_func, 5, 1E-5))

"""
Sample run:
python kinematics1.py
(0.36787944117144233, -0.7357588822892723, 0.7357586762068989)
"""

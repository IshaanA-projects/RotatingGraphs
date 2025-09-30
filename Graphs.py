import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 61)
y = x
y_quadratic = x ** 2
y_cubic = x ** 3

def x_rotate(n, z, angle):
    radian = (np.pi / 180) * angle
    x_radian = (n * np.cos(radian)) - (z * np.sin(radian))
    return x_radian

def y_rotate(n, z, angle):
    radian = (np.pi / 180) * angle
    y_radian = (n * np.sin(radian)) + (z * np.cos(radian))
    return y_radian
theta = -1 * float(input("What angle do you want to rotate the graphs by?   "))


rotate_y_linear     = y_rotate(x, y, theta)
rotate_y_quadratic  =  y_rotate(x, y_quadratic, theta)
rotate_y_cubic      = y_rotate(x, y_cubic, theta)


rotate_x_linear = x_rotate(x, y, theta)
rotate_x_quadratic =  x_rotate(x, y_quadratic, theta)
rotate_x_cubic = x_rotate(x, y_cubic, theta)

plt.close("all")

# Make figure square and use square subplots
fig, axes = plt.subplots(3, 2, 
                         figsize=(8, 12),      # overall figure size
                         constrained_layout=True)  # automatically adjusts spacing

# Flatten axes array for easy looping
axes = axes.flatten()

# Original graphs
axes[0].plot(x, y)
axes[0].grid("all")
axes[0].set_title("Linear graph")

axes[1].plot(rotate_x_linear, rotate_y_linear)
axes[1].grid("all")
axes[1].set_title("Rotated linear graph")

axes[2].plot(x, y_quadratic)
axes[2].grid("all")
axes[2].set_title("Quadratic graph")

axes[3].plot(rotate_x_quadratic, rotate_y_quadratic)
axes[3].grid("all")
axes[3].set_title("Rotated Quadratic graph")

axes[4].plot(x, y_cubic)
axes[4].grid("all")
axes[4].set_title("Cubic graph")

axes[5].plot(rotate_x_cubic, rotate_y_cubic)
axes[5].grid("all")
axes[5].set_title("Rotated cubic graph")

# Make each subplot square
for ax in axes:
    ax.set_aspect('equal', adjustable='box')

plt.show()
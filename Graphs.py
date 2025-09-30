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
plt.subplot(3, 2, 1)
plt.plot(x, y)
plt.grid("all")
plt.title("Linear graph")

plt.subplot(3, 2, 2)
plt.plot(rotate_x_linear, rotate_y_linear)
plt.grid("all")
plt.title("Rotated linear graph")

plt.subplot(3, 2, 3)
plt.plot(x, y_quadratic)
plt.grid("all")

plt.title("Quadratic graph")

plt.subplot(3, 2, 4)
plt.plot(rotate_x_quadratic, rotate_y_quadratic)
plt.grid("all")
plt.title("Rotated Quadratic graph")

plt.subplot(3, 2, 5)
plt.plot(x, y_cubic)
plt.grid("all")
plt.title("Cubic graph")

plt.subplot(3, 2, 6)
plt.plot(rotate_x_cubic, rotate_y_cubic)
plt.grid("all")
plt.title("Rotated cubic graph")

plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0.7)

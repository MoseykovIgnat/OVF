import matplotlib.pyplot as plt
import numpy as np

#10 2 
#2 10	
a = d = 10
b = c = 2

y0 = 5.2
x0 = 5
t1 = 0
t2 = 10
N = 1000
#h=(t2-t1)/N
h = 0.005


def draw(title, x, y):
    plt.title(title)
    plt.xlabel("x (Число хищников)")
    plt.ylabel("y (Число жертв)")
    plt.grid()
    plt.plot(x, y)
    plt.show()

def f_x(x, y):
    return a * x - b * x * y

def f_y(x, y):
    return c * x * y - d * y


def RungKut2():
    alpha = 3. / 4
    xarray, yarray = [],[]
    a1 = 1 - alpha
    a2 = alpha
    b2 = 1. / (2 * alpha)
    yi = y0
    xi = x0
    for i in range(0, N + 1):
        x = xi + h * (a1 * f_x(xi, yi) + a2 * f_x(xi + h * b2 * f_x(xi, yi), yi + h * b2 * f_y(xi, yi)))
        y = yi + h * (a1 * f_y(xi, yi) + a2 * f_y(xi + h * b2 * f_x(xi, yi), yi + h * b2 * f_y(xi, yi)))
        xarray.append(x)
        yarray.append(y)
        yi = y
        xi = x   
    return xarray, yarray


tarray = np.linspace(t1, t2, N+1) 
RK = RungKut2()
plt.plot(tarray, RK[0], 'r', label='Хищник(x)')
plt.plot(tarray, RK[1], 'g', label='Жертва(y)')
plt.legend()
plt.show()

draw('Фазовая плоскость',RK[0], RK[1])


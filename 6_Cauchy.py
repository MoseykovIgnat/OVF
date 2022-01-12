# Когда лучше использовать численный методы меньшего порядка(с увеличение порядка метода область абсолютной устойчивости сокращается)
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 10
y0 = 1
N = 90


def draw(title, x, y):
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y)
    plt.show()


def func(x):
    return (-1) * x


def Real():  # y=exp(-x)
    h = (b - a) / N
    yvals, xvals = [], []
    for i in range(0, N + 1):
        y = np.exp((-1) * (a + i * h))
        yvals.append(y)
        xvals.append(a + i * h)
        yi = y
    ax.plot(xvals, yvals, label='Real One')
    return yvals


def Euler():
    h = (b - a) / N
    yvals, xvals = [], []
    yi = y0
    for i in range(0, N + 1):
        y = yi + h * func(yi)
        yvals.append(y)
        xvals.append(a + i * h)
        yi = y
    ax.plot(xvals, yvals, 'g.-', label='Euler')
    return yvals


def RungKut2():
    h = (b - a) / N
    yvals, xvals = [], []
    yi = y0
    al = 3. / 4
    for i in range(0, N + 1):
        fi = func(yi)
        y = yi + h * ((1 - al) * fi + al * func(yi + h * fi/( al)))
        yvals.append(y)
        xvals.append(a + i * h)
        yi = y
    ax.plot(xvals, yvals, 'r.-', label='RungKut2')
    return yvals


def RungKut4():
    h = (b - a) / N
    yvals, xvals = [], []
    yi = y0
    al = 3. / 4
    for i in range(0, N + 1):
        k1 = func(yi)
        k2 = func(yi + k1 * h / 2)
        k3 = func(yi + k2 * h / 2)
        k4 = func(yi +  k3 * h)
        y = yi + h * (k1 + 2 * (k2 + k3) + k4) / 6
        yvals.append(y)
        xvals.append(a + i * h)
        yi = y
    ax.plot(xvals, yvals, 'b.-', label='RungKut4')
    return yvals


yrung4, yrung2, yreal, xvals, diff = [], [], [], [], []
fig, ax = plt.subplots()
yeul = Euler()
yrung4 = RungKut4()
yrung2 = RungKut2()

yreal = Real()
ax.legend(loc=1)
plt.show()

fig, axs = plt.subplots()
h = (b - a) / N
for i in range(0, N + 1):
    xvals.append(a + i * h)
    helper = (yrung4[i] - yrung2[i])
    diff.append(helper)

draw('Погрешность', xvals, diff)

# почему ошибка ньютона растет с увелечением N
import matplotlib.pyplot as plt
import numpy as np
from array import *
import math


def X(k):
    return 1 + k / N


def Y(k):
    return math.sin((X(k)) ** 4)


# Интерполяционный полиноме Лагранжа

# Вспомогательный полином
def li(x, i):
    l = 1
    for j in range(0, N + 1):
        if (j != i):
            l *= (x - X(j))
    return l


def Langr(x):
    Pn = 0
    for i in range(0, N + 1):
        Pn += Y(i) * li(x, i) / li(X(i), i)
    return Pn


# Интерполяционный полином Ньютона
def Newton(x):
    a = []
    for i in range(0, N + 1):
        a.append(Y(i))
        for j in range(0, i):
            a[i] = (a[i] - a[j]) / (X(i) - X(j))
    res = a[N]
    for i in range(N - 1, -1, -1):
        res = res * (x - X(i)) + a[i]
    return res


fig, axs = plt.subplots(nrows=12, ncols=1, figsize=(15, 30))  # axes - список осей
for N in range(38, 50):
    xvals, yvals, Lvals, Nvals = [], [], [], []
    for i in range(0, N + 1):
        x = X(i)
        y = math.sin(x ** 4)
        xvals.append(x)
        yvals.append(y)
        Lvals.append(Langr(x) - y)
        Nvals.append(Newton(x) - y)
    axs[N - 38].plot(xvals, Nvals, label='Ньютон')
    axs[N - 38].plot(xvals, Lvals, label='Лагранж')
    axs[N - 38].set_title("N = %s" % (N))
    axs[N - 38].set_xlabel('X')
    axs[N - 38].set_ylabel('Погрешность')
    axs[N - 38].legend(loc=4)

fig.tight_layout()  # Для того, чтобы графики не накладывались друг на друга
fig.savefig("fifth1.png")

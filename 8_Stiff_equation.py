# import matplotlib.pyplot as plt
import numpy as np
from math import *
import time
import timeit

#Собственные числа системы (-1 и -1000 => отношение 10^3 => система жесткая)
u0 = 1
v0 = 1
N = 1000
left = 0
right = 1

a = 998
b = 1998
c = -999
d = -1999
h = (right - left) / N

def f_u(u,v):
    return a*u + b*v

def f_v(u,v):
    return c*u + d*v

def Euler():
    uarray, varray = [], []
    ui = u0
    vi = v0
    uarray.append(u0)
    varray.append(v0)
    for i in range(0,N):
        u = ui + h*f_u(ui,vi)
        v = vi + h*f_v(ui,vi)
        uarray.append(u)
        varray.append(v)
        ui = u
        vi = v 
    return uarray, varray


def Kramer(h, xi, yi):
    delta = (1 - h*a) * (1 - h*d) - (h*b) * (h*c)
    deltax = (1 - h*d)*xi + h*b*yi
    deltay = (1 - h*a)*yi + h*c*xi
    return deltax/delta, deltay/delta

def impEuler():
    uarray = []
    varray = []
    ui = u0
    vi = v0
    uarray.append(u0)
    varray.append(v0)
    for i in range(0,N):
        u, v = Kramer(h, ui, vi)
        uarray.append(u)
        varray.append(v)
        ui = u
        vi = v  
    return uarray, varray

def realsol():
    realu,realv,tarray = [],[],[]
    tarray.append(left)
    alpha = (u0 + v0)*exp(left)
    beta = -1*(u0+2*v0)*exp(1000*left)
    realu.append(2*alpha*exp(-tarray[0]) + beta*exp(-1000*tarray[0]))
    realv.append(-beta*exp(-1000*tarray[0]) - alpha*exp(-tarray[0]))
    for i in range(0, N):
        tarray.append(tarray[i] + h)
        realu.append(2*alpha*exp(-tarray[i]) + beta*exp(-1000*tarray[i]))
        realv.append(-beta*exp(-1000*tarray[i]) - alpha*exp(-tarray[i]))
    return realu,realv,tarray

def deterr():
    err_exp_u,err_exp_v,err_imp_u,err_imp_v = [],[],[],[]
    for i in range(0, N+1):
        err_exp_u.append(abs(Euler[0][i] - realu[i]))
        err_exp_v.append(abs(Euler[1][i] - realv[i]))
        err_imp_u.append(abs(ImEuler[0][i] - realu[i]))
        err_imp_v.append(abs(ImEuler[1][i] - realv[i]))
    return  err_exp_u,err_exp_v,err_imp_u,err_imp_v   

def draws(t,x,y,title):
    plt.plot(t, x, label = 'x')
    plt.plot(t, y, label = 'y')
    plt.title(title)
    plt.legend()
    plt.show()

def drawer(i,j,t,err,title):
    axs[i, j].plot(t, err)
    axs[i, j].set_xlabel('t')
    axs[i, j].set_ylabel('Error x/y')
    axs[i, j].set_title(title)
    axs[i, j].set_xscale('log')
    axs[i, j].set_yscale('log')
    axs[i, j].grid()






time0=time.time()
Euler =  Euler()
print("Time for explicit method %s\n" % (time.time() - time0))

time1=time.time()
ImEuler = impEuler()
print("Time for implicit method %s" % (time.time() - time1))
realu,realv,tarray = realsol()

# draws(tarray,Euler[0],Euler[1],'Явная схема Эйлера')
# draws(tarray,Euler[0],Euler[1],'Явная схема Эйлера')
# draws(tarray,ImEuler[0],ImEuler[1],'Неявная схема Эйлера')
# draws(tarray,realu,realv,'Аналитическое решение')

# err_exp_u,err_exp_v,err_imp_u,err_imp_v=deterr()

# fig, axs = plt.subplots(2, 2, figsize=(15, 9))
# fig.subplots_adjust(hspace=0.4)
# drawer(0,0,tarray,err_exp_u,'Явная схема Эйлера (Error x)')
# drawer(0,1,tarray,err_exp_v,'Явная схема Эйлера (Error y)')   
# drawer(1,0,tarray,err_imp_u,'Неявная схема Эйлера (Error x)')    
# drawer(1,1,tarray,err_imp_v,'Неявная схема Эйлера (Error y)') 
# plt.show() 
    








import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi,cos,sqrt

xleft=0
xright=1
tleft=0
tright=1
N=100
T=50
h=(xright-xleft)/N
tau=(tright-tleft)/T

def draw(title, x,xtitle, y,ytitle):
    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.grid()
    plt.plot(x, y)
    plt.show()

def Fill_massive_same_values(value,amount):
	massive_name=[]
	for i in range (0,amount+1):
		massive_name.append(value)
	return massive_name

def u0_func(x):
	return x*((1-x/xright)**2)

def Linear_operator(m,j):
	return((u[m][j+1]-2*u[m][j]+u[m][j+1])/h*h)

def boundary_conditions():
	u_0,t,u1=[],[],[]
	for i in range(0,N+1):
		u_0.append(u0_func(xleft+i*h))
	u1.append(u_0)
	for j in range(0,T+1):
		t.append(tleft+j*tau)
	return u1,t


def sweep_method(a, b, c, d):
    for i in range(0, N-1): #Прямая прогонка
        w = a[i]/b[i-1]
        b[i]=b[i]-w*c[i-1]
        d[i]=d[i]-w*d[i-1]
    y=[]
    y = Fill_massive_same_values(0,N-1)
    y[N-2]=d[N-2]/b[N-2]
    for i in range(N-3,-1,-1): #обратная прогонка
        y[i] = 1/b[i]*(d[i]-c[i]*y[i+1])
    return y


a,b,c,d,u,u_max,result,t=[],[],[],[],[],[],[],[]
u,t=boundary_conditions()

for m in range(0,T):
	a=Fill_massive_same_values(-0.5*tau/h**2,N-1)
	b=Fill_massive_same_values(1 + tau/h**2,N-1)
	c=Fill_massive_same_values(-0.5*tau/h**2,N-1)
	a[0]=0
	c[N-2]=0
	d=[]
	for j in range(0,N):
		d.append(u[m][j] + tau / 2 * Linear_operator(m,j))
	result = []
	result = sweep_method(a,b,c,d)
	result.append(0)
	u.append(result)

for i in range(len(u)):
    u_max.append(max(u[i]))

   
draw("The dependence of the maximum temperature versus time",t,"time",u_max,"max_temp")



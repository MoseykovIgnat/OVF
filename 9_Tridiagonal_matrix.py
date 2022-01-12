import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi,cos,sqrt
from array import *
import scipy.special as sc

left=0
right=pi
N=100
h=(right-left)/N
firstlambda=0
secondlambda=0
firstmu=0
secondmu=2
#sin(x^2); sin^2(x)



def inputval(a,value):
	for i in range (0,N+1):
		a.append(value)
	return a
	
def func(x):
	#return sin(x)
	
	return sin(x)*sin(x)

	#return sin(x*x)

def Analytical(x):
    #return -sin(x)+(secondmu-firstmu)/pi*x + firstmu #For sin(x)

    return ((secondmu-firstmu-pi**2/4)/pi)*x+firstmu-1./4+x**2/4+cos(x)**2/4 # for (sin(x))^2

    # Fresnelint=sc.fresnel(sqrt(pi*2))[0]
    # Fresnelintx=sc.fresnel(sqrt(2/pi)*x)[0]
    # c2=(secondmu-cos(pi*pi)/2-sqrt(pi*pi*pi/2)*Fresnelint-firstmu+1/2)/pi
    # c1=firstmu-1/2
    # return c2*x+c1+x*sqrt(pi/2)*Fresnelintx+cos(x*x)/2

def fillin():
	f,x,ay=[],[],[]
	for i in range (0,N+1):
		x.append(left+h*i)
		f.append(h*h*func(x[i]))
		ay.append(Analytical(x[i]))

	return x,f,ay



def sweepmeth(a,b,c,f,x):
	alpha,beta,y=[],[],[]
	alpha=inputval(alpha,0)
	beta=inputval(beta,0)
	y=inputval(y,0)
	alpha[1]=firstlambda
	beta[1]=firstmu
	for i in range(1,N):
		alpha[i+1]=(-b[i] / (c[i] + alpha[i] * a[i]))
		beta[i+1]=(f[i] - a[i] * beta[i]) / (c[i] + alpha[i] * a[i])

	y[N]=(secondmu+secondlambda*beta[N])/(1-alpha[N]*secondlambda)
	for i in range (N-1,-1,-1):
		y[i]=alpha[i+1]*y[i+1]+beta[i+1]

	return y

def draw(title, x, y):
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y)
    plt.show()


def draw2(x, yan, y):
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, yan, label="Analytical solution")
    plt.plot(x,y,label="my solution")
    plt.legend()
    plt.show()


#Fill in lists
a,b,c,f,x,y,ay=[],[],[],[],[],[],[]
x,f,ay=fillin()
f[0]=(-1)*firstmu
f[N]=(-1)*secondmu
a=inputval(a,1)
a[0]=0
c=inputval(c,-2)
b=inputval(b,1)
b[N]=0


y=sweepmeth(a,b,c,f,x)

draw2(x,ay,y)

errorsy=[]
for i in range (0,N+1):
	errorsy.append(abs(y[i]-ay[i]))

draw("Погрешность",x,errorsy)
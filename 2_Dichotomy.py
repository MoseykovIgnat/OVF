import matplotlib.pyplot as plt
import numpy as np
from array import *


a=np.float32(2.0)
a=2.0 #float 64
left=0.1 # f:[left,right]->R
right=0.2
a=10  #width
U_0=1 #height
helper=np.sqrt(2*a*a*U_0)
x1=np.linspace(left,right, 500) #x for func and dfunc

def draw(title,x,y):
	plt.title(title) 
	plt.xlabel("x") 
	plt.ylabel("y") 
	plt.grid()      
	plt.plot(x, y)  
	plt.show()


def func(x):
	return np.sqrt(1/x)-1/(np.tan(helper*np.sqrt(1-x)))

def dfunc(x): #proizvodnaya dlya newton
    helper2=np.sqrt(1-x)
    return (-1)*(helper/(helper2*(np.sin(helper*helper2))**2) + 1/(x*x*np.sqrt(1/x-1)))/2

draw("График ф-ии",x1,func(x1))
draw("График производной",x1,dfunc(x1))

def dichotomy(left,right): # f:[left,right]->R
	counter=0
	fleft=func(left)
	while((right-left)>np.finfo(float).eps): 
		counter+=1
		mid=(right+left)/2
		fmid=func(mid)
		if(fmid==0):
			break
		if(fleft*fmid<=0):
			right=mid
			fright=fmid
		else:
			left=mid
		
	print("Method of dichotomy is done!\nNumber of iterations:",counter)
	print("Result is:",mid,"\n")
	

#dichotomy(left,right)


#print(1/dfunc(0.161660908718538)) #Cheking approxim lambda (res -0.015)
def it():
	counter=0
	lm=-0.015 # lm=1/dfunc(x)
	x=0.16
	while True:
		counter+=1
		xn=x-lm*func(x)
		if (np.abs(xn-x)<np.finfo(float).eps):
			break
		else:
			x=xn
	print("Method of simple iterations is done!\nNumber of iterations:",counter)
	print("Result is:",x,"\n")
		
#it()

def newton():
	counter=0
	x=0.16
	while True:
		counter+=1
		lm=1./dfunc(x)
		xn=x-lm*func(x)
		if (np.abs(xn-x)<np.finfo(float).eps):
			break
		else:
			x=xn
	print("Method of Newton is done!\nNumber of iterations:",counter)
	print("Result is:",x,"\n")

dichotomy(left,right)
it()
newton()
#print(np.finfo(float).eps)
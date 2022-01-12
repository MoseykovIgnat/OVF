import matplotlib.pyplot as plt
import numpy as np

aa=-1
ab=1
ba=0
bb=1
intsegment=[4,8,16]
rresa=np.pi/2
rresb=1.29587400873

def afunc(x):
	return 1/(1+x*x)

def bfunc(x):
	return (x**(1/3))*np.exp(np.sin(x))

def trapezoidm(N,a,b,func,rres):
	h=(b-a)/N
	i=1
	helper=0
	while i<=(N-2):
		helper+=(func(a+h*i))
		i+=1

	res=h*((func(a)+func(b)/2)+helper)
	
	print("Method of trapezoidm is done!\nNumber of integral segment:",N)
	print("Result is:",res)
	print("Absolute error:",np.absolute(res-rres))
	print("Relative error:",(np.absolute(res-rres))/rres,"\n")




def simpson(N,a,b,func,rres):
	h=(b-a)/N
	i=1
	helper=0
	while i<=2*N-1:
		if i%2==0:
			helper+=(2*func(a+h*i/2))		
		else:
			helper+=(4*func(a+h*i/2))
		i+=1
	res=h/6*((func(a)+func(b))+helper)
	print("Method of simpson is done!\nNumber of integral segment:",N)
	print("Result is:",res)
	print("Absolute error:",np.absolute(res-rres))
	print("Relative error:",(np.absolute(res-rres))/rres,"\n")

for row in intsegment:
	trapezoidm(row,aa,ab,afunc,rresa)
	#trapezoidm(row,ba,bb,bfunc,rresb)

for row in intsegment:
	#simpson(row,ba,bb,bfunc,rresb)
	simpson(row,aa,ab,afunc,rresa)

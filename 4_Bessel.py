
import matplotlib.pyplot as plt
import numpy as np

delta1=1e-8
delta2=1e-5
#Для симпсона
a=0
b=np.pi
N=16
h=(b-a)/N
#Для проверки равенства на отрезке
a1=0
b1=2*np.pi
N1=100
h1 = (b1 - a1)/N1 #Делим на 100 равных частей отрезок от 0 до 2Пи



def draw(title,x,y):
	plt.title(title) 
	plt.xlabel("x") 
	plt.ylabel("y") 
	plt.grid()      
	plt.plot(x, y)  
	plt.show()

def func(x,t,m):
    return np.cos(m*t - x*np.sin(t))

def simpson(x,m):
	i=1
	helper=0
	while i<=2*N-1:
		if i%2==0:
			helper+=(2*func(x,a+h*i/2,m))		
		else:
			helper+=(4*func(x,a+h*i/2,m))
		i+=1
	res=h/6*((func(x,a,m)+func(x,b,m))+helper)
	return res


def firstfindiff(x, delta):
    dJ = (simpson(x+delta,0) - simpson(x, 0)) / delta
    return dJ


def secfindiff(x, delta):
    dJ = (simpson(x+delta,0) - simpson(x-delta, 0)) / (2*delta)
    return dJ

def checker(delta1,delta2):
	yfir=[]
	ysec=[]
	xall=[]
	i=0
	while(i<=N1):
		x=a1+i*h1
		xall.append(x)
		yfir.append((1/np.pi)*((firstfindiff(x,delta1))+simpson(x,1)))
		ysec.append((1/np.pi)*((secfindiff(x,delta2))+simpson(x,1)))
		i+=1
	# print(yfir)
	# print(ysec)
	draw("Checker",xall,yfir)
	
def checker2(delta):
	yfir=[]
	ysec=[]
	xall=[]
	i=0
	while(i<=N1):
		x=a1+i*h1
		xall.append(x)
		yfir.append((1/np.pi)*((firstfindiff(x,delta))+simpson(x,1)))
		#ysec.append((1/np.pi)*((secfindiff(x,delta2))+simpson(x,1)))
		i+=1
	# print(yfir)
	# print(ysec)
	return max(yfir)
	#draw("Checker",xall,yfir)

checker(delta1,delta2)
#Обосновать есть оптимальный шаг сеткиЛ8ШЮГБ
mydelta=[1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1]

max_err=[]
for i in mydelta:
	helper=checker2(i)
	max_err.append(helper)

print(max_err)
print(mydelta)
plt.plot(mydelta,max_err,'ro')
plt.show()




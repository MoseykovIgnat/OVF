import numpy as np
from math import sin,pi,cos,sqrt,exp
import matplotlib.pyplot as plt

xleft=-6
xright=6
N=1000
h=(xright-xleft)/N
amount_levels = 1
amount_iterations = 50


def Fill_massive_same_values(value,amount):
    massive_name=[]
    for i in range (0,amount+1):
        massive_name.append(value)
    return massive_name

def sweep_method(a, b, c, d):
    for i in range(0, N): #Прямая прогонка
        w = a[i]/b[i-1]
        b[i]=b[i]-w*c[i-1]
        d[i]=d[i]-w*d[i-1]
    y=[]
    y = Fill_massive_same_values(0,N-1)
    y[N-2]=d[N-1]/b[N-1]
    for i in range(N-2,-1,-1): #обратная прогонка
        y[i] = 1/b[i]*(d[i]-c[i]*y[i+1])
    return y

def U(x):
    return x**2/2

def Analitic_psi(x):
	return ((1/pi)**(1./4))*exp(-x**2/2)


def Orthogonalization(psi_next, psi):
    for i in psi:
        psi_next -= i * (np.inner(psi_next, i)) / np.linalg.norm(i)
    return psi_next

def Reverse_iter_method(psi0):
    E,psi=[],[]
    for i in range(amount_levels):
        psi_next = psi0
        Orthogonalization(psi_next,psi)
        for k in range(0,amount_iterations):
            psi_prev=psi_next
            psi_next=sweep_method(a, np.copy(b), c, np.copy(psi_next))
            psi_next=Orthogonalization(psi_next,psi)
        E0=np.linalg.norm(psi_prev)/np.linalg.norm(psi_next)
        E.append(E0)
        psi_next = psi_next/np.linalg.norm(psi_next)     
        psi.append(psi_next)
    return E,psi

def draw(title, x,xtitle, y,ytitle):
    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.grid()
    plt.plot(x, y)
    plt.show()

def draw_all_levels():
    plt.figure()
    for i in range(0, amount_levels):
        plt.plot(x, psi[i], label = 'psi ' + str(i))
    plt.xlabel("X")
    plt.ylabel("psi(x)", rotation = 0)
    plt.title("The wave functions")
    plt.legend()
    plt.show()

x,y0,a,b,c,E,psi=[],[],[],[],[],[],[]
y0 = np.linspace(1, 5, N) 
for j in range(0,N):
    x.append(xleft+j*h)

a=Fill_massive_same_values(-0.5/h**2,N)
c=Fill_massive_same_values(-0.5/h**2,N)
a[0]=0
c[N-1]=0
for i in range(N+1):
        b.append(1/h**2+U(xleft+i*h))

E, psi = Reverse_iter_method(y0)
print("The ground state energy is",E[0])
draw_all_levels()

###
real_psi,error=[],[]
analytical = [Analitic_psi(i) for i in x]
norm = np.linalg.norm(analytical)
analytical_norm = [i/norm for i in analytical]
draw('Основное состояние',x,'x',analytical_norm,'Phi')

error =  [abs(analytical_norm[i] - psi[0][i]) for i in range(len(x))]
draw('error',x,'x',analytical_norm-psi[0],'res')
plt.plot(x, error)
plt.xlabel("X")
plt.ylabel("Ошибка", rotation = 0)
plt.title("График абсолютной ошибки волновой функции основного состояния")
plt.show()


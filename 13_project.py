import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from scipy import integrate

N=200
x1=0
x2=1
h=(x2-x1)/(N-1)
T=1
M=10
tau=T/M

def forward_step(matrix, right):
    for i in range(matrix.shape[0] - 1):
        e = matrix.A[i+1][i] / matrix.A[i][i]
        matrix.A[i+1][i] = 0
        matrix.A[i+1][i+1] -= e*matrix.A[i][i+1]
        right[i+1] -= e*right[i]
def backward_step(matrix, right):
    N = matrix.shape[0]
    x = np.zeros(N)
    x[N-1] = right[N-1] / matrix.A[N-1][N-1]
    for i in range(N-1):
        x[N-i-2] = (right[N-i-2] - matrix.A[N-i-2][N-i-1]*x[N-i-1])/matrix.A[N-i-2][N-i-2]
    return x

def TDMA(matrix, right):
    d = right.copy()
    mat = matrix.copy()
    
    forward_step(mat, d)
    res = backward_step(mat, d)
    return res

def create_matrix(N, a, b, c, d):
    matrix = np.matrix(np.zeros(N*N).reshape(N, N))
    D = np.zeros(N)
    
    #set left border
    matrix.A[0][ 0 ] = c[0]
    matrix.A[0][ 1 ] = b[0]
    matrix.A[0][N-1] = a[0]
    D[0] = d[0]
    
    #set right border
    matrix.A[N-1][ 0 ]  = b[N-1]
    matrix.A[N-1][N-2]  = a[N-1]
    matrix.A[N-1][N-1] = c[N-1]
    D[N-1] = d[N-1]
    
    #set middle
    for i in range(1, N-1):
        matrix.A[i][i-1] = a[i]
        matrix.A[i][ i ] = c[i]
        matrix.A[i][i+1] = b[i]
        D[i] = d[i]

    return [matrix, D]



def create_v0(N,U_0t,x):
    v_0 = [U_0t(i) for i in x ]
    return v_0

def U_t0(x):
    return 0
def f(x,t):
    return x*(1-x/x2)**2


####Dirichle
def create_a_b_c_dirichle(tau,h,N):
    a = [-1/2*tau/h**2 for i in range(N)]
    a[0] = 0

    b = [-1/2*tau/h**2 for i in range(N)]
    b[N-1] = 0

    c = [1+tau/h**2 for i in range(N)]
    return a,b,c

def fill_v(v_past,f,t,x):
    d = np.zeros(N)
    for i in range(1,N-1):
        d[i]=v_past[i]+tau/2*((v_past[i-1]-2*v_past[i]+v_past[i+1])/h**2+f(x[i],t)+f(x[i],t-1))
    return d

def create_result_diricle(a,b,c,f,v_0,M,N,x):
    v=[v_0]
    for i in range(1,M):
        v_cur=fill_v(v[i-1],f,i,x)
        matr,right = create_matrix(N-2,a,b,c,v_cur)
        res = np.zeros(N)
        res[1:-1] = TDMA(matr, right)
        v.append(res)
    v=np.array(v)
    return v

def method_dirichle(f,U_0t,N,M):
    x=np.linspace(x1,x2,N)
    v_0 = create_v0(N,U_0t,x)
    a,b,c = create_a_b_c_dirichle(tau,h,N)
    res = create_result_diricle(a,b,c,f,v_0,M,N,x)
    return x,res

def find_max(x,v):
    v_max=[]
    x_max=[]
    for i in v:
        v_cur = max(i)
        index = i.index(v_cur)
        v_max.append(v_cur)
        x_max.append(x[index])
    return v_max,x_max


def draw(title, x,xtitle, y,ytitle):
    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.grid()
    plt.plot(x, y)
    plt.show()
t=np.linspace(0,T,M)
x,v = method_dirichle(f,U_t0,N,M)

xgrid, tgrid = np.meshgrid(x, t)
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(xgrid,tgrid ,v ,rstride=1, cstride=1)
pylab.xlim(x1, x2)
pylab.ylim(0, T)
pylab.show()


v_max,x_max = find_max(x,v.tolist())
print("DIRICHLE:Max count of temp and it's position")
print(v_max[-1],x_max[-1])
draw('The dependence of the maximum temperature versus time',t,'time',v_max,'temperature')

#neyman
def create_a_b_c_neyman(tau,h,N):
    a = [-1/2*tau/h**2 for i in range(N)]
    a[0] = 0
    a[N-1] = -1/3*tau/h**2

    b = [-1/2*tau/h**2 for i in range(N)]
    b[0] = -1/3*tau/h**2
    b[N-1] = 0

    c = [1+tau/h**2 for i in range(N)]
    c[0] = 1+tau/h**2/3
    c[N-1] = 1+tau/h**2/3
    return a,b,c

def create_result_neyman(a,b,c,f,v_0,M,N,x):
    v=[v_0]
    for i in range(1,M):
        v_cur=fill_v(v[i-1],f,i,x)
        matr,right = create_matrix(N-2,a,b,c,v_cur)
        res=np.zeros(N)
        res[1:-1] = TDMA(matr, right)
        res[0]= 4/3 * res[1] - 1/3 * res[2]
        res[-1]= 4/3 * res[-2] - 1/3 * res[-3]
        v.append(res)
    v=np.array(v)
    return v

def method_neyman(f,U_0t,N,M):
    x=np.linspace(x1,x2,N)
    v_0 = create_v0(N,U_0t,x)
    a,b,c = create_a_b_c_neyman(tau,h,N)
    res = create_result_neyman(a,b,c,f,v_0,M,N,x)
    return x,res

t=np.linspace(0,T,M)
x,v = method_neyman(f,U_t0,N,M)
xgrid, tgrid = np.meshgrid(x, t)
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(xgrid,tgrid ,v ,rstride=1, cstride=1)
pylab.xlim(x1, x2)
pylab.ylim(0, T)
pylab.show()

v_boarder = []
for i in v:
    v_boarder.append(i[len(i)-1])

v_max,x_max = find_max(x,v.tolist())
print("NEYMAN:Max count of temp and it's position")
print(v_max[-1],x_max[-1])    
draw("maximum temperature vs time",t,'time',v_max,'temperature')
draw("border temperature vs time",t,'time',v_boarder,'temperature')

import numpy as np
import matplotlib.pyplot as plt

N = 200
t1 = -np.pi
t2 = np.pi
a0 = 1
a1 = 0.002
w0 = 5.1
w1 = 25.5

def f(t):
    return a0*np.sin(w0*t) + a1*np.sin(w1*t)

def t(k):
    return (t2-t1)*k/N

def DFT(f, h):
    ftr = []
    w = []
    for i in range(0, round(N/2)): 
        ftr_i =  complex(0, 0)
        for k in range(0, N) :
            ftr_i += 1/N*f(t(k))*np.exp(2*np.pi*(-1j)*i*k/N)*h(i)
        ftr.append(abs(ftr_i))
        w.append(i)
    return [w, ftr]


def NoWindow(k):
    return 1

def RectangleWindow(k):
    if k>=0 and k < N:
            return 1
    return 0

def HannWindow(k):
    if k>=0 and k < N:
        return 0.5*(1-np.cos(2*np.pi*k/N))
    return 0


#
time = np.linspace(t1, t2, N)
# Окна
x_rectOrHann = np.arange(-50, N+50)
y_rect = [RectangleWindow(i) for i in x_rectOrHann]
y_Hann = [HannWindow(i) for i in x_rectOrHann]
y_No = [NoWindow(i) for i in x_rectOrHann]

w, ftr = DFT(f, NoWindow)
power = np.square(ftr)
plt.plot(w, power, 'o-')
plt.title("Signal power spectral density (NoWindow)")
plt.xlabel("frequency, rad/sec")
plt.ylabel("amplitude")
plt.show()

w, ftr = DFT(f, RectangleWindow)
power = np.square(ftr)
plt.plot(w, power, 'o-')
plt.title("Signal power spectral density (RectangleWindow)")
plt.xlabel("frequency, rad/sec")
plt.ylabel("amplitude")
plt.show()

w, ftr = DFT(f, HannWindow)
power = np.square(ftr)
plt.plot(w, power, 'o-')
plt.title("Signal power spectral density (HannWindow)")
plt.xlabel("frequency, rad/sec")
plt.ylabel("amplitude")
plt.show()


# plt.plot(time, f(time), 'o-')
# plt.plot([t1, t2], [0, 0])
# plt.title('Sampled Signal')
# plt.xlabel("time, с")
# plt.ylabel("amplitute")
# plt.show()
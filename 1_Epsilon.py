import numpy as np
import sys

def epsfinder(): 
    epsod=np.float32(1.0)
    Emin=0
    Emax=100
    rank=0  
    while (epsod/2)+1 != 1:
        epsod/=2
        rank+=1
    while pow(2,Emin)>pow(2,(Emin-1)):
        Emin-=1
    #print(np.iinfo(np.int64))
    print(epsod)
    print(rank)

    m = 1.
    max_num = 0
    i = 0
    while m - max_num > epsod:
        max_num = m
        m = m * 2
        i = i + 1
    print("max num = ", max_num, "| rzrd_max = ", i - 1)
    print("max exp = ", i - 1)
    print()





epsfinder()


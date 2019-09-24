import numpy as np
import math

def mean_filter(arr, k):
    kernel = 2*k + 1
    l = len(arr)
    m = arr.copy()
    a = np.arange(kernel).reshape(1,kernel)
    b = np.arange(l).reshape(l,1)
    c = a + b
    z = np.zeros(k)
    fin = np.append(z,m)
    fin = np.append(fin,z)
    val = np.mean(fin[c],axis=1)
    return val



def noisify(arr,var):
    sd = math.sqrt(var)
    new_arr = np.copy(arr)
    noise = np.random.normal(0,sd,np.shape(arr))
    new_arr = noise + new_arr
    return new_arr

def generate_sin_wave(period,range_,num):
    xmin,xmax = range_
    input_arr = np.linspace(xmin,xmax,num=num )
    # print(input_arr)
    wave = np.sin((2*math.pi/period)*input_arr)
    return wave




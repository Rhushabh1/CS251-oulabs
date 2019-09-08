import numpy as np
import math


pointer = 0
new = np.array([])
def mean_filter(arr, ker):
    if pointer == np.size(arr) :
        return new
    else :





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




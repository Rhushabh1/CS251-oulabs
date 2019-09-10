import numpy as np
import math

def mean_filter(arr, k):
	kernel_size = 2*k+1

	m = arr.copy()
	m.astype(float)
	I = np.ones(kernel_size)

	acc = np.convolve(m,I,"full")
	acc = acc[k:-k]

	return acc/kernel_size

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




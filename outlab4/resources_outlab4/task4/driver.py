import numpy as np
from task4 import *
import matplotlib.pyplot as plt


def driver():
    clean_sin = generate_sin_wave(2,(-2,8),1000)
    x_arr = np.linspace(-2, 8, num=1000)
    plt.figure(0)
    plt.plot(x_arr,clean_sin)
    plt.xlabel('X')
    plt.ylabel('clean sin')
    plt.savefig('clean_sin.png')
    plt.show()
    sd = 0.05

    plt.figure(1)
    dirty_sin = noisify(clean_sin, sd*sd)
    plt.plot(x_arr,dirty_sin)
    plt.xlabel('X')
    plt.ylabel('dirty sin')
    plt.savefig('dirty_sin.png')
    plt.show()

    plt.figure(2)
    cleaned_sin = mean_filter(dirty_sin,1)
    plt.plot(x_arr,cleaned_sin)
    plt.savefig('cleaned_sin.png')
    plt.show()



driver()
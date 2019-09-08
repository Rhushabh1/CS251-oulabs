import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fn_plot1d(fn, x_min, x_max, filename):
    x_values = np.linspace(x_min,x_max,num=1000)
    fn_vec = np.vectorize(fn)
    y_values = fn_vec(x_values)

    plt.plot(x_values,y_values)
    # plt.savefig(filename)
    plt.show()



def nth_derivative_plotter(fn, n, x_min, x_max, filename):
    x_values = np.linspace(x_min,x_max,num=1000)
    fn_vec = np.vectorize(fn)
    y = fn_vec(x_values)



def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    x_values = np.linspace(x_min,x_max,num=1000)
    y_values = np.linspace(y_min,y_max,num=1000)
    vec_fn = np.vectorize(fn)
    # z_values = vec_fn(x_values,y_values)

    fig = plt.figure()

    X,Y = np.meshgrid(x_values,y_values)
    Z = vec_fn(X,Y)

    ax = plt.axes(projection='3d')
    ax.plot_surface(X,Y,Z)

    # plt.savefig(filename)
    plt.show()


# def h(t):
#     # write your code here
#     pass

def b(x):
    # write your code here
    if x>0:
        return g(x)
    else :
        return g(-x)

    pass

def g(x):
    # write your code here
    u = h(2-x)
    v = h(x-1)
    return u/(u+v)
    pass

def h(x):
    if x > 0 :
        return math.exp(-1/(x*x))
    else :
        return 0

    pass

def twodsinc(x,y):
    u = math.sqrt(x*x + y*y)
    if u > 0 :
        return math.sin(u)/u
    else :
        return 1

pi = math.pi

fn_plot1d(b,-2,2,'fn1plot.png')
fn_plot2d(twodsinc,-1.5*pi, 1.5*pi,-1.5*pi , 1.5*pi,'fn2plot.png')
'''
Created on Jan 20, 2017

@author: admin
'''
import random
import math
#from one_dimenstional_data import plot_histogram
from matplotlib import pyplot as plt

def normal_cdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt( 2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2 ) / (sqrt_two_pi * sigma))


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p,tolerance=tolerance)
    
    low_z, low_p    = -10.0, 0
    hi_z, hi_p      = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
        
    return mid_z
    

def random_normal():
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(10000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

#plot_histogram(ys1,0.1,"ys1")
#plot_histogram(ys2,0.1,"ys2")

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='red', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very different Joint Distributions")
plt.show()

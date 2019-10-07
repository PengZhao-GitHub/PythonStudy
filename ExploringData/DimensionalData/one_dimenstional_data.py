'''
Created on Jan 20, 2017

@author: admin
'''

import math
from collections import Counter
from matplotlib import pyplot as plt
import random

def bucketize(point, bucket_size):
    return bucket_size * math.floor(point/bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketize(point,bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    print histogram
    print len(histogram)
    plt.bar(histogram.keys(), histogram.values(), width = bucket_size)
    plt.title(title)
    plt.show()
    
    
random.seed(0)

uniform = [200 * random.random() - 100 for _ in range(10000)]

#uniform = [99, 98, 60, 50, 75, 78, 99, 95, 96, 92, 30, 20, 55, 56, 57, 58, 59, 80, 81, 89, 90, 91, 50, 50, 50]


print len(uniform)
print max(uniform)
print min(uniform)

#plot_histogram(uniform, 30, "uniform histogram")    
    
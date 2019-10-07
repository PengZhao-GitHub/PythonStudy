'''
Created on Jan 24, 2017

@author: admin
'''

import math

from scipy.spatial import distance
from sqlalchemy.ext.declarative.clsregistry import _GetColumns
data = [[63,150],
        [67,160],
        [70,171]]

data2 = [[160,150],
         [170.2, 160],
         [177.8, 171]]

print "a to b", distance.euclidean([63,150], [67, 160])
print "a to c", distance.euclidean([63,150], [70, 171])
print "b to c", distance.euclidean([67,160], [70, 171])

print

print "a to b", distance.euclidean([160,150], [170.2, 160])
print "a to c", distance.euclidean([160,150], [177.8, 171])
print "b to c", distance.euclidean([170.2,160], [177.8, 171])

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A,j):
    return [A_i[j]
            for A_i in A]

def dot(v,x):
    return sum(v_i * w_i for v_i, w_i in zip(v,x))

def sum_of_squares(v):
    return dot(v,v)    

def mean(x):
    return sum(x) / len(x)    

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def scale(data_matrix):
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix,j))
             for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix,j))
              for j in range(num_cols)]
    return means, stdevs

def rescale(data_matrix):
    means, stdevs = scale(data_matrix)
    
    def rescaled(i,j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]
        
    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)

print
print data
print 

r_data = rescale(data)
print r_data    
    
print 

print data2
r_data2 = rescale(data2)
print r_data2

row_counter, _ = shape(r_data)
print row_counter

print "a to b", distance.euclidean(get_row(r_data,0), get_row(r_data, 1))
print "a to c", distance.euclidean(get_row(r_data,0), get_row(r_data, 2))
print "b to c", distance.euclidean(get_row(r_data,1), get_row(r_data, 2))

print

print "a to b", distance.euclidean(get_row(r_data2,0), get_row(r_data2, 1))
print "a to c", distance.euclidean(get_row(r_data2,0), get_row(r_data2, 2))
print "b to c", distance.euclidean(get_row(r_data2,1), get_row(r_data2, 2))

                           
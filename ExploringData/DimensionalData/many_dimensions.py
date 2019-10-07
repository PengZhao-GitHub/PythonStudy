'''
Created on Jan 20, 2017

@author: admin
'''

import matplotlib.pyplot as plt

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A,i):
    return A[i]

def get_column(A, j):
    return A[j]

data = [[1,2,3,4,6],
        [2,3,4,5,7],
        [3,4,5,6,8],
        [4,5,6,7,9]]

_, num_columns = shape(data)

fig, ax = plt.subplots(num_columns, num_columns)

for i in range (num_columns-1):
    print "i=", i
    for j in range(num_columns-1):
        print "j=", j
        if i != j: ax[i][j].scatter(get_column(data,j), get_column(data,i))
        else: ax[i][j].annotate("series " + str(i), (0.5,0.5),
                                 xycoords="axes fraction",
                                 ha="center", va="center")
                                  
        if i < num_columns - 1: ax[i][j].xaxis.set_visible(False)
        if j > 0: ax[i][j].yaxis.set_visible(False)
        
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

plt.show()
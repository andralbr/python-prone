'''
    Some useful functions ....
'''

import numpy as np


# Calculating the average of columns 

def calc_average(mat):
    
    num_rows, num_cols = mat.shape
    
    av_vec = np.zeros((num_rows,1))

    for i in range(num_cols):
        mt = mat[:,i, None]
        av_vec = av_vec + mat[:,i, None]

    av_vec = av_vec / num_rows

    return av_vec

def calc_mean(mat):
    res = np.sum(mat)

    return res

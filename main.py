''' 
    Numerical simulation
'''

import numpy as np
from math import pi
import help_functions

# a simple function to create a randomly initialized matrix of desired shape (nx, ny)
def initialize(nx, ny):
    mat = np.random.randn(nx, ny)
    return mat


'''
    a main function that does not do much yet
'''
def main(mat):

    av_vec = help_functions.calc_average(mat)

    print("Dimension of av_vec: " + str(av_vec.shape) )

# setting up a dictionnary to map
def create_dict():
    dict = {}
    for cc in range(10):
        dict["ent" + str(cc)] = cc
    return dict


mat = initialize(4,3)
main(mat)
print("program finished")



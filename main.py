''' 
    Numerical simulation
'''

import numpy as np
from math import pi
import help_functions


def main():
    mat = np.random.randn(4,3)
    av_vec = help_functions.calc_average(mat)

    print("Dimension of av_vec: " + str(av_vec.shape) )

# setting up a dictionnary to map
def create_dict():
    dict = {}
    for cc in range(10):
        dict["ent" + str(cc)] = cc
    return dict

main()    
dict = create_dict()

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:33:19 2024

@author: zhen-
"""

import numpy as np

# nparray = np.fromfunction(lambda i, j: i, (2, 2), dtype=float)
# print(nparray)
#      array([[0., 0.],
#             [1., 1.]])
            
# nparray = np.fromfunction(lambda i, j: j, (2, 2), dtype=float)    
# print(nparray)
#      array([[0., 1.],
#             [0., 1.]])
#  nparray =np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
# print(nparray)
#      array([[ True, False, False],
#             [False,  True, False],
#             [False, False,  True]])
     
# nparray =np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# print(nparray)
#      array([[0, 1, 2],
#             [1, 2, 3],
#             [2, 3, 4]])

def fun_add(x,y):
    return (x+1)*(y+2)
     
nparray =np.fromfunction(fun_add, (5,9))
print(nparray)
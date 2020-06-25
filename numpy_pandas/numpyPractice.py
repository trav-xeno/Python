#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:43:59 2020

@author: travisnevins

NOTE: numpy slices aren't copies to copy use .cpoy() appened  to the end of the slice '
"""
import numpy as np

#just getting the hang of numpy vs normal list
a = np.array([5,6,7,8])
np.random.seed(0)  # seed for reproducibility
print(a)
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional arrayprint("x3: " , x3)
print("x2: " , x2)
print("x3 ndim: ", x3.ndim) #ndim (the number of dimensions)
print("x3 shape: ", x3.shape) #shape (the size of each dimension)
print("x3 size: ", x3.size) #and size (the total size of the array)
print("dtype: ", x3.dtype)#dtype: int64 
#itemsize, which lists the size (in bytes) of each array element 
#nbytes, which lists the total size (in bytes) of the array:
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

#--------------------------
print("Coming up is accessing 2d arrays similar to tuples")
temp = np.array([[3, 5, 2, 4],
                 [7, 6, 8, 8],
                 [1, 6, 7, 7]])
print("temp: ", temp)
print("first index:",temp[0,0] )
print("row 3 col 3: ",temp[2,3])
print("next is slicings arrays")
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#[start:stop:step]

y = np.arange(10)
print(y)
firstfive = x[:5]  
print("first five: " ,firstfive)

temp = x[5:]  # elements after index 5
print("indexes after the fifth: ", temp)
temp = x[4:7]  # middle sub-array
print("middle: ",temp)
temp =  x[::2]  # every other element
print("every other: " ,temp)
temp = x[1::2]  # every other element, starting at index 1
print("print every other starting from index one: ", temp )

temp = x[::-1]  # all elements, reversed
print("handy reverse array: ", temp)
temp = x[5::-2]  # reversed every other from index 5
print("reverse every other starting from index  5", temp )
print("multi demtional array slicing")
multi = np.array([[ 7,  7,  6,  1],
                  [ 8,  8,  6,  7],
                  [ 4,  2,  5, 12]]) 
print("array being used: ", multi)
print("2 rows and 3 columns:  ", multi[:2, :3] ) # two rows, three columns
print("all rows every other column: ", multi[:3, ::2]  )# all rows, every other column
print("reverse reverse!: ",multi[::-1, ::-1]) 
print("accessing rows and columns cominmg up next ")
print("first coumn: " , multi[:, 0])
print("rist row: ", multi[0, :])
#---------------------------------
print("arrya math is coming up next")

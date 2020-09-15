#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:43:27 2020

Data Science practice 
This is some mroe Numpy and Pandas 
This will be for referance to look at differetn basic parts of both numpy and pandas but with some data science through in as well.

@author: travisnevins
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(25)
# make a matrix 6x6 of random ints  
df_obj = DataFrame(np.random.rand(36).reshape((6,6)), 
                  index=["row 1", "row 2", "row 3","row 4","row 5","row 6"], 
                  columns=["col 1","col 2","col 3","col 4","col 5","col 6"])
series_obj = Series( np.arange(8) ,index=["row 1","row 2","row 3","row 4","row 5","row 6","row 7","row 8" ] )
#can access serise like so:
print("datafreme: \n", df_obj )
print("series: ", series_obj)
#accessing sereise 
print("print row 5 data: ",series_obj[["row 5"]])
print("print index at 4 and 7: \n", series_obj[[4,7]]) 
#accessing dataframe 
print("print row 1 - 3 and columns 2 - 4: \n")
print(df_obj.loc[["row 1", "row 2", "row 3"], ["col 2", "col 3", "col 4"]])





















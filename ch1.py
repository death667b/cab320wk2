# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:57:48 2018

@author: n5372828
"""

g = (i*i for i in range(5,10))

print("first number {}".format( next(g)))
print("second number {}".format( next(g)))
print("third number {}".format( next(g)))
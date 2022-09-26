#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:36:12 2021

@author: vsriya23
"""

import matplotlib.pyplot as plt
from numpy import random
# no other libraries are allowed

def func(x):
    return 1/x

def Estimated_area_under_curve(func, lower_limit, higher_limit):
    """
    Estimate the area under the curve for a given function using the method discussed in the class using random numbers.
    Assume the input function to be monotonic.
    """
    
    area = 0
    # in the region between 0.5 and 2 , the max value of 1/x is 2
    # using monte carlo integration to solve the problem
    # imagine a rectange of length 1.5 and width 2 surrounding the function 1/x between 0.5 and 2
    
    """ Add your code here """
    
    square = 0
    curve = 0
    
    sq_area = 1.5*2
    #generating random points lying inside the rectangle and checking if they lie under the curve or not
    for _ in range(10000):
        x = random.uniform(0.5,2)
        y = random.uniform(0,2)
        
        if y <= func(x):
            curve += 1
            square +=1
            
        else:
            square += 1
    # ratio of number of points falling under the curve and number of points falling in the rectangle give the ratio of the area under the curve and area under the rectangle
    # so if we multiply this by the area of the rectangle  we get the area under the curve
            
    area = (curve/square)* sq_area
    return area

Estimated_area = Estimated_area_under_curve(func, 1/2, 2)
estimated_e = 0
# Find the area under the curve analytically. Equating the analytical expression and with the estimated value, find the value of the irrational number e. Hint, use log to the base 2.
""" Add your code here """
# loga(b) = 1/logb(a), log(a^b) = blog(a)  
#by calculating area under 1/x between 0.5 and 2 we are calculating the value of ln(2)-ln(0.5) = ln(4)
#ln(4) = 2ln(2) = 2/log2(e)   => 2/ln(4) = 2/(2/log2(e)) = log2(e)
# 2^log2(e) = e

estimated_e = 2**(2/Estimated_area)

print("e = ", str(estimated_e))
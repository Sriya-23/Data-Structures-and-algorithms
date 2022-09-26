#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 14:42:33 2021

@author: vsriya23
"""
import numpy as np
#print pascal's triangle

# Allowed libraries: numpy

def pascals_triangle(n):
    """
    The values in ith row is iCk i.e. iC0, iC1, iC2 .... iCi
    So the pascals triangle looks like
    
    0C0
    1C0 1C1
    2C0 2C1 2C2
    .
    .
    .
    nC0 nC1 nC2 ... nCn
    
    Here the numbers for each row are being calculated and being added into the list
    then each row is printed
    
    """
    p_triangle = [[int(np.math.factorial(num)/(np.math.factorial(k)* np.math.factorial(num-k))) 
                   for k in range(num+1)] for num in range(n)]
    
    for row in p_triangle:
        print(*row)
    return p_triangle
    
if __name__ == "__main__":
    fin = open("q3_test.txt")
    n = int(fin.read().splitlines()[0])
    fin.close()
    


    # Add your code here
    a = pascals_triangle(n)
    # the triangle is printed in the fucntion so the returned value is not printed

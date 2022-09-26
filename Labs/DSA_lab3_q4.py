#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:00:55 2021

@author: vsriya23
"""

from DSA_lab3_q3 import Queue

def BinaryN(n):
    nums = Queue(size = n)
    for num in range(1,n+1):
        nums.push(num)
        
        print(bin(nums.pop())[2:])
        
    
    
BinaryN(6)

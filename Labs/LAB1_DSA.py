#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:14:56 2021

@author: vsriya23
"""


def recursive_binary_search(arr, num, low, high):
    
    pos  =  low + (high-low)//2
    
    if num in arr:
        
        print(high, low, pos)
        print(arr[pos]== num)
        if arr[pos]== num:
            return pos
            
        elif num > arr[pos]:
            low = pos + 1
                
            recursive_binary_search(arr, num, low, high)
                
        elif num < arr[pos]:
            high = pos -1
            recursive_binary_search(arr, num, low, high)
    return 'Not in array'
    
    
arr = [1, 2, 3, 4, 7, 9, 11, 14, 16, 17]
print(recursive_binary_search(arr , 9,0, len(arr)-1))
def smallest_int(arr):
    i = 0
    
    while True:
        if i not in arr:
            return i
        
        elif i in arr:
            i+= 1
            continue
            
            
        
print(smallest_int([0,1,2,3,4,6,7]))
        
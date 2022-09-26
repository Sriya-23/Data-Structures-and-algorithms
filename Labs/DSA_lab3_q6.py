#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:09:22 2021

@author: vsriya23
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_num = arr[i]
        
        for j in range(i+1,len(arr)):
            
            if arr[j] < min_num:
                min_num = arr[j]
        min_idx = arr.index(min_num)
        arr[i] , arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

if __name__ == '__main__':
    print(selection_sort([1,8,6,6,5,4,0,2]))        
        
        
                
    
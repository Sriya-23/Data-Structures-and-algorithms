#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:27:05 2021

@author: vsriya23
"""
def next_greater_element(arr, elem):
    for i in range(arr.index(elem), len(arr)):
        if arr[i] > elem:
            return arr[i]
        
    return -1
    
def subset_nge(arr1, arr2):
    '''arr1 is subset of arr2'''
    nges = []
    for num in arr1:
        nge = next_greater_element(arr2, num)
        nges.append(nge)
        
        
    return nges
if __name__ == '__main__':
    arr1 = [4,1,2]
    arr2 = [1,3,4,2]
    print(subset_nge(arr1, arr2))
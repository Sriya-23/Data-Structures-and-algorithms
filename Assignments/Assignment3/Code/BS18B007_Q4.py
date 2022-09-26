#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:31:03 2021

@author: vsriya23
"""
# no libraries are allowed

""" Add your functions here """

def Merge_sort_points(xy_list, distances):
    '''Implementing the merge sort algorithm 
    Here we are sorting the xy points  based on the distances
    '''
    n = len(distances)
    if len(distances) == 1:  #base case
        return xy_list,distances
    else:
        return merge(Merge_sort_points(xy_list[:n//2], distances[:n//2]), Merge_sort_points(xy_list[n//2:], distances[n//2:]))
        

def merge(a, b):
    # this algorithm for merging is the same as the original merge sort 
    # the only difference is that as we sort the distances, we swap the points as well along with the distances
    # So even though the space complexity increases, the time complexity remains the same because we still make at most n comparisions between the distance arrays
    pointsA = a[0]
    distA = a[1]
    
    pointsB = b[0]
    distB = b[1]
    
    pts = [None]*(len(distA) +len(distB))
    dists = [None]*(len(distA) +len(distB))
    
    i = j = k = 0
    
    while i < len(distA) and j< len(distB):
        if distA[i] < distB[j]:
            dists[k] = distA[i]
            pts[k] = pointsA[i]
            i+=1
            
        else:
            dists[k] =distB[j]
            pts[k] = pointsB[j]
            j+= 1
            
        k += 1
        
    if i < len(distA):
        dists[k:] = distA[i:]
        pts[k:] = pointsA[i:]
    else:
        dists[k:] = distB[j:]
        pts[k:] = pointsB[j:]
        
    return pts, dists


def k_closest_points(x_array, y_array, point, k):
    """ 
    (list of float, list of float, tuple of two floats, int) -> (list of float), (list of float)
    >>> k_closest_points([1.0, 1.0, 3.0, 5.0], [0.0, 3.0, 4.0, 5.0], (0.0, 0.0), 2)
        [1.0, 1.0], [0.0, 3.0]
    """
    
    """ Add your code here """
    xy_pts = list(zip(x_array, y_array)) #O(n): zip() takes O(1) time and list() takes O(n)
    
    distances = [((point[0] - pt[0])**2 + (point[1] - pt[1])**2)**0.5 for pt in xy_pts] #O(n) time - one for loop
    
    sorted_pts , dists = Merge_sort_points(xy_pts, distances)  # the time complexity for merge sort is O(nlogn)
    
    sort_x = [pt[0] for pt in sorted_pts[:k]] # O(k) time complexity
    sort_y = [pt[1] for pt in sorted_pts[:k]] # O(k) time complexity
    
    # total time complexity = O(n) + O(n) + O(nlogn) + O(k) + O(k)
    # since O(nlogn) has the highest value compared to the other quantitites the complexity of the whole algorithm can be considered as O(nlogn)
    
    
    return sort_x, sort_y
    

if __name__ == '__main__':
    
    x_array = [1.0, 1.0, 3.0, 5.0]
    y_array = [0.0, 3.0, 4.0, 5.0]
    point = (0.0, 0.0)
    k = 2
    
    
    x_clos, y_clos = k_closest_points(x_array, y_array, point, 2)
    
    print(x_clos, y_clos)
    
    
    
    
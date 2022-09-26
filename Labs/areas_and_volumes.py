#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:07:02 2021

@author: vsriya23
"""
from numpy import pi

def circle_and_square(radius):
    """
    calculating the area of a circle with a given radius
    and the area of the smallest square circumscribing it

    """
    
    circle_area = pi * radius **2
    circum_sq_area = 4 * radius**2
    
    return circle_area, circum_sq_area


def sphere_and_cube(radius):
    """
    calculating the volume of a sphere with a given radius
    and the volume of the smallest cube circumscribing it

    """
    
    sphere_volume = 4 * pi * radius **3 / 3
    circum_cube_volume = 8 * radius**3
    
    return sphere_volume, circum_cube_volume
    

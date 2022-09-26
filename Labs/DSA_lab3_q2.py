#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:36:59 2021

@author: vsriya23
"""
from DSA_lab3_q1 import Stack

def reverse_string(string1):
    
    chars = list(string1)
    str_stack = Stack(size = len(string1))
    
    for ch in chars:
        str_stack.push(ch)
        
    reversed_chars = str_stack.get_stack()[::-1]
    
    return ''.join(reversed_chars)


reverse_str = reverse_string('ReverseString')
    
    
        
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:07:17 2021

@author: vsriya23
"""

class BinaryNumber():
    """Minimalist binary number class """
    def __init__(self, a):
        
        self.binary = a
        
    def base_10(self):
        '''function convert binary numbers to number in base 10'''
        binary_str = str(self.binary)
        base_10 = sum([int(binary_str[i])*2**i for i in range(len(binary_str))])
        base_10_str = '['+ str(base_10)+ ']' + '_10'
        print(base_10_str)
        
        return base_10_str
        
    
    def __str__(self):
        
        return '[' + str(self.binary )+ ']' + '_2'
    
    
if __name__ == '__main__':
    bin1 = BinaryNumber(101)
    
    bin1.base_10()
    print(bin1)
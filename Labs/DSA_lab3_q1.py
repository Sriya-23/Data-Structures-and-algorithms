#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:12:54 2021

@author: vsriya23
"""

class Stack:
    
    def __init__(self, size):
        self.stack = []
        self.size = size
        
    def push(self, element):
        if len(self.stack) < self.size:
            self.stack.append(element)
        
    def pop(self):
        
        last_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_element
    
    def get_stack(self):
        return self.stack
    
    def peek(self):
        return self.stack[-1]
    
    def is_Full(self):
        return len(self.stack) == self.size
        
    
    def is_Empty(self):
        return len(self.stack) == 0
        
    
    def __str__(self):
        
        return str(self.stack)
        
if __name__ == '__main__':
    
    stack1 = Stack(size = 10)
    
    stack1.push('a')
    stack1.push('b')
    stack1.push('c')
    print(stack1)
    elem = stack1.pop()
    print(stack1)
    
    print(stack1.peek())
    
        
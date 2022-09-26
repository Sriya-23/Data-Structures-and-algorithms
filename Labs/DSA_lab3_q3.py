#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:43:33 2021

@author: vsriya23
"""

class Queue:
    
    def __init__(self, size):
        self.queue = []
        self.size  = size 
        
    def push(self, element):
        if len(self.queue) < self.size:
            self.queue.append(element)
        
    def pop(self):
        # FIFO
        first_elem = self.queue[0]
        self.queue = self.queue[1:]
        
        return first_elem
    
    def peek(self):
        
        return self.queue[0]
    
    def is_Full(self):
        return len(self.queue) == self.size
        
    
    def is_Empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        
        return str(self.queue)
    
    def get_queue(self):
        
        return self.queue
    
        
    
if  __name__ == '__main__':
    
    queue_test = Queue(size = 4)
    
    queue_test.push('a')
    queue_test.push('b')
    queue_test.push('c')
    queue_test.push('d')
    
    elem = queue_test.peek()
    
    print(elem)
    print(queue_test.is_Empty())
    print(queue_test.is_Full())
    
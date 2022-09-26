#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 03:58:51 2021

@author: vsriya23
"""

# DSA for Biology - Assignment 2
# Template for question  - Stacks and queues

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:16:56 2021

@author: vsriya23
"""
# implementing a queue and a stack class
class Queue:
    
    '''Minimalist queue class'''
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
    
    
#%%

class Stack:
    '''Minimalist Stack class'''
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
    
    def peek(self):
        
        return self.stack[-1]
    
    def is_Full(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False
        
    def is_Empty(self):
        if len(self.stack) == 0:
            return True
        
        else:
            return False
        
    def get_Stack(self):
        return self.stack
    
    def __str__(self):
        
        return str(self.stack[::-1])   
    
#%%
    
    
def Simulate_Sandwitch_for_Students(Students, Sandwiches):
        """(list of integers, list of integers) -> (int)
    	Returns the number of students that were unable to eat.
    	>>> Simulate_Sandwitch_for_Students([1,1,0,0], [0,1,0,1])
    	0
    	>>> Simulate_Sandwitch_for_Students([1,1,1,0,0,1], [1,0,0,0,1,1])
    	3
    	"""
	
        
        student_queue = Queue(len(Students)) 
        sandwiches_stack = Stack(len(Sandwiches))
        n = len(Sandwiches)
        for i in range(len(Students)):
            student_queue.push(Students[i])
            sandwiches_stack.push(Sandwiches[n-i-1])
            
        no_matches = False
        
        
        while not no_matches:
           
            if sandwiches_stack.is_Empty():
                no_matches = True
                return 0
            
            elif all(stu != sandwiches_stack.peek() for stu in student_queue.get_queue()):
                no_matches = True
                return len(student_queue.get_queue())
            
            elif sandwiches_stack.peek() == student_queue.peek():
                sandwiches_stack.pop()
                student_queue.pop()
                
            elif sandwiches_stack.peek() != student_queue.peek():
                student = student_queue.pop()
                student_queue.push(student)
            # print('sq: ', student_queue,', ss: ', sandwiches_stack)




print(Simulate_Sandwitch_for_Students([1,1,0,0], [0,1,0,1]))
print(Simulate_Sandwitch_for_Students([1,1,1,0,0,1], [1,0,0,0,1,1]))
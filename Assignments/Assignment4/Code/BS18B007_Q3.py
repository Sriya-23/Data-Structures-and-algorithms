#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 02:41:21 2021

@author: vsriya23
"""
import networkx as nx
import matplotlib.pyplot as plt
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed

class Queue:
    
    '''Minimalist queue class
    Adding this to use it for writing the algorithm for selecting order of courses
    '''
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
def planning_your_program(prerequisite_dict):
    """
    Given a dictionary of prerequisite courses, return the list of courses such that the sequence denotes the order in which the courses could possibly be done in order to satisfy the prerequisite condition.
    """
    
    """ Add your functions here if needed """
    def create_dependency_graph(prerequisite_dict):
        """Create and return a networkx dependency graph based on the prerequisite dictionary"""
        G = nx.DiGraph()
        for node in prerequisite_dict:
            if len(prerequisite_dict[node]) != 0:
                lst = [(req, node) for req in prerequisite_dict[node]] # the keys represents the course and the values represent its prerequisites
                # so edges are added from the prerequisites to the course: from elements of values to keys
                G.add_edges_from(lst)
        
        return G

    def find_the_program_pathway(G):
        """return the required program pathway from the Course Dependency Graph"""
        course_list = []
        Q = Queue(len(G))
        processed = {}
        
        
        for node in G:
            processed[node] = False
            if len(list(G.predecessors(node))) == 0:
                Q.push(node) # adding the courses with no prerequisites onto the stack
        # Add your code here
        
        while not Q.is_Empty():
            node = Q.pop()
            processed[node] = True
            
            
            course_list.append(node)
            
            for n in G.successors(node):
                if all([True if processed[p] == True else False for p in G.predecessors(n) ]):
                    Q.push(n) # it is added to queue only if all the prerequisites are complete
                    # since it is a queue(first in first out) it will definately get added once all the prerequisites are done
                
                    
                    
            
        

        return course_list
    
    Course_Dependency_Graph = create_dependency_graph(prerequisite_dict)
    nx.draw(Course_Dependency_Graph, with_labels = True)
    plt.show()
    
    program_pathway = find_the_program_pathway(Course_Dependency_Graph)
    
    return program_pathway


prerequisite_dict = {"BT3051":["CS1100", "BT1000"], "CS6024":["BT3051"], "CS6091": ["CS6024", "BT3051", "CS1100"], "CS1100":[], "BT1000":[]}
print(planning_your_program(prerequisite_dict))
# Expected output: ["BT1000", "CS1100", "BT3051", "CS6024", "CS6091"] or ["CS1100", "BT1000", "BT3051", "CS6024", "CS6091"]


"""
Hints:
1. Firstly, complete all the courses that do not have any prerequisities. 
2. Then check if the first neighbors of the previous courses have prerequisities other than already completed courses. If not, then mark them complete.
3. Reinterate the 2nd step until all the courses are completed.
"""    
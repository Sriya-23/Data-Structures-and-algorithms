#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:14:28 2021

@author: vsriya23
"""

import networkx as nx
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed
# You are allowed to use the function that you used in the previous subquestion
class Queue:
    
    '''Minimalist queue class
    Adding this to use it for writing the algorithm to calculate minimum time for spread of contagion
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

def minimum_time_for_spread_of_contagion(G, patient_zero):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community and a node which represents patient zero of the contagion, return the minimum time taken for the contagion to spread in the complete graph.
    """
    #Using Dijkstra's algorithm to solve the problem
    
    time = {v: float('inf') for  v in G.nodes}
    processed = {v: 'not processed' for  v in G.nodes}
    
    time[patient_zero] = 0
    
    
    DQ = Queue(len(time))
    DQ.push(patient_zero)
    
    while not DQ.is_Empty():
        patient = DQ.pop()
        processed[patient] = 'processed'
        for node in G.neighbors(patient):
            if processed[node] != 'processed':
                DQ.push(node)  # if the node is not already processed it is pushed onto the queue
            
            if time[node] > time[patient] + G[node][patient]["weight"]:
                time[node] = time[patient] + G[node][patient]["weight"] # updating the shortest path if its previous path length is greater than the currently calculated path length
                # we update it to choose the minimum possible path to the ith node from the patient zero node
        
    min_time = max(time.values())
    return min_time
#%%
def most_critical_node_for_contagion(G):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community, return the most critical node. The infection of the most critical node will result in minimum time for the spread in the whole community.
    """
    time_taken = {v:minimum_time_for_spread_of_contagion(G, v) for v in G.nodes }
    time_list = list(time_taken.values())
    return list(time_taken.keys())[time_list.index(min(time_list))]
    
    pass

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(most_critical_node_for_contagion(G))
# Expected output: 5
# Explanation: 
# Patient zero node | minimum time taken
#      1            |  15
#      2            |  16
#      3            |  12
#      4            |  11
#      5            |  8 - minimum time
#      6            |  12
#      7            |  15

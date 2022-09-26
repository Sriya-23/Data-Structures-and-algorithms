#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 18:41:04 2021

@author: vsriya23
"""

import networkx as nx
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed

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
    processed = {v: 'not processed' for  v in G.nodes} # to keep track of whether the node is processed or not
    
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

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(minimum_time_for_spread_of_contagion(G, 3))
# Expected output: 12
# Explanation: 
# Infected node | Time taken to reach that node
#      3        |  0
#      4        |  1
#      1        |  2
#      2        |  3
#      5        |  4 (1+3)
#      8        |  6 (1+3+2)
#      7        |  12(1+3+2+6)

# Hint:
# Therefore, minimum time taken to spread in the community = argmax_i(min(time taken to reach node i from patient zero node))
# Mininum time taken to reach node i from patient zero node can be thought of as a dynamic programming question. 
# Time taken to reach node i from node j can be thought of as a dynamic programming question. 
# To find the shortest path/minimum time taken for the person to be infected you can either use Dijkstra's algorithm or a dynamic programming variant of Dijkstra's algorithm i.e. Floyd-Warshall algorithm for all pairs of shortest paths


"""Pseudocode
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u, v) do
    dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
for each vertex v do
    dist[v][v] ← 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j]
                dist[i][j] ← dist[i][k] + dist[k][j]

            end if
"""
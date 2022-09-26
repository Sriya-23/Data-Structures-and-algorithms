#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:55:38 2021

@author: vsriya23
"""

import networkx as nx
import json
import matplotlib.pyplot as plt


class Stack:
    '''implementing a minimalist Stack class with basic methods like pop(), push()...'''
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
    def __str__(self):
        
        return str(self.stack)

def Find_Cycles_In_Metabolic_Graph(Graph):
    """
    Given a bipartite networkx graph, return the list of list of metabolites involved in the cycle i.
    """
    
    parent = {}
    label = {}
    cycles = []
    
    for node in Graph:
        label[node] = 'False'
        
        
    DFS = Stack(len(Graph))
    DFS.push(list(label.keys())[1])
    label[DFS.peek()] = 'Mid'
    parent[DFS.peek()] = None
    
    while not all([label[node] == 'True' for node in Graph]):
        if not DFS.is_Empty():
            node = DFS.peek()
            neighbours = list(Graph.successors(node)) 
            
            if all([True if label[node] == 'True' else False for node in neighbours]) or len(neighbours) == 0:
                label[node] = 'True'
                DFS.pop()
                
            elif all([True if label[node] == 'Mid' else False for node in  neighbours]):
                mid_nodes = [node for node in neighbours if label[node] == 'Mid']
                
                for n in mid_nodes:
                    cycle = [n]
                    c = node
                    while c != n:
                        cycle.append(c)
                        c = parent[c]
                    if cycle[::-1] not in cycles:
                        cycles.append(cycle[::-1])
                    
                DFS.pop()
                
            else:
                for n in neighbours:
                    if label[n] == 'False':
                        parent[n] = node
                        DFS.push(n)
                        label[n] = 'Mid'
                        break
                    
                    elif label[n] == 'Mid':
                        cycle = []
                        c = node
                        while c != n:
                            cycle.append(c)
                            c = parent[c]
                        cycle.append(n)
                        cycles.append(cycle[::-1])
                        continue
        elif DFS.is_Empty():
            nodes = [node for node in Graph if label[node] == 'False']
            DFS.push(nodes[0])
            continue
    return cycles
                        
                    
    
    
    
# DG = nx.DiGraph()    
# DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('D', 'E'), ('E', 'B')])    
# print(nx.info(DG))
# nx.draw(DG, with_labels = True)
# plt.show()

# cycles = Find_Cycles_In_Metabolic_Graph(DG)


# DG2 = nx.DiGraph()    
# DG2.add_edges_from([(1,2),  (2,3), (3,1)])
# cycles2 = Find_Cycles_In_Metabolic_Graph(DG2)


# DG = nx.DiGraph()    
# DG.add_edges_from([('A', 'B'),  ('B', 'C'), ('C', 'E'), ('D', 'C'), ('C', 'G'), ('G', 'H'), ('H', 'D'), ('E', 'F'),('F', 'C') ])    
# print(nx.info(DG))
# nx.draw(DG, with_labels = True)
# plt.show()
# cycles3 = Find_Cycles_In_Metabolic_Graph(DG)

DG = nx.DiGraph() 
DG.add_edges_from([('M1', 'R1'), ('M2', 'R1'), ('R1', 'M3'), ('R1', 'M4'), ('R1', 'M5'), ('M2', 'R2'), ('M5', 'R2'), ('R2', 'M8'),('M8', 'R4'), ('M9', 'R4'), ('R4', 'M10'), ('M10', 'R3'), ('M3', 'R3'), ('R3', 'M5')])
print(nx.info(DG))
nx.draw(DG, with_labels = True)
plt.show()
cycles3 = Find_Cycles_In_Metabolic_Graph(DG)
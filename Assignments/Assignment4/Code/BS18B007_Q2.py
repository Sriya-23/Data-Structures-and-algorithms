#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:42:27 2021

@author: vsriya23
"""


import networkx as nx
# Use of any function from networkx.algorithms module is strictly not allowed.
# Matplotlib can be used for visualization purposes

import json
import matplotlib.pyplot as plt

# Add your functions here if needed

class Stack:
    '''implementing a minimalist Stack class with basic methods like pop(), push()...
        Defining a stack class to implement DFS to detect cycles
    
    
    '''
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
    
#%%
def Get_cycle(start_stop, parent):
    """
    To backtrack on the parent dictionary and find all the nodes present in the cycle
    """

    
    c = start_stop[0]
    cycle = [start_stop[1]]
    
    while c != start_stop[1]:

        cycle.append(c)
        c = parent[c]
    # cycle.append(n)
    
    return cycle[::-1]
    
#%%

def construct_metabolic_graph(name_of_json_file):
    """
    Given the reaction dict, return the metabolic directed bi-partite netwrokx graph
    """
    
    f = open(name_of_json_file)
    data = json.load(f)
    metabs = [met['id'] for met in data['metabolites']]
    
    
    G = nx.DiGraph()
    
    for reac in data['reactions']:
        G.add_node(reac['id'])
        reac_metab = reac['metabolites']
        for met in reac_metab:
            if reac_metab[met] < 0: # if the coefficient is -ve it is a reactant - edge from metabolite to reaction
                G.add_edge(met, reac['id'])
            elif reac_metab[met] > 0: # if the coefficient is +ve it is a product - edge from metabolite to reaction
                G.add_edge(reac['id'], met)
                
    colour_map = ['blue' if node in metabs else 'red' for node in G ] #generating a colour map to colour the reaction nodes and the metabolite nodes differently
    return G , colour_map
            
    
#%%

def Find_Cycles_In_Metabolic_Graph(Graph):
    """
    Given a bipartite networkx graph, return the list of list of metabolites involved in the cycle i.
    """
    
    parent = {node: None for node in Graph}
    label = {node: 'undiscovered' for node in Graph}
    cycles = []
    
    DFS = Stack(len(Graph))
    DFS.push(list(label.keys())[1])
    label[DFS.peek()] = 'discovered'
     
    
    while not all([ label[node] == 'processed' for node in Graph]):
    
        if not DFS.is_Empty():
            node = DFS.peek()
            if label[node] != 'discovered':
                label[node] = 'discovered'
            
                for n in Graph.successors(node):
                    if label[n] == 'undiscovered':
                        parent[n] = node
                
                        DFS.push(n)
                    elif label[n] == 'discovered':# cycle
                        cycle = Get_cycle([node, n], parent)
                        
                       
                        if all([set(cycle) != set(cyc) for cyc in cycles]):
                            cycles.append(cycle)
                            
                            
                        
            elif label[node] == 'discovered': # all the neighbours of the node were already explored in the previous if statement
            # we are encountering this node again after it was already explored, so it is removed from the stack
                label[node] = 'processed'
                DFS.pop()
        
        elif DFS.is_Empty():
            nodes = [node for node in Graph if label[node] == 'undiscovered']
            DFS.push(nodes[0])
            continue

                
    return cycles
                        
                    
#%%    


# For the purpose of parsing, look under the "metabolites" sub-section of "reaction" section. The stoichiometric coefficients will help you in determining if a metabolite is a reactant or a product.
G , colour_map = construct_metabolic_graph('e_coli_core.json')
# Add code to visulaise G below
print(nx.info(G))
nx.draw(G, with_labels = True, node_color = colour_map)
plt.show()
print(len(G))

f = open('e_coli_core.json')
data = json.load(f)
metabs = []
    
for met in data['metabolites']:
    metabs.append(met['id'])
    
reacs =    [] 
for reaction in data['reactions']:
    reacs.append(reaction['id'])

cycles = Find_Cycles_In_Metabolic_Graph(G)
print(cycles)






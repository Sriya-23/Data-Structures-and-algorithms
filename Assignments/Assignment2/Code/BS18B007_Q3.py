#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:26:35 2021

@author: vsriya23
"""
import numpy as np
from matplotlib.pyplot import matshow

class Simulate_Conways_Game_of_Life():
    
    def __init__(self, MyMatrix):
        self.matrix = MyMatrix
        self.pad_matrix = self.zero_pad_matrix()
        
    def rules(self,i,j, neighbours):
        '''Defining the rules for Conway's Game of life'''
        
        if neighbours > 3 or neighbours < 2:
            return 0
                       
        elif( (neighbours == 2  or neighbours == 3) and self.pad_matrix[i][j] ==1) or (neighbours == 3 and self.pad_matrix[i][j] == 0):
            return 1
                       
        
        else:
            return 0
        
        
    def zero_pad_matrix(self):
        '''padding the matrix with zeros to simplify the process of counting neighbours'''
        zero_col = np.array([0 for i in range(100)])
        zero_row = np.concatenate((zero_col, np.array([0,0])))
        matrix = np.column_stack((zero_col, self.matrix))
        matrix = np.column_stack((matrix, zero_col))
        matrix = np.row_stack((matrix, zero_row))
        matrix = np.row_stack((zero_row, matrix))
        
        return matrix
    
    
    def calc_neighbours(self, i ,j):
        '''counting the number of neighbours for a given cell'''
        
        matrix = self.pad_matrix
        neighbours = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] +matrix[i+1][j+1]
        
        return neighbours
            
    def stimulate_one_step(self):
        Glide_next = [[0 for i in range(100)] for j in range(100)]
        
        for i in range(1,100):
           for j in range(1,100):
               # print(i,j)
               # cornercases
               neighbours = self.calc_neighbours( i, j)
               Glide_next[i-1][j-1] = self.rules(i,j,neighbours)
               
               
        self.matrix = Glide_next
        self.pad_matrix = self.zero_pad_matrix()
        
    def final_output(self):
        for i in range(39):
            #print(i)
            self.stimulate_one_step()
            matshow(self.matrix)
        return self.matrix
                   
              
Glider = [[0 for i in range(100)]  for j in range(100)]
Glider[1][2] = 1
Glider[2][3] = 1
Glider[3][1:4] = [1,1,1]

# 0 - Dead cell, 1 - Live cell
Game1 = Simulate_Conways_Game_of_Life(Glider)

Step_39 = Game1.final_output()

from matplotlib.pyplot import matshow

matshow(Step_39)                   
                
                
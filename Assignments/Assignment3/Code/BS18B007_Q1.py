#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:04:19 2021

@author: vsriya23
"""

def min_mutations(seq1, seq2):
    ''' rules
    ED[i+1][j+ 1] = min{ ED[i][j+1] + deletion cost
                         ED[i+1][j] + insertion cost
                         ED[i][j] + substition_cost((seq1[i],seq2[j])
                        }
                                                    
    The substitution costs are given in the array subs
    The subtitution from a purine to purine and pyrimidine to pyrimidine is +1
    The subtitution from a purine to pyrimidine and vice versa is +3
    The insertion and deletion costs are +2
    '''
    # substitution cost for different combinations
    subs = {('A', 'A'): 0, ('T', 'T'): 0, ('G', 'G'):0, ('C', 'C'): 0,
            ('A', 'G'): 1, ('G', 'A'): 1, ('T', 'C'): 1, ('C', 'T'): 1,
            ('A', 'T'): 3, ('T', 'A'): 3, ('C', 'A'): 3, ('A', 'C' ): 3,
            ('G', 'T'): 3, ('T', 'G'): 3, ('C', 'G'): 3, ('G', 'C' ): 3} 
    n = len(seq1) # length of  sequence 1
    m = len(seq2) # length of sequence 2
    ins_cost = 2 # insertion cost
    del_cost = 2 # deletion cost
    ED = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # calculating for first column
    for i in range(n):
        ED[i+1][0] = ED[i][0] + del_cost # top row to bottom row but same column: deletion
        
    # calculating for the first row
    for j in range(m):
        ED[0][j+1] = ED[0][j] + ins_cost # left column to current column but same row : insertion
        
    # calculating the edit distance using the rules    
    for i in range(n):
        for j in range(m):
            ED[i+1][j+1] = min([ED[i][j+1] + del_cost, ED[i+1][j] + ins_cost , 
                                ED[i][j] + subs[(seq1[i],seq2[j])]])
        
    return ED[-1][-1]   # returning the last box in the table which has the value of minimum cost to convert seq1 to seq2



if __name__ == '__main__':
    
    print(min_mutations('ATGC', 'ATGGG'))
    print(min_mutations('TAGTA', 'TGGTA'))
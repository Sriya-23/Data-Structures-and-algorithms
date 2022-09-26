#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:44:06 2021

@author: vsriya23
"""

import random
import math
import matplotlib.pyplot as plt
toss = []
prob_toss = []
for _ in range(5000):
    toss.append(random.choice([0,1])) # coin toss
    prob_toss.append(toss.count(0)/len(toss))

# plt.plot(prob_toss)

z = random.randrange(1,6,1) # dice roll

a = (random.randrange(1,6,1), random.randrange(1,6,1)) # a roll of 2 dice


def random_DNAseq(L): # generate DNA seq of length L
    seq = ''.join(random.choices(['A', 'T', 'G', 'C'], k = L))
    return seq
    
s = random_DNAseq(10)


# get points on a circle

def get_pt_circle(r):
    # centre at origin
    x = []
    y = []
    
    for _ in range(1000):
        theta = 2*math.pi * random.random()
        
        x.append(r * math.cos(theta))
        y.append(r * math.sin(theta))
    
    return x,y

# get points inside a circle

def get_ptin_circle(r):
    # centre at origin
    
    x = []
    y = []
    thetas = []
    Rs = []
    
    for _ in range(1000):
        theta = 2*math.pi * random.random()
    
        R = random.uniform(0, r)
        x.append(R * math.cos(theta))
        y.append(R * math.sin(theta))
        thetas.append(theta)
        Rs.append(R)
    
    return x,y, thetas, Rs


# get points inside a  square

def get_ptin_square(side):
    # centre at origin
    x = []
    y = []
    for _ in range(1000):
        x.append(random.uniform(-side/2, side/2))
        y.append(random.uniform(-side/2, side/2))
    
    return x, y



def get_pi_value():
    square = 0
    circle = 0
    probab = []
    for _ in range(5000):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        
        if x**2 + y**2 < 1:
            circle += 1
            square += 1
            
        else:
            square += 1
          
        probab.append(circle*4/square)
        
    return probab


# probab = get_pi_value()

# plt.plot(list(range(len(probab))), probab)
        

x,y , theta , Rs= get_ptin_circle(1)   
plt.hist(Rs)
     





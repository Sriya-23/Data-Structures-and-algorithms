#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Nov 13 02:52:27 2021

@author: vsriya23
"""

import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import networkx as nx

def get_leaders(G):
    return sorted(G.nodes, key = G.degree, reverse=True)[:6]


SocialGraph = nx.barabasi_albert_graph(60, 2, 42)
Leaders = get_leaders(SocialGraph)
Trump_Card = 59;

# You are given SocialGraph which reflects the social network of the 60 participants.
# Six chosen leaders are given to you as a list using variable called 'Leaders'

# Add any functions required
    
#%%

def Form_Teams(G, Leaders):
    """Form six teams each consisting of 10 individuals"""
    teams = {i:[i] + [0 for i in range(9)] for i in Leaders}
    picked = {i:'not picked' if i not in Leaders else 'picked' for i in G.nodes()}
 
    """ Add your code here """
    Qs = {i : [] for i in Leaders}
    random.shuffle(Leaders)# shuffling the leaders to randomise the order in which the leaders get to choose their first neighbours
    
    for node in Leaders:
        for nb in G.neighbors(node):
            if teams[node][1:].count(0) != 0 and picked[nb] != 'picked':
                idx = teams[node][1:].index(0) + 1
                teams[node][idx] = nb
                picked[nb] = 'picked'
                Qs[node].append(nb)
                
            elif teams[node][1:].count(0) == 0:
                break
            
    
    
    while not all(True if len(Qs[i]) == 0 else False  for i in Qs): #Till all the neighbour lists are empty the while loop keeps running
        random.shuffle(Leaders) #After all the leaders pick the i -1 th neighbours in random order the leaders are shuffled again before picking the ith neighbours
        # Since they are shuffled after every round of picking members. If they have common neighbours the leaders have an equal chance of picking them for their teams
        
        
        for leader in Leaders: 
            neighbour_lst = []# for each leader we are creating a list of i th neighbours
            
            for node in Qs[leader]: # iterating through the list of i-1 th neighbours and iterating through their neighbours to get the ith neighbours
                for nb in G.neighbors(node):
                    if teams[leader][1:].count(0) == 0: # if the team is full no more members are added, the neighbour list will be empty
                        neighbour_lst = []
                        
                        break
                    elif picked[nb] != 'picked'  and teams[leader][1:].count(0) != 0: # if the team is not full and the ith neighbour is not picked, it is added to the team and neighbour list and it is labelled as 'picked'
                        neighbour_lst.append(nb)
                        idx = teams[leader][1:].index(0) + 1
                        teams[leader][idx] = nb
                        picked[nb] = 'picked'
            
            Qs[leader] = neighbour_lst

    # after iterating through the neighbours, if some teams still have free spots, the leaders pick members at random to fill up the team
    random.shuffle(Leaders)
    
    for node in Leaders:
        if node != 0:
            zero_count = teams[node].count(0)
        else:
            zero_count = teams[node].count(0) -1
        if zero_count != 0:
            np_list = [n for n in G.nodes() if picked[n] != 'picked']
            
            node_list = random.choice(np_list, zero_count, replace=False)
            for nd in node_list:
                picked[nd] = 'picked'
                teams[node][teams[node][1:].index(0) + 1] = nd             
                        
            
    
    return teams
#%%

def Tug_of_war_Trump_Card(Teams, Trump_Card): # Update this function from your previous subquestion
    """ Tug of war round. Each team has equal chance of winning. Returns three winning teams."""
    """ Add your code here """
    Leaders = list(Teams.keys())
    winners = []
    players = random.choice(Leaders, size = (len(Leaders)//2, 2), replace = False)
    for game in players:
        teamA = game[0]
        teamB = game[1]
        # if both the teams don't have trump cards they have equal chance of winning
        if Trump_Card not in Teams[teamA] and Trump_Card not in Teams[teamB]:
            winners.append(random.choice(game, replace = False))
            
        # the team with trump card has 90% chance of winning 
        elif Trump_Card in Teams[teamA]: 
            winners.append(random.choice(game, replace = False, p = [0.9, 0.1]))
            
        else:
            winners.append(random.choice(game, replace = False, p = [0.1, 0.9]))
    
    Winning_Teams = {i: Teams[i] for i in winners}
    
    
    
    return Winning_Teams
#%%

def simulate(G, Leaders): # Copy this function from the previous subquestion with appropriate modifications
    """ Simulate the scenario multiple times """
    probabilities_of_winning = {i:0.2 for i in G.nodes}
    """ Modify the code as required """
    for i in range(1, 10001):
        Teams = Form_Teams(G,Leaders)
        # print(Teams)
        Winners = Tug_of_war_Trump_Card(Teams, Trump_Card)
        # Update the probabilites
        winner_lst = []
        for team in Winners:
            winner_lst += Winners[team]
            
        for player in G.nodes:
            if player in winner_lst:
                probabilities_of_winning[player] = (probabilities_of_winning[player]* (i-1) + 1)/i
                
            else:
                probabilities_of_winning[player] = (probabilities_of_winning[player]* (i-1))/i
        
        
        
    return probabilities_of_winning
    
#%%plotting bar plot and histogram for probabilities to visualise the distribution of probabilities

probabilities = simulate(SocialGraph, Leaders)

prob = list(probabilities.values())

plt.figure(1)
plt.bar(list(range(60)), prob)
plt.title('Probability of winning for each player')
plt.xlabel('players')
plt.ylabel('probabilities of winning')


plt.figure(2)
plt.hist(prob)
plt.title('Histogram of probabilities')
plt.xlabel('probabilities')
plt.ylabel('number of players')


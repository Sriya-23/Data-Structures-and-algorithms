#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:58:11 2021

@author: vsriya23
"""
# no libraries allowed


def optimal_investment_stocks_selection(price_2011, price_2021, investment_amount, n):
    
    """
	(list of int), (list of int), (int), (int) -> (list of int)

	>>> optimal_investment_stocks_selection([1000,1000,1800,100,1200], [3900, 1300, 4700, 120, 4500], 3000, 5)
	    [3, 0, 0, 0, 0]
	"""
    if len(price_2011) != n or len(price_2021) != n:
        return 'Incorrect Input!'
    #     raise( 'Incorrect Input!')
    
    ''' very similar coin change but here instead of finding minimum number of coins we are finding maximum profit
    we take a bottom up approach where calculate the maximum of profit 
    
    explanation
    
    o[i][j] - the maximum profit if we have 0th stock to ith stock and investment amount = j
    
    o[i][j] = max { oi[i-1][j] (the same profit as the profit we get with j investment and 0- i-1 stocks),
                   profits[i] + oi[i][j-price_2011[i]] (the profit with j-price_2011[i] investment amount + profit for ith stock)
        
        
        }
    The logic is that either we can include the stock or exclude it. and if we include it we can have 1 or more repetitions of the stock
    the oi[i-1][j] represents the fact that we are excluding it
    in profits[i] + oi[i][j - price_2011[i]] we are finding the profit stored in the table for the 0- i stocks (ith row ) and j - price_2011[i] investment amount and adding the profit for the ith stock
    this allows us to buy more than one stock from a given company -  whenever j is a multiple of price_2011[i] one more of the ith stock is added to it

    
    '''
    
    
    profits = [price_2021[i] - price_2011[i]for i in range(len(price_2011))]
    
    
    
    oi = [[0 for _ in range(investment_amount+1)] for _ in range(n)] 
    
    for i in range(n):
        for j in range(1, investment_amount+1):
            if price_2011[i] <= j:
                
                oi[i][j] = max(profits[i] + oi[i][j - price_2011[i]], oi[i-1][j])
                
            elif price_2011[i] <= j:
                
                oi[i][j] = oi[i-1][j]
                
                
                
    max_profit = oi[-1][-1]
    
    # finding the number of stocks bought for each stock
    
    
    ''' 
    we trace back from the last square in the table - 
    if the square above the current square has the same value as the current square then it means that the it stock was not bought anymore 
    so we go to the previous row
    if the square above the current square has a different value then it means that the ith stock was bought we subtract the selling price from investment amount and we continue
    it is imortant to note that i is the total number of stocks and subtracting values will take it back through the rows
    once the top square has different values it means that buying of the ith stock was completed and now move to the (i- 1)th stock
    
    
    '''
    
    stock_list = []
    
    i = n-1
    count = 0
    while i>= 0 and investment_amount >=0:
        if i > 0 and oi[i][investment_amount] != oi[i-1][investment_amount]:
            count += 1
            
            investment_amount -= price_2011[i]
            
        elif i == 0 and investment_amount >= price_2011[0]:
            
            while investment_amount >= price_2011[0] and investment_amount >= 0:
                count += 1
                investment_amount -= price_2011[0]
            stock_list.append(count)
            break
            
        else:
            stock_list.append(count)
            count = 0
            i -= 1
    
    return stock_list[::-1]


if __name__ == '__main__':
    price_2011 = [1000,1000,1800,100,1200]
    price_2021 = [3900, 1300, 4700, 120, 4500]
    investment_amount = 3500
    n = len(price_2011)
    print((optimal_investment_stocks_selection(price_2011, price_2021, investment_amount, n)))
    

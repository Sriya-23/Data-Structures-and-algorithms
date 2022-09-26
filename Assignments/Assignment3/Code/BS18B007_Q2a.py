# no libraries are allowed

""" Add your functions here """

def optimal_investment_time_series(time_series):
    """
    (list of int) -> int
    
    >>> optimal_investment_time_series([3,3,0,1,2,5,2,2,4,2,7,0])
        10
    """
    """ Add your code here """
    n = len(time_series)
    
    ot = [[0 for _ in range(n)] for _ in range(3)] # the rows represent the number of transactions and the columns represent the days
    
    
    '''
    using dynamic programming to solve 
    
    ot[i][j] - the profit we can get if we have i trasactions till the jth day
    
    Here what we are trying to do is to decide if we want to make a transaction on jth day
    we see when we get maximum value
    either no transaction or
    
    we make transaction and we see which is the best day to buy to sell on the jth day 
    we consider all the days before jth day 
    
    for example
    ot[2][3] = max{
                    ot[2][2] (no transactions are made so the same profit as previous day taken )
                    
                    time_series[3] -  time_series[1] + ot[1][1] ( selling on day 3 and buying on day 1 and also adding the profits before day 1)
                    
                    time_series[3] -  time_series[2] + ot[1][2]} (selling on day 3 and buying on day 2 and also adding the profits before day 2 )
    
    ot[2][4] = max{
                    ot[2][2] (no transactions are made so the same profit as previous day)
                    
                    time_series[4] -  time_series[1] + ot[1][1]
                    time_series[4] -  time_series[2] + ot[1][2]
                    time_series[4] -  time_series[3] + ot[1][3]}
    
    here we can see that in a row, for each day, there is only one extra term added
    so to avoid calculations repeatedly we add the term opt_common_diff which updates every day to see if the new term added is giving a greater maximum or not
    
    
    the final set of rules look like the following
    
    ot[i][j] = max{
                    ot[i][j-1] (no transactions are made so the same profit as previous day)
                    
                    time_series[j] + opt_common_diff
        
        }
    opt_common_diff for jth transaction is = max { opt_common_diff (the previous maximum),
                                                  ot[i-1][j] - time_series[j]
                     
        }
    
    '''
    #we start both the iterations from 1 because
    #if we have zero transactions(i = 0) then we cant get any profit so the whole row remains as 0
    # if we consider only the first day(j = 0), we cant have any profit because we cant buy and sell on the same day- so the whole row remains as 0
    
    for i in range(1,3):
        opt_common_diff = -time_series[0]
        for j in range(1,n):
            opt_common_diff = max(opt_common_diff, ot[i-1][j] - time_series[j])
            ot[i][j] = max(ot[i][j-1], time_series[j] + opt_common_diff)
    # print(ot)
    return ot[-1][-1]


if __name__ == '__main__':
    print(optimal_investment_time_series([3,3,0,1,2,5,2,2,4,2,7,0]))
    print(optimal_investment_time_series([1,2,3,4,5]))
    print(optimal_investment_time_series([5,4,3,2,1]))
    print(optimal_investment_time_series([3,3,5,0, 0, 3,1,4]))
    
#!/usr/bin/python
import math
def Mean(t):
    '''
    Return the mean value of a list t
    '''
    return float(sum(t))/len(t)

def Variance(t,mean=None):
    if mean == None:
        mu = Mean(t)
    else:
        mu = mean

    return Mean([(x - mu)**2 for x in t])

def StandardVar(t,mean=None):
    var = Variance(t,mean)    
    return math.sqrt(var)

def Binom(n,k,dataSet={}):
    '''
    Return the number of way to select k items from n.
    dataSet is a result buffer. Map (n,k) to the value.
    '''
    if k == 0:
        return 1
    if n == 0:
        return 0

    try:
        return dataSet[n,k]
    except KeyError:
        res = Binom(n-1,k) + Binom(n-1,k-1)
        dataSet[n,k] = res
        return res

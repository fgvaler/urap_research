from scipy.stats import skew
import statistics as stats
import numpy as np

def within_10(n):
    if n > 10:
        return 10
    if n < 0:
        return 0
    else:
        return n

def weighted_average(l):
    total = 0
    denom = 0
    for i in range(len(l)):

        #James optimal
        # weight = 1
        
        #Anastassia optimal
        weight = 1 + i

        total += l[i] * weight
        denom += weight
    return total/denom

def experience_score(l):
    l = [x for x in l if x > 0]
    if len(l) < 3:
        l = l + [1 for _ in range(3 - len(l))]
    if len(l) == 0:
        l = [1]
    # if len(l) > 10:
    #     l = l[:10]
    a = (weighted_average(l) + 3*max(l) - skew(np.array(l)))/4
    # a = max(l) - skew(np.array(l))
    # a = weighted_average(l)
    # a = max(l)
    if a > 4:
        a = (a - 3) * 2 + 3
    #James optimal
    # a = (weighted_average(l) + 3*max(l))/4

    #Anastassia optimal
    # a = (weighted_average(l) + 3*max(l))/2 - 1

    return a

def total_score(high, low, exp):
    return round(within_10(high/5 + high/10 + experience_score(exp)))

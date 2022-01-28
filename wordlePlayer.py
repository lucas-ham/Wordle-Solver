# pass it a function that solves wordle and this will run through it's playing a specified number of times using random words from the solution list
from wordleFunction import *

def multiPlayWithHardest(num, func):
    sum = 0
    hard = []
    for i in range(num):
        curr = func(rawList)
        sum += curr[0]
        if curr[0] > 5:
            hard.append(curr[1])
    return sum/num, hard

def multiPlay(num, func):
    sum = 0
    hard = []
    for i in range(num):
        sum += func(rawList)[0]
    return sum/num

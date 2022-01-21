from words import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *


def generateIndices(rawList, tried):
    print(tried)
    letters = list(string.ascii_lowercase)
    for l in tried:
        if letters.count(l):
            letters.remove(l)
    newPoss = list(range(len(rawList)))
    for index in newPoss:
        word = rawList[index]
        for curr in word:
            if letters.count(curr):
                pass
            else:
                newPoss.remove(index)
                break
    return newPoss

def printBad(rawList, tried):
    possibles = generateIndices(rawList, tried)
    print(len(possibles))
    printWords(rawList, possibles)

t = list(string.ascii_lowercase)
t.remove('a')
t.remove('u')
t.remove('d')
t.remove('i')
t.remove('o')

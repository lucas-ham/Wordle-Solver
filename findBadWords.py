from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *


def generateIndices(rawList, tried):
    letters = list(string.ascii_lowercase)
    for l in tried:
        if letters.count(l):
            letters.remove(l)
    allWords = list(range(len(rawList)))
    newPoss = []
    for index in allWords:
        word = rawList[index]
        addWord = True
        for curr in word:
            if tried.count(curr):
                addWord = False
        if addWord:
            newPoss.append(index)
    return newPoss

def printBad(rawList, tried, possibleWords):  #possibleWords = our normal possibles
    possibles = generateIndices(rawList, tried)
    if len(possibles) > 0:
        rankedIndices = generateBadRanking(rawList, tried, possibleWords)
        print("\n Here are the words that will test the most possible letters!")
        print(parseList(rawList, rankedIndices))

def generateBadRanking(rawList, tried, possibleWords):
    possibles = generateIndices(rawList, tried)
    f = frequencyCreator(rawList, possibleWords)
    f[1] = eraseNullLetters(f[0], f[1])
    rankedIndices = rankWords(rawList, possibles, f[0], f[1])
    return rankedIndices

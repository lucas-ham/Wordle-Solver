from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *
from findBadWords import *
import random


class Solver:
    def __init__(self, rawList, startingWord, rankWeight, rightPlaceWeight, doubleWeight):
        self.rawList = rawList
        self.startingWord = startingWord
        self.possibles = [i for i in range(len(rawList))]
        self.tried = []
        self.ranker = genericRanker(self.rawList, rankWeight, rightPlaceWeight, doubleWeight)
        self.guesses = 0
        self.rankWeight = rankWeight
        self.rightPlaceWeight = rightPlaceWeight
        self.doubleWeight = doubleWeight
        self.average = None
    def reset(self):
        self.possibles = [i for i in range(len(rawList))]
        self.tried = []
        self.guesses = 0
    def guessFeedback(self, letters, colors):
        #want this to update self.possibles, self.tried
        i = 0
        greenList = []
        yellowList = []
        greyList = []
        self.guesses += 1
        while i < len(letters):
            if colors[i] == 'g':
                greenList.append(letterStorage(letters[i],i))
            elif colors[i] == 'y':
                yellowList.append(letterStorage(letters[i], i))
            else:
                greyList.append(letterStorage(letters[i], i))
            i += 1
        self.parseLetters(greenList, yellowList, greyList)
    def parseLetters(self, greenList, yellowList, greyList):
        temp = parseGreen(self.rawList, greenList)
        if temp:
            g = temp[0]
            self.tried += temp[1]
            self.possibles = mergePossibles(self.possibles, g)
        temp = parseYellow(self.rawList, yellowList)
        if temp:
            y = temp[0]
            self.tried += temp[1]
            self.possibles = mergePossibles(self.possibles, y)
        temp = parseGrey(self.rawList, self.possibles, greyList)
        if temp:
            self.possibles = temp[0]
            self.tried += temp[1]
    def rankGood(self):
        f = frequencyCreator(rawList, self.possibles)
        f[1] = eraseNullLetters(f[0], f[1])
        rankedIndices = self.ranker(self.possibles,f[0], f[1])
        return rankedIndices
    def rankBad(self):
        possibles = generateIndices(self.rawList, self.tried)
        f = frequencyCreator(self.rawList, self.possibles)
        f[1] = eraseNullLetters(f[0], f[1])
        rankedIndices = self.ranker(possibles, f[0], f[1])
        return rankedIndices
    def getGuess(self):
        goodRanked = self.rankGood()
        badRanked = self.rankBad()
        if (len(badRanked) > 10) and (len(goodRanked) > 15):
            return badRanked[0]
        else:
            return goodRanked[0]
    def checkDone(self):
        if len(self.possibles) > 1:
            return False
        else:
            return self.possibles[0]
    def addAverage(self, avg):
        self.average = avg






def genericRanker(rawList, rankWeight, rightPlaceWeight, doubleWeight):
    def rankWords(possibles, dFreq, digitFreq):
        d = {}
        for num in possibles:
            word = rawList[num]
            d[num] = 0
            log = []
            digit = 0
            for let in word:
                d[num] += (rightPlaceWeight)*digitFreq[digit].storage[let]
                if log.count(let):
                    d[num] += (doubleWeight)*dFreq[let]
                    pass
                else:
                    d[num] += (rankWeight)*dFreq[let]
                    log.append(let)
        #return list(OrderedDict(sorted(d.items())).keys())
        d_inv = {v: k for k, v in d.items()}
        rankedOrder = []
        for key in sorted(d_inv):
            for lookup in d.keys():
                if d[lookup] == key:
                    rankedOrder.append(lookup)
        rankedOrder.reverse()
        return rankedOrder
    return rankWords

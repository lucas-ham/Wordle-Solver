from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict

#letter frequency creator

#rank words by frequency
#- if we make a dict with key/value of index/score, then we should be able to sort and export using dictionary methods

#then order words based on rank

#UPGRADE would be to speed up this computation by saving the current frequencys and updating them with each new word

class digitStorer():
    def __init__(self):
        self.storage = dict.fromkeys(string.ascii_lowercase, 0)
    def add(self, let):
        self.storage[let] +=1


def frequencyCreator(rawList, possibles):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    digitList = []
    for i in range(5):
        digitList.append(digitStorer())
    for num in possibles:
        word = rawList[num]
        digit = 0
        for let in word:
            d[let] += 1
            digitList[digit].add(let)
            digit += 1
    return [d, digitList]

def rankWords(rawList, possibles, dFreq, digitFreq):
    d = {}
    for num in possibles:
        word = rawList[num]
        d[num] = 0
        log = []
        digit = 0
        for let in word:
            d[num] += (1)*digitFreq[digit].storage[let]
            if log.count(let):
                d[num] += (-1/2)*dFreq[let]
                pass
            else:
                d[num] += dFreq[let]
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

def checkDigitExistence(let, digitFreq):
    sum = 0
    for i in range(5):
        if (digitFreq[i].storage[let]):
            sum += 1
    return sum

def findWhichDigit(let, digitFreq):
    for i in range(5):
        if digitFreq[i].storage[let]:
            return i
    return None

def eraseNullLetters(d,digitFreq):
    for let in list(string.ascii_lowercase):
        if num := checkDigitExistence(let, digitFreq):
            if num > 1:
                pass
            else:
                digit = findWhichDigit(let, digitFreq)
                digitFreq[digit].storage[let] = 0
                d[let] = 1/2*d[let]
    return digitFreq


def generateGooRanking(rawList, possibles):
    f = frequencyCreator(rawList, possibles)
    f[1] = eraseNullLetters(f[0], f[1])
    rankedIndices = rankWords(rawList, possibles, f[0], f[1])
    return rankedIndices


def printWords(rawList, possibles):
    rankedIndices = generateGoodRanking(rawList, possibles)
    print(parseList(rawList, rankedIndices))

from words import rawList
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

def frequencyCreator(rawList, possibles):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for num in possibles:
        word = rawList[num]
        for let in word:
            d[let] += 1
    return d

def rankWords(rawList, possibles, dFreq):
    d = {}
    for num in possibles:
        word = rawList[num]
        d[num] = 0
        log = []
        for let in word:
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
        rankedOrder.append(d_inv[key])
    rankedOrder.reverse()
    return [d, rankedOrder, d_inv]

def printWords(rawList, possibles):
    f = frequencyCreator(rawList, possibles)
    rankedIndices = rankWords(rawList, possibles, f)
    print(parseList(rawList, rankedIndices))

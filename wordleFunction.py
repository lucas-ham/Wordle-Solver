#just a function version of the same implementation in main.py, eventually should update main to use This
from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *
from findBadWords import *
import random

def playSingleRound(rawList, possibles, tried, word):
    badRanking = generateBadRanking(rawList, tried, possibles)
    goodRanking = generateGoodRanking(rawList, possibles)
    if badRanking and len(badRanking) > 10:
        guess = badRanking[0]
    else:
        guess = goodRanking[0]
    [letters, colors] = wordleAutomator(rawList, guess, word)
    i = 0
    greenList = []
    yellowList = []
    greyList = []
    while i < len(letters):
        if colors[i] == 'g':
            greenList.append(letterStorage(letters[i],i))
        elif colors[i] == 'y':
            yellowList.append(letterStorage(letters[i], i))
        else:
            greyList.append(letterStorage(letters[i], i))
        i += 1
    if len(greenList) > 4:
        return guess
    else:
        [possibles, tried] = parseAllLetters(rawList, possibles, tried, greenList, yellowList, greyList)
        return [possibles, tried, guess]



def parseAllLetters(rawList, possibles, known, g, y, grey):
    temp = parseGreen(rawList, g)
    if temp:
        g = temp[0]
        known += temp[1]
    possibles = mergePossibles(possibles, g)
    temp = parseYellow(rawList, y)
    if temp:
        y = temp[0]
        known += temp[1]
    possibles = mergePossibles(possibles, y)
    temp = parseGrey(rawList, possibles, grey)
    if temp:
        possibles = temp[0]
        known += temp[1]
    return [possibles, known]






def playFullRound(rawList):
    word = generateWord(rawList)
    guessList = []
    firstGuess = 108
    guessList.append(parseList(rawList, [firstGuess])[0])
    [letters, colors] = wordleAutomator(rawList, firstGuess, word) #this is the index for "arose"
    i = 0
    greenList = []
    yellowList = []
    greyList = []
    while i < 5:
        if colors[i] == 'g':
            greenList.append(letterStorage(letters[i],i))
        elif colors[i] == 'y':
            yellowList.append(letterStorage(letters[i], i))
        else:
            greyList.append(letterStorage(letters[i], i))
        i += 1
    possibles = [i for i in range(len(rawList))]
    tried = colors
    [possibles, tried] = parseAllLetters(rawList, possibles, tried, greenList, yellowList, greyList)
    while len(guessList) < 6:
        curr = playSingleRound(rawList, possibles, tried, word)
        if isinstance(curr, list):
            possibles = curr[0]
            tried = curr[1]
            guessList.append(parseList(rawList, [curr[2]])[0])
        else:
            guessList.append(curr)
            break
    return [len(guessList), word]


def generateWord(rawList):
    return random.randint(0,len(rawList)-1)


def wordleAutomator(rawList,guess,word):
    i = 0
    parsedGuess = parseList(rawList, [guess])[0]
    parsedWord = parseList(rawList, [word])[0]
    lettersOut = []
    colorsOut = [0]*5
    while i < 5:
        lettersOut.append(parsedGuess[i])
        colorsOut[i] = 'grey'
        if parsedGuess[i] == parsedWord[i]:
            colorsOut[i] = 'g'
        else:
            for let in parsedWord:
                if parsedGuess[i] == let:
                    colorsOut[i] = 'y'
        i += 1
    return [lettersOut, colorsOut]

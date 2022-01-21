from words import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *
from findBadWords import *


##SETTINGS:
easyMode = True


leaveLoop = False

def enterWords(color):
    global leaveLoop
    out = wordCollector(color)
    if out or out ==[]:
        return out
    else:
        leaveLoop = True
        return None

def mainRun():
    global leaveLoop
    tries = 1
    known = []
    g = enterWords(0)
    temp = parseGreen(rawList, g)
    if temp:
        g = temp[0]
        known += temp[1]
    y = enterWords(1)
    temp = parseYellow(rawList, y)
    if temp:
        y = temp[0]
        known += temp[1]
    possibles = mergePossibles(g, y)
    grey = enterWords(3)
    if (possibles and len(possibles) == 0):
        possibles = list(range(0,len(rawList)))
    temp = parseGrey(rawList, possibles, grey)
    if temp:
        possibles = temp[0]
        known += temp[1]

    if possibles:
        print("Here are the possible words with the letters you currently know!")
        printWords(rawList, possibles)
        if easyMode:
            printBad(rawList, known)
    elif leaveLoop:
        return None

    while not leaveLoop:
        if (possibles and len(possibles)!=0):
            g = enterWords(0)
            temp = parseGreen(rawList, g)
            if temp:
                g = temp[0]
                known += temp[1]
            possibles = mergePossibles(possibles, g)
            y = enterWords(1)
            temp = parseYellow(rawList, y)
            if temp:
                y = temp[0]
                known += temp[1]
            possibles = mergePossibles(possibles, y)
            grey = enterWords(3)
            temp = parseGrey(rawList, possibles, grey)
            if temp:
                possibles = temp[0]
                known += temp[1]
        else:
            tries = 1
            g = enterWords(0)
            temp = parseGreen(rawList, g)
            if temp:
                g = temp[0]
                known += temp[1]
            y = enterWords(1)
            temp = parseYellow(rawList, y)
            if temp:
                y = temp[0]
                known += temp[1]
            possibles = mergePossibles(g, y)

            grey = enterWords(3)
            temp = parseGrey(rawList, possibles, grey)
            if temp:
                possibles = temp[0]
                known += temp[1]

        if possibles and len(possibles) < 2:
            print("Here is your wordle for today!")
            printWords(rawList, possibles)
            raise leaveLoop
        elif possibles:
            print("Here are the possible words with the letters you currently know!")
            printWords(rawList, possibles)
            if easyMode:
                printBad(rawList, known)
            tries += 1
        if tries == 6 or leaveLoop:
            break


mainRun()

from words import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *


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
    g = enterWords(0)
    g = parseGreen(rawList, g)
    y = enterWords(1)
    y = parseYellow(rawList, y)
    possibles = mergePossibles(g, y)
    grey = enterWords(3)
    if (possibles and len(possibles) == 0):
        possibles = list(range(0,len(rawList)))
    grey = parseGrey(rawList, possibles, grey)

    if possibles:
        print("Here are the possible words with the letters you currently know!")
        print(parseList(rawList, possibles))
    elif leaveLoop:
        return None

    print(leaveLoop)
    while not leaveLoop:
        print(leaveLoop)
        if (possibles and len(possibles)!=0):
            g = enterWords(0)
            g = parseGreen(rawList, g)
            possibles = mergePossibles(possibles, g)
            y = enterWords(1)
            y = parseYellow(rawList, y)
            possibles = mergePossibles(possibles, y)
            grey = enterWords(3)
            grey = parseGrey(rawList, possibles, grey)
        else:
            tries = 1
            g = enterWords(0)
            g = parseGreen(rawList, g)
            y = enterWords(1)
            y = parseYellow(rawList, y)
            possibles = mergePossibles(g, y)

            if possibles:
                print(parseList(rawList, possibles))

            grey = enterWords(3)
            grey = parseGrey(rawList, possibles, grey)

        if possibles and len(possibles) < 2:
            print("Here is your wordle for today!")
            print(parseList(rawList,possibles))
            raise leaveLoop
        elif possibles:
            print("Here are the possible words with the letters you currently know!")
            print(parseList(rawList, possibles))
            tries += 1
        if tries == 6 or leaveLoop:
            break


mainRun()

from words import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *



def mainRun():
    tries = 1
    g = enterWords(0)
    g = parseGreen(rawList, g)
    y = enterWords(1)
    y = parseYellow(rawList, y)
    possibles = mergePossibles(g, y)
    grey = enterWords(3)
    if (len(possibles) == 0):
        possibles = list(range(0,len(rawList)))
    grey = parseGrey(rawList, possibles, grey)

    print("Here are the possible words with the letters you currently know!")
    print(parseList(rawList, possibles))

    while tries < 6:
        if (len(possibles)!=0):
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
            print(parseList(rawList, possibles))
            grey = enterWords(3)
            grey = parseGrey(rawList, possibles, grey)

        if len(possibles) < 2:
            print("Here is your wordle for today!")
            print(parseList(rawList,possibles))
            break
        else:
            print("Here are the possible words with the letters you currently know!")
            print(parseList(rawList, possibles))
            tries += 1


mainRun()

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
    grey = parseGrey(rawList, possibles, grey)

    print("Here are the possible words with the letters you currently know!")
    print(parseList(rawList, possibles))

    while tries < 5:
        g = enterWords(0)
        g = parseGreen(rawList, g)
        possibles = mergePossibles(possibles, g)
        y = enterWords(1)
        y = parseYellow(rawList, y)
        possibles = mergePossibles(possibles, y)
        grey = enterWords(3)
        grey = parseGrey(rawList, possibles, grey)

        if len(possibles) < 2:
            tries = 10

        print("Here are the possible words with the letters you currently know!")
        print(parseList(rawList, possibles))
        tries += 1


mainRun()

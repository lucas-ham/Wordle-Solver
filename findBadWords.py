from words import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *


def generateIndices(rawList, tried):
    letters = list(string.ascii_lowercase)
    for l in tried:
        letters.remove(l)
    newPoss = yellowInitSearch(rawList, letterStorage(letters[0],-1))
    for nuevo in letters[1:]:
        newPoss = yellowAddWord(rawList, masterList, newPoss, letterStorage(nuevo, -1)))
    return newPoss

def printBad(rawList, tried):
    possibles = generateIndies(rawList, tried)
    printWords(rawList, possibles)

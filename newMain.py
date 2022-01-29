from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
import string
from collections import OrderedDict
from improveSolver import *
from findBadWords import *
from solverClass import *
from geneticMethods import *

def mainRun():
    s = Solver(rawList, 108, 5, 6, -2)

    for tries in range(6):
        print("Please input your word\n")
        word = input("Type here:  ")
        print("\nPlease input the string of colors")
        colors = input("Type here:   ")
        useColors = []
        if word == 'quit' or colors == 'quit':
            break
        for let in colors:
            if let == 'r':
                useColors.append('grey')
            elif let == 'g' or let =='y':
                useColors.append(let)
            else:
                print("Color string invalid, please try again")
                continue
        s.guessFeedback(word,useColors)
        if len(s.possibles) > 1:
            print("The recommended guess is:\n")
            print(parseList(rawList,[s.getGuess()]))
            print("\n\n But here are some other guesses if you'd rather try these out!\n\n")
            print("Here are the words with what you do know!\n")
            print(parseList(rawList, s.rankGood()))
            print("\n\n Here are the words that will check the most letters!\n")
            print(parseList(rawList, s.rankBad()),"\n\n")
        else:
            print("Here is your wordle for today!")
            print(parseList(rawList, [s.possibles[0]]))
            break
mainRun()

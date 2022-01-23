from realWordleList import rawList
from generateDictionary import *
from searchByLetters import *
from wordleSolve import *
#from main import *

poss = [1,50,100]
print(parseList(rawList,poss))

grey = letterStorage("t", 5)

n = parseGrey(rawList, poss, grey := [grey])

print(parseList(rawList, n))

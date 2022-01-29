from solverClass import *

from multiprocessing import Pool

def feedBack(rawList, guess, word):
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

def generateWord(rawList):
    return random.randint(0,len(rawList)-1)


def runOnce(rawList, solver):
    w = generateWord(rawList)
    i = 1
    while i < 7 and not solver.checkDone():
        feed = feedBack(rawList, solver.getGuess(), w)
        solver.guessFeedback(feed[0],feed[1])
        i += 1
    guesses = solver.guesses + 1
    solver.reset()
    return guesses

def runGivenWord(rawList, solver, word):
    i = 1
    while i < 7 and not solver.checkDone():
        feed = feedBack(rawList, solver.getGuess(), word)
        solver.guessFeedback(feed[0],feed[1])
        i += 1
    guesses = solver.guesses
    solver.reset()
    return guesses

def evalSolver(solver):
    num = 500
    sum = 0
    for i in range(num):
        sum += runOnce(solver.rawList, solver)
    solver.addAverage(sum/num)
    return sum/num

def evalAllWords(solver):
    sum = 0
    for i in range(len(solver.rawList)):
        sum += runGivenWord(solver.rawList, solver, i)
    solver.addAverage(sum/len(solver.rawList))
    return sum/len(solver.rawList)



def generateRandom(bounds):
    return random.uniform(bounds[0], bounds[1])


def generateSolver(rawList, rankWeightBounds, rightPlaceBounds, doubleBounds):
    startingWord = generateWord(rawList)
    rankWeight = generateRandom(rankWeightBounds)
    rightPlace = generateRandom(rightPlaceBounds)
    double = generateRandom(doubleBounds)
    return Solver(rawList, startingWord, rankWeight, rightPlace, double)

def generateSolverGivenWord(rawList, word, rankWeightBounds, rightPlaceBounds, doubleBounds):
    rankWeight = generateRandom(rankWeightBounds)
    rightPlace = generateRandom(rightPlaceBounds)
    double = generateRandom(doubleBounds)
    return Solver(rawList, word, rankWeight, rightPlace, double)

def createFirstPopulation(rawList, num, rankWeightBounds = [0,5], rightPlaceBounds =[2,6], doubleBounds = [-2,1]):
    popul = []
    for i in range(num):
        popul.append(generateSolver(rawList, rankWeightBounds, rightPlaceBounds, doubleBounds))
    return popul

def createLaterPopulations(rawList, num, word, rankWeightBounds = [0,5], rightPlaceBounds =[2,6], doubleBounds = [-2,1]):
    popul = []
    rankWeightBounds.sort()
    rightPlaceBounds.sort()
    doubleBounds.sort()
    for i in range(num):
        popul.append(generateSolverGivenWord(rawList, word, rankWeightBounds, rightPlaceBounds, doubleBounds))
    return popul

def nextGeneration(rawList, num, best, worst):
    rankWeights = [best.rankWeight, worst.rankWeight]
    rankWeights.sort()
    rightPlaces = [best.rightPlaceWeight, worst.rightPlaceWeight]
    rightPlaces.sort()
    doubles = [best.doubleWeight, worst.doubleWeight]
    doubles.sort()
    return createLaterPopulations(rawList, num, name, rankWeights, rightPlaces, doubles)


def runGenerationsParrellel(rawList, numIndividuals, numGenerations):
    firstGeneration = createFirstPopulation(rawList, numIndividuals)
    if __name__ == '__main__':
        with Pool(5) as p:
            p.map(evalSolver, firstGeneration)
    for f in firstGeneration:
        print(f.average)

def runGenerations(rawList, numIndivs, numGens, toMoveOn):
    firstGen = createFirstPopulation(rawList, numIndivs)
    dict = {}
    for s in firstGen:
        dict[evalAllWords(s)] = s
    i = 0
    for key in sorted(dict):
        if i == 0:
            bestSolver = dict[key]
            worstSolver = dict[key]
        if i == toMoveOn:
            worstSolver = dict[key]
            break
        i += 1
    for g in range(numGens):
        if (g%5 == 0):
            print("We are in the",g+"th generation!")
        currGen = createLaterPopulations(rawList, numIndivs, bestSolver.startingWord,
                                        [bestSolver.rankWeight, worstSolver.rankWeight],
                                        [bestSolver.rightPlaceWeight, worstSolver.rightPlaceWeight],
                                        [bestSolver.doubleWeight, worstSolver.doubleWeight])
        currDict = {}
        for s in currGen:
            currDict[evalAllWords(s)] = s
        i = 0
        for key in sorted(currDict):
            if i == 0:
                bestSolver = currDict[key]
                worstSolver = currDict[key]
            if i == toMoveOn:
                worstSolver = currDict[key]
                break
            i += 1
    for key in sorted(currDict):
        best = currDict[key]
        break
    return best

def compareSolvers(rawList, s1, s2):
    w = generateWord(rawList)
    numSame = 1
    f1 = feedBack(rawList, s1.startingWord, w)
    s1.guessFeedback(f1[0],f1[1])
    f2 = feedBack(rawList, s2.startingWord, w)
    s2.guessFeedback(f2[0], f2[1])
    while len(s1.possibles) > 1 and len(s2.possibles) > 1:
        if s1.getGuess() == s2.getGuess():
            f = feedBack(rawList, s1.getGuess(), w)
            s1.guessFeedback(f[0],f[1])
            s2.guessFeedback(f[0],f[1])
            numSame += 1
        else:
            f1 = feedBack(rawList, s1.getGuess(), w)
            s1.guessFeedback(f1[0],f1[1])
            f2 = feedBack(rawList, s2.getGuess(), w)
            s2.guessFeedback(f2[0], f2[1])
    firstGuesses = s1.guesses
    secondGuesses = s2.guesses
    s1.reset()
    s2.reset()
    if firstGuesses == 2 or secondGuesses == 2:
        print(parseList(rawList, [w]))
    return numSame, firstGuesses, secondGuesses

s1 = Solver(rawList, 108, 5,6,-2)
s2 = Solver(rawList, 108, 1,1,-1/2)
compareSolvers(rawList, s1,s2)

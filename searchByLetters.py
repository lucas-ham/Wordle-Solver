from words import rawList
import generateDictionary
import generateDictionary


def searchKnownDigit(rawList, masterList, letter, digit):
    length = len(masterList[digit])
    i = 0
    digitList = masterList[digit]
    outList = []
    while i < length:
        if (digitList[i] == letter):
            outList.append(i)
        i+=1
    return outList


def mergePossibles(first, second):
    out = second
    i = 0
    for x in first:
        run = True
        while run:
            if (i == len(out) - 1):
                return out
            else:
                if (x < out[i]):
                    run = False
                elif (x == out[i]):
                    run == False
                    i += 1
                elif (x > out[i]):
                    out.pop(i)
    return out

def searchWord(word, letter):
    for l in word:
        if l == letter:
            return True
    return False


#can also use this for the sublists of masterList for yellow words
def removeWords(rawList, possibles, letter):
    out = []
    for n in possibles:
        if (searchWord(rawList[n],letter)):
            pass
        else:
            out.append(n)
    return out

def addWordsWithDigit(rawList, masterList, possibles, letter, digit):
    out = []
    digitList = masterList[digit]
    for n in possibles:
        if (digitList[n] == letter):
            out.append(n)
    return out

def parseList(rawList, possibles):
    out = []
    for n in possibles:
        out.append(rawList[n])
    return out

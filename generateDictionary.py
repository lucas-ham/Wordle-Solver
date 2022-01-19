
##takes a list of all the 5 letter words and returns 5 lists, (first, second, third, forth, fifth) corresponding to each of the letters

from words import rawList


def getDigitList(rawList, digit):
    length = len(rawList)
    i = 0
    outList = [""]*length
    while i < length:
        outList[i] = rawList[i][digit]
        i+=1
    return outList


def generateLists(rawList):
    masterList = [""]*5
    for i in range(5):
        masterList[i] = getDigitList(rawList, i)
    return masterList

l = generateLists(rawList)

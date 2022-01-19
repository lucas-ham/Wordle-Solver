from words import rawList
from generateDictionary import getDigitList
from generateDictionary import generateLists


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
                return outq
            else:
                if (x < out[i]):
                    run = False
                elif (x == out[i]):
                    run == False
                    i += 1
                elif (x > out[i]):
                    out.pop(i)
    return out

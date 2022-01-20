from words import rawList
from generateDictionary import *
from searchByLetters import *

masterList = generateLists(rawList)


class letterStorage():
    def __init__(self, letter, digit):
        self.let = letter
        self.digit = digit

def wordCollector(color):
    if (color == 0):
        print("Please input all green letters \n Use the format 'Letter, Number' to input these values \n For example, if you had found the 'A' in Apple, you would write 'A,1'\n When you have entered all green letters, please enter an empty line (ie '') \n")
    elif (color == 1):
        print("Please input all yellow letters \n Use the format 'Letter, Number' to input these values \n For example, if you had found the 'A' in Apple, you would write 'A,1'\n When you have entered all yellow letters, please enter an empty line (ie '') \n")
    else:
        print("Please input all grey letters \n Use the format 'Letter, Number' to input these values \n For example, if you had found the 'A' in Apple, you would write 'A,1'\n When you have entered all grey letters, please enter an empty line (ie '') \n")
    i = 0
    letterList = []
    while i < 5:
        value = input("Please Enter Your Letter and Digit:     ")
        if (value == ""):
            break
        elif (value == "quit"):
            return None
        elif (len(value) != 3):
            print("Please make sure you followed the formatting correctly, including looking for extra spaces!")
            continue
        elif (value[1] == ","):
            letter = value[0]
            digit = value[2]
            if (not letter.isalpha()):
                print("Please make sure you only enter valid characters")
                continue
            elif (not digit.isnumeric()):
                print("Please make sure you entered a valid number 1-5")
                continue
            else:
                digit = int(digit)
                letterList.append(letterStorage(letter, digit - 1))
                i += 1
    return letterList

def parseGreen(rawList, greenList):
    if greenList:
        if len(greenList) > 0:
            possibles = searchKnownDigit(rawList, masterList, greenList[0].let, greenList[0].digit)
        else:
            return []
        if len(greenList) > 1:
            i = 1
            while i < len(greenList):
                possibles = addWordsWithDigit(rawList, masterList, possibles, greenList[i].let, greenList[i].digit)
                i+=1
        return possibles

def yellowInitSearch(rawList, yellowLet):
    possibles = []
    for i in range(5):
        if i == yellowLet.digit:
            continue
        else:
            possibles += (searchKnownDigit(rawList, masterList, yellowLet.let, i))
    return possibles

def yellowAddWord(rawList, masterList, possibles, yellowLet):
    out = []
    for i in range(5):
        if i == yellowLet.digit:
            continue
        else:
            out += (addWordsWithDigit(rawList, masterList, possibles, yellowLet.let, i))
    return out

def parseYellow(rawList, yellowList):
    if yellowList:
        if (len(yellowList) > 0):
            possibles = yellowInitSearch(rawList, yellowList[0])
        else:
            return []
        if (len(yellowList) > 1):
            i = 1
            while i < len(yellowList):
                possibles = yellowAddWord(rawList, masterList, possibles, yellowList[i])
                i += 1
        return possibles

def parseGrey(rawList, possibles, greyList):
    if greyList:
        for let in greyList:
            possibles = removeWords(rawList, possibles, let.let)
        return possibles

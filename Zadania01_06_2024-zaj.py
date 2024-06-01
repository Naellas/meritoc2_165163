"""
print(======================================1==================================)
print()
print(=========================================================================)

def countAverage(list):
    sum = 0
    for x in list:
        print(x)
        sum += int(x)

    avg = sum / len(list)
    return avg

    

inputlist = input("Insert numbers split by ,").split(',')
print("Average: ", countAverage(inputlist))

def Size(a,b):
    return int(a)*int(b)
a = input("Length of 1 side: ")
b = input("Length of 2nd side: ")
print("a*b = ", Size(a,b))

import random
randomNumber = random.randint(1,6)
print(randomNumber)




def findEven(list):
    numOfEven = 0
    for x in list:
        if int(x)%2==0:
            print(x)
            numOfEven += 1
    return(numOfEven)
        

inputList = input("Insert numbers split by ',': ").split(',')
print("Quantity of even numbers:", findEven(inputList))

def inputNumbers():
    sum = 0
    numberOfNumbers = 0
    while sum <= 99:
        number = int(input("Please type in next number: "))
        sum+=number
        numberOfNumbers += 1
        print(sum)
    return(numberOfNumbers)

print("Amount of inserted numbers: ", inputNumbers())


def appendToList():
    list = []
    numOfEven = 0
    for x in range(10):
        nextNum = int(input("Please insert next number: "))
        list.append(nextNum)
        if int(nextNum)%2 == 0:
            numOfEven +=1
    print(list, numOfEven)

appendToList()

"""
import random

def createNNumberList(n):
    list = []
    modifiedList = []
    for x in range(n):
        list.append(random.randint(1,50))
    print("Unmodified list: ", list)
    for x in list:
        if x >=20 or x <= 11:
            modifiedList.append(x)
    print("Modified list: ", modifiedList)

numOfItems = int(input("Insert number of items: "))
createNNumberList(numOfItems)
        

        
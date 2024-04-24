"""
print("=========================================1==========================================")
print("Adding items within a list")
print("====================================================================================")
def ListSum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


NumberOfItemsInList1 = int(input("How many numbers would you like in your list? "))
NumberList1 = [None] * NumberOfItemsInList1
for n in range(NumberOfItemsInList1):
    print("Please input ", n+1, " number: ")
    NumberList1[n] = int(input())

print("Adding all items in list results in: ", ListSum(NumberList1))

print("=========================================2==========================================")
print("Multiplying items within a list")
print("====================================================================================")
def ListMultiply(numbers):
    total = 1
    for n in numbers:
        total = total*n
    return total


NumberOfItemsInList2 = int(input("How many numbers would you like in your list? "))
NumberList2 = [None] * NumberOfItemsInList2
for n in range(NumberOfItemsInList2):
    print("Please input ", n+1, " number: ")
    NumberList2[n] = int(input())

print("Multiplying all items in list results in: ", ListMultiply(NumberList2))

print("=========================================3==========================================")
print("Finding largest item within a list")
print("====================================================================================")
NumberOfItemsInList3 = int(input("How many numbers would you like in your list? "))
NumberList3 = [None] * NumberOfItemsInList3

for n in range(NumberOfItemsInList3):
    print("Please input ", n+1, " number: ")
    NumberList3[n] = int(input())

def FindLargest(Number):
    largest = NumberList3[0]
    for n in NumberList3:
        if largest < int(n):
            largest = n
    return largest

print("Largest item in your list is: ", FindLargest(NumberList3))

print("=========================================17==========================================")
print("Finding if list is consisted of prime numbers")
print("====================================================================================")
def ReturnIfAllPrime(NumbersList4_1):
    return all(FindPrimeNumbers(n) for n in NumbersList4_1)

def FindPrimeNumbers(Numbers):
    if Numbers == 1:
        return False
    elif Numbers == 2: 
        return True
    else:  
        for n in range(2, Numbers):
            if (Numbers % n == 0):
                return False
        return True
    
NumberOfItemsInList4 = int(input("How many numbers would you like in your list? "))
NumberList4 = [None] * NumberOfItemsInList4

for n in range(NumberOfItemsInList4):
    print("Please input ", n+1, " number: ")
    NumberList4[n] = int(input())

if ReturnIfAllPrime(NumberList4) == True:
    print("Your list: ", NumberList4, " consists only of prime numbers.")
else:
    print("Your list: ", NumberList4, " consists not only of prime numbers.")

print("=========================================21==========================================")
print("Converting a list of characters into a string")
print("====================================================================================")
        
def ConvertToString(ListOfCharacters):
    String21 = ''.join(ListOfCharacters)
    return String21

NumberOfItemsInList4 = int(input("How many numbers would you like in your list? "))
CharacterList21 = [None] * NumberOfItemsInList4

for n in range(NumberOfItemsInList4):
    print("Please input ", n+1, " character: ")
    CharacterList21[n] = input()

print("Character list: ", CharacterList21, "has been converted to following string: ", ConvertToString(CharacterList21))

"""
print("=========================================21==========================================")
print("Converting a list of characters into a string")
print("====================================================================================")
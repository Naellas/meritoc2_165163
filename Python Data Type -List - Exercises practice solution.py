
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

NumberOfItemsInList5 = int(input("How many numbers would you like in your list? "))
CharacterList21 = [None] * NumberOfItemsInList5

for n in range(NumberOfItemsInList5):
    print("Please input ", n+1, " character: ")
    CharacterList21[n] = input()

print("Character list: ", CharacterList21, "has been converted to following string: ", ConvertToString(CharacterList21))

print("=========================================32==========================================")
print("Checking if a list contains a sublist")
print("====================================================================================")

def CheckIfListContainsSublist(ListA, ListB):
    for i in range(len(ListA)):
        if ListA[i:i+len(ListB)] == ListB:
            return True
    return False
                
NumberOfItemsInList6 = int(input("How many numbers would you like in your list? "))
List32 = [None] * NumberOfItemsInList6

for n in range(NumberOfItemsInList6):
    print("Please input ", n+1, " character: ")
    List32[n] = input()

NumberOfItemsInSubList6 = int(input("How many numbers would you like in your sublist? "))
SubList32 = [None] * NumberOfItemsInSubList6

for n in range(NumberOfItemsInSubList6):
    print("Please input ", n+1, " character: ")
    SubList32[n] = input()
    
print("Your list: ", List32, ". Provided Sublist: ", SubList32)

if CheckIfListContainsSublist(List32, SubList32) == False:
    print("Provided sublist is not a sublist of your list")
else:
    print("Provided sublist is a sublist of your list")


print("=========================================35==========================================")
print("Create a list by concatenating a given list with range 1 to n")
print("====================================================================================")

def ConcatenateList(InputList, InputRange):
    NewList = []
    for char in InputList:
        for x in range(InputRange):
            NewList.append(char + str(x+1))
    return NewList

NumberOfItemsInList35 = int(input("Please type in amount of characters in your list: "))

List35 = [''] * NumberOfItemsInList35

for n in range(NumberOfItemsInList35):
    print("Please input ", n+1, " character: ")
    List35[n] = input()

InputRange = int(input("Please input how many elements should be created for each element in your list: "))

print(ConcatenateList(List35, InputRange))

print("=========================================46==========================================")
print("Select odd items from the list")
print("====================================================================================")

def SelectOddNumbers(InputList):
    NewList = InputList[::2]
    return NewList

NumberOfItemsInList46 = int(input("Please type in amount of characters in your list: "))

List46 = [''] * NumberOfItemsInList46

for n in range(NumberOfItemsInList46):
    print("Please input ", n+1, " character: ")
    List46[n] = input()

print("Odd items within ", List46, " : ", SelectOddNumbers(List46))

print("=========================================52==========================================")
print("Compute difference between two lists")
print("====================================================================================")

def ComputeListDifference(ListA, ListB):
    List1_List2 = []
    List2_List1 = []
    for item in ListA:
        if item not in ListB:
            List1_List2.append(item)
    for item in ListB:
        if item not in ListA:
            List2_List1.append(item)
    return [List1_List2, List2_List1]

NumberOfItemsInList1 = int(input("Please type in the number of items in your first list: "))
List1 = []
for n in range(NumberOfItemsInList1):
    print("Please input item", n+1, ": ")
    List1.append(input())

NumberOfItemsInList2 = int(input("Please type in the number of items in your second list: "))
List2 = []
for n in range(NumberOfItemsInList2):
    print("Please input item", n+1, ": ")
    List2.append(input())

difference = ComputeListDifference(List1, List2)
List1_List2 = difference[0]
List2_List1 = difference[1]
print("List1 - List2: ", List1_List2)
print("List2 - List1: ", List2_List1)



print("=========================================66==========================================")
print("Finding all numbers greater than x within the list")
print("====================================================================================")

def FindGreaterNumbers(InputList, Number):
    GreaterList = []
    for x in range(len(InputList)):
        if int(InputList[x]) > int(Number):
            GreaterList.append(InputList[x])
    return GreaterList

NumberOfItemsInList66 = int(input("Please type in the number of items in your list: "))
List66 = []
for n in range(NumberOfItemsInList66):
    print("Please input item", n+1, ": ")
    List66.append(input())

Number66 = int(input("Please say above which number you would like to retrieve items from the list: "))

print("Provided list: ", List66, ". Numbers that are greater than ", Number66, "Within that list: ", FindGreaterNumbers(List66, Number66))


print("=========================================84==========================================")
print("Round numbers in given list, print minimum and maximum value and multiply the results by 5. Print numbers in ascending order separated by space")
print("====================================================================================")

def RoundNumbers(InputList):
    RoundedList = []
    for x in InputList:
        Number = float(x)
        RoundedList.append(round(Number))
    return RoundedList

NumberOfItemsInList84 = int(input("Please type in the number of items in your list: "))
List84 = []
for n in range(NumberOfItemsInList84):
    print("Please input item", n+1, ": ")
    List84.append(input())

RoundedList84 = RoundNumbers(List84)

print("Provided list: ", List84, "has been rounded: ", RoundedList84)

Maximum = RoundedList84[0]
Minimum = RoundedList84[0]
MultipliedRoundedList = RoundedList84

for n in range(len(RoundedList84)):
    if RoundedList84[n] > Maximum:
        Maximum = RoundedList84[n]
    elif RoundedList84[n] < Minimum:
        Minimum = RoundedList84[n]
    MultipliedRoundedList[n] = RoundedList84[n]*5

SortedMultipliedRoundedList = sorted(MultipliedRoundedList)

print("Maximum within rounded list: ", Maximum, ". Minimum within rounded list: ", Minimum, ".")
print("Rounded numbers multiplied by 5 and sorted: ")
for Number in SortedMultipliedRoundedList:
    print(Number, end=" ")


print("=========================================190==========================================")
print("Find specified number of largest products from two given lists multiplying an element from each list")
print("====================================================================================")

def FindLargestProductsFromTwoLists(ListA, ListB):
    LargestList = []
    for x in ListA:
        for y in ListB:
            LargestList.append(int(x)*int(y))
    return LargestList

NumberOfItemsInList1 = int(input("Please type in the number of items in your first list: "))
List1 = []
for n in range(NumberOfItemsInList1):
    print("Please input item", n+1, ": ")
    List1.append(input())

NumberOfItemsInList2 = int(input("Please type in the number of items in your second list: "))
List2 = []
for n in range(NumberOfItemsInList2):
    print("Please input item", n+1, ": ")
    List2.append(input())

XLargestItems = int(input("Please type in how many largest items should be found: "))

SortedLargestList = sorted(FindLargestProductsFromTwoLists(List1, List2), reverse=True)
SortedLargestListSelectedAmount = []
for x in range(XLargestItems):
    SortedLargestListSelectedAmount.append(SortedLargestList[x])

print("All items within provided lists were multiplied. Largest items to provided quantity are: ", SortedLargestListSelectedAmount)


print("=========================================129==========================================")
print("Find specified number of largest products from two given lists multiplying an element from each list")
print("At this stage user input has been abandoned due to time crunch, however this still could be done")
print("====================================================================================")

def reverse_lists(ListA):
    return [sublist[::-1] for sublist in ListA]

ListA = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
reversed_list = reverse_lists(ListA)
print("Original list of lists:")
print(ListA)
print("Reverse each list in the said list of lists:")
print(reversed_list)


print("=========================================131==========================================")
print("Count the frequency of consecutive duplicate elements in a list of numbers")
print("====================================================================================")

def consecutive_duplicates(ListA):
    Freq = {}
    prev = None
    for item in ListA:
        if item == prev:
            Freq[item] = Freq.get(item, 1) + 1
        Prev = item
    return Freq

OriginalList131 = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
result = consecutive_duplicates(ListA)
print("Original lists:")
print(ListA)
print("Consecutive duplicate elements and their frequency:")
print(result)



print("=========================================127==========================================")
print("Remove words from a list of strings containing a character or string")
print("====================================================================================")

def remove_words(ListA, Characters):
        return [' '.join(word for word in sentence.split() if all(char not in word for char in Characters)) for sentence in ListA]



OriginalList127 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
Characters = ['#', 'color', '@']
NewList127 = remove_words(OriginalList127, Characters)
print("Original list:")
print(OriginalList127)
print("Character list:")
print(Characters)
print("New list:")
print(NewList127)

print("=========================================130==========================================")
print("Write a Python program to count the same pair in three given lists.")
print("====================================================================================")


def CountSamePairs(List1, List2, List3):
    return sum(1 for a, b, c in zip(List1, List2, List3) if a == b == c)

List1 = [1, 2, 3, 4, 5, 6, 7, 8]
List2 = [2, 2, 3, 1, 2, 6, 7, 9]
List3 = [2, 1, 3, 1, 2, 6, 7, 9]
SamePairs = CountSamePairs(List1, List2, List3)
print("Provided lists: ", List1, List2, List3)
print("Number of same pairs in the three given lists:", SamePairs)

print("=========================================181==========================================")
print("Write a Python program to iterate a given list cyclically at a specific Index position.")
print("====================================================================================")

def CyclicIteration(ListA, Index):
    Index = Index % len(ListA)
    return ListA[Index:] + ListA[:Index]


ListA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Index = 3
print("Original list:")
print(ListA)
print("Iterate the said list cyclically on specific Index position", Index, ":")
print(CyclicIteration(ListA, Index))

Index = 5
print("Iterate the said list cyclically on specific Index position", Index, ":")
print(CyclicIteration(ListA, Index))

print("=========================================181==========================================")
print("Write a Python program to iterate a given list cyclically at a specific Index position.")
print("====================================================================================")

def find_max_min(ListA, ListB, ListC):
    MaximumValue = max(max(ListA), max(ListB), max(ListC))
    MinimumValue = min(min(ListA), min(ListB), min(ListC))
    return MaximumValue, MinimumValue

ListA = [2, 3, 5, 8, 7, 2, 3]
ListB = [4, 3, 9, 0, 4, 3, 9]
ListC = [2, 1, 5, 6, 5, 5, 4]

MaximumValue, MinimumValue = find_max_min(ListA, ListB, ListC)
print("Provided lists: ", ListA, ListB, ListC)
print("Maximum value of the said three lists:", MaximumValue)
print("Minimum value of the said three lists:", MinimumValue)

print("=========================================214==========================================")
print("Write a Python program to sort a given positive number in descending/ascending order.")
print("====================================================================================")

def sort_number(Number):

    Digits = [int(Digit) for Digit in str(Number)]
    

    DescendingOrder = int(''.join(map(str, sorted(Digits, reverse=True))))
    AscendingOrder = int(''.join(map(str, sorted(Digits))))
    
    return DescendingOrder, AscendingOrder

OriginalNumber = 134543
Descending, Ascending = sort_number(OriginalNumber)
print("Original Number:", OriginalNumber)
print("Descending order of the said number:", Descending)
print("Ascending order of the said number:", Ascending)

print("=========================================66==========================================")
print("Write a Python program to find the list in a list of lists whose sum of elements is the highest.")
print("====================================================================================")

def FindMaxSumList(Lists):
    MaxSum = float('-inf')
    max_list = []

    for Sublist in Lists:
        current_sum = sum(Sublist)
        if current_sum > MaxSum:
            MaxSum = current_sum
            max_list = Sublist

    return max_list

ListA = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

MaxSumList = FindMaxSumList(ListA)

print("Sample lists:", ListA)
print("List with the highest sum of elements:", MaxSumList)
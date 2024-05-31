"""
print("=========================================1==========================================")
print("Finding maximum of three numbers")
print("====================================================================================")

def FindMaxNumber(Number1, Number2, Number3):
    Max1 = Number1
    if(Number2 > Max1):
        Max1 = Number2
    if(Number3 > Max1):
        Max1 = Number3
        
    return Max1

Num1 = input("Please type in 1st number to compare: ")
Num2 = input("Please type in 2nd number to compare: ")
Num3 = input("Please type in 3rd number to compare: ")

MaxProvided = FindMaxNumber(Num1, Num2, Num3)
print("Maximum number from provided ones is: ", MaxProvided)


print("=========================================2==========================================")
print("Sum all numbers in a list")
print("====================================================================================")

List2 = input("Please input numbers separated by , to be inserted into list: ")

def SumItemsInList(List):
    NumberList = [int(count2) for count2 in List.split(",")]
    Total = 0
    for x in NumberList:
        Total = Total+x
    return Total

MultipliedTotal = SumItemsInList(List2)

print("Your multiplication result is: ", MultipliedTotal)


print("=========================================3==========================================")
print("Multiply all numbers in a list")
print("====================================================================================")

List3 = input("Please input numbers separated by , to be inserted into list: ")

def MultiplyItemsInList(List):
    NumberList = [int(count3) for count3 in List.split(",")]
    Total = 1
    for x in NumberList:
        Total = Total*x
    return Total

MultipliedTotal = MultiplyItemsInList(List3)

print("Your multiplication result is: ", MultipliedTotal)

print("=========================================4==========================================")
print("Reverse a string")
print("====================================================================================")

String4 = input("Please type in string to be reversed: ")

def ReverseString(StringToReverse):
    ReversedString = []
    for x in range(len(StringToReverse)):
        ReversedString.append(StringToReverse[len(StringToReverse)-1-x]) 
    return ReversedString

ResultString4 = "".join(ReverseString(String4))
print("Your reversed string is: ", ResultString4)


print("=========================================5==========================================")
print("Calculate factorial of a number (non-negative)")
print("====================================================================================")

Integer5 = int(input("Please type in the integer to find factorial for: "))

def CalculateFactorial(Factorial):
    Result = 1
    if Factorial == 0:
        return 1
    else:
        return Factorial*CalculateFactorial(Factorial-1)
            
print("Factorial for provided number is: ", CalculateFactorial(Integer5))


print("=========================================6==========================================")
print("Find if number within range")
print("====================================================================================")

RangeStart = input("Please type in range start: ")
RangeEnd = input("Please type in range end: ")
Number6 = input("Please provide number to be checked for range: ")

def FindIfInRange(RangeStart, RangeEnd, Number):
    if (Number > RangeStart and Number < RangeEnd) or (Number < RangeStart and Number > RangeEnd):
        return True
    else:
        return False
    
if FindIfInRange(RangeStart, RangeEnd, Number6) == True:
    print("Provided number: ", Number6, "is within range: ", RangeStart, ", ", RangeEnd)
else:
    print("Provided number: ", Number6, "is not within range: ", RangeStart, ", ", RangeEnd)

print("=========================================7==========================================")
print("Count upper and lower case letters within string")
print("====================================================================================")

String7 = input("Please type in string to count upper and lower case letters: ")

def CountUpperLowerCase(StringToCheck):
    UpperCase = 0
    LowerCase = 0
    OtherCharacters = 0
    for x in range(len(StringToCheck)):
        if StringToCheck[x].isupper():
            UpperCase += 1
        elif StringToCheck[x].islower():
            LowerCase += 1
        else:
            OtherCharacters +=1
    Result = [UpperCase, LowerCase, OtherCharacters]
    return Result

ResultList7 = CountUpperLowerCase(String7)

print("Upper case: ", ResultList7[0], "Lower case: ", ResultList7[1], "Other characters: ", ResultList7[2])

print("=========================================8==========================================")
print("Create a new list with distinct items from first list.")
print("====================================================================================") 

List8 = input("Please input numbers separated by , to be inserted into list: ")

def DistinctItems(List):
    CharactersList = [int(count2) for count2 in List.split(",")]
    UniqueList = [len(CharactersList)]
    for x in range(len(CharactersList)):
        print(CharactersList[x])
        if CharactersList[x] not in UniqueList:
            UniqueList.append(CharactersList[x])
    return UniqueList

print("Unique entities within provided list: ", DistinctItems(List8))

print("=========================================9==========================================")
print("Find prime number")
print("====================================================================================")

Number9 = input("Please input number to be checked if prime: ")

def FindPrimeNumber(Number):
    isPrime = True
    for x in range(int(Number)-1):
        if(x>1):
            if(int(Number) % x == 0):
                isPrime = False
    return isPrime

if(FindPrimeNumber(Number9) == True):
    print("Your number: ", Number9, " is a prime number.")
else:
    print("Your number: ", Number9, " is NOT a prime number.")


print("=========================================10==========================================")
print("Find even numbers: ")
print("====================================================================================")

List10 = input("Please input numbers separated by , to be inserted into list: ")

def FindEvenNumbers(List):
    NumberList = [int(count10) for count10 in List.split(",")]
    EvenNumbers = []
    for x in NumberList:
        if(x % 2 == 0):
            EvenNumbers.append(x)
    return EvenNumbers

print("Your even numbers are: ", FindEvenNumbers(List10))

print("=========================================11==========================================")
print("Finding perfect number: ")
print("====================================================================================")

def FindPerfectNumber(n):
    if n < 1:
        return False

    Divisors = [i for i in range(1, n) if n % i == 0]
    
    SumOfDivisors = sum(Divisors)
    
    return SumOfDivisors == n

Number11 = int(input("Please input number to be checked if it is perfect: "))

if(FindPerfectNumber(Number11)==True):
    print("Number: ", Number11, " is perfect!")
else:
    print("Number: ", Number11, " is NOT perfect!")


print("=========================================12==========================================")
print("Find if a passed string is palindrome or not")
print("====================================================================================")

String12 = input("Please insert string to be verified: ")

def CheckIfPalindrome(PalindromeString):
    CheckResult = False
    for x in range(len(PalindromeString)):
        if(PalindromeString[x] == PalindromeString[len(PalindromeString)-1-x]):
            CheckResult = True
        else:
            CheckResult = False
            break
    return CheckResult

if(CheckIfPalindrome(String12) == True):
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")



print("=========================================13==========================================")
print("Write a  Python function that prints out the first n rows of Pascal's triangle.")
print("====================================================================================")

def GeneratePascalsTriangle(RowsCount):
    if RowsCount <= 0:
        return []
    
    PascalTriangle = [[1]]
    
    for i in range(1, RowsCount):
        PreviousRow = PascalTriangle[-1]
        NewRow = [1]
        for j in range(1, i):
            NewRow.append(PreviousRow[j-1] + PreviousRow[j])
        NewRow.append(1)
        PascalTriangle.append(NewRow)
    
    return PascalTriangle

RowsCount = int(input("Please enter the number of rows for Pascal's triangle: "))
PascalsTriangle = GeneratePascalsTriangle(RowsCount)
for Row in PascalsTriangle:
    print(Row)

print("=========================================14==========================================")
print("Write a Python function to check whether a string is a pangram or not.")
print("====================================================================================")

def CheckIfPangram(PangramString):
    AlphabetSet = set("abcdefghijklmnopqrstuvwxyz")
    PangramStringSet = set(PangramString.lower())
    
    return AlphabetSet.issubset(PangramStringSet)

String12 = input("Please insert string to be verified: ")

if CheckIfPangram(String12):
    print("Your string is a pangram")
else:
    print("Your string is not a pangram")

print("=========================================15==========================================")
print("Write a  Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.")
print("====================================================================================")

def SortHyphenSeparatedWords(HyphenSeparatedString):
    WordsList = HyphenSeparatedString.split('-')
    SortedWordsList = sorted(WordsList)
    SortedHyphenSeparatedString = '-'.join(SortedWordsList)
    return SortedHyphenSeparatedString

HyphenSeparatedString = input("Please insert a hyphen-separated sequence of words: ")
SortedString15 = SortHyphenSeparatedWords(HyphenSeparatedString)
print("Sorted hyphen-separated sequence:", SortedString15)
"""
print("=========================================16==========================================")
print("Write a  Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).")
print("====================================================================================")

def GenerateSquaresList():
    SquaresList = [x**2 for x in range(1, 31)]
    return SquaresList

SquaresList = GenerateSquaresList()
print("List of squares from 1 to 30:", SquaresList)

print("=========================================17==========================================")
print("Write a Python program to create a chain of function decorators (bold, italic, underline etc.).")
print("====================================================================================")

def bold(func):
    def wrapper(text):
        return "<b>" + func(text) + "</b>"
    return wrapper

def italic(func):
    def wrapper(text):
        return "<i>" + func(text) + "</i>"
    return wrapper

def underline(func):
    def wrapper(text):
        return "<u>" + func(text) + "</u>"
    return wrapper

# Define the function to display text
def display_text(text):
    return text

# Apply the decorators manually
display_text = bold(italic(underline(display_text)))

TextToDisplay = input("Please enter the text to be styled: ")
print("Styled text:", display_text(TextToDisplay))

print("=========================================18==========================================")
print("Write a Python program to execute a string containing  Python code.")
print("====================================================================================")

CodeString = input("Please enter the Python code to execute: ")

# Execute the code string
try:
    exec(CodeString)
except Exception as e:
    print(f"An error occurred: {e}")

print("=========================================19==========================================")
print("Write a Python program to access a function inside a function.")
print("====================================================================================")

def outer_function():
    def inner_function():
        print("This is the inner function.")
    
    print("This is the outer function.")
    inner_function()  # Call the inner function

# Call the outer function
outer_function()

print("=========================================20==========================================")
print("Write a  Python program to detect the number of local variables declared in a function.")
print("====================================================================================")

def CountVariables():
    x = 5
    y = 6
    String1 = "This is a test string for a variable assignment"

print(CountVariables.__code__.co_nlocals) 

print("=========================================21==========================================")
print("Write a Python program that invokes a function after a specified period of time.")
print("====================================================================================")
import time
import math

def invoke_after_delay(delay_ms, func):
    time.sleep(delay_ms / 1000) 
    func()

def calculate_square_root():
    numbers = [4, 100, 25000]
    for number in numbers:
        print(math.sqrt(number))

delay_ms = int(input("Specify time delay in miliseconds: "))

print("Square root after specific milliseconds:")
invoke_after_delay(delay_ms, calculate_square_root)
"""
print("=========================================1==========================================")
StringToCheckLength = input("Enter string which you want to check: ")
print("Your string length is:")
print(len(StringToCheckLength))

print("=========================================2==========================================")
String2 = input("Please type in string to check character frequency: ")
SplitString2Count = dict()

for Character in String2:
    if Character in SplitString2Count:
        SplitString2Count[Character] += 1
    else:
        SplitString2Count[Character] = 1

print(SplitString2Count)

print("=========================================3==========================================")
StringToSplit3 = input("Enter string to be split - first 2 and last 2 characters will be retrieved:")
if len(StringToSplit3)>2 :
    print(StringToSplit3[:2] + StringToSplit3[-2:])
else:
    print("String is too short")
print("=========================================4==========================================")
StringToModify4 = input ("Enter string for which the first letter will be replaced in further occurences:")
LetterToChange4 = StringToModify4[0]
ModifiedString = ""
for i in range(len(StringToModify4)):
    if i!=0 and StringToModify4[i] == LetterToChange4:
        ModifiedString += "$"
    else:
        ModifiedString += StringToModify4[i]
print(ModifiedString)
print("=========================================5==========================================")
String1_5 = input("Insert first string: ")
String2_5 = input("Insert second string: ")
String2_5_1 = String1_5[:2] + String2_5[2:]
String1_5_1 = String2_5[:2] + String1_5[2:]
print(String1_5_1 + " " + String2_5_1)

print("=========================================6==========================================")
String6 = input("Insert string to check: ")
if String6[-3:] == "ing":
    print(String6 + "ly")
else:
    print(String6 + "ing")

print("=========================================7==========================================")
String7 = input("Please insert not poor string: ")

s7not = String7.find("not")
s7poor = String7.find("poor")
if(s7poor > s7not and s7not > 0 and s7poor > 0):
    String7 = String7.replace(String7[s7not:(s7poor+4)], 'good')
    print(String7)
else:
    print("String did not include not nor poor")

print("=========================================8==========================================")
Array8 = []
n = int(input("Enter number of elements: "))
for i in range(n):
    Word8 = input("Please insert your word into the array: ")
    Array8.append((len(Word8), Word8))

Array8.sort()
print("Longest word: " + Array8[-1][1] + " with length: " + str(Array8[-1][0]))

print("=========================================9==========================================")
Word9 = input("Please insert word from which you want to remove a character: ")
Index9 = int(input("Which letter from within you want to remove (number of the letter): "))
FirstPart9 = Word9[:Index9]
LastPart9 = Word9[Index9+1:]
print(FirstPart9 + LastPart9)

print("========================================10==========================================")
Word10 = input("Please insert word to swap the last letters from: ")
Word10Length = len(Word10)
Word10New = Word10[Word10Length-1:Word10Length] + Word10[1:Word10Length-1] + Word10[0:1]
print(Word10New)

print("========================================11==========================================")
Word11 = input("Please type in a word to extract every even index letter: ")
Word11New = Word11[0::2]
print(Word11New)

print("========================================12==========================================")
Sentence12 = input("Please type in the sentence: ")

Sentence12WordCount = dict()

Sentence12Words = Sentence12.split()

for word in Sentence12Words:
    if word in Sentence12WordCount:
        Sentence12WordCount[word] += 1
    else:
        Sentence12WordCount[word] = 1

print(Sentence12WordCount)

print("========================================13==========================================")
String13 = input("Please type in string to convert to lowercase: ")

print(String13.lower())

print("========================================14==========================================")
String14 = input("Please type in comma separated values into a string so that they are split and sorted alphabetically: ")
String14Split = String14.split(",")
print(sorted(String14Split))

print("========================================15==========================================")
def AddHTMLTags15(Char15, String15):
    NewString = "<" + Char15 + ">" + String15 + "</" + Char15 + ">"
    return NewString

InputChar15 = input("Please type in the HTML tag character to be inserted: ")
InputString15 = input("Please type in the text inside HTML tag: ")

print(AddHTMLTags15(InputChar15, InputString15))

print("========================================16==========================================")    
def InsertStringMiddle16(String16, String16_2):
    NewString16 = String16[:int(len(String16)/2)] + String16_2 + String16[int(len(String16)/2):]
    return(NewString16)

InputString16 = input("Please type in what you would like to put your string in between: ")
InputString16_2 = input("Please type in string to be inserted: ")

print(InsertStringMiddle16(InputString16, InputString16_2))

print("========================================17==========================================")    

def CreateStringFromLastLetters(String17, MultiplyValue17):
    NewString17 = String17[-2:] * max(int(MultiplyValue17),1)
    return NewString17

StringToExtractLastLetters17 = input("Please type in string from which last 2 letters will be extracted to create a new string: ")
MultiplyLastLettersValue17 = input("Please type in how many times you would like to multiply the last 2 letters of the string (negative values and 0 will be converted to 1): ")

print(CreateStringFromLastLetters(StringToExtractLastLetters17, MultiplyLastLettersValue17))

print("========================================18==========================================")    
def CreateStringFromFirstTreeCharacters18(InputString18):
    if len(InputString18) >= 3:
        NewString18 = InputString18[:3]
        return NewString18
    else:
        return InputString18

String18 = input("Please type in string to create new string from its first 3 characters. If string is shorter than 3, entire string will be returned: ")

print(CreateStringFromFirstTreeCharacters18(String18))
"""
print("========================================19==========================================")   
def ReduceStringUntilCertainCharacter19(InputString19, InputSeparator19):
    n = 0
    NewString19 = str()
    while InputString19[n] != Separator19:
        NewString19 += InputString19[n]
        n += 1
    return NewString19

String19 = input("Please type in the string to be displayed before separator: ")
Separator19 = input("Please type in separator until which string will be displayed: ")

print(ReduceStringUntilCertainCharacter19(String19, Separator19))

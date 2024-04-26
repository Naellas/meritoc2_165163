print("=========================================1==========================================")
print("Write a Python script to sort (ascending and descending) a dictionary by value.")
print("====================================================================================")

Dictionary1 = {1: 5, 9: 7, 5: 9, 3: 3, 7: 12}

print("Original dictionary: ", Dictionary1)

SortedDictionary1 = sorted(Dictionary1.items())

print("Sorted dictionary - ascending: ", SortedDictionary1)

SortedDictionary1 = sorted(Dictionary1.items(), reverse = True)

print("Sorted dictionary - descending: ", SortedDictionary1)

print("=========================================2==========================================")
print("Add key to existing dictionary")
print("====================================================================================")

Dictionary2 = {0:10, 1:20, 2:40}
print("Original dictionary: ", Dictionary2)
Dictionary2[3] = 60
print("Dictionary with added key: ", Dictionary2)
Dictionary2.update({4:80})
print("Dictionary with alternatively added key: ", Dictionary2)

print("=========================================3==========================================")
print("Concatenating dictionaries")
print("====================================================================================")

Dictionary3_1 = {1:10, 2:20}
Dictionary3_2 = {3:40, 4:60}
Dictionary3_3 = {5:80, 6:100}

print("Original dictionaries: ", Dictionary3_1, Dictionary3_2, Dictionary3_3)

ConcatenatedDictionary3 = {}

for Record in (Dictionary3_1, Dictionary3_2, Dictionary3_3):
    ConcatenatedDictionary3.update(Record)

print("Concatenated dictionary: ", ConcatenatedDictionary3)

print("=========================================4==========================================")
print("Write a Python script to check whether a given key already exists in a dictionary.")
print("====================================================================================")

Dictionary4 = {0:10, 1:20, 2:40}
print("Entire dictionary: ", Dictionary4)
SearchedKey4 = int(input("What key number are you looking for in dictionary? "))

if SearchedKey4 in Dictionary4:
    print("Key found in dictionary")
else:
    print("Key not found")

print("=========================================5==========================================")
print("Write a Python program to iterate over dictionaries using for loops.")
print("====================================================================================")

Dictionary5 = {'x':1, 'y':5, 'z':10, 'p': 15}
print("Dictionary: ", Dictionary5)
for Key, Value in Dictionary5.items():
    print(Key, " - ", Value)

print("=========================================7==========================================")
print("Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.")
print("====================================================================================")

Dictionary6 = {}

for Number in range(1,16):
    Dictionary6[Number] = Number ** 2

print("Created dictionary: ", Dictionary6)

print("=========================================18==========================================")
print("Write a Python program to check if a dictionary is empty or not.")
print("====================================================================================")
print("Dictionary has been initialized here!")
Dictionary18 = {}
if not bool(Dictionary18):
    print("Dictionary is empty")
else:
    print("Dictionary is not empty: ", Dictionary18)

print("=========================================19==========================================")
print("Write a Python program to combine two dictionary by adding values for common keys.")
print("====================================================================================")

Dictionary19_1 = {'a': 100, 'b': 200, 'c':300}
Dictionary19_2 = {'a': 300, 'b': 200, 'd':400}
SummedDictionary19 = {}

for key, value in Dictionary19_1.items():
    if key in Dictionary19_2:
        SummedDictionary19[key] = Dictionary19_1[key] + Dictionary19_2[key]
    else:
        SummedDictionary19[key] = Dictionary19_1[key]

for key, value in Dictionary19_2.items():
    if key not in Dictionary19_1:
        SummedDictionary19[key] = Dictionary19_2[key]

print(SummedDictionary19)

print("=========================================26==========================================")
print("Write a Python program to combine two dictionary by adding values for common keys.")
print("====================================================================================")

Dictionary26 = {'a': [1, 2, 3], 'b': [4, 5]}
print("Original dictionary: ", Dictionary26)

for key, value in Dictionary26.items():
    print(len(value))



print("=========================================32==========================================")
print("Write a Python program to print a dictionary line by line.")
print("====================================================================================")

Dictionary32 = {'Alex' : {'Grade' : 10, 'DOB': 1999}, 'Sophia' : {'Grade' : 6, 'DOB': 2001}}
print("Original dictionary: ", Dictionary32)
for key32 in Dictionary32:
    print(key32)
    for sub_key in Dictionary32[key32]:
        print(sub_key, ':', Dictionary32[key32][sub_key])


print("=========================================76==========================================")
print("Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.")
print("====================================================================================")

Keys76 = ['a', 'b', 'c', 'd', 'e', 'f']
Values76 = [1,2,3,4,5]

CombinedDictionary76 = {Keys76[i]: Values76[i] for i  in range(min(len(Keys76), len(Values76)))}

print("Initial keys: ", Keys76, " Initial values: ", Values76)
print("Combined lists in dictionary: ", CombinedDictionary76)

print("=========================================79==========================================")
print("Write a Python program to create a flat list of all the values in a flat dictionary.")
print("====================================================================================")

Dictionary79 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
NewList79 = []

for x in Dictionary79:
    NewList79.append(Dictionary79[x])

print("Original dictionary: ", Dictionary79)
print("List of values: ", NewList79)


print("=========================================80==========================================")
print("Write a Python program to find the key of the maximum value in a dictionary.")
print("====================================================================================")

Dictionary80 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

MaxKey80 = max(Dictionary80, key=Dictionary80.get)
MinKey80 = min(Dictionary80, key=Dictionary80.get)

print("Original dictionary: ", Dictionary80)
print("Maximum value key: ", MaxKey80)
print("Minimum value key: ", MinKey80)

print("=========================================57==========================================")
print("Write a Python program to filter even numbers from a dictionary of values.")
print("====================================================================================")

Dictionary57 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
FilteredDictionary57 = {}

for Key57, Value57 in Dictionary57.items():
    EvenNumbers = [num for num in Value57 if num % 2 == 0]
    FilteredDictionary57[Key57] = EvenNumbers

print("Original dictionary: ", Dictionary57)

print("Filtered dictionary (even numbers only):", FilteredDictionary57)


print("=========================================51==========================================")
print("Write a Python program to filter even numbers from a dictionary of values.")
print("====================================================================================")

def UpdateListValues51(dictionary, subject, newvalues):
    if subject in dictionary:
        dictionary[subject] = newvalues
    
Dictionary51 = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
print("Original dictionary: ", Dictionary51)

UpdateListValues51(Dictionary51, 'Math', [89,91,100])
UpdateListValues51(Dictionary51, 'Physics', [95,90,105])
UpdateListValues51(Dictionary51, 'Chemistry', [13,52,147])

print("Updated dictionary: ", Dictionary51)


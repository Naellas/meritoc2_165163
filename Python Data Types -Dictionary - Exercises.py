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

print("=========================================6==========================================")
print("Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.")
print("====================================================================================")

Dictionary6 = {}

for Number in range(1,16):
    Dictionary6[Number] = Number ** 2

print("Created dictionary: ", Dictionary6)
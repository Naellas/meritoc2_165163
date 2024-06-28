import os

print("==========================================================================")
print("1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.")
print("==========================================================================")

try:
    num = 10
    print("Attempting to divide ", num, " by 0")
    result = num / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.")
print("==========================================================================")

try:
    user_input = input("Please enter an integer: ")
    user_int = int(user_input)
    print(f"You entered: {user_int}")
except ValueError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.")
print("==========================================================================")

try:
    print("Attempting to open non_existent_file.txt: ")
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.")
print("==========================================================================")

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = float(num1) + float(num2)
    print(f"The sum is: {result}")
except ValueError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.")
print("==========================================================================")

file_path = "protected_file.txt"
# Create a file with read-only permissions
with open(file_path, "w") as file:
    file.write("This file is read-only.")

# Change the file permissions to read-only
os.chmod(file_path, 0o444)

try:
    # Try to open the file with write permissions
    with open(file_path, "w") as file:
        file.write("Trying to write to a read-only file.")
except PermissionError as e:
    print(f"Caught an exception: {e}")
finally:
    # Change the file permissions back to writable and delete it
    os.chmod(file_path, 0o666)
    os.remove(file_path)

print("==========================================================================")
print("6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.")
print("==========================================================================")

try:
    my_list = [1, 2, 3]
    print(my_list, "Printing list index of 5: ")
    print(my_list[5])
except IndexError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.")
print("==========================================================================")

try:
    user_input = input("Please enter a number: ")
    print(f"You entered: {user_input}")
except KeyboardInterrupt as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.")
print("==========================================================================")

try:
    num1 = 10
    num2 = 0
    print(num1, "/", num2)
    result = num1 / num2

    
except ArithmeticError as e:
    print(f"Caught an exception: {e}")

print("==========================================================================")
print("9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.")
print("==========================================================================")

try:
    with open("encoded_file.txt", "w", encoding="utf-8") as file:
        print("Creating input file with non-ASCII characters - äöü")
        file.write("This is a test file with non-ASCII characters: äöü")
    with open("encoded_file.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError as e:
    print(f"Caught an exception: {e}")

# Clean up the file after testing
os.remove("encoded_file.txt")

print("==========================================================================")
print("10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.")
print("==========================================================================")

try:
    my_list = [1, 2, 3]
    print("Trying to do my_list.appendd (invalid attribute)")
    my_list.appendd(4)
except AttributeError as e:
    print(f"Caught an exception: {e}")

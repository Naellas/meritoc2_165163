"""
print("=========================================5==========================================")
print("Write a Python program that accepts a word from the user and reverses it.")
print("====================================================================================")

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

print("=========================================5==========================================")
print("Write a Python program to count the number of even and odd numbers in a series of numbers.")
print("====================================================================================")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print("Provided numbers: ", numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

print("=========================================8==========================================")
print("Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.")
print("====================================================================================")

for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=" ")



a, b = 0, 1
fibonacci_series = []
while b < 50:
    fibonacci_series.append(b)
    a, b = b, a + b
print("Fibonacci series between 0 and 50:", fibonacci_series)

print("========================================10==========================================")
print("Write a Python program that iterates the integers from 1 to 50. For multiples of three print Fizz instead of the number and for multiples of five print Buzz. For numbers that are multiples of three and five, print FizzBuzz.")
print("====================================================================================")

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print("=========================================13==========================================")
print("Write a Python program that accepts a sequence of comma-separated 4-digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma-separated sequence.")
print("====================================================================================")

binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')
divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print("Numbers divisible by 5:", ','.join(divisible_by_5))

print("=========================================17==========================================")
print("Write a Python program to print the alphabet pattern 'A'.")
print("====================================================================================")

for i in range(7):
    if i == 0:
        print("  ***")
    elif i == 3:
        print(" *****")
    else:
        print("*    *")

print("=========================================19==========================================")
print("Write a Python program to print the alphabet pattern 'E'.")
print("====================================================================================")

for i in range(7):
    if i == 0 or i == 3 or i == 6:
        print("*****")
    else:
        print("*")

print("=========================================21==========================================")
print("Write a Python program to print the alphabet pattern 'L'.")
print("====================================================================================")

for i in range(7):
    if i == 6:
        print("*****")
    else:
        print("*")

print("=========================================23==========================================")
print("Write a Python program to print the alphabet pattern 'O'.")
print("====================================================================================")

for i in range(7):
    if i == 0 or i == 6:
        print(" *** ")
    else:
        print("*   *")

print("=========================================25==========================================")
print("Write a Python program to print the alphabet pattern 'R'.")
print("====================================================================================")

for i in range(7):
    if i == 0 or i == 3:
        print("****")
    elif i < 3:
        print("*   *")
    else:
        print("*  *")

print("=========================================31==========================================")
print("Write a Python program to calculate a dog's age in dog years.")
print("====================================================================================")

human_years = int(input("Input a dog's age in human years: "))
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4
print("The dog's age in dog's years is", dog_years)

print("=========================================34==========================================")
print("Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.")
print("====================================================================================")

def sum_or_twenty(a, b):
    result = a + b
    if 15 <= result <= 20:
        return 20
    else:
        return result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum or 20 if between 15 and 20:", sum_or_twenty(num1, num2))

print("=========================================29==========================================")
print("Write a Python program to print the alphabet pattern 'X'.")
print("====================================================================================")

for i in range(7):
    if i == 0 or i == 6:
        print("*   *")
    elif i == 1 or i == 5:
        print(" * * ")
    else:
        print("  *  ")


print("=========================================27==========================================")
print("Write a Python program to print the alphabet pattern 'T'.")
print("====================================================================================")

for i in range(7):
    if i == 0:
        print("*****")
    else:
        print("  *  ")

print("=========================================44==========================================")
print("Write a Python program to construct the following pattern, using a nested loop number.")
print("====================================================================================")

for i in range(1, 10):
    print(str(i) * i)

print("=========================================43==========================================")
print("Write a Python program to create the multiplication table (from 1 to 10) of a number.")
print("====================================================================================")

number = int(input("Input a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
"""
print("=========================================16==========================================")
print("Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.")
print("====================================================================================")

result = []

for num in range(100, 401):
    digits = [int(d) for d in str(num)]
    if all(digit % 2 == 0 for digit in digits):
        result.append(str(num))

print(", ".join(result))

print("=========================================14==========================================")
print("Write a Python program that accepts a string and calculates the number of digits and letters.")
print("====================================================================================")

def count_digits_and_letters(input_string):
    num_digits = 0
    num_letters = 0
    
    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1
    
    return num_digits, num_letters

input_string = input("Enter a string: ")
digits, letters = count_digits_and_letters(input_string)
print("Letters:", letters)
print("Digits:", digits)
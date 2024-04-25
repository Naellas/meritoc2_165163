print("=========================================5==========================================")
print("Write a Python program that accepts a word from the user and reverses it.")
print("====================================================================================")

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

print("=========================================1==========================================")
print("Write a Python program to import a built-in array module and display the namespace of the said module.")
print("====================================================================================")
import array
print(dir(array))

print("=========================================2==========================================")
print("Write a Python program to create a class and display the namespace of that class.")
print("====================================================================================")

class MyClass:
    pass

print(dir(MyClass))

print("=========================================3==========================================")
print("Write a Python program to create an instance of a specified class and display the namespace of the said instance.")
print("====================================================================================")

class Classes: 
    def __init__(self, class_id, class_name, class_number):
        self.class_id = class_id
        self.class_name = class_name
        self.class_number = class_number
student = Classes('V12', 'Frank Gibson', 'V')
print(student.__dict__)

print("=========================================4==========================================")
print("Write a Python program that imports the abs() function using the builtins module, displays the documentation of the abs() function and finds the absolute value of -155.")
print("====================================================================================")

import builtins

print(help(builtins.abs))
print(abs(-155))

print("=========================================5==========================================")
print("Define a Python function student(). Using function attributes display the names of all arguments.")
print("====================================================================================")

def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'

print("=========================================6==========================================")
print("Write a  Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.")
print("====================================================================================")

print(student("John", 15, "A"))

def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    if student_name:
        print(f"Student Name: {student_name}")
    if student_class:
        print(f"Student Class: {student_class}")

student_data(124, student_name="Alice")
student_data(125, student_name="Bob", student_class="Class X")

print("=========================================7==========================================")
print("Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.")
print("====================================================================================")

class Student:
    pass

print(type(Student))

print(Student.__dict__.keys())

print(Student.__module__)

print("=========================================8==========================================")
print("Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.")
print("====================================================================================")

class Student:
    pass

class Marks:
    pass

student_obj = Student()
marks_obj = Marks()

print(isinstance(student_obj, Student))  
print(isinstance(marks_obj, Marks))      
print(isinstance(marks_obj, Student))
print(issubclass(Student, object))  
print(issubclass(Marks, object))  

print("=========================================9==========================================")
print("Write a  Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.")
print("====================================================================================")

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("John", 85)

print("Original values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)

student.student_name = "Alice"
student.marks = 90

print("\nModified values:")
print("Student Name:", student.student_name)
print("Marks:", student.marks)

print("=========================================10==========================================")
print("Write a  Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.")
print("====================================================================================")

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

student = Student(1, "John")

student.add_class("Class X")

print("Entire attribute and values:")
print(student.__dict__)

del student.student_name

print("\nEntire attribute with values after removal:")
print(student.__dict__)


print("=========================================11==========================================")
print("Write a  Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.")
print("====================================================================================")

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print("Attributes and values:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Student(1, "John")

student.add_class("Class X")

student.display_attributes()

print("=========================================12==========================================")
print("Write a  Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.")
print("====================================================================================")

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "John")
student2 = Student(2, "Alice")

print("Student 1:")
for attr, value in student1.__dict__.items():
    print(f"{attr}: {value}")

print("\nStudent 2:")
for attr, value in student2.__dict__.items():
    print(f"{attr}: {value}")

print("=========================================13==========================================")
print("Write a Python class to convert an integer to a Roman numeral.")
print("====================================================================================")

class IntegerToRoman:
    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_numeral = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral

converter = IntegerToRoman()
NumToConvert = int(input("Please type in number to be converted: "))
print(converter.int_to_roman(NumToConvert))

print("=========================================14==========================================")
print("Write a Python class to convert a Roman numeral to an integer.")
print("====================================================================================")

class RomanToInteger:
    def roman_to_int(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result


converter = RomanToInteger()
NumToConvert = input("Please type in roman number to be converted: ")

print(converter.roman_to_int(NumToConvert))

print("=========================================15==========================================")
print("Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].")
print("====================================================================================")

class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

validator = ParenthesesValidator()

print(validator.is_valid("()"))         # Output: True
print(validator.is_valid("()[]{}"))     # Output: True
print(validator.is_valid("[)"))         # Output: False
print(validator.is_valid("({[)]"))      # Output: False
print(validator.is_valid("{{{"))        # Output: False

print("=========================================16==========================================")
print("Write a  Python class to get all possible unique subsets from a set of distinct integers.")
print("====================================================================================")

class SubsetGenerator:
    def get_subsets(self, nums):
        subsets = [[]]
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        return subsets

generator = SubsetGenerator()
print(generator.get_subsets([4, 5, 6]))

print("=========================================17==========================================")
print("Write a  Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.")
print("====================================================================================")

class PairFinder:
    def find_pair(self, numbers, target):
        num_indices = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return None

finder = PairFinder()
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
result = finder.find_pair(numbers, target)
print("Numbers: ", numbers)
if result:
    print("Index 1: ", result[0], ", Index 2: ", result[1])
else:
    print("No such pair found.")

print("=========================================18==========================================")
print("Write a Python class to find the three elements that sum to zero from a set of n real numbers.")
print("====================================================================================")

class ThreeSumFinder:
    def three_sum_zero(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

finder = ThreeSumFinder()
nums = [-25, -10, -7, -3, 2, 4, 8, 10]
print("Provided numbers: ", nums)
print(finder.three_sum_zero(nums))

print("=========================================19==========================================")
print("Write a  Python class to implement pow(x, n).")
print("====================================================================================")

class PowerCalculator:
    def pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

calculator = PowerCalculator()
print(calculator.pow(2, 3))
print(calculator.pow(2, -3)) 

print("=========================================20==========================================")
print("Write a  Python class to reverse a string word by word.")
print("====================================================================================")

class StringReverser:
    def reverse_words(self, s):

        words = s.split()

        reversed_words = words[::-1]

        reversed_string = ' '.join(reversed_words)

        return reversed_string

reverser = StringReverser()
input_string = 'hello . py'
print(input_string)
print(reverser.reverse_words(input_string)) 

print("=========================================21==========================================")
print("Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.")
print("====================================================================================")

class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print("Uppercase String:", self.input_string.upper())

processor = StringProcessor()
processor.get_string()
processor.print_string()

print("=========================================22==========================================")
print("Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.")
print("====================================================================================")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

Length = int(input("Please input length: "))
Width = int(input("Please input width: "))

rectangle = Rectangle(Length, Width)
print("Area of the rectangle:", rectangle.compute_area()) 

print("=========================================23==========================================")
print("Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.")
print("====================================================================================")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius ** 2

    def compute_perimeter(self):
        return 2 * 3.14 * self.radius

size = int(input("Please insert radius of the circle: "))
circle = Circle(5)
print("Area of the circle:", circle.compute_area()) 
print("Perimeter of the circle:", circle.compute_perimeter()) 

print("=========================================24==========================================")
print("Write a  Python program to get the class name of an instance in  Python.")
print("====================================================================================")

class MyClass:
    pass

my_instance = MyClass()

class_name = type(my_instance).__name__

print("Class name:", class_name)

print("=========================================25==========================================")
print("Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details")
print("====================================================================================")

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_rate = self.emp_salary / 50
            overtime_amount = overtime * overtime_rate
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee Details:")
        print("Name:", self.emp_name)
        print("ID:", self.emp_id)
        print("Salary:", self.emp_salary)
        print("Department:", self.emp_department)

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

employee1.assign_department("HR")

employee1.print_employee_details()

print("Total salary with overtime for employee1:", employee1.calculate_emp_salary(55))

print("=========================================26==========================================")
print("Write a  Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.")
print("====================================================================================")

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been successfully booked.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, items):
        order = {"table_number": table_number, "items": items}
        self.customer_orders.append(order)
        print(f"Order for Table {table_number}: {items} has been placed.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_booked_tables(self):
        print("Booked Tables:")
        print(", ".join(str(table) for table in self.booked_tables))

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['items']}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Burger", 10)
restaurant.add_item_to_menu("Pizza", 12)
restaurant.add_item_to_menu("Salad", 8)

restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(1)

restaurant.customer_order(1, ["Burger", "Pizza"])
restaurant.customer_order(2, ["Salad"])

restaurant.print_menu()
restaurant.print_booked_tables()
restaurant.print_customer_orders()

print("=========================================27==========================================")
print("Write a  Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.")
print("====================================================================================")


class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount("123456789", "John Doe", "2024-06-01", initial_balance=1000)

account.deposit(500)

account.withdraw(200)

account.check_balance()


print("=========================================28==========================================")
print("Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.")
print("====================================================================================")

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
            print(f"Item with ID {item_id} added to inventory.")
        else:
            print(f"Item with ID {item_id} already exists in inventory.")

    def update_item(self, item_id, **kwargs):
        if item_id in self.items:
            for key, value in kwargs.items():
                if key in self.items[item_id]:
                    self.items[item_id][key] = value
                    print(f"{key} updated successfully for item with ID {item_id}.")
                else:
                    print(f"{key} is not a valid attribute for item with ID {item_id}.")
        else:
            print(f"Item with ID {item_id} does not exist in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            print(f"Item Details for ID {item_id}: {self.items[item_id]}")
        else:
            print(f"Item with ID {item_id} does not exist in inventory.")

inventory = Inventory()

inventory.add_item("001", "Laptop", 10, 1200)
inventory.add_item("002", "Mouse", 20, 20)
inventory.add_item("001", "Keyboard", 15, 30)

inventory.update_item("001", stock_count=20, price=1500)
inventory.update_item("002", price=25)
inventory.update_item("003", stock_count=5)

inventory.check_item_details("001")
inventory.check_item_details("002")
inventory.check_item_details("003")
import unittest
import os
import threading
import sqlite3

# Function to check if a number is prime
def find_prime(num):
    num = int(num)
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a list is sorted in ascending order
def find_if_sorted_asc(lst):
    return lst == sorted(lst)

# Function to check if two lists are equal
def lists_are_equal(list1, list2):
    return list1 == list2

# Function to check if a string is a palindrome
def check_if_palindrome(s):
    return s == s[::-1]

# Function to check if a file exists in a specified directory
def file_exists(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

# Function to handle floating-point calculations
def add_floats(a, b):
    return a + b

# Function to increment counter for multithreading test
def increment_counter(counter):
    counter[0] += 1

# Function to connect to database
def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Function to get users from the database
def get_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    return cursor.fetchall()

# Function to validate and parse input data
def validate_and_parse(data):
    if isinstance(data, str):
        return data.strip()
    else:
        raise ValueError("Invalid data type")

# Unit Test Classes

class TestPrimeCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("1. Write a Python unit test program to check if a given number is prime or not.")
        print("==========================================================================")

    def test_prime_number(self):
        num = 7
        print("Prime number test:", num)
        self.assertTrue(find_prime(num))

    def test_non_prime_number(self):
        num = 10
        print("Non-prime number test:", num)
        self.assertFalse(find_prime(num))

    def test_negative_number(self):
        num = -5
        print("Negative number test:", num)
        self.assertFalse(find_prime(num))

    def test_one(self):
        num = 1
        print("One test:", num)
        self.assertFalse(find_prime(num))

class TestSorting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("2. Write a Python unit test program to check if a list is sorted in ascending order.")
        print("==========================================================================")

    def test_sorted_list(self):
        lst = [1, 2, 3, 4, 5]
        print("Sorted list test:", lst)
        self.assertTrue(find_if_sorted_asc(lst))
    
    def test_unsorted_list(self):
        lst = [1, 3, 2, 7, 4, 6, 8]
        print("Unsorted list test:", lst)
        self.assertFalse(find_if_sorted_asc(lst))
    
    def test_empty_list(self):
        lst = []
        print("Empty list test:", lst)
        self.assertTrue(find_if_sorted_asc(lst))
    
    def test_single_element_list(self):
        lst = [1]
        print("Single element list test:", lst)
        self.assertTrue(find_if_sorted_asc(lst))

class TestListEquality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("3. Write a Python unit test program that checks if two lists are equal.")
        print("==========================================================================")

    def test_equal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        print("Equal list test:", nums1, nums2)
        self.assertTrue(lists_are_equal(nums1, nums2), "The lists are not equal")

    def test_unequal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        print("Unequal list test:", nums1, nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")

    def test_different_lengths(self):
        nums1 = [10, 20, 30]
        nums2 = [10, 20, 30, 40]
        print("Different lengths list test:", nums1, nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")

class TestPalindrome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("4. Write a Python unit test program to check if a string is a palindrome.")
        print("==========================================================================")

    def test_palindrome(self):
        s = "madam"
        print("Palindrome test:", s)
        self.assertTrue(check_if_palindrome(s))
    
    def test_non_palindrome(self):
        s = "hello"
        print("Non-palindrome test:", s)
        self.assertFalse(check_if_palindrome(s))
    
    def test_empty_string(self):
        s = ""
        print("Empty string test:", s)
        self.assertTrue(check_if_palindrome(s))
    
    def test_single_character(self):
        s = "a"
        print("Single character test:", s)
        self.assertTrue(check_if_palindrome(s))

class TestFileExists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("5. Write a Python unit test program to check if a file exists in a specified directory.")
        print("==========================================================================")

    def setUp(self):
        self.test_dir = "test_dir"
        self.test_file = "test_file.txt"
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, self.test_file), 'w') as f:
            f.write("This is a test file.")

    def tearDown(self):
        os.remove(os.path.join(self.test_dir, self.test_file))
        os.rmdir(self.test_dir)

    def test_file_exists(self):
        print("File exists test:", self.test_dir, self.test_file)
        self.assertTrue(file_exists(self.test_dir, self.test_file))

    def test_file_does_not_exist(self):
        print("File does not exist test:", self.test_dir, "non_existent_file.txt")
        self.assertFalse(file_exists(self.test_dir, "non_existent_file.txt"))

class TestFloatingPoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("6. Write a Python unit test that checks if a function handles floating-point calculations accurately.")
        print("==========================================================================")

    def test_floating_point_addition(self):
        a, b = 0.1, 0.2
        print("Floating point addition test:", a, "+", b)
        self.assertAlmostEqual(add_floats(a, b), 0.3, places=7)

class TestMultithreading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("7. Write a Python unit test program to check if a function handles multi-threading correctly.")
        print("==========================================================================")

    def test_threading(self):
        counter = [0]
        threads = []
        print("Multithreading test: Initial counter:", counter[0])
        for _ in range(100):
            thread = threading.Thread(target=increment_counter, args=(counter,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print("Final counter:", counter[0])
        self.assertEqual(counter[0], 100)

class TestDatabaseConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("8. Write a Python unit test program to check if a database connection is successful.")
        print("==========================================================================")

    def test_connection(self):
        print("Database connection test:")
        conn = connect_to_database(":memory:")
        self.assertIsNotNone(conn)
        conn.close()

class TestDatabaseQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("9. Write a Python unit test program to check if a database query returns the expected results.")
        print("==========================================================================")

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE users (name TEXT)")
        self.conn.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")

    def tearDown(self):
        self.conn.close()

    def test_query(self):
        print("Database query test:")
        users = get_users(self.conn)
        print("Queried users:", users)
        self.assertEqual(users, [('Alice',), ('Bob',)])

class TestInputValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==========================================================================")
        print("10. Write a Python unit test program to check if a function correctly parses and validates input data.")
        print("==========================================================================")

    def test_valid_string(self):
        s = "  hello  "
        print("Valid string test:", s)
        self.assertEqual(validate_and_parse(s), "hello")
    
    def test_invalid_data_type(self):
        data = 123
        print("Invalid data type test:", data)
        with self.assertRaises(ValueError):
            validate_and_parse(data)

if __name__ == "__main__":
    unittest.main()

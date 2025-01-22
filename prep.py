"""
1. Understanding and Implementing functions

* Function encapsulate code for reuse
    Functions allow you to group a block of code into a single, reusable unit
"""

# Example code

def calculate_area(length, width):
    return length * width

print(f"Area 1: {calculate_area(5, 3)}")
print(f"Area 2: {calculate_area(6, 4)}")


# Exercises

"""Write a function to convert Celsius to Fahrenheit."""

def celsius_to_fahreiheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = float(input("Enter the temperature in celsius: "))
fahranheit_temp = celsius_to_fahreiheit(celsius_temp)
print(f"{celsius_temp} °C is equal to {fahranheit_temp} °F")


"""Write a function that takes a list of numbers and returns their sum."""

def calculate_number(number):
    total = sum(number)
    return total

list_of_numbers = [1,3,5,7,9]
results = calculate_number(list_of_numbers)
print(f"The sum of {list_of_numbers} is {results}")


"""
2. Handling User Input and Validation
* Always sanitize and validate user input
* Use 'try' and 'except' for error handling
"""

# Example code

def get_positive_number():
    while True:
        try:
            num = float(input("Enter positive number: "))
            if num <= 0:
                raise ValueError("The number must be positive")
            return num
        except ValueError as e:
            print(e)

positive_number = get_positive_number()
print(f"You have entered : {positive_number}")

# Exercises

"""Create a function that asks for a number between 1 and 100 and validates it."""

def get_number_between_1_and_100():
    while True:
        try:
            num = int(input("Enter a number between 1 and 100: "))
            if 1 <= num <= 100:
                return num
            else:
                print("Number must be between 1 and 1oo. Try again")
        except:
            raise ValueError("Invalid number. Please enter a valid number")
        
valid_number = get_number_between_1_and_100()
print(f"You have entered: {valid_number}")

"""Modify the function above to handle empty inputs"""

def get_number_between_1_and_100():
    while True:
        try:
            user_input = input("Enter a number between 1 and 100: ").strip()
            if not user_input :
                raise ValueError("Input cannot be empty")
            num = int(user_input)

            if 1 <= num <= 100:
                return num
            else:
                print("Number must be between 1 and 1oo. Try again")

        except ValueError as e:
            print(f"Invalid input: {e}")
        
valid_number = get_number_between_1_and_100()
print(f"You have entered: {valid_number}")


"""
3. Utilizing control struxtures(Loops and Conditionals)
   * Use 'if', 'elif' and 'else' for decisions
   * Loops(for and while) repeat actions based on conditions 
"""

# Example code

import random

target = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == target:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break
    elif guess < target:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

# Exercises

"""
Write a loop to calculate the sum of all even numbers between 1 and 50.
"""

def calculate_sum_of_evens(start, end):
    sum_of_evens = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens

start = 1
end = 50
result = calculate_sum_of_evens(start, end)
print(f"The sum of all even numbers between {start} and {end} is: {result}")


"""
Create a simple menu-driven program where users choose options to perform actions.
"""

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Calculate the sum of two numbers")
    print("2. Find the largest of three numbers")
    print("3. Check if a number is even or odd")
    print("4. Exit")


def calculate_sum():
    """Calculate the sum of two numbers."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")


def find_largest():
    """Find the largest of three numbers."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    largest = max(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")


def check_even_or_odd():
    """Check if a number is even or odd."""
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


# Main Program
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        calculate_sum()
    elif choice == "2":
        find_largest()
    elif choice == "3":
        check_even_or_odd()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


"""
4. Working with Data Structures (Lists, etc.)
   *Lists are ordered, mutable collections of items.
   *Common operations: append, remove, sort, slice.
"""

# Example code 

def count_occurrences(items):
    item_count = {}
    for item in items:
        item_count[item] = item_count.get(item, 0) + 1
    return item_count



fruits = ["apple", "banana", "orange", "apple", "banana", "apple"]
fruit_count = count_occurrences(fruits)
print(fruit_count)  

# Exercises

"""Write a function that takes a list of numbers and returns the second largest number."""

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  
    
    unique_numbers = sorted(set(numbers), reverse=True)
    
    if len(unique_numbers) < 2:
        return None
    
    return unique_numbers[1]

numbers = [4, 2, 9, 7, 5, 9, 4]
second_largest = find_second_largest(numbers)
if second_largest is not None:
    print(f"The second largest number is: {second_largest}")
else:
    print("The list does not have a second largest number.")




"""Create a program to reverse a list without using the built-in reverse() function."""

def reverse_list(original_list):
    reversed_list = []
    for item in original_list:
        reversed_list.insert(0, item)
    return reversed_list

my_list = [1, 2, 3, 4, 5]
reversed_my_list = reverse_list(my_list)
print(f"Original list: {my_list}")
print(f"Reversed list: {reversed_my_list}")


"""
5. Implementing Algorithms for Shape Drawing
   *Use nested loops for patterns.
   *Combine loops and string manipulation for shapes.
"""

# Example code

def draw_diamond(rows):
    # Top half
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

    # Bottom half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

number_of_rows = 5
draw_diamond(number_of_rows)

# Exercises

"""Draw a square, triangle, and rectangle using loops."""

def draw_square(size):
    """Draw a square of a given size."""
    for i in range(size):
        print("*" * size)

def draw_triangle(height):
    """Draw a right-angled triangle with the given height."""
    for i in range(1, height + 1):
        print("*" * i)

def draw_rectangle(width, height):
    """Draw a rectangle with the given width and height."""
    for i in range(height):
        print("*" * width)

size = 5
height = 5
width = 8

print("Square:")
draw_square(size)

print("\nTriangle:")
draw_triangle(height)

print("\nRectangle:")
draw_rectangle(width, height)


"""Create a checkerboard pattern with # and spaces."""

def draw_checkerboard(size):
    """Draw a checkerboard pattern with the given size."""
    for i in range(size):
        row = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                row += "#"
            else:
                row += " "
        print(row)

size = 8
draw_checkerboard(size)


"""
6. Problem-Solving Skills Through Algorithm Design
   *Break problems into steps: Input → Process → Output.
   *Use pseudocode or diagrams before implementation.
"""

# Example code

def first_non_repeating_char(string):
    """Finds the first non-repeating character in a string."""
    char_count = {}

    # Count occurrences
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

# Test
string = "swiss"
print(f"First non-repeating character: {first_non_repeating_char(string)}")

"""
Write an algorithm to determine if a number is prime.
"""
import math

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False 
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  
    return True 


num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


"""
Implement a function to find the greatest common divisor (GCD) of two numbers.
"""

def gcd(a, b):
    """Find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b 
    return a 

num1 = 56
num2 = 98
gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")

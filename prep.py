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


# Exercise

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

# Exercise

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



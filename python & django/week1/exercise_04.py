# Exercise 4: Functions and Arguments
# Practice with functions, parameters, and return values

print("=== EXERCISE 4: FUNCTIONS ===\n")

# TODO 1: Basic function
# Create a function called 'introduce' that takes name and age as parameters
# It should print: "Hi, I'm [name] and I'm [age] years old"
# Call it with your own name and age
def introduce(name, age):
    print(f"Hi, I'm {name} and I'm {age} years old")

introduce("Vaisakh", 32)

# TODO 2: Function with return value
# Create a function 'calculate_discount' that takes price and discount_percent
# Return the final price after discount
# Example: calculate_discount(100, 20) should return 80
# Test it with a few different values and print the results
def calculate_discount(price, discount_percent):
    final_price = (discount_percent / 100) * price
    return price - final_price

print(calculate_discount(100, 20))

# TODO 3: Default parameters
# Create a function 'create_email' with parameters: username, domain="gmail.com"
# Return the email string: "[username]@[domain]"
# Call it:
# - With just username (uses default domain)
# - With both username and custom domain
def create_email(username, domain="gmail.com"):
    return username + "@" + domain

print(create_email("vaisakh"))
print(create_email("vaisakh","custom.com"))


# TODO 4: Multiple return values
# Create a function 'get_min_max' that takes a list of numbers
# Return both the minimum and maximum values
# Example: get_min_max([5, 2, 9, 1, 7]) returns (1, 9)
# Hint: Use built-in min() and max() functions

def get_min_max(numbers):
    return min(numbers), max(numbers)

# def get_min_max(*numbers):
#     return min(numbers), max(numbers)

minimum, maximum = get_min_max([1,2,3,4,5])
print(f"{minimum}: {maximum}")

# TODO 5: Keyword arguments
# Create a function 'book_details' with parameters: title, author, year, pages
# Print all the details in a formatted way
# Call it using keyword arguments (not positional)
def book_details(**kwargs):
    for key, value in kwargs.items():
        print(f"\n {key}: {value}")

book_details(title = "ABCD", author="vaisakh", year = 2025, pages=10)


# TODO 6: *args - Variable arguments
# Create a function 'multiply_all' that takes any number of arguments
# Return the product of all numbers
# Example: multiply_all(2, 3, 4) returns 24
# Test with different numbers of arguments
def multiply_all(*numbers):
    products = 1
    for number in numbers:
        products *= number
    return products

print(f"Product : {multiply_all(2, 3, 4)}") 


# TODO 7: List processing function
# Create a function 'filter_long_words' that takes a list of words and min_length
# Return a new list with only words longer than min_length
# Example: filter_long_words(["hi", "hello", "hey", "greetings"], 3)
# Returns: ["hello", "greetings"]
def filter_long_words(words, min_length):
    result = []
    for word in words:
        if len(word) > min_length:
            result.append(word)
    return result

print(f"Result is {filter_long_words(["hi", "hello", "hey", "greetings"], 3)}")



# TODO 8: **kwargs - Keyword arguments dictionary
# Create a function 'create_profile' that takes **kwargs
# It should print all the key-value pairs passed to it
# Call it with different combinations like:
# create_profile(name="Alice", age=25, role="Developer", skills="React")
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"\n{key} - {value}")


create_profile(name="Alice", age=25, role="Developer", skills="React")


# TODO 9: Lambda function
# Create a lambda function that converts Celsius to Fahrenheit
# Formula: (celsius * 9/5) + 32
# Assign it to a variable and test with different temperatures

fahrenheit = lambda celsius: (celsius * 9 / 5) + 32;
print(fahrenheit(10))


# TODO 10: Practical function - Email validator
# Create a function 'is_valid_email' that takes an email string
# Return True if email contains both "@" and "."
# Return False otherwise
# Test with valid and invalid emails
def is_valid_email(email):
    return "@" in email and "." in email

print(f"is vaisakh@custom.com valid?  {is_valid_email("vaisakh@custom.com")}")
print(f"is vaisakhcustomcom valid?  {is_valid_email("vaisakhcustomcom")}")


# TODO 11: Calculator function
# Create a function 'calculator' with parameters: num1, num2, operation="add"
# Based on operation, return the result:
# - "add" -> num1 + num2
# - "subtract" -> num1 - num2
# - "multiply" -> num1 * num2
# - "divide" -> num1 / num2
# Test all operations
def calculator(num1, num2, operation = "add"):
    result = 0;
    if(operation == "add"):
        result = num1 + num2
    elif(operation == "subtract"):
        result = num1 - num2
    elif(operation == "multiply"):
        result = num1 * num2
    elif(operation == "divide"):
        result = num1 / num2
    else:
        print("Invalid operation")
    return result

print(f" 11 + 25 = {calculator(11, 25)}")
print(f" 11 - 25 = {calculator(11, 25, "subtract")}")
print(f" 11 * 25 = {calculator(11, 25, "multiply")}")
print(f" 11 / 25 = {calculator(11, 25, "divide")}")

# TODO 12: List comprehension in function (Preview!)
# Create a function 'get_squares' that takes a list of numbers
# Return a new list with squares of all numbers
# Use list comprehension: [x**2 for x in numbers]
# def get_squares(numbers):
#     result = []
#     for num in numbers:
#         result.append(num ** 2);
#     return result

# print(get_squares([1,2,3,4,5,6,7,8,9]))

# numbers = [1,2,3,4,5,6,7,8,9]
# squared = lambda numbers: list(map(lambda x: x ** 2, numbers))
# print(f"Squared: {squared(numbers)}")

def get_squares(numbers):
    return [num ** 2 for num in numbers]

print(get_squares([1,2,3,4,5,6,7,8,9]))

print("\n✅ Exercise complete! Check your solution when ready.")

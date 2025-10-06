# Day 1: Functions and Arguments
# Coming from JavaScript? Let's compare!

print("=== BASIC FUNCTION SYNTAX ===")

# Python: Use 'def' keyword (not 'function')
def greet():
    print("Hello, World!")

greet()  # Call the function

# JS equivalent:
# function greet() {
#     console.log("Hello, World!")
# }
# greet()

print("\n=== FUNCTIONS WITH PARAMETERS ===")

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Vaisakh")
greet_user("Alex")

# Multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)
add(10, 20)

print("\n=== RETURN VALUES ===")

# Functions can return values (just like JS)
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(f"4 * 5 = {result}")

# Without return, function returns None
def say_hi():
    print("Hi!")

value = say_hi()
print(f"Return value: {value}")  # None

print("\n=== DEFAULT PARAMETERS ===")

# Set default values for parameters
def greet_with_title(name, title="Developer"):
    print(f"Hello, {name} - {title}")

greet_with_title("Alice")                    # Uses default
greet_with_title("Bob", "Designer")          # Overrides default
greet_with_title("Charlie", "Full-Stack Dev")

# JS equivalent:
# function greet(name, title = "Developer") {
#     console.log(`Hello, ${name} - ${title}`)
# }

print("\n=== KEYWORD ARGUMENTS (Python-specific!) ===")

def create_profile(name, age, role, skills):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Role: {role}")
    print(f"Skills: {skills}")

# Call with keyword arguments (any order!)
create_profile(
    role="Frontend Dev",
    name="Alice",
    skills="React, CSS",
    age=25
)

# Mix positional and keyword (positional must come first)
create_profile("Bob", 30, role="Backend Dev", skills="Python, Django")

print("\n=== RETURN MULTIPLE VALUES ===")

# Python can return multiple values (returns a tuple)
def get_user_info():
    name = "Vaisakh"
    age = 25
    role = "Developer"
    return name, age, role

# Unpack the values
user_name, user_age, user_role = get_user_info()
print(f"Name: {user_name}, Age: {user_age}, Role: {user_role}")

# Or get as tuple
info = get_user_info()
print(f"Info tuple: {info}")

print("\n=== *args (Variable Length Arguments) ===")

# *args allows any number of positional arguments
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {add_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {add_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10,20: {add_all(10, 20)}")

# *args is a tuple inside the function
def show_args(*args):
    print(f"Type: {type(args)}")
    print(f"Values: {args}")

show_args("a", "b", "c")

# JS equivalent: rest parameters
# function addAll(...numbers) {
#     return numbers.reduce((sum, num) => sum + num, 0)
# }

print("\n=== **kwargs (Keyword Arguments) ===")

# **kwargs allows any number of keyword arguments
def create_user(**user_data):
    print("User data:")
    for key, value in user_data.items():
        print(f"  {key}: {value}")

create_user(name="Alice", age=22, city="Mumbai", role="Developer")
create_user(name="Bob", email="bob@example.com")

# **kwargs is a dictionary inside the function
def show_kwargs(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Values: {kwargs}")

show_kwargs(a=1, b=2, c=3)

print("\n=== COMBINING PARAMETERS ===")

# Order matters: regular params, *args, default params, **kwargs
def complex_function(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function(
    "Must provide this",
    1, 2, 3,                    # *args
    default="Changed",          # override default
    extra1="value1",            # **kwargs
    extra2="value2"
)

print("\n=== LAMBDA FUNCTIONS (Anonymous Functions) ===")

# Short one-line functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda a, b: a + b
print(f"3 + 7 = {add(3, 7)}")

# JS equivalent:
# const square = (x) => x ** 2
# const add = (a, b) => a + b

# Useful with map, filter, etc.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

print("\n=== SCOPE (Local vs Global) ===")

# Global variable
global_var = "I'm global"

def test_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error!

# Modifying global variable
count = 0

def increment():
    global count  # Must declare 'global' to modify
    count += 1

increment()
increment()
print(f"Count: {count}")

print("\n=== DOCSTRINGS (Function Documentation) ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length * width)
    """
    return length * width

print(f"Area: {calculate_area(5, 3)}")
print(f"Docstring: {calculate_area.__doc__}")

print("\n=== COMMON PATTERNS ===")

# Pattern 1: Validation function
def is_valid_email(email):
    return "@" in email and "." in email

print(f"Valid: {is_valid_email('user@example.com')}")
print(f"Valid: {is_valid_email('invalid')}")

# Pattern 2: Transform data
def to_title_case(text):
    return text.title()

print(f"Title: {to_title_case('hello world')}")

# Pattern 3: List processing
def get_passing_grades(scores):
    passing = []
    for score in scores:
        if score >= 60:
            passing.append(score)
    return passing

all_scores = [45, 78, 92, 55, 88, 63]
print(f"Passing: {get_passing_grades(all_scores)}")

# Pattern 4: Default mutable parameter (GOTCHA!)
# BAD - Don't do this:
# def add_item(item, my_list=[]):  # Default list is shared!
#     my_list.append(item)
#     return my_list

# GOOD - Do this instead:
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(f"List 1: {add_item('a')}")
print(f"List 2: {add_item('b')}")  # Creates new list each time

print("\n🎯 KEY DIFFERENCES FROM JAVASCRIPT:")
print("1. Use 'def' keyword (not 'function')")
print("2. Indentation instead of curly braces")
print("3. Keyword arguments (call with param names)")
print("4. Can return multiple values")
print("5. *args and **kwargs for variable arguments")
print("6. Lambda instead of arrow functions")
print("7. 'global' keyword to modify global variables")
print("8. Docstrings for documentation")

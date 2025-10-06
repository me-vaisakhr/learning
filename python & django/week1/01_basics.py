# Day 1: Python Basics - Variables & Data Types
# Coming from JavaScript? Let's compare!

print("=== VARIABLES ===")
# Python: No 'let', 'const', or 'var' - just assign directly
name = "Vaisakh"
age = 25
is_learning = True

print(f"Name: {name}")  # f-strings are like template literals
print(f"Age: {age}")
print(f"Learning: {is_learning}")

# JS: const name = "Vaisakh"
# Python: name = "Vaisakh"  (that's it!)

print("\n=== DATA TYPES ===")

# 1. Strings
greeting = "Hello, World!"
multi_line = """This is a
multi-line string"""

# JS: `Hello ${name}`
# Python: f"Hello {name}"
print(f"Greeting: {greeting}")

# 2. Numbers
integer_num = 42           # int
float_num = 3.14          # float
result = integer_num + 10  # No type coercion like JS!

print(f"Integer: {integer_num}, Float: {float_num}")

# 3. Booleans
# JS: true/false (lowercase)
# Python: True/False (capitalized!)
is_react_dev = True
knows_python = False

print(f"React dev? {is_react_dev}")

# 4. None (like JavaScript's null)
nothing = None
print(f"Nothing: {nothing}")

print("\n=== TYPE CHECKING ===")
# Python is dynamically typed but you can check types
print(f"type(name) = {type(name)}")      # <class 'str'>
print(f"type(age) = {type(age)}")        # <class 'int'>
print(f"type(3.14) = {type(3.14)}")      # <class 'float'>
print(f"type(True) = {type(True)}")      # <class 'bool'>

print("\n=== STRING METHODS ===")
text = "python is awesome"
print(f"Upper: {text.upper()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title: {text.title()}")
print(f"Replace: {text.replace('python', 'Python')}")

# String slicing (like JS .slice())
course = "Full-Stack"
print(f"First 4 chars: {course[:4]}")     # Full
print(f"Last 5 chars: {course[-5:]}")     # Stack
print(f"Middle: {course[5:10]}")          # Stack

print("\n=== OPERATORS ===")
# Arithmetic (same as JS)
x = 10
y = 3
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")               # Always returns float
print(f"Floor Division: {x // y}")        # Returns int (Python only!)
print(f"Modulo: {x % y}")
print(f"Exponent: {x ** y}")              # 10^3 = 1000 (Python only!)

# Comparison (same as JS)
print(f"\n10 > 5: {10 > 5}")
print(f"10 == 10: {10 == 10}")
# Python: Use 'and', 'or', 'not' instead of &&, ||, !
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

print("\n=== INPUT (Getting user input) ===")
# Uncomment below to test interactively:
# user_name = input("What's your name? ")
# print(f"Hello, {user_name}!")

print("\n=== TYPE CONVERSION ===")
# Converting between types
num_string = "42"
num = int(num_string)      # JS: parseInt("42")
print(f"String to int: {num}")

age_str = str(25)          # JS: String(25) or 25.toString()
print(f"Int to string: {age_str}")

pi = float("3.14")
print(f"String to float: {pi}")

print("\n🎯 KEY DIFFERENCES FROM JAVASCRIPT:")
print("1. No semicolons needed")
print("2. True/False capitalized (not true/false)")
print("3. None instead of null")
print("4. f-strings instead of template literals")
print("5. 'and', 'or', 'not' instead of &&, ||, !")
print("6. ** for exponents, // for floor division")

# Day 1: Conditionals & Loops
# Coming from JavaScript? Let's compare!

print("=== CONDITIONALS (if/elif/else) ===")

# Python uses indentation instead of curly braces!
age = 22

if age < 13:
    print("Child")
elif age < 20:  # JS: else if
    print("Teenager")
else:
    print("Adult")

# JS equivalent:
# if (age < 13) {
#     console.log("Child")
# } else if (age < 20) {
#     console.log("Teenager")
# } else {
#     console.log("Adult")
# }

print("\n=== COMPARISON OPERATORS ===")
x = 10
y = 20

print(f"{x} == {y}: {x == y}")     # Equal to
print(f"{x} != {y}: {x != y}")     # Not equal to
print(f"{x} < {y}: {x < y}")       # Less than
print(f"{x} > {y}: {x > y}")       # Greater than
print(f"{x} <= {y}: {x <= y}")     # Less than or equal
print(f"{x} >= {y}: {x >= y}")     # Greater than or equal

print("\n=== LOGICAL OPERATORS ===")
# Python: and, or, not
# JS: &&, ||, !

is_react_dev = True
knows_python = False

if is_react_dev and knows_python:
    print("Full-stack ready!")
elif is_react_dev or knows_python:
    print("Learning in progress...")
else:
    print("Just starting!")

# Checking if value exists
name = "Vaisakh"
if name:  # Truthy check (like JS if (name))
    print(f"Hello, {name}!")

print("\n=== MEMBERSHIP OPERATORS (in, not in) ===")
# Python-specific! Very useful
skills = ["React", "JavaScript", "HTML", "CSS"]

if "React" in skills:
    print("You know React!")

if "Python" not in skills:
    print("Time to learn Python!")

# Works with strings too
email = "user@example.com"
if "@" in email:
    print("Valid email format")

print("\n=== FOR LOOPS ===")

# Loop through a list
frameworks = ["React", "Django", "Express", "Next.js"]
print("Frameworks I want to learn:")
for framework in frameworks:
    print(f"  - {framework}")

# JS equivalent:
# for (const framework of frameworks) {
#     console.log(`  - ${framework}`)
# }

print("\n=== RANGE FUNCTION ===")
# range(start, stop, step)
# Like JS: for (let i = 0; i < 5; i++)

print("Numbers 0-4:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")

print("\n\nNumbers 1-5:")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i, end=" ")

print("\n\nEven numbers 0-10:")
for i in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(i, end=" ")

print("\n\n=== ENUMERATE (Loop with index) ===")
# Like JS: array.forEach((item, index) => ...)

languages = ["Python", "JavaScript", "TypeScript"]
for index, language in enumerate(languages):
    print(f"{index}: {language}")

# Starting index from 1
print("\nStarting from 1:")
for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")

print("\n=== LOOP THROUGH DICTIONARY ===")
student = {
    "name": "Alex",
    "age": 22,
    "course": "Computer Science"
}

# Loop through keys
print("Keys:")
for key in student:
    print(f"  {key}")

# Loop through values
print("\nValues:")
for value in student.values():
    print(f"  {value}")

# Loop through key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# JS equivalent:
# Object.entries(student).forEach(([key, value]) => {
#     console.log(`${key}: ${value}`)
# })

print("\n=== WHILE LOOPS ===")
# Like JS while loops

count = 5
print("Countdown:")
while count > 0:
    print(count, end=" ")
    count -= 1  # Python: count -= 1 (no count-- syntax!)
print("Blast off!")

# JS equivalent:
# let count = 5
# while (count > 0) {
#     console.log(count)
#     count--
# }

print("\n=== BREAK AND CONTINUE ===")

# break - exit the loop
print("Using break (stop at 5):")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

# continue - skip to next iteration
print("\n\nUsing continue (skip odd numbers):")
for i in range(1, 11):
    if i % 2 != 0:  # If odd
        continue
    print(i, end=" ")

print("\n\n=== NESTED LOOPS ===")
# Loop inside a loop

print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Empty line between rows

print("\n=== LIST COMPREHENSION (Preview!) ===")
# Python's elegant way to create lists
# We'll learn this more later, but it's worth seeing now

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares: {squares}")

# List comprehension way (Pythonic!)
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comp}")

# With condition
evens = [i for i in range(1, 11) if i % 2 == 0]
print(f"Even numbers: {evens}")

# JS equivalent:
# const evens = [...Array(10).keys()].map(i => i+1).filter(i => i % 2 === 0)
# Python is more readable!

print("\n=== COMMON PATTERNS ===")

# Pattern 1: Sum of list
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")
# Or use built-in: sum(numbers)

# Pattern 2: Find maximum
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Max: {max_num}")
# Or use built-in: max(numbers)

# Pattern 3: Filter items
long_words = []
words = ["hi", "hello", "hey", "greetings"]
for word in words:
    if len(word) > 3:
        long_words.append(word)
print(f"Long words: {long_words}")

print("\n🎯 KEY DIFFERENCES FROM JAVASCRIPT:")
print("1. Indentation matters! No curly braces {}")
print("2. elif instead of else if")
print("3. for item in list (not for...of)")
print("4. range() for number sequences")
print("5. 'and', 'or', 'not' instead of &&, ||, !")
print("6. 'in' operator to check membership")
print("7. No count++ or count-- (use count += 1 or count -= 1)")
print("8. enumerate() for index + value")
print("9. .items() for looping through dict key-value pairs")

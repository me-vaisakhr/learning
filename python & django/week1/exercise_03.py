# Exercise 3: Conditionals and Loops
# Practice with if/elif/else and for/while loops

print("=== EXERCISE 3: CONDITIONALS & LOOPS ===\n")

# TODO 1: Age checker
# Create a variable 'age' with any number
# Write if/elif/else to print:
# - "Child" if age < 13
# - "Teenager" if age 13-19
# - "Adult" if age >= 20
age = 1
if(age < 13):
    print("Child");
elif(age >= 13 and age <=19):
    print("Teenager")
else:
    print("Adult")


# TODO 2: Grade calculator
# Create a variable 'score' (0-100)
# Use if/elif/else to print letter grade:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: below 60
score = 70
if(score >= 90 and score <= 100):
    print("A")
elif(score >= 80 and score < 90):
    print("B")
elif(score >= 70 and score < 80):
    print("C")
elif(score >= 60 and score < 70):
    print("D")
else:
    print("F")


# TODO 3: FizzBuzz (Classic!)
# Loop from 1 to 30 and print:
# - "Fizz" if number divisible by 3
# - "Buzz" if number divisible by 5
# - "FizzBuzz" if divisible by both
# - The number itself otherwise
# Hint: Use % (modulo) operator
for index in range(1, 30):
    if(index % 3 == 0 and index % 5 == 0):
        print("FizzBuzz")
    elif(index % 3 == 0):
        print("Fizz")
    elif(index % 5 == 0):
        print("Buzz")
    else:
        print(index)


# TODO 4: Loop through a list
# Given list: frameworks = ["React", "Django", "Express", "Flask", "Next.js"]
# Loop through and print: "I want to learn [framework]"
# Then print only frameworks that contain the letter 'e' (case insensitive)
frameworks = ["React", "Django", "Express", "Flask", "Next.js"]
for framework in frameworks:
    print(f"I want to learn {framework}")
for framework in frameworks:
    if('e' in framework.lower()):
        print(f"{framework}")


# TODO 5: While loop - countdown
# Create a countdown from 10 to 1, then print "Blast off!"
# Use a while loop
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -=1
print("Blast off!")


# TODO 6: Find in list
# Given list: technologies = ["HTML", "CSS", "Python", "JavaScript", "SQL"]
# Ask user: Write code that checks if "Python" is in the list
# - If found: print "Found Python at index [position]"
# - If not found: print "Python not found"
# Hint: Use 'in' operator and .index() method
technologies = ["HTML", "CSS", "Python", "JavaScript", "SQL"]
is_python = "Python" in technologies;
if(is_python is True):
    print(f"Found Python at index {technologies.index("Python")}")
else:
    print("Python not found")




# TODO 7: Sum with loop
# Create list: numbers = [10, 25, 30, 45, 50]
# Use a for loop to calculate and print the sum of all numbers
# Then print the average
numbers = [10, 25, 30, 45, 50]
sum = 0;
for number in numbers:
    sum += number;
print(f"Sum : {sum}")
print(f"Average : {sum / len(numbers)}")

# TODO 8: Nested loops (Multiplication table)
# Create a multiplication table for numbers 1-5
# Output should look like:
# 1 x 1 = 1
# 1 x 2 = 2
# ... up to 5 x 5 = 25
for multiplicant in range(1, 6):
    for multiplier in range(1, 6):
        print(f"\n{multiplicant} X {multiplier} = {multiplicant * multiplier}")


# TODO 9: Loop with break and continue
# Loop through numbers 1 to 20
# - Skip (continue) numbers divisible by 3
# - Stop (break) when you reach 15
# Print all other numbers
for number in range(1, 20):
    if(number % 3 == 0):
        continue
    elif(number == 15):
        break
    else:
        print(number)


# TODO 10: Dictionary iteration
# Given dict:
# student = {"name": "Alex", "age": 22, "course": "CS", "grade": "A"}
# Loop through and print: "[key]: [value]" for each item
student = {"name": "Alex", "age": 22, "course": "CS", "grade": "A"}
for key, value in student.items():
    print(f"{key}:{value}")


print("\n✅ Exercise complete! Check your solution when ready.")

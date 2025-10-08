"""
EXERCISE 05: FILE HANDLING
Practice exercises for file operations
"""

# =======================
# EXERCISE 1: Read and Display
# =======================
# Task: Read 'sample.txt' and print its content
# Hint: Use 'with open()' and read() method

print("Exercise 1: Read and Display")
# Your code here:
with open("sample.txt") as file:
    print(f"{file.read()}")


# =======================
# EXERCISE 2: Count Lines
# =======================
# Task: Write a function that counts the number of lines in a file
# Hint: Use readlines() or iterate through file

print("\nExercise 2: Count Lines")

def count_lines(filename):
    # Your code here:
    count = 0
    with open(filename) as file:
        for _ in file.readlines():
            count +=1
    return count

# Test it:
line_count = count_lines('sample.txt')
print(f"Number of lines: {line_count}")


# =======================
# EXERCISE 3: Create a Shopping List
# =======================
# Task: Create a file called 'shopping.txt' and write 5 items to it
# Each item should be on a new line
# Hint: Use 'w' mode and '\n' for new lines

print("\nExercise 3: Create Shopping List")
# Your code here:
with open("shopping.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"Line {i}\n")



# =======================
# EXERCISE 4: Append to Shopping List
# =======================
# Task: Append 3 more items to 'shopping.txt'
# Hint: Use 'a' mode (append)

print("\nExercise 4: Append to Shopping List")
# Your code here:
with open("shopping.txt", "a") as file:
    for i in range(6, 10):
        file.writelines(f"New Line {i}\n")



# =======================
# EXERCISE 5: Search in File
# =======================
# Task: Write a function that searches for a word in a file
# Return True if found, False otherwise
# Hint: Read file content and use 'in' operator

print("\nExercise 5: Search in File")

def search_word(filename, word):
    # Your code here:
    status = False
    with open(filename) as file:
        for line in file:
            if(word in line):
                status = True
                break
    return status

# Test it:
result = search_word('sample.txt', 'Python')
print(f"Word found: {result}")


# =======================
# EXERCISE 6: Word Frequency
# =======================
# Task: Count how many times a specific word appears in a file
# Hint: Split content into words and count

print("\nExercise 6: Word Frequency")

def word_frequency(filename, word):
    # Your code here:
    count = 0;
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            for current_word in words:
                if current_word == word:
                    count +=1
            return count
    except FileNotFoundError:
        return count

# Test it:
freq = word_frequency('sample.txt', 'file')
print(f"Word 'file' appears {freq} times")


# =======================
# EXERCISE 7: Reverse File Content
# =======================
# Task: Read a file and write its content in reverse order to a new file
# Reverse the lines, not the characters
# Example: Line 1, Line 2, Line 3 → Line 3, Line 2, Line 1

print("\nExercise 7: Reverse File Content")

def reverse_file(input_file, output_file):
    # Your code here:
    try:
        with open(input_file, "r") as src:
            content = src.readlines()
        
        with open(output_file, "w") as dest:
            dest.writelines(reversed(content))
        print("File content reversed successfully")
    except FileNotFoundError:
        print(f"❌ Source file not found error")

# Test it:
reverse_file('sample.txt', 'sample_reversed.txt')


# =======================
# EXERCISE 8: Filter Long Lines
# =======================
# Task: Read a file and write only lines with more than 50 characters to a new file
# Hint: Check len(line) for each line

print("\nExercise 8: Filter Long Lines")

def filter_long_lines(input_file, output_file):
    # Your code here:
    try:
        with open(input_file, "r") as src:
            lines = src.readlines()
        with open(output_file, "w") as dest:
            for line in lines:
                if len(line) > 50 :
                    dest.write(line)
        print("File updated successfully")
    except FileNotFoundError:
        print("File updated failed: 404")
# Test it:
filter_long_lines('sample.txt', 'long_lines.txt')


# =======================
# EXERCISE 9: File Statistics
# =======================
# Task: Create a function that returns statistics about a file:
# - Number of lines
# - Number of words
# - Number of characters
# Return as a dictionary

print("\nExercise 9: File Statistics")

def file_stats(filename):
    # Your code here:
    lines = 0
    characters = 0
    words = 0
    with open(filename) as file:
        for line in file:
            lines +=1
            word_list = line.split()
            words += len(word_list)
            characters += len(line)
        return {
            'lines': lines,
            'words': words,
            'characters': characters,
        }

# Test it:
stats = file_stats('sample.txt')
print(f"File stats: {stats}")


# =======================
# EXERCISE 10: Todo List Manager (CHALLENGE)
# =======================
# Task: Create a simple todo list manager with functions:
# - add_todo(task): Append a task to 'todos.txt'
# - view_todos(): Display all tasks
# - mark_done(task_number): Remove a task by its line number
# - clear_todos(): Delete all tasks

print("\nExercise 10: Todo List Manager")

def add_todo(task):
    # Your code here:
    with open('todos.txt', 'a') as file:
        file.write(f"{task}\n")
    return "Success"

def view_todos():
    # Your code here:
    with open('todos.txt') as file:
        print(f"TODOS: {file.read()}")

def mark_done(task):
    # Your code here:
    with open('todos.txt', 'r') as init_tasks:
        temp_tasks = init_tasks.readlines()

    with open('todos.txt', 'w') as tasks:
        for current_task in temp_tasks:
            print(f"Current: {current_task}")
            if current_task.strip() != task.strip():
                tasks.write(f"{current_task}")
    print("Successfully updated")

def clear_todos():
    # Your code here:
    with open('todos.txt', 'w') as tasks:
        tasks.write("")
    print("Cleared successfully")

# Test it:
add_todo("Learn Python file handling")
add_todo("Practice exercises")
add_todo("Build CLI calculator")
view_todos()
mark_done("Practice exercises")
view_todos()
clear_todos()


# =======================
# BONUS: CSV File Handler (ADVANCED)
# =======================
# Task: Create functions to work with CSV (comma-separated values)
# - read_csv(filename): Return list of lists (rows)
# - write_csv(filename, data): Write data to CSV
# - add_row(filename, row): Append a row to CSV

print("\nBonus: CSV File Handler")

def read_csv(filename):
    # Your code here:
    pass

def write_csv(filename, data):
    # Your code here:
    pass

def add_row(filename, row):
    # Your code here:
    pass

# Test it:
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', '25', 'NYC'],
#     ['Bob', '30', 'LA']
# ]
# write_csv('users.csv', data)
# add_row('users.csv', ['Charlie', '28', 'SF'])
# result = read_csv('users.csv')
# print(result)


print("\n" + "=" * 50)
print("File Handling Exercises - Complete when solved! ✅")
print("=" * 50)

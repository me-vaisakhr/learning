"""
FILE HANDLING BASICS
Learning how to read, write, and manipulate files in Python
"""

# =======================
# 1. READING FILES
# =======================

# Method 1: Basic file reading (manual close)
# file = open('example.txt', 'r')  # 'r' = read mode
# content = file.read()
# file.close()

# Method 2: Using 'with' statement (RECOMMENDED - auto closes file)
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# File Reading Methods:
# - read()           → Read entire file as string
# - readline()       → Read one line at a time
# - readlines()      → Read all lines into a list

# Example: Read entire file
with open('sample.txt', 'r') as file:
    content = file.read()
    print("Full content:")
    print(content)
    print()

# Example: Read line by line
with open('sample.txt', 'r') as file:
    print("Line by line:")
    for line in file:
        print(line.strip())  # strip() removes newline characters
    print()

# Example: Read all lines into a list
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    print("All lines as list:")
    print(lines)
    print()

# =======================
# 2. WRITING FILES
# =======================

# 'w' mode - Write (overwrites existing content)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")

# 'a' mode - Append (adds to existing content)
with open('output.txt', 'a') as file:
    file.write("This line is appended.\n")

# Writing multiple lines
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'a') as file:
    file.writelines(lines_to_write)

print("✅ Files written successfully!")
print()

# =======================
# 3. FILE MODES
# =======================

"""
File Modes:
'r'  → Read (default) - file must exist
'w'  → Write - creates new file or overwrites existing
'a'  → Append - adds to end of file
'r+' → Read and Write
'w+' → Write and Read (overwrites)
'a+' → Append and Read

Binary modes (for images, PDFs, etc.):
'rb' → Read binary
'wb' → Write binary
'ab' → Append binary
"""

# =======================
# 4. FILE EXISTS CHECK
# =======================

import os

# Check if file exists
if os.path.exists('sample.txt'):
    print("✅ sample.txt exists")
else:
    print("❌ sample.txt does not exist")

# Get file size
if os.path.exists('sample.txt'):
    size = os.path.getsize('sample.txt')
    print(f"File size: {size} bytes")

print()

# =======================
# 5. WORKING WITH PATHS
# =======================

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Join paths safely (works on all OS)
file_path = os.path.join('week1', 'sample.txt')
print(f"Joined path: {file_path}")

# Get absolute path
abs_path = os.path.abspath('sample.txt')
print(f"Absolute path: {abs_path}")

print()

# =======================
# 6. PRACTICAL EXAMPLES
# =======================

# Example 1: Count words in a file
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0

word_count = count_words('sample.txt')
print(f"Word count in sample.txt: {word_count}")
print()

# Example 2: Read CSV-like data
def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split(',')
                data.append(row)
        return data
    except FileNotFoundError:
        return []

# Example 3: Copy file content
def copy_file(source, destination):
    try:
        with open(source, 'r') as src:
            content = src.read()

        with open(destination, 'w') as dest:
            dest.write(content)

        print(f"✅ Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"❌ Source file {source} not found")

# copy_file('sample.txt', 'sample_copy.txt')

# Example 4: Append to log file
def log_message(message):
    with open('app.log', 'a') as log_file:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
print("✅ Log entries added")
print()

# =======================
# 7. ERROR HANDLING
# =======================

# Always handle file errors
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("❌ Error: File not found!")
except PermissionError:
    print("❌ Error: Permission denied!")
except Exception as e:
    print(f"❌ Error: {e}")

print()

# =======================
# 8. COMPARISON WITH JAVASCRIPT
# =======================

"""
Python vs JavaScript (Node.js) File Handling:

JavaScript (Node.js):
const fs = require('fs');
fs.readFileSync('file.txt', 'utf8');
fs.writeFileSync('file.txt', 'content');

Python:
with open('file.txt', 'r') as file:
    content = file.read()

with open('file.txt', 'w') as file:
    file.write('content')

Key Differences:
1. Python uses 'with' statement (context manager) - auto closes files
2. Python has simpler syntax for file operations
3. JavaScript requires fs module, Python has built-in open()
4. Python's 'with' prevents memory leaks automatically
5. Python modes ('r', 'w', 'a') vs JS flags
"""

# =======================
# 9. BEST PRACTICES
# =======================

"""
✅ DO's:
1. Always use 'with' statement - auto closes files
2. Handle FileNotFoundError exceptions
3. Use os.path.join() for cross-platform paths
4. Close files explicitly if not using 'with'
5. Use appropriate mode ('r', 'w', 'a')

❌ DON'Ts:
1. Don't forget to close files (use 'with')
2. Don't assume file exists - always check or handle error
3. Don't use 'w' mode if you want to preserve content
4. Don't hardcode file paths (use os.path)
5. Don't read huge files into memory at once (use line-by-line)
"""

print("=" * 50)
print("File Handling Basics - Complete! ✅")
print("=" * 50)

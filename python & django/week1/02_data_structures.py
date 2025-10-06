# Day 1: Data Structures - Lists, Tuples, Dictionaries, Sets
# JavaScript comparison included!

print("=== LISTS (like JS arrays) ===")
# Python lists are mutable (can be changed)
skills = ["JavaScript", "React", "HTML", "CSS"]
print(f"Skills: {skills}")

# Accessing elements (same as JS)
print(f"First skill: {skills[0]}")
print(f"Last skill: {skills[-1]}")  # Negative indexing! (Python feature)

# Adding items
skills.append("Python")  # JS: skills.push("Python")
print(f"After append: {skills}")

skills.insert(1, "TypeScript")  # Insert at index 1
print(f"After insert: {skills}")

# Removing items
skills.remove("HTML")  # Remove by value
print(f"After remove: {skills}")

last_skill = skills.pop()  # Remove and return last item
print(f"Popped: {last_skill}, Remaining: {skills}")

# List operations
print(f"Length: {len(skills)}")  # JS: skills.length
print(f"'React' in list? {'React' in skills}")  # JS: skills.includes('React')

# Slicing (powerful feature!)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nNumbers: {numbers}")
print(f"First 5: {numbers[:5]}")      # [0, 1, 2, 3, 4]
print(f"Last 3: {numbers[-3:]}")      # [7, 8, 9]
print(f"Middle: {numbers[3:7]}")      # [3, 4, 5, 6]
print(f"Every 2nd: {numbers[::2]}")   # [0, 2, 4, 6, 8]
print(f"Reversed: {numbers[::-1]}")   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# List methods
numbers_copy = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {numbers_copy}")
numbers_copy.sort()  # Sorts in place (mutates)
print(f"Sorted: {numbers_copy}")
numbers_copy.reverse()  # Reverses in place
print(f"Reversed: {numbers_copy}")

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # JS: [...list1, ...list2]
print(f"\nCombined: {combined}")

print("\n=== TUPLES (immutable lists) ===")
# Tuples cannot be changed after creation - use for fixed data
coordinates = (10, 20)
rgb = (255, 128, 0)

print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")
print(f"RGB: {rgb}")

# Tuple unpacking (super useful!)
x, y = coordinates
r, g, b = rgb
print(f"Unpacked - X: {x}, Y: {y}")
print(f"Unpacked - R: {r}, G: {g}, B: {b}")

# Tuples are used for functions returning multiple values
def get_user():
    return ("John", 25, "Developer")  # Return tuple

name, age, role = get_user()  # Unpack
print(f"\nUser: {name}, {age}, {role}")

# When to use what?
# List: When you need to modify data (mutable)
# Tuple: When data shouldn't change (immutable, faster)

print("\n=== DICTIONARIES (like JS objects) ===")
# Key-value pairs
user = {
    "name": "Vaisakh",
    "age": 25,
    "role": "React Developer",
    "skills": ["React", "JavaScript"],
    "is_learning_python": True
}

print(f"User: {user}")

# Accessing values
print(f"\nName: {user['name']}")  # JS: user.name or user['name']
print(f"Role: {user['role']}")

# Safe access with .get() (returns None if key doesn't exist)
print(f"Email: {user.get('email')}")  # Returns None
print(f"Email: {user.get('email', 'Not provided')}")  # Default value

# Adding/updating
user["email"] = "vaisakh@example.com"
user["age"] = 26  # Update existing key
print(f"\nUpdated user: {user}")

# Dictionary methods
print(f"\nKeys: {user.keys()}")
print(f"Values: {user.values()}")
print(f"Items: {user.items()}")  # Key-value pairs

# Looping through dictionary
print("\nUser info:")
for key, value in user.items():
    print(f"  {key}: {value}")

# Check if key exists
print(f"\n'name' in user? {'name' in user}")
print(f"'phone' in user? {'phone' in user}")

# Nested dictionaries (like JS objects)
project = {
    "name": "E-commerce App",
    "tech_stack": {
        "frontend": "React",
        "backend": "Django",
        "database": "PostgreSQL"
    },
    "team": ["Alice", "Bob", "Charlie"]
}

print(f"\nProject: {project['name']}")
print(f"Backend: {project['tech_stack']['backend']}")
print(f"Team: {project['team']}")

print("\n=== SETS (unique collections) ===")
# Sets store unique values only (like JS Set)
fruits = {"apple", "banana", "orange"}
print(f"Fruits: {fruits}")

# Adding duplicates has no effect
fruits.add("apple")
fruits.add("mango")
print(f"After adding: {fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")  # All unique values
print(f"Intersection: {set1 & set2}")  # Common values
print(f"Difference: {set1 - set2}")  # In set1 but not set2

# Use case: Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_dupes))
print(f"\nWith duplicates: {numbers_with_dupes}")
print(f"Unique: {unique_numbers}")

print("\n=== QUICK REFERENCE ===")
print("""
List:    [1, 2, 3]           - Ordered, mutable, allows duplicates
Tuple:   (1, 2, 3)           - Ordered, immutable, allows duplicates
Dict:    {"key": "value"}    - Key-value pairs, mutable
Set:     {1, 2, 3}           - Unordered, mutable, unique values only
""")

print("🎯 KEY DIFFERENCES FROM JAVASCRIPT:")
print("1. Lists use [] but have more features than JS arrays")
print("2. Tuples () are immutable - JS doesn't have this")
print("3. Dicts use {} with explicit keys (not object literal syntax)")
print("4. Negative indexing: list[-1] gets last item")
print("5. Slicing: list[start:end:step] is super powerful")
print("6. Sets {} automatically remove duplicates")

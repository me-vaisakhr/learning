# Exercise 2: Data Structures
# Practice with Lists, Tuples, Dictionaries, and Sets

print("=== EXERCISE 2: DATA STRUCTURES ===\n")

# TODO 1: Create a list of your favorite programming languages
# Add at least 5 languages, then:
# - Print the list
# - Print the first and last language
# - Add a new language to the end
# - Insert a language at position 2
# - Remove one language
# - Print the final list and its length
languages = ['React', 'Nodejs', 'Python', 'Django', 'Angular']
print(f"Language List : {languages}")
print(f"First : {languages[0]}, Last : {languages[-1]}")
languages.append('HTML')
languages.insert(2, 'CSS')
languages.remove("Angular")
print(f"Final List : {languages}")


# TODO 2: List slicing practice
# Create a list: days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# Print:
# - Weekdays (first 5)
# - Weekend (last 2)
# - Every other day (starting from Monday)
# - Days in reverse order
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(f"Weekdays: {days[:5]}")
print(f"Weekends: {days[5:]}")
print(f"Every other day: {days[::2]}")
print(f"Reverse Order: {days[::-1]}")


# TODO 3: Create a dictionary for a book
# Include: title, author, year, pages, is_read (boolean), genres (list)
# Print the dictionary in a formatted way
# Update is_read to True
# Add a new key "rating" with a value 1-5
# Print all keys and values
book = {
    "title": "ABCD",
    "author": "EFGH",
    "year": 2025,
    "pages": 10,
    "is_read": False,
    "genres": ['Fiction']
}
print(f"Book: {book}")
book["is_read"] = True
book["rating"] = 4.5
for key, value in book.items():
    print(f"{key}: {value}")


# TODO 4: Nested dictionary - Create your project portfolio
# Create a dictionary with 2 projects, each project should have:
# - name, description, tech_stack (list), year, status (completed/in-progress)
# Print each project's name and tech stack
projects = {
    "project_1": {
        "name": "Sample 1",
        "description": "Lorem ipsum",
        "tech_stack": ['React'],
        "year": 2025,
        "status": "in-progress"
    },
    "project_2": {
        "name": "Sample 2",
        "description": "Lorem ipsum",
        "tech_stack": ['React', 'NodeJS'],
        "year": 2025,
        "status": "completed"
    },
}

for project in projects:
    print(f"\nProjects: {projects[project]["name"]} > {projects[project]["tech_stack"]}")


# TODO 5: Sets practice
# Create two sets:
# - frontend_skills = {"HTML", "CSS", "JavaScript", "React", "Vue"}
# - backend_skills = {"Python", "Django", "JavaScript", "SQL", "Node.js"}
# Find and print:
# - All unique skills (union)
# - Common skills (intersection)
# - Frontend-only skills (difference)

frontend_skills = {"HTML", "CSS", "JavaScript", "React", "Vue"}
backend_skills = {"Python", "Django", "JavaScript", "SQL", "Node.js"}

print(f"Unique Skills {frontend_skills | backend_skills}")
print(f"Common skills {frontend_skills & backend_skills}")
print(f"Frontend-only {frontend_skills - backend_skills}")
# TODO 6: Remove duplicates
# Given this list: scores = [85, 90, 85, 78, 90, 92, 78, 88, 90]
# Remove duplicates and print the unique scores in sorted order
scores = [85, 90, 85, 78, 90, 92, 78, 88, 90]
print(f"List without duplicates: {list(set(scores))}")


# TODO 7: Tuple unpacking
# Create a tuple: student = ("Alice", 22, "Computer Science", 3.8)
# Unpack it into: name, age, major, gpa
# Print: "Alice is 22 years old, majoring in Computer Science with a 3.8 GPA"
student = ("Alice", 22, "Computer Science", 3.8)
name, age, major, gpa = student
print(f"{name} is {age} years old, majoring in {major} with a {gpa} GPA")


# TODO 8: List of dictionaries (common pattern!)
# Create a list of 3 users, each user is a dictionary with:
# - name, age, role, skills (list)
# Loop through and print each user's name and number of skills
# Hint: "John has 5 skills"
users = [
    {
       "name": "ABCD1",
       "age": 10,
       "role": "student",
       "skills": ["asd"]
    },
    {
       "name": "ABCD2",
       "age": 10,
       "role": "student",
       "skills": ["sdf","sdfs"]
    },
    {
       "name": "ABCD3",
       "age": 10,
       "role": "student",
       "skills": ["jdfkbg","kdfngk","dfg"]
    },
]

for user in users:
    print(f"{user["name"]} has {len(user["skills"])} skills")


print("\n✅ Exercise complete! Check your solution when ready.")

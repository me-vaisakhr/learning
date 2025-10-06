# Exercise 1: Variables and Data Types
# Complete the TODOs below

print("=== EXERCISE 1 ===\n")

# TODO 1: Create variables for your information
# Create: first_name, last_name, current_role, years_of_experience, is_fulltime
first_name = "John"
last_name = "Doe"
current_role = "manager"
years_of_experience = 5
is_fulltime = True


# TODO 2: Print a formatted introduction using f-strings
# Example: "Hi, I'm John Doe, a Senior Developer with 5 years of experience."
print(f"Hi, I'm {first_name} {last_name}, a {current_role} with {years_of_experience} years of experience.")

# TODO 3: Calculate and print your experience in months
# Hint: years_of_experience * 12
years_of_experience_in_months = years_of_experience * 12
print(f"Experience in months: {years_of_experience_in_months}")


# TODO 4: Create a variable for your hourly rate (as a float)
# Calculate your daily rate (8 hours) and print it
hourly_rate = 50.0
daily_rate = hourly_rate * 8
print(f"Daily Rate: {daily_rate}")

# TODO 5: String manipulation
# Take your full name, convert it to uppercase, then print just your initials
# Example: "JOHN DOE" -> "J.D."
print(f"{first_name.upper()} {last_name.upper()} -> {first_name[0].upper()}.{last_name[0].upper()}")


# TODO 6: Temperature converter
# Create a variable celsius = 25
# Convert to Fahrenheit using: (celsius * 9/5) + 32
# Print: "25°C is 77°F"
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is {fahrenheit}°F")


# TODO 7: Check your knowledge
# Create a boolean variable for each:
# - knows_javascript
# - knows_python
# - knows_django
# Print them with appropriate labels
knows_javascript = True
knows_python = False
knows_django = False
print(f"""
Javascript : {knows_javascript}
Python : {knows_python}
Django : {knows_django}
""")


print("\n✅ Exercise complete! Compare with solution when ready.")

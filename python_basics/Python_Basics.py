# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    Python_Basics.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/03/31 23:52:16 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/03/31 23:53:05 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# Declare and initialize variables
name = "John"
age = 25
height = 1.8
is_student = True

# Print out variable values using f-strings
print(f"My name is {name}, I'm {age} years old, and I'm {height} meters tall.")
if is_student:
    print("I'm a student.")
else:
    print("I'm not a student.")

# Create a list and loop through it
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}s.")

# Create a dictionary and access its values
person = {"name": "Mary", "age": 30, "is_student": False}
print(f"{person['name']} is {person['age']} years old.")
if person["is_student"]:
    print(f"{person['name']} is a student.")
else:
    print(f"{person['name']} is not a student.")
    
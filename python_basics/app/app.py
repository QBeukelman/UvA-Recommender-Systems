# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    app.py                                             :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/03/31 23:52:01 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/03/31 23:52:06 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# Retrieve input from user
first = input("First: ")
second = input("Second: ")


# Type cast to float
sum = float(first) + float(second)
print("The sum is: " + str(sum))


# Operators
print(sum > 10.0 or sum < 30.0)
print(sum > 10.0 and sum < 30.0)
print(not sum > 100)


# If
if sum > 30:
	print("It's a hot day")
elif sum < 10:
	print ("It's a cold day")


# Loops
i = 1
while i <= 5:
	print(i * '*');
	i += 1


# While
i = 1
names = []
while i <= 5:
	names.append("name_" + str(i))
	i += 1
print(names)


# Range
numbers = range(5)
for item in numbers:
	print(item)


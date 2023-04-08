# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    Python_Program.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/03/31 23:52:49 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/03/31 23:53:31 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# Define a function to add two numbers
def add_numbers(x, y):
    return x + y

# Define a function to subtract two numbers
def subtract_numbers(x, y):
    return x - y

# Define a main function to call the other functions
def main():
    # Call the add_numbers function and print the result
    sum = add_numbers(5, 7)
    print(f"The sum is {sum}")

    # Call the subtract_numbers function and print the result
    difference = subtract_numbers(10, 3)
    print(f"The difference is {difference}")

# Call the main function
if __name__ == "__main__":
    main()

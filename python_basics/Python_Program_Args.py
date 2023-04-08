# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    Python_Program_Args.py                             :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/03/31 23:52:28 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/03/31 23:53:31 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# python3 Python_Program_Args.py Alice
# python3 greet.py Alice
# python3 greet.py

import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    greet(name)

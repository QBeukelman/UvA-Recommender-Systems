# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    nearest_neighbour.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/11 13:01:17 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/11 13:01:28 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('movie_name', type=str, help='Name of a movie')
    args = parser.parse_args()

    # Print the movie name
    print(args.movie_name)

if __name__ == '__main__':
    main()


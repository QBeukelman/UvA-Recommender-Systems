# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    recommend_movies.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/12 14:50:09 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/12 16:22:17 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import csv
import sys
from termcolor import colored

# ==============================================================================: RECOMMEND
def ft_recommend_list(movie_id):
    with open('../data/cosign_similarity_matrix.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        similarity_scores = {}
        
        for row in reader:
            if row[0] == movie_id:
                for i in range(1, len(row)):
                    similarity_scores[header[i]] = float(row[i])
                break

    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    top_movies = [movie[0] for movie in sorted_scores[:10]]
    
    if movie_id in top_movies:
        top_movies.remove(movie_id)  # remove searched movie from recommended movies
    sim_values = [movie[1] for movie in sorted_scores[:10]]
    
    if movie_id in top_movies:
        sim_values.remove(similarity_scores[movie_id])  # remove similarity score for searched movie

    return top_movies, sim_values


# ==============================================================================: ID TO TITLE
def ft_id_to_title(movie_ids):
    movie_names = []
    with open('../data/movies.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        movie_data = {}
        for row in reader:
            movie_data[row[0]] = row[1]

    for movie_id in set(movie_ids):  # Use set to remove duplicates
        if movie_id in movie_data:
            movie_names.append(movie_data[movie_id])

    return movie_names


# ==============================================================================: GET ID
def ft_get_id(movie_name):
    with open('../data/movies.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == movie_name:
                return row[0]
    return None


# ==============================================================================: MAIN 
def main():
    movie_name = sys.argv[1]
    movie_id = ft_get_id(movie_name)
    if movie_id:
        print(colored(f"\nHere are some movies like: '{movie_name}'\n", attrs=['bold']))
        top_movies, sim_values = ft_recommend_list(movie_id)
        top_movies_titles = ft_id_to_title(top_movies)
        print(colored("{:<60} {:<10}".format("Title", "Similarity"), attrs=['bold']))
        
        for i in range(len(top_movies_titles)):
            title = colored(top_movies_titles[i], 'green')
            similarity = colored("{:.4f}".format(sim_values[i]), 'yellow')
            print("{:<60} {:<10}".format(title, similarity))

    else:
        print(colored(f"No movie with name '{movie_name}' found in file.", 'red'))

if __name__ == '__main__':
    main()


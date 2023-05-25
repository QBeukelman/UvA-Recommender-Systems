# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    recommend_movies_user.py                           :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/18 19:45:10 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/05/25 10:24:45 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import csv
import sys
from termcolor import colored

# ==============================================================================: RECOMMEND
def ft_recommend_list(ui, n=10, threshold=0.5):
    with open('../data/cosign_similarity_matrix.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        similarity_scores = {}

        for row in reader:
            movie_title = row[0]
            if ui.lower() in movie_title.lower():
                for i in range(1, len(row)):
                    similarity_scores[header[i]] = float(row[i])

        sorted_scores = ft_sort_scores(similarity_scores, threshold)
        top_movies = [movie[0] for movie in sorted_scores[:n]]
        sim_values = [movie[1] for movie in sorted_scores[:n]]

        return top_movies, sim_values
        

def ft_sort_scores(similarity_scores, threshold):
    weighted_scores = {}
    for movie, score in similarity_scores.items():
        if score < 1.0:
            weighted_scores[movie] = score
    sorted_scores = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_scores = [(movie, score) for movie, score in sorted_scores if score >= threshold]
    return sorted_scores


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


# ==============================================================================: MAIN 
def main(ui):
    print(colored(f"\nHere are some movies related to: '{ui}'\n", attrs=['bold']))
    top_movies, sim_values = ft_recommend_list(ui)
    top_movies_titles = ft_id_to_title(top_movies)
    print(colored("{:<60} {:<10}".format("Title", "Cosign Similarity"), attrs=['bold']))

    for i in range(len(top_movies_titles)):
        title = colored(top_movies_titles[i], 'green')
        similarity = colored("{:.4f}".format(sim_values[i]), 'yellow')
        print("{:<60} {:<10}".format(title, similarity))

if __name__ == '__main__':
    ui = input("Enter a UI: ")
    main(ui)

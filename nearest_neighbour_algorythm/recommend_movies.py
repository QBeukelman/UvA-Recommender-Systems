# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    recommend_movies.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/12 14:50:09 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/12 15:12:00 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import csv
import sys


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
    return top_movies


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
        print(f"Here are 10 movies like: '{movie_name}'")
        top_movies = ft_recommend_list(movie_id)
        top_movies_titles = ft_id_to_title(top_movies)
        for title in top_movies_titles:
            print(title)
    else:
        print(f"No movie with name '{movie_name}' found in file.")

if __name__ == '__main__':
    main()

# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    nearest_neighbour.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/08 07:20:20 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/11 10:37:34 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import math
import argparse
import matplotlib.pyplot as plt
from scipy import sparse
import re


# 		 M1		  M2	  M3	
# M1	  1		-0.12	 0.16
# M2	-0.12	  1		-0.51
# M3	 0.16	-0.51	  1

# ==============================================================================: Similarity Matrix
def ft_similarity_matrix(ratings_table, user_ids):
    num_users = len(user_ids)
    similarity_matrix = np.zeros((num_users, num_users))
    for i in range(num_users):
        for j in range(i, num_users):
            user1 = user_ids[i]
            user2 = user_ids[j]
            if user1 not in ratings_table.index or user2 not in ratings_table.index:
                continue
            movie_ratings1 = ratings_table.loc[user1].values
            movie_ratings2 = ratings_table.loc[user2].values
            common_movies = np.logical_and(~np.isnan(movie_ratings1), ~np.isnan(movie_ratings2))
            if np.sum(common_movies) < 2:
                continue
            movie_ratings1 = movie_ratings1[common_movies]
            movie_ratings2 = movie_ratings2[common_movies]
            similarity_matrix[i,j] = ft_cosine_similarity(movie_ratings1, movie_ratings2)
            similarity_matrix[j,i] = similarity_matrix[i,j]
    return similarity_matrix


def ft_cosine_similarity(array1, array2):
    dot_product = sum(array1[i]*array2[i] for i in range(len(array1)))
    magnitude1 = math.sqrt(sum([val**2 for val in array1]))
    magnitude2 = math.sqrt(sum([val**2 for val in array2]))
    
    # check for division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    similarity = dot_product/(magnitude1*magnitude2)
    return similarity



# ==============================================================================: Utility Matrix
def ft_load_ratings_table():
    # MovieLens dataset
    movies_df = pd.read_csv('../data/movies.csv') # Features
    ratings_df = pd.read_csv('../data/ratings.csv') # Data Points
    merged_df = pd.merge(movies_df, ratings_df, on='movieId')
    
    # Remove rows with non-integer movie IDs
    merged_df = merged_df[merged_df['movieId'].astype(str).str.isdigit()]
    # Remove non-numeric characters from title column
    merged_df['title'] = merged_df['title'].str.replace(r'\D', '')

    # Remove non-numeric characters from title column
    user_ids = []
    for user_id in merged_df['userId'].unique():
        user_ratings = merged_df[merged_df['userId'] == user_id]
        movie_ids = [x for x in user_ratings['title'].tolist() if x != '']  # <-- Skip movies with empty ids
        user_ids.append(user_id)
        # print(f"User {user_id} movie IDs: {movie_ids}")
            
    # Utility Matrix
    ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title'])
    ratings_table.fillna(0, inplace=True)

    # Check dimensions of ratings table
    num_users, num_movies = ratings_table.shape

    # Reshape ratings table to have same number of rows and columns
    if num_users > num_movies:
        pad_cols = np.zeros((num_users, num_users - num_movies))
        ratings_table = pd.concat([ratings_table, pd.DataFrame(pad_cols)], axis=1)
    else:
        pad_rows = np.zeros((num_movies - num_users, num_movies))
        ratings_table = pd.concat([ratings_table, pd.DataFrame(pad_rows)])

    # Range of sample set
    ratings_table = ratings_table.iloc[:400, :]
    ratings_table = ratings_table.iloc[:, :400]

    print(ratings_table)
    return ratings_table




# ==============================================================================: MAIN
def main():
    
    # Load ratings table
    ratings_table = ft_load_ratings_table()
    # print(ratings_table.columns)

    # Extract user IDs
    user_ids = list(ratings_table.index)

    # Calculate similarity matrix
    similarity_matrix = ft_similarity_matrix(ratings_table, user_ids)
    
    # Heatmap
    plt.figure(figsize=(12,12))
    plt.imshow(similarity_matrix, cmap='hot', interpolation='nearest')
    plt.title('Movie Similarity Heatmap')
    plt.xlabel('Movie ID')
    plt.ylabel('Movie ID')
    plt.colorbar()
    plt.show()
    
if __name__ == '__main__':
    main()


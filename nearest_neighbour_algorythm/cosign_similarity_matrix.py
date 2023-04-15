# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    cosign_similarity_matrix.py                        :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/11 12:50:06 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/15 22:36:41 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import sparse
import re

# Normalized Cosign Similarity Matrix

# 		 M1		  M2	  M3	
# M1	  1		-0.12	 0.16
# M2	-0.12	  1		-0.51
# M3	 0.16	-0.51	  1

# ==============================================================================: Similarity Matrix
def ft_similarity_matrix(ratings_table, user_ids):
    num_users = len(user_ids)
    similarity_matrix = np.zeros((num_users, num_users))
    i = 0
    while i < num_users:
        j = i
        while j < num_users:
            user1 = user_ids[i]
            user2 = user_ids[j]
            if user1 not in ratings_table.index or user2 not in ratings_table.index:
                j += 1
                continue
            movie_ratings1 = ratings_table.loc[user1].values
            movie_ratings2 = ratings_table.loc[user2].values
            common_movies = np.logical_and(~np.isnan(movie_ratings1), ~np.isnan(movie_ratings2))
            if np.sum(common_movies) < 2:
                j += 1
                continue
            movie_ratings1 = movie_ratings1[common_movies]
            movie_ratings2 = movie_ratings2[common_movies]
            similarity_matrix[i,j] = ft_cosine_similarity(movie_ratings1, movie_ratings2)
            similarity_matrix[j,i] = similarity_matrix[i,j]
            j += 1
        i += 1
    return similarity_matrix


def ft_cosine_similarity(array1, array2):
    # Subtract the row mean from each array
    mean1 = np.nanmean(array1)
    array1 = array1 - mean1
    mean2 = np.nanmean(array2)
    array2 = array2 - mean2
    
    # Calculate dot product of the two arrays
    i = 0
    dot_product = 0
    while i < len(array1):
        dot_product += array1[i] * array2[i]
        i += 1
    
    # Calculate magnitudes of each array
    i = 0
    magnitude1 = 0
    magnitude2 = 0
    while i < len(array1):
        magnitude1 += array1[i] ** 2
        magnitude2 += array2[i] ** 2
        i += 1
    magnitude1 = math.sqrt(magnitude1)
    magnitude2 = math.sqrt(magnitude2)
    
    # check for division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    similarity = dot_product / (magnitude1 * magnitude2)
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
    merged_df['title'] = merged_df['title'].str.replace(r'\D', '', regex=True)

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
    ratings_table = ratings_table.iloc[:1000, :]
    ratings_table = ratings_table.iloc[:, :1000]

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
    
	# Write similarity matrix to CSV file
    # similarity_matrix_df = pd.DataFrame(similarity_matrix, index=user_ids, columns=user_ids)
    # similarity_matrix_df.to_csv('../data/cosign_similarity_matrix.csv', index=True, header=True)
    
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


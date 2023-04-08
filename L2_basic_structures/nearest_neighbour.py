# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    nearest_neighbour.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/08 07:20:20 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/08 11:03:53 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import math
import argparse
from scipy import sparse

# 		 M1		  M2	  M3	
# M1	  1		-0.12	 0.16
# M2	-0.12	  1		-0.51
# M3	 0.16	-0.51	  1

# ==============================================================================: Similarity Matrix
def ft_similarity_matrix(ratings_table, user_ids):
    # Normalize the ratings_table by subtracting the mean of each row
    normalized_ratings = ratings_table.apply(lambda x: (x - np.mean(x)), axis=1)

    # Create three lists to be used to create the sparse matrix
    movie_ids = list(normalized_ratings.columns)
    movie_ratings = [list(normalized_ratings.iloc[i]) for i in range(len(normalized_ratings))]

    # Get the total number of unique users and movies
    num_users = ratings_table.shape[0]
    num_movies = ratings_table.shape[1]

    # Indices start at 0 and end at num_users-1 and num_movies-1
    movie_ids = [int(x) - 1 for x in movie_ids]
    movie_ids = [x - 1 for x in movie_ids]

    # Create the sparse matrix
    ratings_sparse = sparse.coo_matrix((movie_ratings, (user_ids, movie_ids)), shape=(num_users, num_movies))

    # Compute the cosine similarity matrix
    similarity_matrix = cosine_similarity(ratings_sparse.T, dense_output=False)
    return similarity_matrix


def ft_cosine_similarity(matrix):
    num_rows, num_cols = matrix.shape
    similarity_matrix = np.zeros((num_rows, num_rows))

    for i in range(num_rows):
        for j in range(i+1, num_rows):
            dot_product = sum(matrix[i,k]*matrix[j,k] for k in range(num_cols))
            magnitude1 = math.sqrt(sum([val**2 for val in matrix[i,:]]))
            magnitude2 = math.sqrt(sum([val**2 for val in matrix[j,:]]))
            similarity_matrix[i,j] = dot_product/(magnitude1*magnitude2)
            similarity_matrix[j,i] = similarity_matrix[i,j]

    return similarity_matrix


# ==============================================================================: Utility Matrix
def ft_load_ratings_table():
    # MovieLens dataset
    movies_df = pd.read_csv('../data/movies.csv') # Features
    ratings_df = pd.read_csv('../data/ratings.csv') # Data Points
    merged_df = pd.merge(movies_df, ratings_df, on='movieId')
    # Remove columns with non-integer movie IDs
    invalid_columns = [col for col in merged_df.columns if not col.startswith("movieId_")]
    merged_df.drop(columns=invalid_columns, inplace=True)
    
    # Utility Matrix
    ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title']) # columns=['title']
    return ratings_table



# ==============================================================================: MAIN
def main():
    # Load ratings table
    ratings_table = ft_load_ratings_table()
    # print(ratings_table.columns)

    # # Extract user IDs
    # user_ids = list(ratings_table.index)

    # # Calculate similarity matrix
    # similarity_matrix = ft_similarity_matrix(ratings_table, user_ids)

    # # Find nearest neighbors
    # k = 10
    # nearest_neighbors = ft_find_nearest_neighbors(similarity_matrix, k)

    # # Print results
    # print("Nearest neighbors:")
    # print(nearest_neighbors)
    
    # Heatmap
    # plt.imshow(similarity_matrix, cmap='hot', interpolation='nearest')
    # plt.title('Movie Similarity Heatmap')
    # plt.xlabel('Movie ID')
    # plt.ylabel('Movie ID')
    # plt.colorbar()
    # plt.show()
    
if __name__ == '__main__':
    main()















# # ==============================================================================: Similar Users
# def ft_find_similar_users(user_id, movie_title, ratings_table):
# 	# 1. Calculate similarity 
# 		# --> Similarity Matrix (-1 to 1) 
# 		# --> To what extent is one film a good indicator for another film
# 	# 2. Find a neighbourhood
# 	# 3. Find a Rating form neighbourhood
# 	# 4. Determine which item to recommend


# # ==============================================================================: Rating Bool
# def ft_rating_is_present(rating):
# 	if pd.isnull(rating):
# 		return True
# 	else:
# 		return False


# # ==============================================================================: Ratings
# def ft_fill_in_ratings(ratings_table):

# 	user_index = 0

# 	# Loop through each user in the ratings table
# 	while user_index < len(ratings_table.index):
# 		user_id = ratings_table.index[user_index]
# 		# print("User ID:", user_id)

# 		# Loop through each movie in the ratings table
# 		movie_index = 0
# 		rating_count = 0
# 		while movie_index < len(ratings_table.columns):

# 			movie_title = ratings_table.columns[movie_index]
# 			rating = ratings_table.loc[user_id, movie_title]

# 			if ft_rating_is_present(rating):
# 				rating_count += 1
# 				ft_find_similar_users(user_id, movie_title, ratings_table)

# 			movie_index += 1

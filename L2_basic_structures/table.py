# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    table.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/08 06:56:04 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/08 06:59:17 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd

# Load the MovieLens dataset
movies_df = pd.read_csv('../data/movies.csv')
ratings_df = pd.read_csv('../data/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Create a pivot table with user IDs as rows, movie titles as columns, and ratings as values
ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title'])

# Count the number of missing values and non-missing values in the ratings table
num_cells_with_rating = ratings_table.notna().sum().sum()
num_cells_without_rating = ratings_table.isna().sum().sum()

# Print the results
print(f"Number of cells with a rating: {num_cells_with_rating}")
print(f"Number of cells without a rating: {num_cells_without_rating}")

# Show the ratings table
print(ratings_table)
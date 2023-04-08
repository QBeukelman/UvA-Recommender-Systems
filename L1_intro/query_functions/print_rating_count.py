# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    rating_count.py                                    :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/04 21:49:00 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/04 21:49:26 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd

# Load the MovieLens dataset
movies_df = pd.read_csv('ml-latest-small/movies.csv')
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Count the number of ratings for each movie
movie_ratings = ratings_df['movieId'].value_counts()

# Get the 10 movies with the lowest number of ratings
min_movie_ids = movie_ratings.sort_values().head(100).index

# Get the titles of the 10 movies with the lowest number of ratings
min_movie_titles = movies_df[movies_df['movieId'].isin(min_movie_ids)]['title']

# Print the titles of the 10 movies with the lowest number of ratings
print("The 10 movies with the lowest amount of ratings are:")
for title in min_movie_titles:
    print("- {}".format(title))

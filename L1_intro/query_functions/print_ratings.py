# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    print_ratings.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/04 21:48:53 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/04 21:49:54 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd

# Load the MovieLens dataset
movies_df = pd.read_csv('ml-latest-small/movies.csv')
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Print top 10
# Group the ratings DataFrame by movie ID and count the number of ratings for each movie
movie_ratings_count = ratings_df.groupby('movieId').count()['rating'].reset_index()

# Sort the movie ratings count DataFrame in descending order by number of ratings
sorted_movie_ratings_count = movie_ratings_count.sort_values('rating', ascending=False)

# Merge the sorted movie ratings count DataFrame with the movies DataFrame to get the movie titles
top_rated_movies = pd.merge(sorted_movie_ratings_count, movies_df, on='movieId')

# Display the top 10 movies with the most ratings
print(top_rated_movies[['title', 'rating']].head(10))
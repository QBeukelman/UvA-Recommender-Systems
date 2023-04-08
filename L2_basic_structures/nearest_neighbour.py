# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    nearest_neighbour.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/08 07:20:20 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/08 08:00:27 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd

def rating_is_present(rating):
	if pd.isna(rating):
		return True
	else:
		return False
	

def fill_in_ratings(ratings_table):

	user_index = 0

	# Loop through each user in the ratings table
	while user_index < len(ratings_table.index):
		user_id = ratings_table.index[user_index]
		# print("User ID:", user_id)

		# Loop through each movie in the ratings table
		movie_index = 0
		rating_count = 0
		while movie_index < len(ratings_table.columns):

			movie_title = ratings_table.columns[movie_index]
			rating = ratings_table.loc[user_id, movie_title]
			
			# print(f"Rating for '{movie_title}': {rating}")

			if rating_is_present(rating):
				rating_count += 1

			movie_index += 1

		print(f"User '{user_id}': {rating_count}")
		user_index += 1


def load_ratings_table():
    # Load the MovieLens dataset
    movies_df = pd.read_csv('../data/movies.csv')
    ratings_df = pd.read_csv('../data/ratings.csv')

    # Merge the movies and ratings DataFrames
    merged_df = pd.merge(movies_df, ratings_df, on='movieId')

    # Create a pivot table with user IDs as rows, movie titles as columns, and ratings as values
    ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title'])

    return ratings_table


def main():
	ratings_table = load_ratings_table()
	fill_in_ratings(ratings_table)
	
if __name__ == '__main__':
    main()

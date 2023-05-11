# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    knn_cosign.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/05/09 12:15:13 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/05/11 12:46:47 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def ft_load_ratings_table():
    # MovieLens dataset
    movies_df = pd.read_csv('../../data/movies.csv')
    ratings_df = pd.read_csv('../../data/ratings.csv')
    # Create ratings table
    ratings_table = pd.pivot_table(ratings_df, values='rating', index='userId', columns='movieId')

    # Resize the ratings table to 300x300
    # ratings_table = ratings_table.iloc[:600, :600]

    return ratings_table

def ft_predict_rating(ratings_table):
    # Calculate the mean rating for each user
    user_means = ratings_table.mean(axis=1)

    # ! Replace NaN values with the mean rating of the corresponding user
    for user_id in ratings_table.index:
        ratings_table.loc[user_id] = ratings_table.loc[user_id].fillna(user_means[user_id])

    # Calculate the similarity matrix using cosine similarity
    similarity_matrix = cosine_similarity(ratings_table)

    # print(similarity_matrix)
    # print("Shape of similarity_matrix:", similarity_matrix.shape)

    # Create a new ratings table with the same dimensions as the original
    predicted_ratings_table = ratings_table.copy()

    # Iterate over each user and movie
    for user_id in ratings_table.index:
        for movie_id in ratings_table.columns:
            if np.isnan(ratings_table.loc[user_id, movie_id]):
                # Get the users who have rated the current movie
                movie_raters = ratings_table[movie_id].dropna().index

                # Get the similarity values between the current user and each movie rater
                user_similarities = similarity_matrix[user_id][movie_raters]

                # Get the ratings of each movie rater for the current movie
                movie_ratings = ratings_table.loc[movie_raters, movie_id]

                # Calculate the predicted rating using the weighted average formula
                weighted_sum = np.dot(user_similarities, movie_ratings)
                sim_sum = np.abs(user_similarities).sum()
                if sim_sum != 0:
                    predicted_rating = user_means[user_id] + weighted_sum / sim_sum
                else:
                    predicted_rating = user_means[user_id]

                # Store the predicted rating in the predicted_ratings_table
                predicted_ratings_table.loc[user_id, movie_id] = predicted_rating

    return predicted_ratings_table

def main():
    # Load ratings table
    ratings_table = ft_load_ratings_table()
    print(ratings_table)
    print("Number of ratings not null or NaN in ratings_table:", ratings_table.notnull().sum().sum())

    # Predict ratings for unrated movies
    ratings_table = ratings_table.fillna(ratings_table.mean(axis=1))
    predicted_ratings_table = ft_predict_rating(ratings_table)
    print(predicted_ratings_table)
    print("Number of ratings not null or NaN in predicted_ratings_table:", predicted_ratings_table.notnull().sum().sum())

    # Save the new ratings table
    predicted_ratings_table.to_csv('../../data/new_ratings.csv')

if __name__ == '__main__':
    main()

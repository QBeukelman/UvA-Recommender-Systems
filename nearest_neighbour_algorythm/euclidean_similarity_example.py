# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    euclidean_similarity_example.py                    :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/16 09:28:22 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/16 10:00:09 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd
import math

# ==============================================================================: DATA
def ft_get_data():
    # Load the MovieLens dataset
    movies_df = pd.read_csv('../data/movies.csv')
    ratings_df = pd.read_csv('../data/ratings.csv')

    # Merge the movies and ratings DataFrames
    merged_df = pd.merge(movies_df, ratings_df, on='movieId')

    # Filter the DataFrame to only include ratings for Forrest Gump, Pulp Fiction, and Body Parts
    movies = ['Forrest Gump (1994)', 'Pulp Fiction (1994)', 'Body Parts (1991)']
    merged_df = merged_df[merged_df['title'].isin(movies)]

    # Get the ratings for each movie
    forrest_gump_ratings = merged_df[merged_df['title'] == 'Forrest Gump (1994)']
    pulp_fiction_ratings = merged_df[merged_df['title'] == 'Pulp Fiction (1994)']
    body_parts_ratings = merged_df[merged_df['title'] == 'Body Parts (1991)']

    # Join the ratings DataFrames on the userId column
    ratings = pd.merge(pulp_fiction_ratings[['userId', 'rating']], forrest_gump_ratings[['userId', 'rating']], on='userId', suffixes=['_pulp', '_gump'])

    return ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings


# ==============================================================================: PLOT
def ft_scatter_plot(ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings):
    # Adjust the window size
    plt.figure(figsize=(12, 12))

    # Create a scatter plot of the ratings for Forrest Gump and Pulp Fiction
    plt.scatter(ratings['rating_pulp'], ratings['rating_gump'], alpha=0.1, s=500)

    # Mark the ratings for users who have also rated "Body Parts (1991)" in blue
    # and for those who haven't in red
    common_users = set(pulp_fiction_ratings['userId']).intersection(forrest_gump_ratings['userId'])
    for user_id in common_users:
        matrix_rating = body_parts_ratings[(body_parts_ratings['userId'] == user_id)]['rating'].iloc[0] if body_parts_ratings[(body_parts_ratings['userId'] == user_id)].shape[0] > 0 else None
        if matrix_rating:
            color = 'blue'
        else:
            color = 'red'
        user_ratings = ratings[ratings['userId'] == user_id]
        plt.scatter(user_ratings['rating_pulp'], user_ratings['rating_gump'], color=color, alpha=0.03, s=500)

    
    # Set the plot title and axis labels
    plt.title('Ratings for Forrest Gump and Pulp Fiction')
    plt.xlabel('Pulp Fiction Ratings')
    plt.ylabel('Forrest Gump Ratings')

    # Set the y-axis range to 0-5
    plt.ylim(0, 6)
    plt.xlim(0, 6)

    # Draw a circle around the point at x=5, y=4
    circle_00 = plt.Circle((2, 2), radius=0.14, color='green', fill=False)
    circle_01 = plt.Circle((4.5, 1), radius=0.14, color='green', fill=False)
    plt.gca().add_patch(circle_00)
    plt.gca().add_patch(circle_01)
    
    plt.plot([2, 2], [2, 1], color='green', linestyle='-')
    plt.plot([4.5, 2], [1, 1], color='green', linestyle='-')
    plt.plot([2, 4.5], [2, 1], color='green', linestyle='--')
    
    plt.text(1.8, 1.5, r'1', color='green', fontsize=16)
    plt.text(3.25, 0.8, r'2.5', color='green', fontsize=16)
    
    plt.text(4, 1.57, r'distance = √(1² + 2.5²) = 0.4', color='green', fontsize=12)
    plt.text(4, 1.4, r'similarity = 1/(1 + 0.4) = 0.714', color='green', fontsize=12)

    # Show the plot
    plt.show()
    
    

# ==============================================================================: MAIN
def main():
    ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings = ft_get_data()
    ft_scatter_plot(ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings)

if __name__ == '__main__':
    main()

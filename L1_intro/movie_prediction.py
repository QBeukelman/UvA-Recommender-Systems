# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    movie_prediction.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/04 21:06:11 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/04 21:51:45 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd

# Load the MovieLens dataset
movies_df = pd.read_csv('ml-latest-small/movies.csv')
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Filter the DataFrame to only include ratings for Forrest Gump, Pulp Fiction, and Why Stop Now
movies = ['Forrest Gump (1994)', 'Pulp Fiction (1994)', 'Body Parts (1991)']
merged_df = merged_df[merged_df['title'].isin(movies)]

# Get the ratings for each movie
forrest_gump_ratings = merged_df[merged_df['title'] == 'Forrest Gump (1994)']
pulp_fiction_ratings = merged_df[merged_df['title'] == 'Pulp Fiction (1994)']
why_stop_now_ratings = merged_df[merged_df['title'] == 'Body Parts (1991)']

# Join the ratings DataFrames on the userId column
ratings = pd.merge(pulp_fiction_ratings[['userId', 'rating']], forrest_gump_ratings[['userId', 'rating']], on='userId', suffixes=['_pulp', '_gump'])

# Create a scatter plot of the ratings for Forrest Gump and Pulp Fiction
plt.scatter(ratings['rating_pulp'], ratings['rating_gump'], alpha=0.1, s=500)
common_users = set(pulp_fiction_ratings['userId']).intersection(forrest_gump_ratings['userId'])
# Mark the ratings for users who have also rated "Body Parts (1991)" in blue
# and for those who haven't in red
for user_id in common_users:
    matrix_rating = merged_df[(merged_df['userId'] == user_id) & (merged_df['title'] == 'Body Parts (1991)')]['rating'].iloc[0] if merged_df[(merged_df['userId'] == user_id) & (merged_df['title'] == 'Body Parts (1991)')].shape[0] > 0 else None
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

# Show the plot
plt.show()
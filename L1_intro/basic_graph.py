# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    basic_graph.py                                     :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/04 18:51:10 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/04 21:50:01 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd

# Load the MovieLens dataset
movies_df = pd.read_csv('ml-latest-small/movies.csv')
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Filter the DataFrame to only include ratings for Forrest Gump and Pulp Fiction
forrest_gump_ratings = merged_df[merged_df['title'] == 'Forrest Gump (1994)']['rating']
pulp_fiction_ratings = merged_df[merged_df['title'] == 'Shawshank Redemption, The (1994)']['rating']

if len(pulp_fiction_ratings) != len(forrest_gump_ratings):
    # modify data or select subset to ensure same length
    forrest_gump_ratings = forrest_gump_ratings[:len(pulp_fiction_ratings)] # select subset of y with same length as x

# Create a scatter plot of the ratings for Forrest Gump and Pulp Fiction
plt.scatter(pulp_fiction_ratings, forrest_gump_ratings, alpha=0.1, s=500)

# Set the plot title and axis labels
plt.title('Ratings for Forrest Gump and Pulp Fiction')
plt.xlabel('Pulp Fiction Ratings')
plt.ylabel('Forrest Gump Ratings')

# Set the y-axis range to 0-5
plt.ylim(0, 6)
plt.xlim(0, 6)

# Show the plot
plt.show()

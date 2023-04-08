# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    heatmap.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/08 07:03:45 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/08 07:18:04 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import seaborn as sns # install
import matplotlib.pyplot as plt

# Load the MovieLens dataset
movies_df = pd.read_csv('../data/movies.csv')
ratings_df = pd.read_csv('../data/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Create a pivot table with user IDs as rows, movie titles as columns, and ratings as values
ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title'])

# Create the heatmap
plt.figure(figsize=(12,12))
sns.heatmap(ratings_table, cmap='coolwarm', vmin=0, vmax=5, cbar_kws={'label': 'Rating'})
plt.title('Movie Ratings by User', fontsize=16)
plt.xlabel('Movie Titles', fontsize=14)
plt.ylabel('User IDs', fontsize=14)

# Adjust the bottom margin
plt.subplots_adjust(bottom=0.2)

plt.show()

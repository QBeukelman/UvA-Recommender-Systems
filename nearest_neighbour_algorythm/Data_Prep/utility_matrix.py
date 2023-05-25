# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    utility_matrix.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/12 15:16:21 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/05/25 10:25:05 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the MovieLens dataset
movies_df = pd.read_csv('../data/movies.csv')
ratings_df = pd.read_csv('../data/ratings.csv')

# Merge the movies and ratings DataFrames
merged_df = pd.merge(movies_df, ratings_df, on='movieId')

# Create a pivot table with user IDs as rows, movie titles as columns, and ratings as values
ratings_table = pd.pivot_table(merged_df, values='rating', index=['userId'], columns=['title'])

# Save the pivot table to a .csv file called utility_matrix
# ratings_table.to_csv('../data/utility_matrix.csv')

# Create the heatmap
plt.figure(figsize=(12,12))
sns.heatmap(ratings_table, cmap='coolwarm', vmin=0, vmax=5, cbar_kws={'label': 'Rating'})
plt.title('User-Based Utility Martrix', fontsize=16)
plt.xlabel('Movie Titles (Features)', fontsize=12)
plt.ylabel('User IDs (Data Points)', fontsize=12)

# Set the font size and rotation of the tick labels
plt.xticks(fontsize=4)
plt.yticks(fontsize=6)

# Adjust the bottom margin
plt.subplots_adjust(bottom=0.24)

plt.show()


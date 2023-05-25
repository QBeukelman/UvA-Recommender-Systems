# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    pearson_correlation_example.py                     :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/19 13:51:58 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/05/25 10:24:11 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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
    # Add a jointplot to show the distribution of ratings for each movie
    joint_plot = sns.jointplot(data=ratings, x="rating_pulp", y="rating_gump", kind="kde", height=12)

    # Add a regression line to the jointplot
    sns.regplot(data=ratings, x="rating_pulp", y="rating_gump", ax=joint_plot.ax_joint, scatter=True, color='red')

    # Set the plot title and axis labels
    plt.subplots_adjust(top=0.95) # to avoid title overlap with plot
    plt.xlabel('Pulp Fiction Ratings')
    plt.ylabel('Forrest Gump Ratings')
    plt.title('Pulp Fiction and Forrest Gump Ratings Scatter Plot with Regression Line')

    # Show the plot
    plt.show()



    
    

# ==============================================================================: MAIN
def main():
    ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings = ft_get_data()
    ft_scatter_plot(ratings, pulp_fiction_ratings, forrest_gump_ratings, body_parts_ratings)

if __name__ == '__main__':
    main()
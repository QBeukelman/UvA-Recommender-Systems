# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    item_similarity_matrix.py                          :+:    :+:             #
#                                                      +:+                     #
#    By: quentinbeukelman <quentinbeukelman@stud      +#+                      #
#                                                    +#+                       #
#    Created: 2023/04/13 07:59:20 by quentinbeuk   #+#    #+#                  #
#    Updated: 2023/04/13 08:13:39 by quentinbeuk   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import pandas as pd

def ft_merge_data():
    # load tags table
    tags_df = pd.read_csv('../data/tags.csv')

    # load movies table
    movies_df = pd.read_csv('../data/movies.csv')

    # merge tags and movies tables on movieId
    merged_df = pd.merge(tags_df, movies_df, on='movieId')
    
	# pivot the merged dataframe to get one row per movie, one column per user, and each entry representing that user's rating of that movie
    user_movie_ratings = merged_df.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

    return user_movie_ratings

def main():
    # load and merge data
    user_movie_ratings = ft_merge_data()

    # do something with merged data, e.g. print first 10 rows
    print(user_movie_ratings.head(10))

if __name__ == '__main__':
    main()

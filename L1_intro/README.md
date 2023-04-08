
# Collective intelligence

A system for personalisation. The recommendations of the Volkskrant is not specifically a recommender system, it is not personal.

> Data set [MovieLenz](https://grouplens.org/datasets/movielens/)

</br>

### Content based filtering

</br>

### Collaborative filtering

A technique that can filter our items that a user might like on the basis of reactions by similar users. Requires less knowladge of the content.

It works by searching a large group of people and finding smaller sets of uses with tastes similar to the particular user. It looks at the items they liked and combines them to create a ranked list of suggestions. 

## Single nearest neighbour
    threashold
    classification

## k-nearest neighbour
    - **gemiddelde / gewoon gemiddelde**
    - **Eucledian similarity** (distance between points)
    - **cosign similiraty** (draw line from orign to point. Measure angles between lines), Cosign similiraty comes closer to the representation, and reduces biases such as the tendency to overrate films. 
    - "Mean centering" in cosign similiraty (Method of normalisation).
    - **Adjasent cosign**
    - The pridiction of the missing values.
    - User based collaborative filtering / item based filtering.

Testing
    Test with people who have seem the film, pretend if they havent seen the film. A training set and a test set.
    Mean squared error test. Differance between pridictions and training set, for all points, the average difference - Mathamatically more correct. 


Matrix representitive
User-based vs items-based


### K-nearest Neighbour

Example: Get neighbours, average scores (pridiction of how this person might rate the film), measure if value is above threshold.

Suggestions algos - Make pridictions
Classification algo - Yes or no if an item is in a specific class

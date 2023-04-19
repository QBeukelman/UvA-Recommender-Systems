

<h1 align="center">
	Recommender Algorythm using K-Nearest Neighbour Cosign Similarity method
</h1>

<br />


This repository contains an implementation of the nearest neighbor algorithm for building a recommender system. The algorithm is based on the k-nearest neighbors approach and is designed to recommend movies to users based on their previous ratings.


- [Installation](#installation)
- [Nearest Neighbour Algorythm](#nearest-neighbour-algorythm)
	- [The dataset](#the-dataset)
	- [Utility Martix](#utility-martix)
	- [Similarity Calculations](#similarity-calculations)
		- [Cosign Similarity (user-based)](#cosign-similarity-user-based)
		- [Euclidean Similarity (user-based)](#euclidean-similarity-user-based)
		- [Pearson Corrolation (item-based)](#pearson-corrolation-item-based)
	- [Similarity Matrix](#similarity-matrix)
	- [Result](#result)

<br />


## The Recommendation Problem

The recommendation problem can be formulated in two primary models: the prediction version and the ranking version. 

- **Pridiction** In the prediction version, the goal is to predict the rating value for a user-item combination using available training data. This is known as the matrix completion problem, where the missing values are predicted using a learning algorithm. 

- **Ranking** In the ranking version, the goal is to recommend the top-k items for a particular user, and the absolute values of the predicted ratings are not important. The ranking formulation is more common and referred to as the top-k recommendation problem. The solutions to the ranking version can be derived by solving the prediction version for various user-item combinations and then ranking the predictions. However, it is often easier to design methods for solving the ranking version directly.

<br />


## Goals of Recommender Systems

The primary goal of a recommender system is to increase product sales for the merchant.

The operational and technical goals of a recommender system are:

- **Relevance** recommend items that are relevant to the user
- **Novelty** recommend items that the user has not seen before
- **Serendipity** recommend unexpected items that the user might find interesting
- **Diversity** recommend items of different types to reduce the risk of the user not liking any of them

Recommender systems can also help improve user satisfaction, increase user loyalty, and provide insights for further customization.

<br />


## Collaborative Filtering Approaches

Two types of collaborative filtering methods: memory-based and model-based.

- **Memory-based methods (neighborhood-based collaborative filtering):**
Predict the ratings of user-item combinations based on their neighborhoods, which can be defined in one of two ways:

	- User-based: Similar users' ratings are used to make recommendations for a target user A. Predicted ratings of A are computed as the weighted average values of peer group ratings for each item.
	- Item-based: To make recommendations for an item, the first step is to determine a set of similar items. The ratings of a particular user for the items in the set are determined. The weighted average of these ratings is used to predict the rating of the user for the item.

	Advantages of memory-based methods: Simple to implement and resulting recommendations are easy to explain. Disadvantages of memory-based methods: Do not work well with sparse matrices and lack full coverage of rating predictions.

- **Model-based methods:** 
	Use machine learning and data mining methods in the context of predictive models. Parameters of model-based methods are learned within an optimization framework. Model-based methods have a high level of coverage even for sparse ratings matrices.

<br />



# Installation

To use the algorithm, you will need to have Python installed on your system. You can download Python from the official website.

You will also need to install the following packages:

- pandas
- numpy
- scikit-learn

You can install these packages using pip, by running the following command:

```bash
python3 -m pip install <package>
```

<br />


# Nearest Neighbour Algorythm

The algorythm is a study of different methods of collaborative filltering within recommender stystems.

1. Data merged into the Utility Maxrix or _"Feature Space"_.

2. Similarity calculations are compared.
   
3. A K-Nearest Neighbour algorythm recommends a list of movies for a target user.

<br />


## The dataset

MovieLens
20000 Movies
100000 User Ratings

- links.csv
- movies.csv
- ratings.csv
- tags.csv

<br />


## Utility Martix

Neighborhood-based methods for making recommendations involve using user-user or item-item similarity to predict ratings from a ratings matrix. The approach involves finding similar users or items in order to make predictions for specific user-item combinations.

![Utility Matirx Heatmap](../media/utility_matrix.png)

<br />


## Similarity Calculations

### Cosign Similarity (user-based)

If the user has given a rating for the third movie "Body Parts", points are blue, otherwise red.

$$\cos(\mathbf{A},\mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$


![2D Utility Matirx Heatmap](../media/cosign_similarity_simple.png)

<br />


### Euclidean Similarity (user-based)

$$similarity_{euclidean}(a, b) = \frac{1}{1 + \sqrt{\sum_{i=1}^{n}(a_i - b_i)^2}}$$

![2D Utility Matirx Heatmap](../media/euclidean_similarity_simple.png)

<br />



### Pearson Corrolation (item-based)


<br />




## Similarity Matrix

[400 rows]
[400 cols]

The problem with the similarity martix is that we have assumed that absent ratings are 0. To fix this we can use a Centered-Cosign. Normalise the ratings of a given user by subtracting the row mean.

![Similarity Matrix Heatmap](../media/similarity_matrix.png)

<br />


## Result

<pre>
Here are some movies like: 'Taxi Driver (1976)'

Title                                               Similarity
Birdcage, The (1996)                                1.0000
Bushwhacked (1995)                                  0.7079
GoldenEye (1995)                                    0.6938
My Family (1995)                                    0.6517
Immortal Beloved (1994)                             0.6362
Flirting With Disaster (1996)                       0.6273
Seven (a.k.a. Se7en) (1995)                         0.6269
Mr. Holland's Opus (1995)                           0.6158
Little Buddha (1993)                                0.6106
</pre>

<br />

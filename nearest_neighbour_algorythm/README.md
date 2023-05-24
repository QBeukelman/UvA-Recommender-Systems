

<h1 align="center">
	Recommender Algorythm using K-Nearest Neighbour Cosign Similarity method
</h1>

<br />


The algorythm is a study of different methods of collaborative filltering within recommender stystems.

1. Data merged into the Utility Maxrix or _"Feature Space"_.

2. Similarity calculations are compared.
   
3. A K-Nearest Neighbour algorythm recommends a list of movies for a target user.

---
<br />



## Utility Martix

Neighborhood-based methods for making recommendations involve using user-user or item-item similarity to predict ratings from a ratings matrix. The approach involves finding similar users or items in order to make predictions for specific user-item combinations.

The utility matrix, also known as the feature space, is constructed by merging the data and represents the ratings given by users for different items. Each row in the utility matrix corresponds to a user, and each column corresponds to an item. The values in the matrix represent the ratings given by users to the corresponding items.

![Utility Matirx Heatmap](..\media/utility_matrix.png)

---
<br />



## Similarity Matrix

[400 rows]
[400 cols]

To calculate similarity between users, we construct a similarity matrix. The similarity matrix is a square matrix with dimensions equal to the number of users in the dataset. Each element of the matrix represents the similarity between two users. 

Further comparison between these methods is given in `/Similarity_Calculations`, Cosign Similarity, Euclidian Similarity and Pearson Correlation.

Below is a heatmap showing the Cosign Similarity based on the above Utility Matrix.

![Similarity Matrix Heatmap](..\media/similarity_matrix.png)

---
<br />


# 1. Pridiction Problem

Pridict the rating that a target user u might give to item j. The weighted average of the mean-centered rating of item j in top-k neighbours of target user u.

$$ \hat{r}_ {uj} = \mu_u + \frac{\sum_{v\in Pu(j)} \text{Sim}(u,v) \cdot (r_{vj} - \mu_u)}{\sum_{v\in Pu(j)} |\text{Sim}(u,v)|} $$

where:
- $\hat{r}_ {uj}$ is the predicted rating of target user u for item j, $\mu_u$ is the mean rating of user u.
- $s_{vj}$ or $(r_{vj} - \mu_u)$ is the mean-centered rating of user v for item j.
- $\text{Sim}(u,v)$ is the Pearson correlation coefficient between user u and user v.
- $Pu(j)$ is the set of k closest users to target user u, who have specified ratings for item j.

(Aggarwal, 2016, p. 36)

The program is implemented following the steps:

1. Similarity Computation
2. Neighbor Selection
3. Predict User Rating

<br />


## Program Output

`[610 rows x 9724 columns]`


**Utility matrix Simplified:**

Number of ratings not null or NaN: 100,836

|	movieID     |	1		|	2		|	3		|
|	:---:       |	:---:	|	:---:	|	:---:	|
|	u1			|	4.00	|	NaN		|	4.00	|
|	u2			|	NaN		|	NaN		|	NaN		|



**Pridicted Rating Simplified:**

Number of ratings not null or NaN: 5,931,640

|	movieID     |	1		|	2		|	3		|
|	:---:       |	:---:	|	:---:	|	:---:	|
|	u1			|	4.00	|	3.94	|	4.00	|
|	u2			|	4.37	|	3.23	|	2.44	|

---
<br />


# 2. Ranking Problem

To recommend movies to a user, the program takes a user ID ranging from `1 to 600` and generates a list of the top `k = 10` recommended movies. The recommendations are based on the similarity of the target user to other users in the dataset.

<br />


## Program Output

Here are some movies similar to: 'Taxi Driver (1976)'

|	Title     						|	Similarity	|
|	:--- 							|	:---:		|
|	Bushwhacked (1995)				|	0.7079		|
|	GoldenEye (1995)				|	0.6938		|
|	My Family (1995)				|	0.6517		|
|	Immortal Beloved (1994)			|	0.6362		|
|	Flirting With Disaster (1996)	|	0.6273		|
|	Seven (a.k.a. Se7en) (1995)		|	0.6269		|
|	Mr. Holland's Opus (1995)		|	0.6158		|
|	Little Buddha (1993)			|	0.6106		|	

---
<br />



# Citations

Aggarwal, C. C. (2016). Recommender systems: The textbook. Springer International Publishing.
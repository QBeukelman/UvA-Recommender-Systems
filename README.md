
<h1 align="center">
	About
</h1>

This repository contains a selection of cource material form the Recommender Systems course from the Univercity of Amserdam. The course detials various methods of collaborative filtering, and is based in the Python programming language.

The repository consists of two algotythms based on the K Nearest Neighbors (KNN) approach; along with supporting data preperation and calculations, that solve two common problems with recommender systems:

1. Ranking Problem: How to rank relevant content?
2. Pridiction Problem: How to pridict the rating a user will give to content?

---
<br />



# MovieLens Data

> `MovieLens`
> [Education and Development (Small)](https://grouplens.org/datasets/movielens/) 

`20000` Movies, `100000` User Ratings

- links.csv
- movies.csv
- ratings.csv
- tags.csv

---
<br />



# Setup

### Installation

To use the algorithm, you will need to have Python installed on your system. You can download Python from the official website.

You will also need to install the following packages:

- math
- pandas
- numpy
- sklearn
- matplotlib
- seaborn

You can install these packages using pip, by running the following command:

```bash
python3 -m pip install <package_name>
```


### Run

To run a program, navigare to the directory and run:

```bash
python3 <program_name.py>
```

---
<br />



# Further Reading

> `Chapter 5`
> [Python for Data Analysis](https://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/Python-for-Data-Analysis.pdf) 

> `Chapters 1 & 7`
> [Recommender Systems: The Textbook](http://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf) 

<br>


<details>
<summary>The Recommendation Problem</summary>
<br>
The recommendation problem can be formulated in two primary models: the prediction version and the ranking version. 

- **Pridiction** In the prediction version, the goal is to predict the rating value for a user-item combination using available training data. This is known as the matrix completion problem, where the missing values are predicted using a learning algorithm. 

- **Ranking** In the ranking version, the goal is to recommend the top-k items for a particular user, and the absolute values of the predicted ratings are not important. The ranking formulation is more common and referred to as the top-k recommendation problem. The solutions to the ranking version can be derived by solving the prediction version for various user-item combinations and then ranking the predictions. However, it is often easier to design methods for solving the ranking version directly.
</details>

<details>
<summary>Goals of a Recommender System</summary>
<br>
The primary goal of a recommender system is to increase product sales for the merchant.

The operational and technical goals of a recommender system are:

- **Relevance** recommend items that are relevant to the user
- **Novelty** recommend items that the user has not seen before
- **Serendipity** recommend unexpected items that the user might find interesting
- **Diversity** recommend items of different types to reduce the risk of the user not liking any of them

Recommender systems can also help improve user satisfaction, increase user loyalty, and provide insights for further customization.
<br>
</details>



<details>
<summary>Collaborative Filtering Approaches</summary>
<br>
Two types of collaborative filtering methods: memory-based and model-based.

- **Memory-based methods (neighborhood-based collaborative filtering):**
Predict the ratings of user-item combinations based on their neighborhoods, which can be defined in one of two ways:

	- User-based: Similar users' ratings are used to make recommendations for a target user A. Predicted ratings of A are computed as the weighted average values of peer group ratings for each item.
	- Item-based: To make recommendations for an item, the first step is to determine a set of similar items. The ratings of a particular user for the items in the set are determined. The weighted average of these ratings is used to predict the rating of the user for the item.

	Advantages of memory-based methods: Simple to implement and resulting recommendations are easy to explain. Disadvantages of memory-based methods: Do not work well with sparse matrices and lack full coverage of rating predictions.

- **Model-based methods:** 
	Use machine learning and data mining methods in the context of predictive models. Parameters of model-based methods are learned within an optimization framework. Model-based methods have a high level of coverage even for sparse ratings matrices.
<br>
</details>


---
<br />

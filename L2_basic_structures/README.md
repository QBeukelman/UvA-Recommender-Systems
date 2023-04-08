 

# Goal of Recommender System

<pre>
Recommender Systems
	Content-Based Filtering
	Collaborative Filtering
		User-Based
		Item-Based
</pre>

Neighborhood based

Abundunce of data on the web.

Personalized web tool to help people find content that you may be interested in. Model peoples opinion, preferences and behaviour.

Strong dependency between users and items. Catagories of items may show significant correlations.

Capture relationships between previous interactions and catagories.


</br>


# Basic Models of Recomender Systems

## 1. Collaborative Filtering Models

- **Memory based methods**

Also known as Neighborhood based.
These models are very well understood and applicable in many domains.
It uses a "wisdom of the crowd" approach.
Assumptions - Have access to rating data, and customers who had similar preferances in the past will also have them in the future.
Output - A score, or a list

Types of rating (Utility data):
1. Continuous 
2. Interrval
3. Ordinal - "Agree/disagree"
4. Binary - "Like/dislike"
5. Unary - "Implicit feedback"


The recommender system will take as input Rating Matrix. Y Users, X Movies


User based collaborative filter

Based on the simliar preferences of of users.


Item based collaborative filter

Based on the similiarity of the content 



**KNN** User based 

Basic technique 

Find a target user.
Find a set of neighbours who likes the same items, and have rated them.
Average their pridictions.
Do this for all items the target user has not interacted with in the past.


Some basic questions
1. How do we measure similiarty among users?
2. How many neighbours to consider?
3. How to generate pridictions from neighbours?

Consider Notations
Ruk - rating giben by user U to item K.


### Similarity computation - How do we measure similiarty among users?

Commonly used: "Pearson" coefficient is a well known similarity metric.
First compute average for each user.
Compute the intersection between users.
Square works as a normalisation.


### Neighbour selection - How many neighbours to consider?

Normally decide on K.
Only consider users with the heighest Pearson Coefficient with the target user.
Rating pridiction equation.
Important to normalise for users that tend to rate heigher or lower, or other rating behaviour. -> Mean center
The equation is the user rating and the weighted rating of others.



## Item-Based collaborative filtering

Similarity Calculation
Commonly used: Cosign similiraty


## Neighbour selection

Similar to user based sollaborative filtering.


## Rating prodiction Equation



# Comparisons between algorythms

Item Based
- Item based comparison often provieds more relevant recommendations. Because it is based on users own ratings. This is also able to provide explaination. 

User Based
- User based method often provids more diverse recommendations. Diversity, the recommendation might list items across multiple catogories. If the items are not **diverse**, if the first item is not interesting, they may not like the others. Additionally, they might recommend obvious items, which are not **novel**.

Weaknesses
- Weaknesses of both algorythms include: Offline mode can be inpractical on large-scale. Once you have similarity the pridition can be efficent.
- Some times a pridiction is not possible. A target user may not have any neighbours, which is impossible to pridict before selecting a user. These methods dont work well with sparce matrixes. With few neighbours the pridiction is not robust

Strengths
- Easy to implement/debug.
- Easy to justify why an item was selected (mostly for item based).
- Recommendations are stable, same pridiction every time.
- Update model incrementally. Without computing entire mode again







**Model based methods**

## 2. Content-Based

## 3. Knowladge-Based

## 4. Demographic

## 5. Hybrid and Ensemble-Based

</br>


# Domain Specific Challengs in Recommender Systems

## 1. Context-Based

## 2. Time-Sensitive

## 3. Location-Based

## 4. Social

</br>


# Overview of Recommender Systems

### Efficency and effectiveness
Few users many items
    Depends on density of matrixes
    User-based is more effecient
    
Few items many users
    Item-based effecient


# Problems

Pridiction probelm
    Assume user preference for items
    Missing values are pridicted (Pridict rating in same range)


Ranking problem
    Recommend top k items for each user


# Goals 

Balance between:
- Relevance (Accuracy)
- Novelty (New but already interested in)
- Serendipity (Surprising, different from novel, did not know your interests) --> Test with other tages and identifiers e.g. Catagory
- Recommendation Divercity


Social Network
    Link Pridicition

News
    Items have a date
    May not have ratings, but clicked on is a binary rating


*User-Based
    Opinions of similar users




# Model based collaborative filtering

If a matrix is not dense enough, you may not be able to determine a neighbourhood.
In the case of a sparce ratings matrix, these options work better:

- Decition tree
- Bayesian method
- Rule method
- Latent factor models


# Content-Based filtering

User discritive attributes of the items. If only one user has rated a movie, collaborative filetering will fail.
E.g. Search catagories, or search descrition for keywords

Make recommendations for new items.
Does not work well for new users.

In many cases, content based filtering provides obvious recommendataions.



# Knowladge based Recommender System

Not enough interactions/ratings. Example expensive items are not bought often.
Also useful in complex items with many attributes.
In this case, the user will give an input. Such as refine requirements.
Match similarity between user input and item description.
Not generally a good recommender for personalisation and are generally used in combination.

### 1. Constraint-Based (Knowladge)
Give system constraints and attributes (Upper or lower limits)

### 2. Case-Based (Knowladge)
Specify an anchor point, such as a zip-code


# Demographic Recommender

Demographic information is used to learn classifiers that can map demographics to ratings.
Not generally a good recommender for personalisation and are generally used in combination.


# Hybrid Recommender

Combine
    User profile
    Community Data
    Product features
    Knowladge models

Diferent hybridisiation
    Parallel use of several systems - Combine output of models
    Monolithinc - One model, that is a combination of models
    Piplined design - Sequential recommender - Output from one model is the input to another




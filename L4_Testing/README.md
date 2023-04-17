
# Evaluating Recommender Systems

## Offline evaluation

- Gives a measuer of acuracy, but not novelty and serindipity.
- Some of the data is used for training(60%), validation(20%), testing(20%).

## Validation data
Used for selection and paramater tuning.
If multiple models are used, validation can is used to determin the accuracy of each.

## Testing data

Determine the final accuracy of the model, after fine-tuning.



# Segmenting input data

All datasets contain all users -> Users are split based on profiles.
If a user has made 7 ratings, some are in each group.
Sorting of user profile splitting -> Several methods, random, timestamp.



# Rating Pridiction Problem:

# Accuracy Metrics (Calcularing Error)

## Mean Squared Error
How close was your pridiction to the actual result.
If outliers are not specifically important.

## Root Mean Square Error
Square root of MSE
Often used instead of MSE
This is sensitive to outliers, can produce large errors -> Robustness of pridictions accross various ratings is important. (*Squre changes the linearaty)

## Mean Absolute Error
Any negative is returned as positive.




# Rating Ranking Problem: 

Preprocess for relevant items, e.g. include only ratings above a value
Ground truth data (Preprocessed Test Data) -> Recommendation list

## Pricistion
What percentage of recommended items are relevant
For each user, get average to gage whole program
Compare recommendations with relevant results
Often used in comparing deferent recommendation algorythms

Pricistion depends on number of ratings.
To compencate for this, the recal metric is used

### Recall Metric
Complements pricition measure.
This is a measure of completness, determins the fraction of relevant items retrived out of all items.
Increate the size of recommendation list, Recall increases.


## F1 - Pricition and Recall
Gives equal weights to procision and recall
Pricition and Recall, do not consider the position of an item in a recommended list. Thus does not evaluate the quality of the list.



# Normalized Duscounted Cumulative Gain
Measuer the ranking quality of the recommendation model. What is the best renking for this user?
Assigns weights to order of each position in the recommended list.
Relavance is 1 or 0.

## Non accuracy metrics

Novelty -> 8.3.6
Serendipty -> 3.8.7
Divercity -> 3.8.8

 

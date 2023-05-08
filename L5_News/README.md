

# L6 - Linear Algeobra



Regression is about continous values.
Classification is about classes.

KNN is a regrassive algorythm because of the contineous ratings 0-5, but with the addition of the threshold value, we can see it as a clasification.



# Matrix Factorisation

A mathmatical trick to fill in the missing values


## Factors

A factor is an other notation for a list.
Dot-product

Pandas dot-product
dot-product = s1 @ s2
The result of the dot-product is not a (factor), but a regular numbers (scalers)


Cos(l,d) = s1 @ s2 / (np.squrt(s1 @ s1) * np.squrt(s2 @ s2))


# Catagories
## One Hot encoding

Get factor values for catagorasation
With binary features -> Cosign may not be best choice, Jaccard index could be better.

            Action  Adventure
Inception      1       1
Frozen         0       1


# Text

Factorise text, count instances of words.

Two problems with simple word factorisation table:

   1. Words such as "the" dont have much information (List of exculded words) (If the word appears in all sentences, the amount of occurences in all sentences / length of sentencces. "Inverse Document/sentences  Frequency"). Log is added to the equation, the more often the word occurs, the less weight/score it has.
   
   2. The longer the sentence, the higher the similarity (Normalise, with the length of sentence "term frequency").

Combine these two:

Term frequency * Inverse Document Frequency


Have not considered:

Semantic -> Word2Vec Algorythm
Grammer


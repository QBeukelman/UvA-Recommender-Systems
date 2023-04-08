


<h1 align="center">
	Twitter - the Algorithm
</h1>

<br />


> https://github.com/twitter/the-algorithm


The recommendation pipeline is made up of three main stages that consume three freatures.

1. Candidate Sourcing
2. Ranking
3. Heuristics and Filters


--- 
<br />

![alt text](https://raw.githubusercontent.com/twitter/the-algorithm/main/docs/system-diagram.png)

<br />


# Candidate Sources

For each request, the best 1500 Tweets from a pool of hundereds of millions are extracted. On average the timeline consists of 50% in-network and 50% out-of-network.

### In-Network Sources

Tweets are ranked using a logistic regression model, where the top tweets are then sent to the next stage.

The most important component in ranking in-network tweets is the Real Graph.
Read Graph is a model which pridicts liklihood of engagement between two users.
The higher the Real Graph score between you and the author of the tweet, the more of their tweets are included.

### Out-of-Network Sources

How can Twitter tell if a certain tweet will be relevant to you if you dont follow the author? Twitter takes two approches.

#### Social Graph

Estimate what you find relevant by analyzing the engagement of people you follow, or those with similar interests. Traverse the graph of engagements and follows to answer two questions:

- What tweets did the people I follow recently engage with?
- Who likes similar tweets to me, and what else they recently liked?

The tweets are ranked using a logistic regression model. This type of graph traversal is essential to this kind recommendation algorythm.
GraphJet is a processessing engine that maintains a real-time interaction graph between users and tweets.
Social Graph recommendations serve roughly 15% of home time-line tweets. 

#### Embedding Spaces

Aim to answer a more general question about content similarity: What tweets and users are similar to my interests?

Embedding works by generating numberical representations of users interests and tweets content. Then calculate the similarity between any two users, tweets or user-tweet pairs in this embedding space. Tweets are embedded into communities by looking at the current popularity of a tweet in each community. The more users in a community like a tweet, the more of that tweet associated with that community.

A twitter servie SimClusers, discovers communities anchored by a cluster of influential users using a Matrix Factorization Algrythm.
There are 145k communities updated every three weeks. Users and tweets are represented in the space of communities, and can belong to multiple communities. Some large comminities include: news, nba, pop, bollywood, football

---
<br />


# Ranking

At this point there are ~1500 candidates that may be relevant. Scoring directly pridicts the relevance of each candidate, and is the primary signal for ranking tweets on the time-line. At this stage all sources are treated equally.

Ranking is achieved with a ~48M parameter Neural Network. It is countinually trained on tweet interactions to optimize for positive engangement (likes, retweets, replies).

The ranking mechanism takes into account thousends of features and outputs ten labels to give each tweet a score, where each label represents the probability of engagement.

---
<br />

# Heuristics, Filters, and Product Features

These product features work together to create a balanced and diverse feed:

- Visibility filtering
- Author Diversity
- Content Balance
- Feedback-based Fatigue
- Social Proof
- Conversations
- Edited Tweets

---
<br />


# Mixing and Serving

Tweets are blended with other non-tweet content such as, Ads, Follow Recommendations, and Onboarding Prompts, which are returned to your device to display.

The pipeline above runs ~5B/day, and complets in ~1.5 seconds. A single pipeline execution requires 220 seconds of UPU time.

---
<br />

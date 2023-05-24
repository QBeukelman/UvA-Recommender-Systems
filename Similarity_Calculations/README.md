

<h1 align="center">
	Similarity Calculations
</h1>


Below is a comparison of various similarity calculations commonly used in collaborative filtering. The choice of similarity metric depends on the characteristics of the dataset and the requirements of the recommendation system.

---
<br />


# Cosign Similarity (item-based)

Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between them. In the context of collaborative filtering, cosine similarity is used to determine the similarity between items based on their user rating patterns. It is particularly useful when the ratings are sparse and high-dimensional. The cosine similarity between two vectors, a and b, is computed using the formula:

$$\cos(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$$

Consider the following utility matrix, where users (u) rate items (i) on a scale from 0 to 10:

|  | **i1** | **i2** | **i3** | **i4** | **i5** | **i6** |
| --- | --- | --- | --- | --- | --- | --- |
| **u1** | 7 | 6 | 7 | 4 | 5 | 4 |
| **u1** | 6 | 7 | ? | 4 | 3 | 4 |
| **u1** | <span style="color:red"> **?** </span> | 3 | 3 | 1 | 1 | ? |
| **u1** | 1 | 2 | 2 | 3 | 3 | 4 |
| **u1** | 1 | ? | 1 | 2 | 3 | 3 |

<br />


To compute the cosine similarity between user 3 and all the other users, we take the dot product of their rating vectors and divide it by the product of their Euclidean norms:

$$
\cos(1,3) = \frac{6 \cdot 3 + 7 \cdot 3 + 4 \cdot 1 + 5 \cdot 1}{\sqrt{62 + 72 + 42 + 52} \cdot \sqrt{3^2 + 3^2 + 1^2 + 1^2}} = 0.956
$$

A cosine similarity example can be visualized using a heatmap as shown below (if the target user has given a rating for the third movie "Body Parts", points are `blue`, if not points are `red`):

![2D Utility Matirx Heatmap](..\media/cosign_similarity_simple.png)

---
<br />


# Euclidean Similarity (user-based)

Euclidean similarity, also known as Euclidean distance, measures the distance between two vectors in the Euclidean space. In the context of collaborative filtering, Euclidean similarity is used to calculate the similarity between users based on their rating profiles. It is commonly employed when the ratings are dense and low-dimensional. The Euclidean similarity between two vectors can be computed using the formula:

$$
\text{distance} = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}
$$

$$
\text{similarity} = \frac{1}{{1 + \text{distance}}}
$$

Consider the same utility matrix mentioned earlier. To calculate the Euclidean similarity between user 1 and user 4, we measure the Euclidean distance between their rating vectors:

$$
distance = √(1² + 2.5²) = 0.4
$$

$$
similarity = 1/(1 + 0.4) = 0.714
$$

A heatmap can be used to visualize the Euclidean similarity calculation (if the target user has given a rating for the third movie "Body Parts", points are `blue`, if not points are `red`):

![2D Utility Matirx Heatmap](..\media/euclidean_similarity_simple.png)

---
<br />



# Pearson Corrolation (user-based)

Pearson correlation measures the linear correlation between two variables, taking into account their mean values and standard deviations. In collaborative filtering, Pearson correlation is employed to determine the similarity between users based on their rating patterns, considering both the magnitude and direction of the ratings. The Pearson correlation coefficient between two vectors, a and b, can be calculated using the following formula:

$$r_{\mathbf{a},\mathbf{b}} = \frac{\sum_{i=1}^n (a_i - \bar{a})(b_i - \bar{b})}{\sqrt{\sum_{i=1}^n (a_i - \bar{a})^2} \sqrt{\sum_{i=1}^n (b_i - \bar{b})^2}}$$

Here, $\bar{a}$ and $\bar{b}$ represent the mean ratings of vectors a and b, respectively.

A heatmap can be utilized to visualize the Pearson correlation coefficients between users, as shown below:

![2D Utility Matirx Heatmap](..\media/pearson_correlation_simple.png)

---
<br />
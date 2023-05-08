
# Representing data matrixes

## Film genres as vectors

(Using -1 > 1)

With pandas a series is a vector

If you take the and product of two vectors, the higher the value, the more similar they are.

With all values near 0, it does not say enough about the filems. Realistically, this is normalised.

The matrix is made up of the and product of each vector.



### Output matrix

Each row of the films table + each row of colum of the user table.


Ut - User matrix
M - Genre matrix

R^ = M.Ut

user_matric_transposed = user_matrix.T <- Set on side
Pridicted ratings = movie_matric @ user_matric_transposed

Recommendations are based on a threshold

The resulting matrix will have the same number of rows as there are genres, and the same number of culumns as there are users.

        U1      U2
genre1  0.02    0.44
genre2  1.22    1.03
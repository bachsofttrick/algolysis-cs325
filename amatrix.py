import numpy as np

# Define the adjacency matrix A
A = np.array([
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
])

# Calculate the degree matrix D
D = np.diag(np.sum(A, axis=1))

# Calculate the Laplacian matrix L
L = D - A

print("Adjacency matrix A:")
print(A)
print("\nDegree matrix D:")
print(D)
print("\nLaplacian matrix L:")
print(L)

# Define a function to calculate the determinant of a matrix
def determinant(matrix):
    return np.linalg.det(matrix)

# Create a submatrix by removing the last row and column
submatrix = L[:-1, :-1]

# Calculate the determinant of the submatrix
num_spanning_trees = int(round(determinant(submatrix)))

print("\nSubmatrix (after removing last row and column):")
print(submatrix)
print("\nDeterminant of the submatrix (number of spanning trees):")
print(num_spanning_trees)

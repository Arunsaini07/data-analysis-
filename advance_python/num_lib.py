import numpy as np

# Creating arrays
a = np.array([10, 20, 30, 40])
b = np.array([5, 10, 15, 20])

print("Array A:")
print(a)

print("\nArray B:")
print(b)


# Addition
print("\nAddition:")
print(a + b)


# Subtraction
print("\nSubtraction:")
print(a - b)


# Multiplication
print("\nMultiplication:")
print(a * b)


# Division
print("\nDivision:")
print(a / b)


# Sum of array
print("\nTotal sum of A:")
print(np.sum(a))


# Maximum value
print("\nMaximum value in A:")
print(np.max(a))


# Minimum value
print("\nMinimum value in A:")
print(np.min(a))


# Average
print("\nAverage of A:")
print(np.mean(a))


# 2D Array (Matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:")
print(matrix)


# Matrix shape
print("\nShape of matrix:")
print(matrix.shape)


e = np.zeros(4)
f = np.ones(4)
g = np.full(4, 7)
h= np.arange(0, 10, 2)
print (e, f, g, h)
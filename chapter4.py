import math

# vector
def add2Vector(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def soNhanVector(c, v):
    return [c * v_i for v_i in v]

def sumOfvectors(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = add2Vector(result, vector)
    
    return result

def dot(v, w):
    return [v_i * w_i for v_i, w_i in zip(v, w)]

def distance(v, w):
    result = 0
    for v_i, w_i in zip(v, w):
        result = result + pow(v_i - w_i, 2)
        print(result)
    
    result = math. sqrt(result)
    return result

v = [1, 3, 5, -3, 6]
w = [0.2, 0.5, 4, 0, -5]
print("tong: ", add2Vector(v, w))
print("hieu: ", vector_subtract(v, w))
print("c * w : ", soNhanVector(10, w))
print("dot v and w : ", dot(v, w))
print("distance v and w : ", distance(v, w))

# Matrices
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols

def getRow(A, i):
    return A[i]

def getCol(A, j):
    return [A_i[j] for A_i in A]

from typing import Callable
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

A = [[1,2], [4, 5], [8, 9]]
B = [[1, 3, 5], [2, 4, 6]]
print("shape of A: ", shape(A))
print("rows: ", getRow(A,2))
print("cols: ", getCol(A,1))

# print("make matrix : ", make_matrix(len(A), len(A[i]), entry_fn))

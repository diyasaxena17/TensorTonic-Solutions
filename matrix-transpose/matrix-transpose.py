import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # get input
    A = np.asarray(A)
    # get shape of rows / cols
    rows, cols = A.shape
    # new empty array
    B = np.empty((cols, rows), dtype = A.dtype)
    # fill in values
    for i in range(rows):
        for j in range(cols):
            B[j, i] = A[i, j]
    # return result
    return B

    

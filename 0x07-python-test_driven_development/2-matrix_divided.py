#!/usr/bin/python3

"""Define a matrix devision function"""


def matrix_divided(matrix, div):
    """Divide all element of a matrix.

    Args:
        matrix(list): A list of lists of int/floats.
        div(int/float): The diviaor.

    Raises:
        TypeError:if the matrix contains non number,
                  if the matrix contains rows of d/ff sizes,
                  if div is not int/float
       ZeroDivisionError: if div is 0.
    Returns:
       A new matrix with the result of the division
    """
    # Checks if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Checks if the first element in matrix is a list so len can be used
    if isinstance(matrix[0], list):
        rowlen = len(matrix[0])

    # Checking if matrix is formatted correctly
    for mtx in matrix:

        # Checks if mtx is a list
        if not isinstance(mtx, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        # Checks if the length of each row is the same
        if len(mtx) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")

        # Checks if the elements in the matrix are int or float
        for elemnt in mtx:
            if not isinstance(elemnt, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Checks if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checks if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Dividing original matrix and creating a new matrix
    new_matrix = [[round(idx / div, 2) for idx in mtx] for mtx in matrix]

    return new_matrix

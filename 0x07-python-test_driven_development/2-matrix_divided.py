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
    # checks if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # checks if the first element in matrix is a list so len can be used
    if isinstance(matrix[0], list):
        rowlen = len(matrix[0])

    # checks for the format of a matrix
    for mx in matrix:
        # check if mx is a list
        if not isinstance(mx, list):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "integers/floats")

        # checks if the len of the row is the same
        if len(mx) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")

        # checks the elements in the matrix to be int/float
        for element in mx:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")

        # check if div is a number
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        # check if div is 0
        if div == 0:
            raise ZeroDivisionError("division by zero")

        # dividing original matrix and creating a new matrix
        new_matrix = [[round(idx/div, 2) for idx in mx] for mx in matrix]

        return new_matrix

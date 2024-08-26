from typing import Tuple

import numpy as np

if __name__ == "__main__":
    import sys
    from pathlib import Path

    parent_dir = Path(__file__).resolve().parents[1]
    sys.path.append(str(parent_dir))
    from utils import timer


@timer
def add_2x2_matrices(*args: Tuple[np.array, ...]) -> None:
    """Add any number of 2x2 matrices.

    Q: Write a function that can take any number of 2x2 matrices and add them all
        together. Assume that all matrix values are real numbers.

    Args:
        *args (np.ndarray): Variable length argument list of 2x2 numpy arrays. Each
            argument must be a 2x2 matrix (numpy.ndarray).

    Returns:
        np.ndarray: The the 2x2 matrix that results after summing those provided.

    """
    result = np.array([[0, 0], [0, 0]])
    for matrix in args:
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                result[i][j] += col
    return result


@timer
def add_2x2_matrices_chatgpt(*args: Tuple[np.array, ...]) -> None:
    """Add any number of 2x2 matrices using ChatGPT's recommended answer."""
    result = np.array(
        [sum(matrix[i][j] for matrix in args) for j in range(2) for i in range(2)]
    ).reshape(2, 2)
    return result


@timer
def add_2x2_matrices_simple(*args: Tuple[np.array, ...]) -> None:
    """Add 2x2 matrices in the laziest way possible.

    Note that this method wins while ChatGPT's recommended answer is the slowest.
    """
    return sum(args)


if __name__ == "__main__":
    a = np.array([[1, 0], [0, 1]])
    add_2x2_matrices(a, a, a)
    add_2x2_matrices_chatgpt(a, a, a)
    add_2x2_matrices_simple(a, a, a)

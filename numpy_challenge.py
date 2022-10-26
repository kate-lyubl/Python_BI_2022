import numpy as np


def matrix_multiplication(a, b):
    return np.dot(a, b)


def multiplication_check(matrix_list):
    width = matrix_list[0].shape[1]
    for m in matrix_list[1:]:
        height = m.shape[0]
        if width != height:
            return False
        width = m.shape[1]
    return True


def multiply_matrices(matrix_list):
    if multiplication_check(matrix_list):
        return np.linalg.multi_dot(matrix_list)
    return None


def compute_2d_distance(a, b):
    return compute_multidimensional_distance(a, b)


def compute_multidimensional_distance(a, b):
    return np.linalg.norm(a - b)


def compute_pair_distances(arr):
    arr_reshaped = arr.reshape(arr.shape[0], arr.shape[1])
    return np.linalg.norm(arr[:, None, :] - arr_reshaped[None, :, :], axis=-1)


if __name__ == "__main__":
    array_1 = np.array([0, 1, 2, 3, 4])
    array_2 = np.arange(5)
    array_3 = np.linspace(0, 4, num=5)






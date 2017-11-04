"""
Removes voids, repetitions and already contained terms.

"""

import numpy as np


def check(result):
    result = np.unique(result, axis=0)
    result_col_even = result[:, ::2]
    result_col_odd = result[:, 1::2]
    result_sum = result_col_even + result_col_odd
    del_rows = np.array([])
    for i in range(result_sum.shape[0]):
        for j in range(result_sum.shape[1]):
            if result_sum[i, j] == 0:
                del_rows = np.append(del_rows, i)
    final_result = np.delete(result, del_rows, axis=0)
    contain = list()
    for i in range(0, final_result.shape[0]-1):
        for j in range(i+1, final_result.shape[0]):
            if np.array_equal(np.logical_or(final_result[i, :], final_result[j, :]).astype(int), final_result[i, :]):
                contain.append(i)
            if np.array_equal(np.logical_or(final_result[i, :], final_result[j, :]).astype(int), final_result[j, :]):
                contain.append(j)
    final_result = np.delete(final_result, contain, axis=0)
    return final_result

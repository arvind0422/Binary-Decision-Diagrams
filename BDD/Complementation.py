"""
This code helps to find the complement of a function
Authors: Arvind, Sripathi, Shantanu
"""

import numpy as np
import URP_Tautology as URPT
import Cofactor as cof
import Check_void as CV
from Union import union as Union


def complement(F):
    # First find the cofactors of the function wrt to each variable. Run a recursion. Check for terminating conditions.

    zero_list = np.zeros(F.shape[0])
    alpha = np.ones(F.shape[1])

    # Making a temporary array of ones for deMorgan's rule implementation
    F_temp = np.ones(shape=(F.shape[0],F.shape[0]), dtype=int)

    # Removing voids
    F = np.unique(F, axis=0)
    F_col_even = F[:, ::2]
    F_col_odd = F[:, 1::2]
    F_sum = F_col_even + F_col_odd
    del_rows = np.array([])
    for i in range(F_sum.shape[0]):
        for j in range(F_sum.shape[1]):
            if F_sum[i, j] == 0:
                del_rows = np.append(del_rows, i)
    F = np.delete(F, del_rows, axis=0)

    if URPT.URP(F) == 1:
        return np.zeros(F.shape[1])
    elif F.size == 0:
        return np.ones(F.shape[1])
    elif F.shape[0] == 1:
        F = np.logical_not(F).astype(int)
        count = 0
        for i in range(0,F.shape[0],2):
            F_temp[count, i] = F[i]
            F_temp[count, i+1] = F[i+1]
            count = count + 1
        F = F_temp
        return F
    else:
        if zero_list.tolist() in F.T.tolist():
            index = F.T.tolist().index(zero_list.tolist())
        alpha[index] = 0
        alpha_not = np.logical_not(alpha).astype(int)
        # Finding the cofactor wrt alpha
        F_cof = np.zeros(shape=(F.shape[0],F.shape[1]))
        for i in range(F.shape[0]):
            F_cof[i, :] = cof.cofactor(alpha, F[i, :])
        F_cof = CV.check(F_cof)
        F_cof_comp = complement(F_cof)
        # Uncomment this statement
        F_comp = Union(alpha_not, F_cof_comp)
        return F_comp

complement(np.array([1, 0]))
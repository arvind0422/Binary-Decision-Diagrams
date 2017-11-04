
"""
Function: To check if a Function is Tautology or not using URP

Finding if a function is a Tautology using Unate Recursive Paradigm
Authors: Arvind, Shantanu, Sripathi

Instructions:
+ Edit PCN_data.txt -
Input format:
    First line: Variable Ordering
    Remaining Lines: Input Implicants in PCN Format.
+ Run URP_Tautology.py

Brief Working:
1. Returns Tautology if a row of 1's detected.
2. Returns Not Tautology if column of 0's are detected.
3.

"""

import numpy as np
from ITE import ite_master


def weakly_unate(F):
    weak_unate_list = list()
    for i in range(0, F.shape[1], 2):
        # print(i)
        row_del = list()
        F_temp = np.copy(F[:, i:i+2])
        # print(F_temp)
        for j in range(0, F.shape[0]):
            # print(j)
            if F[j][i] == 1 and F[j][i+1] == 1:
                row_del.append(j)
        # print(row_del)
        F_temp = np.delete(F_temp, row_del, axis=0)
        # print(F_temp)
        zero_list = np.zeros(F_temp.shape[0])
        if zero_list.tolist() in F_temp.T.tolist():
            weak_unate_list.append(i)
    return weak_unate_list


def URP(F):  # F is a numpy array
    one_list = np.ones(F.shape[1])
    zero_list = np.zeros(F.shape[0])
    sum_rows = np.sum(F, axis=0)
    sum_rows_even = sum_rows[::2]
    sum_rows_odd = sum_rows[1::2]
    weak_unate_list = weakly_unate(F)
    a_ind = np.where(sum_rows_even < F.shape[0])
    if one_list.tolist() in F.tolist():
        return 1
    elif zero_list.tolist() in F.T.tolist():
        return 0
    elif len(a_ind[0]) == 1:
        if sum_rows_odd[a_ind[0][0]] < F.shape[0]:
            return 1
    elif len(weak_unate_list) == int(F.shape[1]/2) and one_list.tolist() not in F.tolist():
        return 0
    else:
        weak_unate_list = weakly_unate(F)
        # print(weak_unate_list)
        if len(weak_unate_list) == 0:  # Condition for Binate
            answer = ite_master()
            # print(answer)
            if answer == 1:
                return 1
            else:
                return 0
        else:
            del_indices = list()
            for i in weak_unate_list:
                del_indices.append(i)
                del_indices.append(i+1)
            F_new = np.delete(F, del_indices, axis=1)
            return URP(F_new)

if __name__ == "__main__":
    PCNread = open("PCN_data.txt", "r")
    data = PCNread.readlines()
    data = [line.rstrip('\n') for line in data]
    data = data[1:]
    data = [line.replace(" ", "") for line in data]
    data = list(list(line) for line in data)
    k = list(np.zeros([len(data), len(data[0])]))
    for i in range(len(data)):
        for j in range(len(data[0])):
            k[i][j] = int(data[i][j])
    # print(k)
    x = URP(np.array(k))
    if x == 1:
        print("Tautology")
    else:
        print("Not a Tautology")

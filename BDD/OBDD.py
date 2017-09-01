"""
Cool Algo which we made - Sripathi, Shantanu, Arvind

In the tree, left child is 0, right child is 1.
"""

import readPCN
import numpy as np
from Stack import Stack

max_no = 26  # Max No. Of Variables


def weight(col_no, n_size, pcode):
    if pcode == "10" or pcode == "11":
        return 0
    elif pcode == "01":
        return (2 ** n_size) / (2 ** (col_no+1))


def dist(col_no, n):
    return (2 ** (n-col_no)) - 1


def get_leaf_nodes():
    pcn_mat, no_of_splitting_var, splitVarOrder = readPCN.readData()
    if np.array_equal(pcn_mat, np.zeros([1, no_of_splitting_var])):
        return np.zeros(2 ** no_of_splitting_var)
    answer = np.zeros(2 ** no_of_splitting_var)

    for pcn_row_1 in pcn_mat:
        pcn_row = list(pcn_row_1)
        # print(pcn_row)
        s = Stack()
        s.push(1)
        for i in range(len(pcn_row)):
            if pcn_row[i] == "11":
                s.push(i+max_no)
                # print(s.peek())

        ini_pos = 0
        for i in range(len(pcn_row)):
            ini_pos += weight(i, no_of_splitting_var, pcn_row[i])

        answer[int(ini_pos)] = s.peek()
        while s.peek() != 1:
            popkey = s.pop()
            # print(popkey)
            indices = np.argwhere(answer == popkey)
            indices = indices.reshape(len(indices))
            # print(indices)
            for i in indices:
                # print(dist(popkey-max_no+1, no_of_splitting_var))
                answer[i] = popkey
                answer[i + dist(popkey-max_no+1, no_of_splitting_var) + 1] = popkey
            # print(answer)
            answer = np.where(answer == popkey, s.peek(), answer)
            # print(answer)
    # print(answer)
    return answer

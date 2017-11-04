"""
In the tree, left child is 0, right child is 1.

"""

import readPCN
import numpy as np

# from Stack import Stack


class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def weight(col_no, n_size, pcode):  # Function to Hash to a Particular Location in Leaf Node Array
    if pcode == "10" or pcode == "11":
        return 0
    elif pcode == "01":
        return (2 ** n_size) / (2 ** (col_no+1))


def dist(col_no, n):  # To calculate separation between leaf nodes in case of Don't Care
    return (2 ** (n-col_no)) - 1


def get_leaf_nodes():
    max_no = 26  # Max No. Of Variables
    pcn_mat, no_of_splitting_var, splitVarOrder = readPCN.readData()
    if np.array_equal(pcn_mat, np.zeros([1, no_of_splitting_var])):
        return np.zeros(2 ** no_of_splitting_var)
    answer = np.zeros(2 ** no_of_splitting_var)

    for pcn_row_1 in pcn_mat:
        pcn_row = list(pcn_row_1)
        # print(pcn_row)
        s = Stack()  # To Hold Occurrence of Don't Care in the BDD
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


def build():
    leaf_nodes = get_leaf_nodes()
    pcnmat, n, splitVarOrder = readPCN.readData()

    # Creating a list of all the nodes in the tree
    var_list = list()
    for index, var in enumerate(splitVarOrder):
        var_alpha = chr(97+int(var))
        var_list.append(list(var_alpha)*(2 ** index))

    # Appending the Leaf Nodes
    var_list.append(list(map(str, list(map(int, leaf_nodes)))))

    # Flattening the list
    flat_var_list = [item for sublist in var_list for item in sublist]

    return flat_var_list

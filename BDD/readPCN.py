"""
This file helps to read PCN matrix and then output the matrix with proper splitting variable order.
First line is the splitting order (to be given as indices separated by spaces)
Second onwards is the data in PCN format
No of columns of the matrix depends on the no. of variables chosen
Author : Sripathi, Shantanu, Arvind
"""

import numpy as np


def readData():
    # Opening the file
    PCNread = open("PCN_data.txt", "r")

    # Reading all lines of the file
    data = PCNread.readlines()
    data = [line.rstrip('\n') for line in data]

    # Getting the variable splitting order
    splitVarOrder = data[0]
    splitVarOrder = splitVarOrder.split(" ")

    # Putting data into the numpy array
    data_matrix = np.array([])  # TODO
    for item in data[1:]:
        item = item.split(" ")
        if "00" in item:   # Finding 00 terms and removing those rows
            continue
        # Convert any type to an array (lists, tuples, etc)
        temp = np.asarray(item)
        if data_matrix.size == 0:
            data_matrix = temp
        else:
            data_matrix = np.vstack((data_matrix, temp))
        data_matrix = np.atleast_2d(data_matrix)

    if not data_matrix.size:
        # print(np.zeros([1, len(splitVarOrder)]))
        return np.zeros([1, len(splitVarOrder)]), len(splitVarOrder), splitVarOrder
    # print(data_matrix)

    # Reordering data_matrix according to splitting variable

    data_out = np.copy(data_matrix)
    for i, j in zip(splitVarOrder, range(len(splitVarOrder))):
        data_out[:, j] = data_matrix[:, int(i)]
    # print(data_out)

    return data_out, len(splitVarOrder), splitVarOrder

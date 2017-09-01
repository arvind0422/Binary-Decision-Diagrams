"""
This file contains the code to build the tree and represent it on graphviz
Authors : Sripathi, Shantanu, Arvind
"""

import OBDD
import readPCN


def build():
    leaf_nodes = OBDD.get_leaf_nodes()
    pcnmat, n, splitVarOrder = readPCN.readData()

    # Creating a list of the variables
    var_list = list()
    for index, var in enumerate(splitVarOrder):
        var_alpha = chr(97+int(var))
        var_list.append(list(var_alpha)*(2 ** index))

    var_list.append(list(map(str, list(map(int, leaf_nodes)))))
    # Flattening the list
    flat_var_list = [item for sublist in var_list for item in sublist]

    return flat_var_list

"""
Function 2: Generated ROBDD for a given function in PCN format using graphviz.

Instructions:
+ Edit PCN_data.txt
+ Run this file.
+ ROBDD.pdf file stores the graph.

"""


from graphviz import Digraph, Source
import numpy as np

import readPCN
import OBDD
from OBDD import get_leaf_nodes


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        # print(e)
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


def robdd():
    graph = Digraph(format="pdf")

    # Handling Tautology and All Zeros

    check_array = get_leaf_nodes()
    matrixdata, number, numberlist = readPCN.readData()
    # print(check_array)
    nody = list()
    # for variable in numberlist:
    #     nody.append(chr(int(variable)+97))
    edgy = list()
    # for i in range(number-1):
    #     edgy.append((chr(int(numberlist[i])+97), chr(int(numberlist[i+1])+97)))
    if np.array_equal(check_array, np.ones(len(check_array))):
        nodes_1 = ("1", {"label": "1", "shape": "box"})
        nody.append(nodes_1)
        # edgy.append((chr(int(numberlist[number-1])+97), "1"))
        # print(nody, edgy)
        add_edges(add_nodes(graph, nody), edgy).render("ROBDD")
    elif np.array_equal(check_array, np.zeros(len(check_array))):
        nodes_0 = ("0", {"label": "0", "shape": "box"})
        nody.append(nodes_0)
        # edgy.append((chr(int(numberlist[number-1]) + 97), "0"))
        # print(nody, edgy)
        add_edges(add_nodes(graph, nody), edgy).render("ROBDD")

    # If Not Tautology or All Zeros
    # Creating A List Of All Parent, Left Child, Right Child Combinations
    else:
        node_list = OBDD.build()
        id_dict = list()
        id_dict.append(("0", "-", "-"))
        id_dict.append(("1", "-", "-"))

        for i in range(int(len(node_list)/2)-1, -1, -1):
            left = node_list[2*i + 1]
            right = node_list[2*i + 2]
            temp = (node_list[i], left, right)
            if left == right:
                node_list[i] = str(left)
            elif temp not in id_dict:
                id_dict.append(temp)
                node_list[i] = str(len(id_dict)-1)
            else:
                node_list[i] = str(id_dict.index(temp))

        # print(id_dict)
        nodes = list()
        for i in range(len(id_dict)):
            label = dict()
            label['label'] = id_dict[i][0]
            tup = (str(i), label)
            nodes.append(tup)
        nodes = list(reversed(nodes))
        nodes[len(nodes)-2][1]["shape"] = "box"  # Adding Shapes to Leaf Nodes
        nodes[len(nodes)-1][1]["shape"] = "box"  # Adding Shapes to Leaf Nodes
        # print(nodes)

        # Building edge tuples
        edges = list()
        # print(len(id_dict))
        for i in range(2, len(id_dict)):
            label = dict()
            label['label'] = '1'
            tup1 = (str(i), id_dict[i][2])
            tup = (tup1, label)
            # edges.append(tup)  # Edges With Labels
            edges.append(tup1)
            label = dict()
            label['label'] = '0'
            tup1 = (str(i), id_dict[i][1])
            tup = (tup1, label)
            # edges.append(tup)  # Edges With Labels
            edges.append(tup1)
        edges = list(reversed(edges))
        # print(edges)

        add_edges(add_nodes(graph, nodes), edges)

    # To Make Left -> 0 and Right -> 1

    statement = "\n	graph [ordering=\"out\"]\n"
    source = graph.source
    dot = source[0:9]+statement+source[10:]
    # print(dot)

    # Rendering The Graph

    dot = Source(dot)
    dot.render('ROBDD', view=True)

if __name__ == "__main__":
    robdd()

import buildTree
import functools
import graphviz as gv
import os
import webbrowser
from OBDD import get_leaf_nodes
import numpy as np
import readPCN


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

    graph = functools.partial(gv.Graph, format="svg")

    # Handling Tautology and All Zeros
    check_array = get_leaf_nodes()
    matrixdata, number, numberlist = readPCN.readData()
    # print(check_array)
    nody = list()
    for variable in numberlist:
        nody.append(chr(int(variable)+97))
    edgy = list()
    for i in range(number-1):
        edgy.append((chr(int(numberlist[i])+97), chr(int(numberlist[i+1])+97)))
    if np.array_equal(check_array, np.ones(len(check_array))):
        nodes_1 = ("1", {"label": "1"})
        nody.append(nodes_1)
        edgy.append((chr(int(numberlist[number-1])+97), "1"))
        # print(nody, edgy)
        add_edges(add_nodes(graph(), nody), edgy).render("ROBDD")
    elif np.array_equal(check_array, np.zeros(len(check_array))):
        nodes_0 = ("0", {"label": "0"})
        nody.append(nodes_0)
        edgy.append((chr(int(numberlist[number-1]) + 97), "0"))
        # print(nody, edgy)
        add_edges(add_nodes(graph(), nody), edgy).render("ROBDD")

    # If Not Tautology or All Zeros
    else:
        node_list = buildTree.build()
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
        # print(nodes)

        # Building edge tuples
        edges = list()
        # print(len(id_dict))
        for i in range(2, len(id_dict)):
            label = dict()
            label['label'] = '0'
            tup1 = (str(i), id_dict[i][1])
            tup = (tup1, label)
            edges.append(tup)
            label = dict()
            label['label'] = '1'
            tup1 = (str(i), id_dict[i][2])
            tup = (tup1, label)
            edges.append(tup)
        # print(edges)

        # g = add_nodes_graph(g, nodes)
        # g = add_edges_graph(g, edges)
        # print(g.source)

        add_edges(add_nodes(graph(), nodes), edges).render('ROBDD')

    # Automatic Opening
    os.remove("/Users/arvindkumar/Documents/My Documents/Academics/5th Sem/SDC/Project/ROBDD")
    url = "file:///Users/arvindkumar/Documents/My%20Documents/Academics/5th%20Sem/SDC/Project/ROBDD.svg"
    path = 'open -a /Applications/Safari.app %s'
    webbrowser.get(path).open(url)

# robdd()

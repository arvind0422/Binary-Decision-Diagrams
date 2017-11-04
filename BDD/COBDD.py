"""
Function 1: Generated COBDD for a given function in PCN Format using graphviz.

Instructions:
+ Edit PCN_data.txt
+ Run this file.
+ COBDD.pdf file stores the graph.

"""

from graphviz import Digraph

import OBDD


def add_nodes_graph(graph1, nodes1):  # Function To Add Node to Grpah

    # Iterating over all nodes in the list
    for n in nodes1:
        if isinstance(n, tuple):
            graph1.node(n[0], **n[1])
        else:
            graph1.node(n)
    return graph1


def add_edges_graph(graph2, edges2):  # Function To Create An Edge in Graph

    # Iterating over all edges in the list
    for e in edges2:
        # print(e)
        graph2.edge(e[0], e[1])
    return graph2


def cobdd():

    list_OBDD = OBDD.build()
    graph = Digraph(format="pdf")

    # Adding nodes to the graph
    nodes = list()
    for i in range(int(len(list_OBDD)/2)):
        label = dict()
        label['label'] = list_OBDD[i]  # Label of Nodes
        tup = (str(i), label)
        nodes.append(tup)

    for i in range(int(len(list_OBDD)/2), len(list_OBDD)):
        label = dict()
        label['label'] = list_OBDD[i]  # Label & Box Shape of Leaf Nodes
        label['shape'] = "box"
        tup = (str(i), label)
        nodes.append(tup)

    # Building edge tuples
    edges = list()
    for i in range(int(len(list_OBDD)/2)):
        tup = (str(i), str(2*i+1))
        edges.append(tup)
        tup = (str(i), str(2*i+2))
        edges.append(tup)

    # Rendering The Graph
    g = add_edges_graph(add_nodes_graph(graph, nodes), edges)
    g.render('COBDD', view=True)

if __name__ == "__main__":
    cobdd()

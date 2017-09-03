# from id_dict_return import id_dict
import webbrowser
import buildTree
from OBDD import get_leaf_nodes
import numpy as np


def ite_master():

    node_list = buildTree.build()
    id_dict = list()
    id_dict.append(("0", "-", "-"))
    id_dict.append(("1", "-", "-"))

    for i in range(int(len(node_list) / 2) - 1, -1, -1):
        left = node_list[2 * i + 1]
        right = node_list[2 * i + 2]
        temp = (node_list[i], left, right)
        if left == right:
            node_list[i] = str(left)
        elif temp not in id_dict:
            id_dict.append(temp)
            node_list[i] = str(len(id_dict) - 1)
        else:
            node_list[i] = str(id_dict.index(temp))
    list_of_lists = [list(elem) for elem in id_dict]
    id_dict = list_of_lists
    print(id_dict)
    id_dict[0] = 0
    id_dict[1] = 1

    def ite(tup):
        if tup == 1 or tup == 0:
            return tup
        else:
            tup[1] = ite(id_dict[int(tup[1])])
            tup[2] = ite(id_dict[int(tup[2])])
            return tup

    check_array = get_leaf_nodes()
    if np.array_equal(check_array, np.ones(len(check_array))):
        answer = 1
    elif np.array_equal(check_array, np.zeros(len(check_array))):
        answer = 0
    else:
        answer = ite(id_dict[len(id_dict)-1])

    print(answer)

    filepath = "ITE.txt"
    path = 'open -a /Applications/TextEdit.app %s'

    file = open(filepath, "w")
    file.write(str(answer))

    file.close()
    url = "file:///Users/arvindkumar/Documents/My%20Documents/Academics/5th%20Sem/SDC/Project/ITE.txt"
    webbrowser.get(path).open(url)

# ite_master()

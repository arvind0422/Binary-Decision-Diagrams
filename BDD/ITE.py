"""
Function 3: Generates ITE for a given function in PCN format.

Instructions:
+ Edit PCN_data.txt
+ Run this file.
+ Result is rendered as a .txt file and is stored in ITE.txt

"""

import numpy as np
import webbrowser

import OBDD
from OBDD import get_leaf_nodes


def ite_master():

    # Creating A List Of All Parent, Left Child, Right Child Combinations
    node_list = OBDD.build()
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
    # print(id_dict)
    id_dict[0] = 0
    id_dict[1] = 1
    for ele in id_dict[2:]:
        ele[1], ele[2] = ele[2], ele[1]

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
        answer = ite(id_dict[len(id_dict)-1])  # Call to Recursive Function

    filepath = "ITE.txt"
    file = open(filepath, "w")
    file.write(str(answer))
    file.close()

    # path = 'open -a /Applications/TextEdit.app %s'
    # url = "file:///Users/arvindkumar/Documents/My%20Documents/Academics/5th%20Sem/SDC/Project/ITE.txt"
    # webbrowser.get(path).open(url)

    # print(answer)
    return answer

if __name__ == "__main__":
    ite_master()

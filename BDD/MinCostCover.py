"""
Module 2:
Minimum Cost Cover Search.

Instructions:
+ Edit Implicant_Table_Costs.txt
    Line 1: Costs for each implicant.
    Other Lines: Implicant Table.
+ Run this file

This function checks if all possible combinations of the rows of good matrix covers the function.

Note:
Implicant Names start from 0. If there are 3 implicants, they are denoted as 0,1,2.

"""

import numpy as np


def RemEssPrimes(filename):
    PCNread = open(filename, "r")

    # Reading all lines of the file
    data = PCNread.readlines()
    data = [line.rstrip('\n') for line in data]

    # Getting the variable splitting order
    cost = data[0]
    cost = cost.split(" ")
    cost = np.array(list(map(int, cost)))
    # print(cost)

    matrix = np.array([])  # TODO
    for item in data[1:]:
        item = item.split(" ")
        temp = np.asarray(item)
        if matrix.size == 0:
            matrix = temp
        else:
            matrix = np.vstack((matrix, temp))
        matrix = np.atleast_2d(matrix)
    matrix = np.copy(matrix.astype(int))
    # print(matrix)

    row_sum = np.sum(matrix, axis=1)
    index_1 = np.where((row_sum == 1), row_sum, 0).nonzero()[0]
    col_interested = np.zeros(matrix.shape[0])
    rows_gone = list()
    implicants = list()
    for i in index_1:
        # rows_gone.append(i)
        row_interested = matrix[i, :]
        col_ind = np.where((row_interested == 1), row_interested, 0).nonzero()[0]
        implicants.append(col_ind[0])
        col_interested += matrix[:, col_ind].flatten('F')
        col_interested[col_interested>1] = 1

    rows_gone.append(np.where((col_interested == 1), col_interested, 0).nonzero()[0])
    rows_gone = np.asarray(rows_gone[0])
    good_matrix = np.delete(matrix, rows_gone, 0)

    # print(good_matrix)
    print("Essential Primes:")
    print(implicants)
    return good_matrix, implicants, cost


def MinCostCover(filename):

    good_matrix, implicants, cost = RemEssPrimes(filename)

    if np.size(good_matrix) == 0:
        local_cost = 0
        for i in range(len(implicants)):
            local_cost += cost[implicants[i]]
        implicants = [np.sort(implicants)]
        local_cost1 = list()
        local_cost1.append(local_cost)
        print("Cost\tImplicants")
        print("\n".join("{}    \t{}".format(k, v) for k, v in zip(local_cost1, implicants)))
        print("\nMinimum Cost Cover:")
        print(np.sort(implicants[0]))
        return

    else:
        no_of_col = len(np.transpose(good_matrix))
        global_implicant_list = list()
        for i in range(1, 2 ** no_of_col):
            temp_implicant = list()
            temp_implicant.append(implicants.copy())
            character_pos = '{0:0'+str(no_of_col)+'b}'
            chosen = np.array([int(x) for x in character_pos.format(i)[:]])

            # First filter - removing essential implicants
            flag1 = 0
            for imp in implicants:
                if chosen[imp] == 1:
                    flag1 = 1
                    break
            if flag1 == 1:
                continue
            col_sum = np.zeros(len(good_matrix))

            # Filter 2 - covering check
            for ij in list(np.where(chosen == 1)[0]):
                col_sum += good_matrix[:, ij]
            flag2 = 0
            for st in col_sum:
                if st == 0:
                    flag2 = 1
            if flag2 == 1:
                continue

            # Adding the non-essential implicants
            # print("Added")
            temp_implicant.append(list(np.where(chosen == 1)[0]))
            temp_implicant_flat = [item for sublist in temp_implicant for item in sublist]
            temp_implicant_flat = np.array(temp_implicant_flat)
            temp_implicant_flat = np.copy(np.sort(temp_implicant_flat))
            temp_implicant_flat = list(temp_implicant_flat)
            global_implicant_list.append(temp_implicant_flat)
        # print(global_implicant_list)

        # Finding cost for each cover
        costlist = list()
        for imp_list in global_implicant_list:
            # imp_list = np.array(imp_list)
            new_cost = 0
            for im in imp_list:
                new_cost += cost[im]
            costlist.append(new_cost)

        costlist = np.array(costlist)
        final_list = global_implicant_list[np.argmin(costlist)]

        print("\nCost\tImplicants")
        print("\n".join("{}    \t{}".format(k, v) for k, v in zip(costlist, global_implicant_list)))

        print("\nMinimum Cost Cover:")
        print(np.sort(final_list))

if __name__ == "__main__":
    MinCostCover("Implicant_Table_Costs.txt")

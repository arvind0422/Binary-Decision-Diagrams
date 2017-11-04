"""
This code helps one perform the consensus operation on two given vectors.
Inputs: Two numpy vectors with data in PCN format.
Outputs: A matrix with the consensus operator applied on the two vectors.
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void as CV


def consensus(a, b):
    result = np.zeros(a.shape)
    temp = np.logical_and(a, b).astype(int)
    for i in range(a.size):
        temp_ele = temp[i]
        temp[i] = a[i] or b[i]
        if np.count_nonzero(result) == 0:
            result = temp
        else:
            result = np.vstack((result, temp))
        temp[i] = temp_ele
    final_result = CV.check(result)
    print("Consensus\n")
    print(final_result)
    return final_result

if __name__ == "__main__":
    print("Input Format: PCN\nExample: ab'c -> 01 10 01\n\nOutput Format: Matrix\nEach element "
          "denotes a digit in PCN with unique, non zero cubes.\n")

    a = input("1st Implicant\n")
    a = a.rstrip('\n')
    a = a.replace(" ", "")
    a = list(list(a))
    a = np.array([int(x) for x in a])

    b = input("2nd Implicant\n")
    b = b.rstrip('\n')
    b = b.replace(" ", "")
    b = list(list(b))
    b = np.array([int(x) for x in b])

    consensus(a, b)

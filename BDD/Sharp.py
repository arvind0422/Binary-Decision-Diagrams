"""
This code helps one perform the sharp operation.
Inputs: Two numpy vectors which need to undergo sharp operation.
Outputs: A matrix obtained after sharp operation - with any void cubes removed.
It has two functions - sharp and dis_sharp
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void as CV
# Corner cases: Check if both are non-void cubes, both have the same length.


def sharp(a, b):
    b_not = np.logical_not(b).astype(int)
    temp1 = np.ones(a.shape, dtype=int)
    result = np.zeros(a.shape, dtype=int)
    for i in range(a.size):
        temp_ele = temp1[i]
        temp1[i] = b_not[i]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if np.count_nonzero(result) == 0:
            result = temp2
        else:
            result = np.vstack((result, temp2))
        temp1[i] = temp_ele
    final_result = CV.check(result)
    print("Sharp Matrix\n")
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

    sharp(a, b)

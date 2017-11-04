"""
This program helps one to find the cofactor w.r.t an implicant.
Inputs: Two vectors - first one is from the function and the second one w.r.t which you have to find the cofactor.
Outputs: Cofactor implicant
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void


def intersect(a, b):
    result = np.logical_and(a, b).astype(int)
    result_sum = result[::2]+result[1::2]
    # print(result_sum)
    if np.count_nonzero(result_sum) == int(a.size/2):
        return 1, result
    else:
        return 0, result


def cofactor(a, b):
    flag, result = intersect(a, b)
    b_not = np.logical_not(b)
    if flag == 0:
        result_cof = np.zeros(a.size, dtype=int)
    else:
        cof = np.logical_or(a, b_not).astype(int)
        cof_sum = cof[::2] + cof[1::2]
        if np.count_nonzero(cof_sum) == int(a.size/2):
            result_cof = cof
        else:
            result_cof = np.zeros(a.size, dtype=int)
    return result_cof

if __name__ == "__main__":
    print("Co-factor of A with respect to B\n"
          "Input Format: PCN\nExample: ab'c -> 01 10 01\n\n"
          "Output: Cofactor in PCN with unique, non zero cubes.\n")

    a = input("Implicant A\n")
    a = a.rstrip('\n')
    a = a.replace(" ", "")
    a = list(list(a))
    a1 = np.array([int(x) for x in a])

    b = input("Implicant B\n")
    b = b.rstrip('\n')
    b = b.replace(" ", "")
    b = list(list(b))
    b1 = np.array([int(x) for x in b])

    r = cofactor(a1, b1)
    print("Cofactor of A wrt B")
    print(Check_void.check(np.atleast_2d(r)))

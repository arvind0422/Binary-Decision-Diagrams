"""
This program helps one to find the union of two functions
Inputs: Two matrices containing SOP implicants
Outputs: Union of input matrices
Authors: Arvind, Shantanu, Sripathi
"""

import numpy as np
import Check_void


def union(a, b):
    c = np.vstack((a,b))
    u = np.unique(c, axis=0)
    return u

if __name__ == "__main__":
    print("Input Format: PCN\nExample: ab'c -> 01 10 01\n\n"
          "Output: Union in PCN with unique, non zero cubes.\n")

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

    result = union(a1, b1)
    print("Union")
    print(Check_void.check(np.atleast_2d(result)))

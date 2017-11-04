import numpy as np
import Check_void


def intersect(a, b):
    return np.logical_and(a, b).astype(int)


if __name__ == "__main__":
    print("Input Format: PCN\nExample: ab'c -> 01 10 01\n\n"
          "Output: Intersection in PCN with unique, non zero cubes.\n")

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

    result = intersect(a1, b1)
    print("Intersection")
    print(Check_void.check(np.atleast_2d(result)))

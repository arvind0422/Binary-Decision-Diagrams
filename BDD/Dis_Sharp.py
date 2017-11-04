import numpy as np
import Check_void as CV


def dis_sharp(a, b):
    b_not = np.logical_not(b)
    temp1 = np.ones(a.shape, dtype=int)
    result = np.zeros(a.shape, dtype=int)
    for i in range(int(a.size/2)):
        if i == 0:
            temp_ele = temp1[0:2]
            temp1[0:2] = b_not[0:2]
        else:
            temp_ele = temp1[0:2*i+2]
            temp1[0:2*i] = b[0:2*i]
            temp1[2*i:2*i+2] = b_not[2*i:2*i+2]
        temp2 = (np.logical_and(a, temp1)).astype(int)
        if np.count_nonzero(result) == 0:
            result = temp2
        else:
            result = np.vstack((result, temp2))
        if i == 0:
            temp1[0:2] = temp_ele
        else:
            temp1[0:2*i+2] = temp_ele
    final_result = CV.check(result)
    print("Disjoint Sharp Matrix\n")
    print(str(final_result))
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

    dis_sharp(a, b)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    l = list(set(a))
    z = b[0]
    z = b[0] // (l[-1])
    arr = []
    arr2 = []
    for i in range(1, z + 1):
        c = l[-1] * i
        if (c % l[0] == 0):
            arr.append(c)
    for i in range(0, len(arr)):
        counter = 0
        for j in range(0, len(b)):
            if (b[j] % arr[i] == 0):
                counter += 1
        if (counter == len(b)):
            arr2.append(i)
    return len(arr2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

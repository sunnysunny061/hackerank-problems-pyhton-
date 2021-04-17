#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    arr = []
    arr2 = []
    arr3 = []
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if (a[i] == a[j] + 1 or a[j] == a[i]):
                arr.append(a[j])
                arr3.append(len(arr))
            elif (a[i] + 1 == a[j] or a[j] == a[i]):
                arr2.append(a[j])
                arr3.append(len(arr))

        arr = []
        arr2 = []
    return max(arr3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

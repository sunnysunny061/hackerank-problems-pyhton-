#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l = len(arr)
    arr = sorted(arr)
    arr2 = arr
    arr3 = [len(arr)]
    while (len(arr2) > 0):
        m = min(arr2)
        arr2 = []
        for i in range(0, l):
            arr[i] = arr[i] - m
            if arr[i] > 0:
                arr2.append(arr[i])
        if (len(arr2) > 0):
            arr3.append(len(arr2))
    return arr3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

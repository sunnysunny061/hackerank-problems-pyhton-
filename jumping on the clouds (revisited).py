#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    l = len(c)
    arr = []
    energy = 100
    s = 0
    for i in range(0, 10):
        for j in range(0, l):
            arr.append(c[j])
    for m in range(0, len(arr)):
        s = s + k
        if (arr[s] == 1):
            energy = energy - 1 - 2
        else:
            energy = energy - 1
        if (s % (l) == 0):
            return energy
            break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

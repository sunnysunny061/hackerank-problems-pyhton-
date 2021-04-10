#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(t, n):
    counter = 1
    arr = [1]
    for i in range(1, 100):
        if (i % 2 != 0):
            counter = counter * 2
            arr.append(counter)
        else:
            counter = counter + 1
            arr.append(counter)
    return arr[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(t, n)

        fptr.write(str(result) + '\n')

    fptr.close()

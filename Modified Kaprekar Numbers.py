#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    arr = []
    for i in range(p, q + 1):
        first = ''
        last = ''
        sum = 0
        z = i
        c = i * i
        c = list(str(c))
        if (len(c) == 1):
            if (i == 9 or i == 1):
                arr.append(i)
        else:
            m = len(c) // 2
            for j in range(0, m):
                first += c[j]
            for j in range(m, len(c)):
                last += c[j]
            sum = int(first) + int(last)
            if (sum == z):
                arr.append(sum)
    if (len(arr) == 0):
        print('INVALID RANGE')
    else:
        for i in arr:
            print(i, end=' ')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

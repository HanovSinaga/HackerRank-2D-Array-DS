#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ans = -1000
    i = 0
    while i<4:
        j = 0
        while j<4:
            up = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            middle = arr[i+1][j+1]
            down = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            total = up + middle + down

            j=j+1
            if total>ans:
                ans=total
        i=i+1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    bribeMap = {}
    
    for i in range(0, len(q)):
        for j in range(0, len(q) - i - 1):
            currentNumber = q[j]
            nextNumber = q[j + 1]
            if currentNumber > nextNumber:
                q[j] = nextNumber
                q[j+1] = currentNumber
                
                bribes += 1
                
                if str(currentNumber) in bribeMap:
                    bribeMap[str(currentNumber)] = bribeMap[str(currentNumber)] + 1
                else:
                    bribeMap[str(currentNumber)] = 1
                
                if bribeMap[str(currentNumber)] > 2:
                    print("Too chaotic")
                    return None
    
    print(bribes)

minimumBribes([2, 5, 1, 3, 4])
minimumBribes([2, 1, 5, 3, 4])

# expected output
# 3
# Too chaotic
